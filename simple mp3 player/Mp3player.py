from tkinter import *
from tkinter import filedialog
from pygame import mixer
import time
import tkinter.ttk as ttk
import pygame
import numpy as np
import librosa
import soundfile as sf
import wave
import matplotlib.pyplot as plt

# ********************
def slide(x):
    song = play_list.get(ACTIVE)
    song = f"{song}"
    mixer.music.load(song)
    mixer.music.play()


def volume(x):
    pygame.mixer.music.set_volume(vs.get())
    cv = pygame.mixer.music.get_volume()
    sl.config(text=int((cv * 100)))
    cv = int(cv * 100)
    if cv < 1:
        vm.config(image=vol0)
        voll.config(image=silent)
    elif cv > 0 and cv <= 25:
        vm.config(image=vol1)
        voll.config(image=vol)
    elif cv > 25 and cv <= 50:
        vm.config(image=vol2)
        voll.config(image=vol)
    elif cv > 50 and cv <= 75:
        vm.config(image=vol3)
        voll.config(image=vol)
    elif cv > 75 and cv <= 100:
        vm.config(image=vol4)
        voll.config(image=vol)


# ******************
def original():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal7 = librosa.effects.time_stretch(signal, rate=1)
    sf.write("augmented8.wav", augmented_signal7, sr)
    pygame.mixer.music.load("augmented8.wav")
    mixer.music.play()
    wav0 = wave.open("augmented8.wav", "r")
    raw = wav0.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav0.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" original audio ")
    plt.plot(time, raw, color="lightblue")
    plt.ylabel("Amplitude")
    plt.show()


# increase amplitude *********


def scale():
    y, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal5 = librosa.effects.pitch_shift(y, sr=sr, n_steps=6)
    sf.write("augmented6.wav", augmented_signal5, sr)
    pygame.mixer.music.load("augmented6.wav")
    mixer.music.play()
    wav2 = wave.open("augmented6.wav", "r")
    raw = wav2.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav2.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" Expansion ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# Decrease amplitude  **************
def scale1():
    y, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal5 = librosa.effects.pitch_shift(y, sr=sr, n_steps=-6)
    sf.write("augmented7.wav", augmented_signal5, sr)
    pygame.mixer.music.load("augmented7.wav")
    mixer.music.play()
    wav2 = wave.open("augmented7.wav", "r")
    raw = wav2.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav2.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" Expansion ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# increase the speed of the song *******
def compress():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal3 = librosa.effects.time_stretch(signal, rate=2)
    sf.write("augmented2.wav", augmented_signal3, sr)
    pygame.mixer.music.load("augmented2.wav")
    mixer.music.play()
    wav3 = wave.open("augmented2.wav", "r")
    raw = wav3.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav3.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" Compression ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# decrease the speed of the song *******
def expansion():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal2 = librosa.effects.time_stretch(signal, rate=0.5)
    sf.write("augmented3.wav", augmented_signal2, sr)
    pygame.mixer.music.load("augmented3.wav")
    mixer.music.play()
    wav2 = wave.open("augmented3.wav", "r")
    raw = wav2.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav2.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" Expansion ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# ***********************************
def add_white_noise(signal, noise_percentage_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal


def whitenoise():
    signal, sr = librosa.load(
        play_list.get(ACTIVE)
    )  # load the active song on play list
    augmented_signal1 = add_white_noise(
        signal, 0.2
    )  # rate =0.2 if we increase it's value the white noise increase
    sf.write("augmented4.wav", augmented_signal1, sr)
    pygame.mixer.music.load("augmented4.wav")
    mixer.music.play()
    wav1 = wave.open("augmented4.wav", "r")
    raw = wav1.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav1.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" with white noise ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# *********************************************************************
def addsongs():
    songselect = filedialog.askopenfilenames(
        initialdir="Documents/",
        title="choose songs",
        filetypes=(("mp3 files", "*.mp3"),),
    )
    for s in songselect:
        s = s.replace("C:/Users/eslam/OneDrive/Documents/", "")
        play_list.insert(END, s)


# ***********************************
def deletesong():
    cursong = play_list.curselection()
    play_list.delete(cursong[0])


# Delay song 5 second  ****************
def delay():
    song = play_list.get(ACTIVE)
    song = f"{song}"
    mixer.music.load(song)
    time.sleep(5)
    mixer.music.play()


# ***************************************
def playsong():
    music = play_list.get(ACTIVE)
    music = f"{music}"
    mixer.music.load(music)
    mixer.music.play()


# ********************************************
def stopmusic():
    mixer.music.stop()
    play_list.select_clear(ACTIVE)


# ************************************************
def pausemusic():
    mixer.music.pause()


# ***************************************
def resumemusic():
    mixer.music.unpause()


# next music function **************
def nextmusic():
    nextone = play_list.curselection()
    nextone = nextone[0] + 1
    song = play_list.get(nextone)
    song = f"{song}"
    mixer.music.load(song)
    mixer.music.play()
    play_list.select_clear(0, END)
    play_list.activate(nextone)
    play_list.select_set(nextone)


# previos function*************
def prevmusic():
    prev1 = play_list.curselection()
    prev1 = prev1[0] - 1
    song = play_list.get(prev1)
    song = f"{song}"
    mixer.music.load(song)
    mixer.music.play()
    play_list.select_clear(0, END)
    play_list.activate(prev1)
    play_list.select_set(prev1)


# *************************
def skip_forward():
    current_pos = mixer.music.get_pos() // 1000
    new_pos = current_pos + 0.001
    mixer.music.set_pos(new_pos * 10)


# *************************
def reverse():
    y, sr = librosa.load(play_list.get(ACTIVE))
    y_reverse = y[::-1]
    sf.write("augmented9.wav", y_reverse, sr)
    pygame.mixer.music.load("augmented9.wav")
    mixer.music.play()


# *******************************
def echo():
    # signal, sr = librosa.load(play_list.get(ACTIVE))
    # echo_signal = np.zeros_like(signal)
    # delay = 0.5
    # decay = 0.5
    # offset = int(delay * sr)
    # echo_signal[offset:] = signal[:-offset] + decay * signal[offset:]
    # sf.write('augmented10.wav', echo_signal, sr)
    # Get the audio data and sample rate
    signal, sr = librosa.load(play_list.get(ACTIVE))
    # Create a delayed version of the signal with a delay of 0.5 seconds
    delay = int(0.5 * sr)
    delayed_signal = np.zeros_like(signal)
    delayed_signal[delay:] = signal[:-delay]
    # Add the delayed signal to the original signal with an amplitude of 0.5
    echo_signal = signal + 0.5 * delayed_signal
    # Save the echo signal to a temporary file
    sf.write("echo.wav", echo_signal, sr)
    pygame.mixer.music.load("echo.wav")
    pygame.mixer.music.play()
    wav1 = wave.open("echo.wav", "r")
    raw = wav1.readframes(-1)
    raw = np.frombuffer(raw, "int16")
    sampleRate = wav1.getframerate()
    time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
    plt.title(" echo ")
    plt.plot(time, raw, color="green")
    plt.ylabel("Amplitude")
    plt.show()


# Design window form **********************
win = Tk()
win.geometry("750x610")
win.title("Music Player")
img = PhotoImage(file=r"b.png")
win.iconphoto(False, img)
win.configure(bg="#0f1a2b")
mixer.init()
# *************************
mymenu = Menu(win)
win.config(menu=mymenu)
controlsongmenu = Menu(mymenu)
mymenu.add_cascade(label="Menu", menu=controlsongmenu)

controlsongmenu.add_command(label="add songs", command=addsongs)
controlsongmenu.add_command(label="delete song", command=deletesong)
# *****************************
mp = PhotoImage(file="mp3 (1).png")
mpl = Label(win, image=mp, background="#0f1a2b")
mpl.place(x=0, y=475)
wav = PhotoImage(file="wave (2).png")
mpl3 = Label(win, image=wav, background="#0f1a2b")
mpl3.place(x=125, y=540)
mpl2 = Label(win, image=mp, background="#0f1a2b")
mpl2.place(x=630, y=475)
em = PhotoImage(file="emoji (4).png")
eml = Label(win, image=em, background="#0f1a2b")
eml.place(x=610, y=358)
# # eml.place(x=665,y=20)
# *******************************

# define volume images and make them glopal to use in any function *********************
global silent
global vol0
global vol1
global vol2
global vol3
global vol4
silent = PhotoImage(file="hj (1).png")
vol0 = PhotoImage(file="volume0.png")
vol1 = PhotoImage(file="volume1.png")
vol2 = PhotoImage(file="volume2.png")
vol3 = PhotoImage(file="volume3.png")
vol4 = PhotoImage(file="volume4.png")
# design list box ********
play_list = Listbox(
    win,
    bg="cadetblue",
    fg="black",
    font="arial",
    height=18,
    width=72,
    selectmode=SINGLE,
    selectbackground="gray",
    selectforeground="black",
)
play_list.grid(columnspan=9)
# **********************************
k = PhotoImage(file="p1 (2).png")
playbtn = Button(win, command=playsong, width=60, height=60, image=k, bg="#0f1a2b")
playbtn.grid(row=3, column=0)
# *************************
p = PhotoImage(file="pau.png")
pausebtn = Button(
    win, text="Pause", command=pausemusic, image=p, height=60, width=60, bg="#0f1a2b"
)
pausebtn.grid(row=3, column=1)
# ***************************
s = PhotoImage(file="st.png")
stopbtn = Button(win, command=stopmusic, image=s, height=60, width=60, bg="#0f1a2b")
stopbtn.grid(row=3, column=2)
# *************************************
g = PhotoImage(file="esl (2).png")
resumebtn = Button(win, command=resumemusic, width=60, height=60, image=g, bg="#0f1a2b")
resumebtn.grid(row=3, column=3)
# ************************
pr = PhotoImage(file="prev (1).png")
prevbtn = Button(
    win, text="Prev", command=prevmusic, image=pr, width=60, height=60, bg="#0f1a2b"
)
prevbtn.grid(row=3, column=4)
# ***********************************
next = PhotoImage(file="prev (2).png")
nextbtn = Button(win, command=nextmusic, image=next, width=60, height=60, bg="#0f1a2b")
nextbtn.grid(row=3, column=5)
# ***************
white = PhotoImage(file="white noise (1).png")
whitenoisebtn = Button(
    win, command=whitenoise, image=white, width=123, height=60, bg="#0f1a2b"
)
whitenoisebtn.grid(row=3, column=6)
# ***************************************
ex = PhotoImage(file="expansion (1).png")
expanbtn = Button(
    win,
    text="expansion",
    command=expansion,
    image=ex,
    height=60,
    width=123,
    bg="#0f1a2b",
)
expanbtn.grid(row=3, column=7)
# *************************************
com1 = PhotoImage(file="compression (1).png")
compbtn = Button(
    win,
    text="compression",
    command=compress,
    image=com1,
    width=125,
    height=60,
    bg="#0f1a2b",
)
compbtn.grid(row=4, column=0, columnspan=2)
# ***************************
inc = PhotoImage(file="amp+ (1).png")
incrbtn = Button(
    win, text="increase", command=scale, image=inc, width=125, height=60, bg="#0f1a2b"
)
incrbtn.grid(row=4, column=4, columnspan=2)
# ********************************
dec = PhotoImage(file="dec2 (1).png")
incrbtn = Button(
    win, text="increase", command=scale1, image=dec, width=125, height=60, bg="#0f1a2b"
)
incrbtn.grid(row=4, column=2, columnspan=2)
# **************************************
ori = PhotoImage(file="origin (1).png")
oribtn = Button(
    win,
    text="original",
    width=123,
    height=60,
    bg="#0f1a2b",
    image=ori,
    command=original,
)
oribtn.grid(row=4, column=6)
# ********************
de = PhotoImage(file="delay (1).png")
debtn = Button(win, command=delay, image=de, width=123, height=60, bg="#0f1a2b")
debtn.grid(row=4, column=7)
# **********************************
echo1 = PhotoImage(file="echo (1).png")
echob = Button(win, image=echo1, command=echo, width=125, height=60, bg="#0f1a2b")
echob.place(x=153, y=478)
# *******************************
revers = PhotoImage(file="reverse (1).png")
rev = Button(win, image=revers, command=reverse, width=125, height=60, bg="#0f1a2b")
rev.place(x=285, y=478)
# *****************************************
skip = PhotoImage(file="skip (1).png")
skipp = Button(
    win, image=skip, command=skip_forward, width=125, height=60, bg="#0f1a2b"
)
skipp.place(x=418, y=478)
# create a volume slider
vs = ttk.Scale(
    win,
    from_=1,
    to=0,
    orient=VERTICAL,
    cursor="hand2",
    value=0.25,
    length=200,
    command=volume,
)
vs.place(x=690, y=55)
# **********
sl = Label(win, text="25")
sl.place(x=715, y=145)
# ***********************
vm = Label(win, image=vol1)
vm.place(x=656, y=265)
#  ***********
global vol
vol = PhotoImage(file="vol (2).png")
voll = Label(win, image=vol, background="#0f1a2b")
voll.place(x=682, y=5)
# *******************

win.mainloop()
