#!/usr/bin/env python3

while True:

    print("Hello, are you haveing a good day?""\n")
    answer = input("Yes or no--> ")

    if answer == 'yes':
        print("Then have a good day.""\n")
        break

    elif answer == 'no':
        print("Have you tried drinking?""\n")
        answer = input("Yes or no--> ")

        if answer == 'yes':
            print("Is it helping?""\n")
            answer = input("Yes or no--> ")

            if answer == 'yes':
                print("Then have a good day.""\n")
                break

            elif answer == 'no':
                print("Is weed legal where you are?""\n")
                answer = input("Yes or no--> ")

                if answer == 'yes':
                    print("I'd start there.""\n")
                    break

                elif answer == 'no':
                    print("Have you tried yoga?""\n")
                    answer = input("Yes or no--> ")

                    if answer == 'yes':
                        print("Then you should go back for a refund, if your still having a bad day.""\n")
                        break

                    elif answer == 'no':
                        print("I wouldn't start there, but if all else fails, try anything once.""\n")
                        break

        elif answer == 'no':
            print("You should start there.""\n")
            break
    else:
        print("I'm sorry I didn't get that?""\n")

print("So long!""\n")
