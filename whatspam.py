from Spammer import Wspammer
from os import path

ws = None


def login():
    selected = False
    while not(selected):
        print("How do you want to login\n" + "1) Login Through QR Code\n" +
              "2) Login Through Saved Session File")
        choice = int(raw_input(">>>"))
        if choice == 1:
            selected = True
            print("Please Login With QR Code")
            print("waiting 5 minutes till reset")
            x = ws.wait_till_login()
            if x:
                return False
            else:
                selected = False
        elif choice == 2:
            selected = True
            filexist = False
            while not(filexist):
                print("Please input filename for session file")
                Filename = raw_input(">>>")
                if(path.exists(Filename)):
                    ws.load_from_file(Filename)
                    x = ws.is_logged_in()
                    if x:
                        return True
                    else:
                        filexist = True
                        selected = False
                else:
                    print("could not find file in current directory")
        else:
            print("Please choose between 1 and 2")


def ask_for_save():
    answered = False
    while not(answered):
        print("Do you want to save the session in a file")
        print("1) Yes")
        print("2) No")
        choice = int(raw_input(">>>"))
        if choice == 2:
            return None
        elif choice == 1:
            while(True):
                print("Please insert a name for the session file")
                filename = raw_input(">>>")
                if(path.exists(filename)):
                    print("file already exists please input a different name")
                else:
                    ws.store_to_file(filename)
                    return None


def ask_and_spam():
    target = raw_input("Enter target >>> ")
    message = raw_input("Enter message to send >>> ")
    number = int(raw_input("How many times to spam >>> "))
    ws.spam_person(target, message, number)


if __name__ == '__main__':
    ws = Wspammer()
    filelog = login()
    if not(filelog):
        ask_for_save()
    ask_and_spam()
    ws.driver.close()