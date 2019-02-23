import lib, json

button = True

for n in range(4):
    if button == True:
        data = lib.recognize()
        print(data)
        parsed = json.loads(data)
        print(parsed)
        button = False
        if parsed["success"] == True:
            print("Zamek otwarty!")
        else:
            print("Nie otwarto")
    else:
        print("Podejscie:", n)