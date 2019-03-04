import lib, json

button = True

if button:
    print("START")
    
    result = lib.recognize()

    if result is True:
        print("Otworzono zamek")
    else:
        print("Nie rozpoznano!")