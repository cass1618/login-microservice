import time

while True:
    time.sleep(1)
    file = open("createRequest.txt", 'r+')
    read = file.read()

    if type(read) == str and read != '':
        f = open("users.txt", 'a')
        f.write(read)
        f.close()

        file.truncate(0)
        file.close()
