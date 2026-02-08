import pyttsx3
import os

def clear_screen():
    os.system('cls')
# Main Menu
def main():
    clear_screen()
    print("1. Text to Speech")
    print("2. Exit")
    input_choice = input("Choose an option: ")
    if input_choice == '1':
        text = input("Enter text to speak: ")
        speak(text)
    elif input_choice == '2':
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

# Text to Speech Function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    main()

main()