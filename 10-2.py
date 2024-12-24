# Open the file in read mode and read its contents
with open("learning_python.txt", "r") as file:
    content = file.read()

# Replace 'Python' with 'It' in the content
updated_content = content.replace('Python', 'It')

# Open the file in write mode and write the updated content
with open("learning_python.txt", "w") as file:
    file.write(updated_content)

# Print the updated content
print(updated_content)
