# Define the path to the counter file (stores number as text)
file_path = 'output.txt'

# 1. Try to read the current number from the file
try:
    with open(file_path, 'r') as file:
        # Read and strip any extra spaces; if the file is empty, treat it as 0
        content = file.read().strip()
        # If the file is empty, set number to 0, else convert content to integer
        if content == '':
            number = 0
        else:
            number = int(content)
except FileNotFoundError:  # If file doesn't exist, initialize to 0
    number = 0

# 2. Increment the number by 1
number += 1

# 3. Save the updated number back to the file
with open(file_path, 'w') as file:
    file.write(str(number))

# 3a. Append a log entry to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Incremented to {number}\n")

# 4. Output the incremented number
print(f"The incremented number is: {number}")
