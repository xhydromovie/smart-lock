import lib, json

button = True

if button:
    data = lib.recognize()
    print(data)
    parsed = json.loads(data)
    print(parsed)

    if parsed["success"] == True:
        print("Zamek otwarty!")
    else:
        print("Nie otwarto")