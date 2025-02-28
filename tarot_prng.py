import random
import time

# Read number of values to generate from the text file to integer
with open('needed_nums.txt', 'r') as file:
    draws = int(file.read().strip())

# Initialize our tarot deck represented by values 1-78
tarot_deck = list(range(1, 79))


def reading(deck, cards_in_reading):
    # random.sample selects non-repeating values from the deck
    drawn_cards = random.sample(deck, cards_in_reading)
    # allows for reverse card values without repeating the same card
    tarot_draw = [
        (card * 2 - 1) if random.choice([True, False]) else (card * 2)
        for card in drawn_cards
    ]

    return tarot_draw

tarot_reading = reading(tarot_deck, draws)

# Write output as list of CSV to text file
with open('needed_nums.txt', 'w') as file:
    file.write(", ".join(map(str, tarot_reading)))
