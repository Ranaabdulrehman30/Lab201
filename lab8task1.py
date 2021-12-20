while True:
    try:
        value = int(input("Please enter your number: "))
    except ValueError:
        print("Sorry, Valid Input")
        continue
    except:
        print("Some different error occurred")

