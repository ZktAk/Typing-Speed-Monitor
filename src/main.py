from pynput import keyboard
from spellchecker import SpellChecker
from time import time as tm
import time
import statistics
import pickle
import os

class Seasion:
    def __init__(self, path):
        self.raw = []
        self.wpm_history = []
        self.time = tm()
        self.last_save = self.time
        self.id = str(path) + "/" + str(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime()))

    def add(self):
        elapsed_seconds = tm() - self.time
        elapsed_minutes = elapsed_seconds / 60
        wpm = round(1/elapsed_minutes)
        self.raw.append(wpm)

        while len(self.raw) > 3:
            self.raw.pop(0)

        self.wpm_history.append(statistics.mean(self.raw))

        if self.time - self.last_save > 15:
                self.save()
                self.last_save = tm()

        self.time = tm()

    def save(self):
        os.makedirs(os.path.dirname(self.id), exist_ok=True)
        my_history_file = open(self.id, "wb")
        pickle.dump(self.wpm_history, my_history_file)
        my_history_file.close()



class Collector:
    def __init__(self, path):
        self.current_word = ""
        self.spell = SpellChecker()  # loads default word frequency list
        self.puctuation = [',', '.', '?', '!', ';', ':', '-', '_', '\'', '\"', '/', '\\', '|', '(', ')', '{', '}', '[', ']', '%',]
        self.seasion = Seasion(path)

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


    def check_word(self):
        if self.is_word(self.current_word):
            self.seasion.add()
        else:
            pass
        self.current_word = ""

    def on_press(self, key):
        try:
            character = '{0}'.format(key.char).lower()

            if character in self.puctuation:
                self.check_word()
            else:
                self.current_word += character

        except AttributeError:
            key = '{0}'.format(key)
            if not len(self.current_word) == 0:
                if key == "Key.space" or key == "Key.enter":
                    self.check_word()
                elif key == "Key.backspace":
                    self.current_word = self.current_word[0:-1]

    def is_word(self, word):
        return self.spell.known([word]) == {word}

    def on_release(self, key):
        try:
            character = '{0}'.format(key.char).lower()
            if character == "`":
                # Stop listener
                return False

        except AttributeError:
            pass

if __name__ == '__main__':

    tool = Collector(os.environ['sessions_path'])
    tool.start()
