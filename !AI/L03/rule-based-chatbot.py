import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def greet_user():
    print(Fore.CYAN + "Hello! I'm TravelBot, your virtual travel assistant.")
    name = input(Fore.YELLOW + "May I know your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}! How can I assist you today?")
    return name

# Function to show help options
def show_help():
    print(Fore.MAGENTA + "\nI can assist you with the following:")
    print(Fore.GREEN + "- Provide travel recommendations")
    print(Fore.GREEN + "- Offer packing tips")
    print(Fore.GREEN + "- Tell travel jokes")
    print(Fore.CYAN + "Just ask me a question or type 'exit' to leave.\n")

# Function to process user input
def process_input(user_input):
    # Convert input to lowercase, remove leading/trailing spaces, and replace multiple spaces with one
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+', ' ', user_input)  # Replace multiple spaces with a single space
    return user_input

# Function to provide travel recommendations
def provide_recommendations():
    print(Fore.CYAN + "TravelBot: Sure! Are you interested in beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = process_input(preference)  # Normalize the input

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like this suggestion? (yes/no)")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(Fore.GREEN + f"TravelBot: Great! Have an amazing time in {suggestion}!")
        elif response == "no":
            print(Fore.RED + "TravelBot: No worries! Let's find another place.")
            provide_recommendations()  # Recur to suggest another destination
        else:
            print(Fore.RED + "TravelBot: I didn't catch that. Let's start over.")
            provide_recommendations()  # Recur to handle unexpected input
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that preference.")

    # Show the help options again
    show_help()

# Function to offer packing tips
def offer_packing_tips():
    print(Fore.CYAN + "TravelBot: Where are you traveling to?")
    destination = input(Fore.YELLOW + "You: ")
    destination = process_input(destination)  # Normalize the input
    print(Fore.CYAN + "TravelBot: How many days will you be staying?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {destination}:")
    print(Fore.GREEN + "- Pack versatile clothing items.")
    print(Fore.GREEN + "- Don't forget travel adapters and chargers.")
    print(Fore.GREEN + "- Check the weather forecast before packing.")

# Function to tell a joke
def tell_joke():
    joke = random.choice(jokes)
    print(Fore.YELLOW + f"TravelBot: {joke}")

# Main chat function
def chat():
    name = greet_user()
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        processed_input = process_input(user_input)
        if "recommendation" in processed_input or "suggest" in processed_input:
            provide_recommendations()
        elif "pack" in processed_input or "packing" in processed_input:
            offer_packing_tips()
        elif "joke" in processed_input or "funny" in processed_input:
            tell_joke()
        elif "help" in processed_input:
            show_help()
        elif "exit" in processed_input or "bye" in processed_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't quite catch that. Could you please rephrase?")

# Start the chatbot
if __name__ == "__main__":
    chat()
