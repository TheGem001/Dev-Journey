import os
import pyjokes
import pyttsx3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tell_joke():
    # Generate the joke
    joke = pyjokes.get_joke()
    
    # Print it to the screen
    print(f"\nJoke: {joke}")
    
    # Speak the joke audio
    pyttsx3.speak(joke)

if __name__ == "__main__":
    clear_screen()
    print("Welcome! Turn up your volume.")

    while True:
        clear_screen()
        print("Joke Teller")
        print("\n---------------------------")
        print("Press 1 to hear a joke")
        print("Press 2 to exit")
        pyttsx3.speak("Press 1 to hear a joke or 2 to exit.")
        
        choice = input("Enter choice: ")

        if choice == '1':
            clear_screen()
            tell_joke()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please press 1 or 2.")