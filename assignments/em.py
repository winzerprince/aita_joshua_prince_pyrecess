import tty
import sys
import termios


def show_values(items: list):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)

    output = ""
    selected = 0

    try:
        while True:
            # Full clear + hide cursor
            sys.stdout.write("\033[2J\033[H\033[?25l")

            # 1. Input line
            sys.stdout.write("\033[2;1H")
            sys.stdout.write(f"Search / Type: {output}")
            sys.stdout.write(f"\033[2;{len('Search / Type: ') + len(output) + 1}H")

            # 2. Hello
            sys.stdout.write("\033[4;1H\033[32mHello\033[0m")

            # 3. List - Start at row 6
            sys.stdout.write("\033[6;1H")
            for i, item in enumerate(items):
                if i == selected:
                    line = f"\033[1;36m > {item} \033[0m"  # Highlighted
                else:
                    line = f"   {item}"
                sys.stdout.write("\r" + line + "\n")  # Clear rest of line + newline

            sys.stdout.flush()

            # Read key
            key = sys.stdin.read(1)

            if key == "q":
                break
            elif key == "\x1b":  # Arrow keys
                seq = sys.stdin.read(2)
                if seq == "[A" and items:  # Up
                    selected = (selected - 1) % len(items)
                elif seq == "[B" and items:  # Down
                    selected = (selected + 1) % len(items)
            elif key == "\x7f":  # Backspace
                output = output[:-1]
            elif key in ("\r", "\n"):  # Enter
                sys.stdout.write(f"\033[20;1HSelected: {items[selected]}\n")
                break
            else:
                output += key

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("\033[?25h\033[0m")  # Restore cursor and color


# Run
nums = list(range(1, 20))
print("\033[2J")
show_values(nums)

