fh = open("input.txt", "r")
password_count = 0
actual_password_count = 0
# Part-1
for i in fh:
    rule, password = i.split(":")
    rule, password = rule.replace(" ", ""), password.replace(" ", "")
    password = password.replace("\n", "")
    char, rule = rule[-1], rule[:-1]
    num_1, num_2 = rule.split("-")
    if password.count(char) >= int(num_1) and password.count(char) <= int(num_2):
        password_count += 1
    #Part-2
    if (password[int(num_1) - 1] == char) ^ (password[int(num_2) - 1] == char):
        actual_password_count += 1 
    
    
print(f"Valid Passwords: {password_count}")
print(f"\"Acual\" Valid Passwords: {actual_password_count}")
    