import os
import tkinter as tk
from timeit import default_timer as timer
import random

# Firstly make a list of sentences into a file
def sentences_to_write():
    sentences = [
        'School Has Always been fun.',
        "Try not to be petty it's not good",
        "All work and no play makes Jack a dull boy",
        'It takes two to Quarrel',
        'And I kept Running for a Safe Place to Find.'
    ]

    file = open('sentences.txt', 'w')
    for sentence in sentences:
        file.write(sentence + '\n')
    file.close()

# Now we need to load sentences from the file
def load_sentences(sentences):
    file = open('sentences.txt', 'r')
    sentences = []
    for line in file:
        sentences.append(line.strip())
    file.close()
    return sentences

# Function to save player score to the scoreboard file

def save_score(name, time):
    scores = read_scores()
    fileobj = open('scoreboard.txt', 'w')
    update = False
    for score in scores:
        if score[0] == name:
            score[1] = time
            update = True
        fileobj.write(f'{score[0]}: {score[1]} seconds\n')
    if not update:
        fileobj.write(f'{name}: {time} seconds\n')
    fileobj.close()

# Function to read scores from the file

def read_scores():
    scores = []
    try:
        fileobj = open('scoreboard.txt', 'r')
        for line in fileobj:
            name, time = line.strip().split(': ')
            scores.append((name, time))
        fileobj.close()
    except FileNotFoundError:
        pass
    return scores

# Function to display scores
#Video
def display_scores():
    scores = read_scores()
    if not scores:
        return ["No scores available"]
    
    sorted_scores = sorted(scores, key=lambda x: x[1])
    formatted_scores = []
    for name, time in sorted_scores:
        formatted_scores.append(f'{name}: {time} seconds')
    return formatted_scores

# Function to delete all scores
#video
def delete_all_scores():
    if os.path.exists('scoreboard.txt'):
        os.remove('scoreboard.txt')

 
# Open scoreboard window
def open_scoreboard_window():
    def refresh_scoreboard():
        scores = display_scores()
        formatted_scores = '\n'.join(scores)
        scoreboard_text.set(formatted_scores)


    def delete_all():
        delete_all_scores()
        refresh_scoreboard()

# Function to open the scoreboard window
def open_scoreboard_window():
    # Function to refresh the scoreboard
    def refresh_scoreboard():
        scores = display_scores()
        formatted_scores = '\n'.join(scores)
        scoreboard_text.set(formatted_scores)
        
    def delete_all():
        delete_all_scores()
        refresh_scoreboard()

    # GUI for the scoreboard window
    scores = display_scores()
    scoreboard_window = tk.Toplevel()
    scoreboard_window.geometry('500x500')
    scoreboard_window.title('Scoreboard')

    tk.Label(scoreboard_window, text='Scoreboard', font='times 20').pack()

    scoreboard_text = tk.StringVar(value='\n'.join(scores))
    tk.Label(scoreboard_window, textvariable=scoreboard_text, font='times 14', justify=tk.LEFT).pack()

    delete_all_button = tk.Button(scoreboard_window, text='Delete All Scores', command=delete_all, width=12, bg='lightblue')
    delete_all_button.pack()


# Function for checking typing speed
# Typing speed checker function

def speed_test():
    sentences = load_sentences('sentences.txt')
    sentence = random.choice(sentences)
    start = timer()
    result_calculated = False  # To keep track if the result has been calculated
    
    # Typing speed test with Python [MINI PROJECT] [video]
    
    def check_result():
        nonlocal result_calculated
        
        if not result_calculated:
            end = timer()
            time_taken = round((end - start), 3)
            name = name_entry.get()
            
            if not name:
                label_3.configure(text='Please enter your name')
                
            elif not all(char.isalnum() or char.isspace() for char in name):
                label_3.configure(text='Invalid characters in name')
                
            elif entry.get() == sentence:
                save_score(name, time_taken)
                global result_text
                result_text = f'Correct! Time: {time_taken} seconds'
                
            else:
                result_text = 'Wrong Input'
                
            label_3.configure(text=result_text)
            result_calculated = True  # To prevent further calculations


    main_window = tk.Tk()
    main_window.geometry('800x600')
    main_window.title("Typing Speed Test")


    tk.Label(main_window, text='Enter your name:', font='times 20').pack()
    name_entry = tk.Entry(main_window, font='times 20', width=30)
    name_entry.pack()

    tk.Label(main_window, text=sentence, font='times 20').pack()
    tk.Label(main_window, text='Start Typing:', font='times 20').pack()

    entry = tk.Entry(main_window, font='times 20', width=50)
    entry.pack()

   

    tk.Button(main_window, text='Done', command=check_result, width=10, bg='lightblue').place(x=350, y=200)
    tk.Button(main_window, text='Try Again', command=lambda: [main_window.destroy(), speed_test()], width=10, bg='lightblue').place(x=350, y=250)
    tk.Button(main_window, text='Scoreboard', command=open_scoreboard_window, width=10,bg='lightblue').place(x=350, y=300)

    label_3 = tk.Label(main_window, text='', font='times 20')
    label_3.place(x=325, y=400)

    main_window.mainloop()

sentences_to_write()
speed_test()
