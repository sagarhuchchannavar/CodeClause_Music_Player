import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Initialize the pygame mixer
pygame.init()
pygame.mixer.init()

# Create the music player window
music_player = tkr.Tk()
music_player.title('Py Music Player')
music_player.geometry('450x350')

# Ask for the directory containing music files
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# Create a listbox to display the song list
play_list = tkr.Listbox(music_player, font='Helvetica 12 bold', bg='black', fg='white', selectbackground='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    play_list.insert(tkr.END, item)

# Function to play the selected song
def play():
    song = play_list.get(tkr.ACTIVE)
    pygame.mixer.music.load(song)
    var.set(song)
    pygame.mixer.music.play()

# Function to stop playback
def stop():
    pygame.mixer.music.stop()

# Function to pause playback
def pause():
    pygame.mixer.music.pause()

# Function to unpause playback
def unpause():
    pygame.mixer.music.unpause()

# Create buttons with matching colors
Button1 = tkr.Button(music_player, width=6, height=2, font='Helvetica 12 bold', text='PLAY', command=play, bg='green', fg='white')
Button2 = tkr.Button(music_player, width=6, height=2, font='Helvetica 12 bold', text='STOP', command=stop, bg='red', fg='white')
Button3 = tkr.Button(music_player, width=6, height=2, font='Helvetica 12 bold', text='PAUSE', command=pause, bg='purple', fg='white')
Button4 = tkr.Button(music_player, width=6, height=2, font='Helvetica 12 bold', text='RESUME', command=unpause, bg='orange', fg='white')

# Create a label to display the currently playing song
var = tkr.StringVar()
song_title = tkr.Label(music_player, font='Helvetica 12 bold', textvariable=var, bg='black', fg='white')

# Pack widgets
song_title.pack()
Button1.pack(fill='x', side='left', padx=10)
Button2.pack(fill='x', side='left', padx=10)
Button3.pack(fill='x', side='left', padx=10)
Button4.pack(fill='x', side='left', padx=10)
play_list.pack(fill='both', expand='yes', padx=10, pady=10)

# Start the Tkinter main loop
music_player.mainloop()
