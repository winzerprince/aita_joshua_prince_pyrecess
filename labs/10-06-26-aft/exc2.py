grades = ["A", "B", "C", "D"]
message = ""

score = input("Enter the grade (A,B,C,D)\n")

if score in grades:
    match score:
        case "A":
            message = "Excellent work"
        case "B":
            message = "Satisfactory work"
        case "C":
            message = "Nice try"
        case "D":
            message = "Are you even trying"
else:
    print("you entered wrong grade")

print(message)
