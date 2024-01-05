import random
import time
from tkinter import END, Button, Label, StringVar, Text, Tk


class TypingSpeedTestApp:
    '''A simple typing speed test application using Tkinter.'''

    def __init__(self, root):
        '''
        Initialize the TypingSpeedTestApp.

        Parameters:
        - root (Tk): The main Tkinter window.
        '''
        self.root = root
        self.root.title('Typing Speed Test')

        self.passages = ['The quick brown fox jumps over the lazy dog.',
                         'Programming is fun and challenging.',
                         'Type fast, but also type accurately.',
                         'Practice makes perfect.',
                         'Keep calm and code on.']

        self.current_passage = StringVar()
        self.current_passage.set(random.choice(self.passages))

        self.time_start = 0
        self.time_end = 0

        self.create_widgets()

    def create_widgets(self):
        '''Create and configure the GUI widgets.'''
        self.passage_label = Label(
            self.root, textvariable=self.current_passage, wraplength=400, font=('Helvetica', 12))
        self.passage_label.pack(pady=10)

        self.text_entry = Text(self.root, height=5,
                               width=50, font=('Helvetica', 12))
        self.text_entry.pack(pady=10)

        self.start_button = Button(
            self.root, text='Start Typing Test', command=self.start_typing_test)
        self.start_button.pack(pady=10)

    def start_typing_test(self):
        '''Start the typing test.'''
        self.text_entry.delete('1.0', END)  # Clear previous text
        self.current_passage.set(random.choice(self.passages))
        self.time_start = time.time()
        self.root.bind('<Return>', self.end_typing_test)

    def end_typing_test(self, event):
        '''End the typing test.'''
        self.time_end = time.time()
        self.root.unbind('<Return>')
        self.calculate_speed()

    def calculate_speed(self):
        '''Calculate and display the typing speed and accuracy.'''
        entered_text = self.text_entry.get('1.0', END)
        words_per_minute = len(entered_text.split()) / \
            ((self.time_end - self.time_start) / 60)
        accuracy = self.calculate_accuracy(entered_text)

        result_message = f'Your typing speed: {words_per_minute:.2f} words per minute\nAccuracy: {accuracy:.2f}%'
        result_label = Label(self.root, text=result_message,
                             font=('Helvetica', 12))
        result_label.pack(pady=10)

    def calculate_accuracy(self, entered_text):
        '''
        Calculate the typing accuracy.

        Parameters:
        - entered_text (str): The text entered by the user.

        Returns:
        - float: The accuracy percentage.
        '''
        reference_text = self.current_passage.get()
        correct_characters = sum(1 for a, b in zip(
            reference_text, entered_text) if a == b)
        total_characters = max(len(reference_text), len(entered_text))

        accuracy = (correct_characters / total_characters) * 100
        return accuracy


if __name__ == '__main__':
    root = Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
