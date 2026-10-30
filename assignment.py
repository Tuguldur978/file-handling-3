# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    file = open(filename, "r", encoding="utf-8")
    line = ""
    for _ in range(line_number):
        line = file.readline()
        if not line:
            file.close()
            return ""
    file.close()
    return line.removesuffix("\n").removesuffix("\r")

# Exercise 2
def reverse_lines(source, destination):
    src_file = open(source, "r", encoding="utf-8")
    lines = src_file.readlines()
    src_file.close()
    lines.reverse()
    dst_file = open(destination, "w", encoding="utf-8")
    count = 0
    for line in lines:
        dst_file.write(line.strip() + "\n")
        count += 1
    dst_file.close()
    return count

# Exercise 3
def merge_files(first, second, destination):
    total_written = 0
    dst_file = open(destination, "w", encoding="utf-8")
    first_file = open(first, "r", encoding="utf-8")
    for line in first_file:
        dst_file.write(line.strip() + "\n")
        total_written += 1
    first_file.close()
    second_file = open(second, "r", encoding="utf-8")
    for line in second_file:
        dst_file.write(line.strip() + "\n")
        total_written += 1
    second_file.close()
    dst_file.close()
    return total_written
# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
