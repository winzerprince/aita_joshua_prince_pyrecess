# Write a file with content I love python programming in the same directory as this file
# with the second line saying I am becoming a data scientist

with open("text.txt", "w") as file:
    file.write("I love programming\n")
    file.write("I am becoming a data scientist\n")

with open("text.txt", "a") as file:
    file.write("Every data scientist must learn python")
