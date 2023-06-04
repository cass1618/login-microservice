import time


# Main service that reads file for valid usernames and passwords
def userLogin(username, password, path):
    try:
        password = password + "\n"

        with open(path, 'r') as openFile:

            lines = openFile.readlines()

            for i in lines:

                read_lines = i.split(",")

                if read_lines[0] == username and read_lines[1] == password:
                    return True

    except Exception:
        print(Exception)

    return False


# Continuously runs looking for request from outside service
while True:
    time.sleep(1)
    file = open("loginRequest.txt", 'r+')
    read = file.read()

    if type(read) == str and read != '':
        pu = read.split(",")
        f = open("loginResponse.txt", 'r+')
        f.truncate(0)
        f.write(str(userLogin(pu[0], pu[1], "users.txt")))
        f.close()

        time.sleep(2)
        file.truncate(0)
        file.close()
