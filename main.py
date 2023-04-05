
'''
    pip install winsay
    then it will run "say" command in windows
'''

import os

if __name__ == '__main__':
    print("\n\nWelcome to RoboSpeaker 1.1 | Created by Dip\n")

    while True:
        x = input("Enter what you want me to say:")

        command = f"say {x}"

        if(x=="exit()"):
            os.system("say 'Bye Bye Friend'")
            break
        os.system(command)


