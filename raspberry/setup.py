import lib

button = True

if button:
    data = lib.recognize()
    print(data)
    # if data["success"] == True:
    #     print("Zamek otwarty!")
    # else:
    #     print("Nie otwarto")