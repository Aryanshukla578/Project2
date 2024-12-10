import kivy
kivy.require('2.0.0')  # Replace with your Kivy version
from kivy.config import Config
Config.set('kivy', 'log_level', 'debug')
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
    # Import necessary Kivy modules
from kivy.uix.image import Image

# Add card images to the UnoGame class
class UnoGame(Widget):
    def draw_card(self):
        # Display an image of the card drawn
        card_image = Image(source='path/to/card_image.png')
        self.add_widget(card_image)

    def play_card(self):
        print("Play card action")
# Add player turns and hand display
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)
                # Update UI to show the new card in player's hand
                card_image = Image(source=f'path/to/{card.color}_{card.value}.png')
                self.add_widget(card_image)

class UnoGame(Widget):
    def next_turn(self):
        # Logic to handle player turns
        pass
from kivy.core.audio import SoundLoader
class UnoGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.draw_sound = SoundLoader.load('path/to/draw_sound.wav')
        self.play_sound = SoundLoader.load('path/to/play_sound.wav')
        self.background_music = SoundLoader.load('path/to/background_music.mp3')
        if self.background_music:
            self.background_music.play()

    def draw_card(self):
        if self.draw_sound:
            self.draw_sound.play()
        # Existing draw card logic

    def play_card(self):
        if self.play_sound:
            self.play_sound.play()
        # Existing play card logic
class UnoGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Existing code...
        self.current_player_index = 0
        self.direction = 1  # 1 for clockwise, -1 for counterclockwise

    def next_turn(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)
        self.update_current_player()

    def update_current_player(self):
        # Logic to update current player display on the UI
        pass

    def play_card(self, card):
        if card.value == "Skip":
            self.next_turn()
        elif card.value == "Reverse":
            self.direction *= -1
        elif card.value == "Draw Two":
            self.next_turn()
            self.players[self.current_player_index].draw(self.deck, 2)
        elif card.value == "Wild":
            # Prompt player to choose a color
            pass
        elif card.value == "Wild Draw Four":
            self.next_turn()
            self.players[self.current_player_index].draw(self.deck, 4)
            # Prompt player to choose a color
            pass
        # Existing play card logic
        super().play_card(card)
        self.next_turn()
class UnoGame(Widget):
    def choose_color(self):
        # Display color options and handle user input
        pass

    def play_card(self, card):
        if card.value in ["Wild", "Wild Draw Four"]:
            self.choose_color()
        # Existing play card logic
        super().play_card(card)
class UnoGame(Widget):
    def update_current_player(self):
        # Logic to update current player display on the UI
        current_player_label = Label(text=f"Current Player: {self.players[self.current_player_index].name}")
        self.add_widget(current_player_label)
class UnoGame(Widget):
    def play_card(self, card):
        super().play_card(card)
        if not self.players[self.current_player_index].hand:
            self.end_game(self.players[self.current_player_index])
        self.next_turn()

    def end_game(self, winner):
        # Display winner and end the game
        winner_label = Label(text=f"{winner.name} wins!")
        self.add_widget(winner_label)
        # Optionally, reset the game or exit
from kivy.uix.button import Button

class UnoGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.draw_button = Button(text="Draw Card", on_press=self.draw_card)
        self.add_widget(self.draw_button)
        self.play_buttons = []

    def draw_card(self, instance):
        # Logic to draw a card
        pass

    def update_play_buttons(self):
        for button in self.play_buttons:
            self.remove_widget(button)
        self.play_buttons = []
        for card in self.players[self.current_player_index].hand:
            btn = Button(text=str(card), on_press=lambda instance, card=card: self.play_card(card))
            self.play_buttons.append(btn)
            self.add_widget(btn)
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="Hello, Kivy!")

if __name__ == "__main__":
    TestApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

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

class UnoGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deck = Deck()
        self.players = [Player("Alice"), Player("Bob")]
        self.current_player_index = 0
        self.direction = 1  # 1 for clockwise, -1 for counterclockwise
        self.draw_sound = SoundLoader.load('path/to/draw_sound.wav')
        self.play_sound = SoundLoader.load('path/to/play_sound.wav')
        self.background_music = SoundLoader.load('path/to/background_music.mp3')
        if self.background_music:
            self.background_music.play()
        self.draw_button = Button(text="Draw Card", on_press=self.draw_card)
        self.add_widget(self.draw_button)
        self.play_buttons = []

    def draw_card(self, instance=None):
        if self.draw_sound:
            self.draw_sound.play()
        player = self.players[self.current_player_index]
        player.draw(self.deck)
        self.update_hand_display(player)

    def play_card(self, card):
        if self.play_sound:
            self.play_sound.play()
        player = self.players[self.current_player_index]
        player.play_card(card)
        self.update_hand_display(player)
        self.next_turn()

    def next_turn(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)
        self.update_current_player()

    def update_current_player(self):
        current_player_label = Label(text=f"Current Player: {self.players[self.current_player_index].name}")
        self.add_widget(current_player_label)

    def update_hand_display(self, player):
        for widget in self.children[:]:
            if isinstance(widget, Image):
                self.remove_widget(widget)
        for card in player.hand:
            card_image = Image(source=f'path/to/{card.color}_{card.value}.png')
            self.add_widget(card_image)

class UnoApp(App):
    def build(self):
        return UnoGame()

if __name__ == "__main__":
    UnoApp().run()
