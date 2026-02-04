# Write a program to mine a log file and find out whether it contains ‘python’.
# Write a program to find out the line number where python is present from ques 6.
word = 'python'
with open("logs_python.log", "r") as rf:
    log_text = rf.read().lower()

if word in log_text:
    print("logs_python.log contains the python keyword.", log_text.count('python'))
else:
    print("logs_python.log does not contain the python keyword.")

with open("logs_python.log", "r") as arf:
    log_lines = arf.readlines()
print("python keyword present in following lines : ")
i = 1
for line in log_lines:
    if word in line.lower():
        print(i)
    i += 1
# for i in range(len(log_lines)):
#     if log_lines[i].lower().find('python') >-1:
#         print(i+1)
