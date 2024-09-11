import datetime
import requests
import json
from pathlib import path


def update_card_data():
    # URL to fetch divination cards data from poe.ninja for Standard league
    url = "https://poe.ninja/api/data/itemoverview?league=Standard&type=DivinationCard"

    # Fetching the data
    response = requests.get(url)
    cards = response.json()

    # Saving the data to a JSON file
    with open('divination_cards.json', 'w') as json_file:
        json.dump(cards, json_file, indent=4)

    print("Divination cards data saved to 'divination_cards.json'")


# Method to display information about a single card
def display_card_info(card_name, cards_data):
    # Search for the card in the loaded JSON data
    card = next((card for card in cards_data['lines'] if card['name'].lower() == card_name.lower()), None)

    # If card is found, display its details
    if card:
        print(f"Card Found: {card['name']}")
        print(f"Reward: {card['reward']}")
        print(f"Chaos Value: {card['chaosValue']}")
        print(f"Stack Size: {card['stackSize']}")
    else:
        print(f"Card '{card_name}' not found.")

# Example: Display info about "The Doctor" card
display_card_info("The Doctor", cards)
