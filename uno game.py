class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"
import random

class Deck:
    def __init__(self):
        self.cards = []
        colors = ["Red", "Yellow", "Green", "Blue"]
        values = list(range(1, 10)) + ["Skip", "Reverse", "Draw Two", "Wild", "Wild Draw Four"]
        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

    def play_card(self, card):
        self.hand.remove(card)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

class UnoGame(Widget):
    pass

class UnoApp(App):
    def build(self):
        return UnoGame()

if __name__ == "__main__":
    UnoApp().run()