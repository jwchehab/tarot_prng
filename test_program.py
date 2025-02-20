import os
import subprocess
import time
from playsound import playsound


def get_tarot_reading(num_cards):
    """ Call the tarot PRNG microservice to get a reading."""

    # Dramatization for the video
    playsound("startup.mp3")
    print("Requesting cards", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(0.75)

    # Write required number of cards for reading to file
    with open("needed_nums.txt", 'w') as file:
        file.write(str(num_cards))

    # Record the time that you wrote to the file
    write_time = os.path.getmtime("needed_nums.txt")

    # Execute the microservice
    # Note: subprocess.run() will not allow the interpreter to continue
    # until the process completes
    # subprocess.run(['python', 'tarot_prng.py'])

    # Or for dramatic effect
    process = subprocess.Popen(['python', 'tarot_prng.py'],
                               creationflags=subprocess.CREATE_NEW_CONSOLE)

    process.wait()

    # Check that the microservice actually worked and wrote to the file
    modified_time = os.path.getmtime("needed_nums.txt")
    if modified_time == write_time:
        raise Exception("PRNG microservice did not update the file.")
    else:
        # Dramatization for the video
        print()
        print("Reading received!")
        playsound("success.mp3")

    # Read the outputted list of card numbers
    with open("needed_nums.txt", 'r') as file:
        result = file.read().strip()
        # Dramatization for the video
        print(result)
        print()
        time.sleep(1)

    # This takes a set of comma separated values and reads them into a list
    tarot_cards = [int(value.strip()) for value in result.split(',')]

    return tarot_cards


# Sample call
if __name__ == '__main__':
    tarot_reading = list()
    cards = get_tarot_reading(7)

    tarot_deck = (
        "The Fool", "The Fool (Reversed)",
        "The Magician", "The Magician (Reversed)",
        "The High Priestess", "The High Priestess (Reversed)",
        "The Empress", "The Empress (Reversed)",
        "The Emperor", "The Emperor (Reversed)",
        "The Hierophant", "The Hierophant (Reversed)",
        "The Lovers", "The Lovers (Reversed)",
        "The Chariot", "The Chariot (Reversed)",
        "Strength", "Strength (Reversed)",
        "The Hermit", "The Hermit (Reversed)",
        "Wheel of Fortune", "Wheel of Fortune (Reversed)",
        "Justice", "Justice (Reversed)",
        "The Hanged Man", "The Hanged Man (Reversed)",
        "Death", "Death (Reversed)",
        "Temperance", "Temperance (Reversed)",
        "The Devil", "The Devil (Reversed)",
        "The Tower", "The Tower (Reversed)",
        "The Star", "The Star (Reversed)",
        "The Moon", "The Moon (Reversed)",
        "The Sun", "The Sun (Reversed)",
        "Judgement", "Judgement (Reversed)",
        "The World", "The World (Reversed)",
        "Ace of Wands", "Ace of Wands (Reversed)",
        "Two of Wands", "Two of Wands (Reversed)",
        "Three of Wands", "Three of Wands (Reversed)",
        "Four of Wands", "Four of Wands (Reversed)",
        "Five of Wands", "Five of Wands (Reversed)",
        "Six of Wands", "Six of Wands (Reversed)",
        "Seven of Wands", "Seven of Wands (Reversed)",
        "Eight of Wands", "Eight of Wands (Reversed)",
        "Nine of Wands", "Nine of Wands (Reversed)",
        "Ten of Wands", "Ten of Wands (Reversed)",
        "Page of Wands", "Page of Wands (Reversed)",
        "Knight of Wands", "Knight of Wands (Reversed)",
        "Queen of Wands", "Queen of Wands (Reversed)",
        "King of Wands", "King of Wands (Reversed)",
        "Ace of Cups", "Ace of Cups (Reversed)",
        "Two of Cups", "Two of Cups (Reversed)",
        "Three of Cups", "Three of Cups (Reversed)",
        "Four of Cups", "Four of Cups (Reversed)",
        "Five of Cups", "Five of Cups (Reversed)",
        "Six of Cups", "Six of Cups (Reversed)",
        "Seven of Cups", "Seven of Cups (Reversed)",
        "Eight of Cups", "Eight of Cups (Reversed)",
        "Nine of Cups", "Nine of Cups (Reversed)",
        "Ten of Cups", "Ten of Cups (Reversed)",
        "Page of Cups", "Page of Cups (Reversed)",
        "Knight of Cups", "Knight of Cups (Reversed)",
        "Queen of Cups", "Queen of Cups (Reversed)",
        "King of Cups", "King of Cups (Reversed)",
        "Ace of Swords", "Ace of Swords (Reversed)",
        "Two of Swords", "Two of Swords (Reversed)",
        "Three of Swords", "Three of Swords (Reversed)",
        "Four of Swords", "Four of Swords (Reversed)",
        "Five of Swords", "Five of Swords (Reversed)",
        "Six of Swords", "Six of Swords (Reversed)",
        "Seven of Swords", "Seven of Swords (Reversed)",
        "Eight of Swords", "Eight of Swords (Reversed)",
        "Nine of Swords", "Nine of Swords (Reversed)",
        "Ten of Swords", "Ten of Swords (Reversed)",
        "Page of Swords", "Page of Swords (Reversed)",
        "Knight of Swords", "Knight of Swords (Reversed)",
        "Queen of Swords", "Queen of Swords (Reversed)",
        "King of Swords", "King of Swords (Reversed)",
        "Ace of Pentacles", "Ace of Pentacles (Reversed)",
        "Two of Pentacles", "Two of Pentacles (Reversed)",
        "Three of Pentacles", "Three of Pentacles (Reversed)",
        "Four of Pentacles", "Four of Pentacles (Reversed)",
        "Five of Pentacles", "Five of Pentacles (Reversed)",
        "Six of Pentacles", "Six of Pentacles (Reversed)",
        "Seven of Pentacles", "Seven of Pentacles (Reversed)",
        "Eight of Pentacles", "Eight of Pentacles (Reversed)",
        "Nine of Pentacles", "Nine of Pentacles (Reversed)",
        "Ten of Pentacles", "Ten of Pentacles (Reversed)",
        "Page of Pentacles", "Page of Pentacles (Reversed)",
        "Knight of Pentacles", "Knight of Pentacles (Reversed)",
        "Queen of Pentacles", "Queen of Pentacles (Reversed)",
        "King of Pentacles", "King of Pentacles (Reversed)",
    )

    print("Your reading:")
    time.sleep(1)
    for n, card in enumerate(cards):
        # Since the microservice outputs numbers from 1 to 156, need to
        # re-index to read out of the tarot deck
        index = card - 1
        tarot_reading.append(tarot_deck[index])
        print(tarot_reading[n])
        # Dramatization for the video
        playsound("stamp.mp3")
        time.sleep(0.25)
    time.sleep(0.25)
    print()
    print("Success!")
    playsound("complete.mp3")

