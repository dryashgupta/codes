import winsound,time,os

def sound(x):
    for i in range(2): # Number of repeats
        for j in [261,303,349,399,523,399,349,303,261]: # Number of beeps
            winsound.Beep(j,400)
        time.sleep(3) # Duration between beeps

def alarm(n):
    print("Wait time",n)
    time.sleep(n)
    sound(n)

def choice(user_input):

    if user_input == '1':
        second_input = input("Enter the number of Hours ")
        try:
            main_input = int(second_input)
        except:
            print("Enter a valid Number")
        main_input = main_input*60*60
        alarm(main_input)

    elif user_input == '2':
        second_input = input("Enter the number of Minutes ")
        try:
            main_input = int(second_input)
        except:
            print("Enter a valid Number")
        main_input = main_input*60
        alarm(main_input)

    elif user_input == '3':
        second_input = input("Enter the number of Seconds ")
        try:
            main_input = int(second_input)
        except:
            print("Enter a valid Number")
        alarm(main_input)

    elif user_input == '4':
        hours = input("Enter the number of Hours ")
        minutes = input("Enter the number of Minutes ")
        seconds = input("Enter the number of Seconds ")
        try:
            hrs = int(hours)
            mins = int(minutes)
            secs = int(seconds)
        except:
            print("Enter a valid Number")
        main_input = ((hrs*60*60)+(mins*60)+secs)
        alarm(main_input)

    else:
        os.system('cls')
        main()

def main():
    print("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
    first_input = input("")
    choice(first_input)
main()
