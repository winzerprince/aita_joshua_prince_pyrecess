# The Format
# ●​ Time: 60 Minutes (Strict).
# ●​ Team: 5 People.
# ●​ Goal: A working prototype (CLI or Basic GUI) that passes specific test cases.
# ●​ Concept: Each challenge focuses on a different core Python pillar.
# Idea 1: The "Code Climate" CLI Tool
# Focus: File I/O, String Manipulation, and Dictionaries.
# The Challenge:​
# Your team is a "Developer Productivity" squad. Build a CLI tool that scans a given
# Python file (provided by the judges) and returns a "Health Score" based on specific
# rules.
# The Requirements:
# 1.​ Line Counter: Count the total lines, blank lines, and lines of code (excluding
# comments).
# 2.​ Complexity Check: Count the number of if, elif, else, for, and while
# statements.
# 3.​ Comment Ratio: Calculate the percentage of lines that are comments.
# 4.​ Variable Check: Find all variables assigned with = and ensure they follow
# snake_case (warn if not).
# Output: Print a JSON-like dictionary to the terminal with the stats.
# Team Splitting Strategy:
# ●​ Person 1: The File Reader & Line Counter.
# ●​ Person 2: Regex/Logic for finding keywords (if, for).
# ●​ Person 3: Comment detection logic (handling # and docstrings).
# ●​ Person 4: Variable extraction and naming rule validator.
# ●​ Person 5: The "Integrator" – builds the main function, compiles the dict, and
# formats the output.

#imports
import argparse
import json
import re
import sys

# Group D parallel assignment plan:
# Section 1 - File Reader & Line Counter
# - Alinda Joel (24/U/03258/PS | 2400703258)
# - Reads the file and counts total, blank, and code lines.
#
# Code space:

# read the file and return its content as a list of lines
def read_file(path):
    """Read a file and return its lines."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        return None
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def get_code_lines(lines):
    """Return only the lines that count as code, excluding comments and docstrings."""
    code_lines = []
    in_docstring = False
    docstring_delimiter = None

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
            # When in a doctstring i.e """ """ section , skip line
        if in_docstring:
            if docstring_delimiter in stripped_line and stripped_line.count(docstring_delimiter) % 2 == 1:
                in_docstring = False
                docstring_delimiter = None
            continue
            # Identify when entering a docstring
        if stripped_line.startswith(("'''", '"""')):
            if stripped_line.count("'''") % 2 == 1:
                in_docstring = True
                docstring_delimiter = "'''"
            elif stripped_line.count('"""') % 2 == 1:
                in_docstring = True
                docstring_delimiter = '"""'
            continue

       
        

        if stripped_line.startswith('#'):
            continue

        code_lines.append(line)

    return code_lines


def count_lines(lines):
    """Count total, blank, and code lines."""
    if lines is None:
        return {"total_lines": 0, "blank_lines": 0, "code_lines": 0}

    total_lines = len(lines)
    blank_lines = 0
    code_lines = len(get_code_lines(lines))

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            blank_lines += 1

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "code_lines": code_lines,
    }


# Section 2 - Keyword / Complexity Counter
# - Jovia Minallah Matata (24/U/0429 | 2400700429)
# - Counts if, elif, else, for, and while statements.
#
# Code space:

def count_keywords(lines):
    """Count if, elif, else, for, and while keywords."""
    keywords = ['if', 'elif', 'else', 'for', 'while']
    counts = {keyword: 0 for keyword in keywords}
    pattern = re.compile(r'\b(' + '|'.join(keywords) + r')\b') 

    for line in get_code_lines(lines):
        code_part = line.split('#', 1)[0]
        for match in pattern.findall(code_part):
            counts[match] += 1

    return counts


# Section 3 - Comment Detection
# - Birungi Hairat Muhamed (24/U/04397/EVE | 2400704397)
# - Detects comment lines and helps handle docstrings.
#
# Code space:

def count_comments(lines):
    """Count comment and non-comment lines, including docstrings as comments."""
    commented_lines = 0
    uncommented_lines = 0
    in_docstring = False
    docstring_delimiter = None

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '':
            continue

        if in_docstring:
            commented_lines += 1
            if docstring_delimiter in stripped_line and stripped_line.count(docstring_delimiter) % 2 == 1:
                in_docstring = False
                docstring_delimiter = None
            continue

        if stripped_line.startswith(("'''", '"""')):
            commented_lines += 1
            if stripped_line.count("'''") % 2 == 1:
                in_docstring = True
                docstring_delimiter = "'''"
            elif stripped_line.count('"""') % 2 == 1:
                in_docstring = True
                docstring_delimiter = '"""'
            continue

        if stripped_line.startswith('#'):
            commented_lines += 1
        else:
            uncommented_lines += 1

    total_checked_lines = commented_lines + uncommented_lines
    if total_checked_lines == 0:
        return {
            'commented_lines': 0,
            'uncommented_lines': 0,
            'comment_percentage': 0.0,
        }

    comment_percentage = (commented_lines / total_checked_lines) * 100
    return {
        'commented_lines': commented_lines,
        'uncommented_lines': uncommented_lines,
        'comment_percentage': round(comment_percentage, 2),
    }


# Section 4 - Variable Naming Validator
# - Aita Joshua Prince (24/U/0128 | 2400700128)
# - Finds assignments and checks snake_case variable names.
#
# Code space:

def validate_variables(lines):
    """Return only invalid variable-name warnings with their line numbers."""
    assignment_pattern = re.compile(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=(?!=)')
    snake_case_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')

    warnings = []

    for line_num, line in enumerate(lines, start=1):
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith('#'):
            continue

        code_part = line.split('#', 1)[0]

        for match in assignment_pattern.finditer(code_part):
            variable_name = match.group(1)
            if not snake_case_pattern.fullmatch(variable_name):
                warnings.append({
                    'variable': variable_name,
                    'line_num': line_num,
                })

    return warnings


# Section 5 - Integrator / Final Output
# - Naluyange Emilly Shirley (24/U/08843/PS | 2400708843)
# - Combines all results into one dictionary and prints it.

def build_report(input_path):
    """Build the final JSON-ready analysis report."""
    lines = read_file(input_path)
    if lines is None:
        return None

    return {
        'input_file': input_path,
        'line_stats': count_lines(lines),
        'keyword_stats': count_keywords(lines),
        'comment_stats': count_comments(lines),
        'variable_stats': validate_variables(lines),
    }


def main():
    """Parse CLI arguments and print or save the JSON report."""
    parser = argparse.ArgumentParser(description='Analyze a Python file and output JSON stats.')
    parser.add_argument('-i', '--input', required=True, help='Python file to analyze')
    parser.add_argument('-o', '--output', help='Output file to save the JSON report')
    args = parser.parse_args()

    report = build_report(args.input)
    if report is None:
        sys.exit(1)

    report_json = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as output_file:
            output_file.write(report_json)
            output_file.write('\n')
    else:
        print(report_json)


if __name__ == '__main__':
    main()

# Suggested Live Share workflow:
# 1. Person 1 sets up the file reader and line counters first.
# 2. Person 2 adds keyword counting using small helper logic.
# 3. Person 3 handles comments and docstrings carefully.
# 4. Person 4 validates variable names and collects warnings.
# 5. Person 5 merges everything into one result dictionary and final print.
#
# Team rule: keep each part in a separate small section or function, then
# test the output shape together before polishing details.