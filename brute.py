correct_password = "admin123"
file = open("passwords.txt", "r")
for line in file:
    password = line.strip()
    print("Trying password:", password)
    if password == correct_password:
       print("password Found:", password)
       break
file.close()
