#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

def main():
    try:
        print("Hello!")
        while True:
            cmd = input("Enter two strings > ").strip()
            strings = [str(x) for x in cmd.split(' ')]
            if len(strings) != 2:
                print("Wrong input!")
            else:
                if len(strings[0]) != len(strings[1]):
                    print("Length should be equal")
                else:
                    break;
        string1 = strings[0]
        string2 = strings[1]
        similarComponents = []
        currentComponent = ""
        difference = []

        for i in range(0, min(len(string1), len(string2))):
            if string1[i] == string2[i]:
                currentComponent += string1[i]
            else:
                difference.append(i)
                if len(currentComponent) > 0:
                    similarComponents.append(currentComponent)
                    currentComponent = ""

        if len(currentComponent) > 0:
            similarComponents.append(currentComponent)

        if len(difference) == 0:
            print("Strings are equal!")
        else:
            print("Found similar components: ", similarComponents)
            print("Differences found at following indices: ", difference)
    except KeyboardInterrupt:
        print("Goodbye!")
        exit(0)

if __name__ == "__main__":
    main()
