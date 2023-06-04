from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.configure(bg='black')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white',
            padx=10,
            pady=10,
            borderwidth=0,
            highlightthickness=0)

lbl.pack(anchor='center')
time()

# Function to display the current date
def date():
    date_string = strftime('%B %d, %Y')
    date_lbl.config(text=date_string)
    date_lbl.after(60000, date)  # Update every minute

date_lbl = Label(root, font=('calibri', 20, 'bold'),
                 background='black',
                 foreground='white',
                 padx=10,
                 pady=10,
                 borderwidth=0,
                 highlightthickness=0)

date_lbl.pack(anchor='center')
date()

# Function to set an alarm
def set_alarm():
    alarm_time = entry.get()  # Get alarm time from entry widget
    # Code to set up the alarm using the alarm_time
    # You can use libraries like 'datetime' or 'threading' to implement this functionality

entry = Entry(root, font=('calibri', 20),
              bg='white',
              fg='black',
              justify='center')

entry.pack(anchor='center')
entry.insert(0, 'HH:MM')  # Placeholder text for the alarm time
set_alarm_btn = Button(root, text='Set Alarm', command=set_alarm)
set_alarm_btn.pack(anchor='center')

# Function to start a countdown timer
def start_countdown():
    countdown_time = entry.get()  # Get countdown time from entry widget
    # Code to start the countdown timer using the countdown_time
    # You can use libraries like 'datetime' or 'threading' to implement this functionality

entry = Entry(root, font=('calibri', 20),
              bg='white',
              fg='black',
              justify='center')

entry.pack(anchor='center')
entry.insert(0, 'MM:SS')  # Placeholder text for the countdown time
start_countdown_btn = Button(root, text='Start Countdown', command=start_countdown)
start_countdown_btn.pack(anchor='center')

# Functionality for a stopwatch
def start_stopwatch():
    # Code to start the stopwatch
    pass

def stop_stopwatch():
    # Code to stop the stopwatch and display the elapsed time
    pass

start_stopwatch_btn = Button(root, text='Start Stopwatch', command=start_stopwatch)
start_stopwatch_btn.pack(anchor='center')
stop_stopwatch_btn = Button(root, text='Stop Stopwatch', command=stop_stopwatch)
stop_stopwatch_btn.pack(anchor='center')

# Function to change the displayed timezone
def change_timezone():
    selected_timezone = timezone_combobox.get()  # Get the selected timezone
    # Code to update the displayed time based on the selected timezone
    pass

timezones = ['GMT', 'EST', 'CST', 'PST']  # Add more timezones as required
timezone_combobox = Combobox(root, values=timezones)
timezone_combobox.pack(anchor='center')
change_timezone_btn = Button(root, text='Change Timezone', command=change_timezone)
change_timezone_btn.pack(anchor='center')

def toggle_theme():
    if root.cget('bg') == 'black':
        root.configure(bg='white')
        lbl.configure(bg='white', fg='black')
        date_lbl.configure(bg='white', fg='black')
        entry.configure(bg='white', fg='black')
    else:
        root.configure(bg='black')
        lbl.configure(bg='black', fg='white')
        date_lbl.configure(bg='black', fg='white')
        entry.configure(bg='white', fg='black')

btn = Button(root, text="Toggle Theme", command=toggle_theme)
btn.pack(side=BOTTOM)

root.mainloop()
