# Stephan Kotl
# MidiInput - Main


from MidiInput import midInput
from midiFuckery import *
from mido import MidiFile
from Network import *
from Trainer import load_data
import os

def run(fileDir):
    # Define the midi
    print("Openning Mid File")
    mid = MidiFile(fileDir)
    
    
    # Format the notes into the following:
    # [[Active Notes on Tick 1], [Active Notes on Tick 2], ... ]
    print("Formatting Midi")
    notes = listed(mid)
    
    print("Splitting Midi")
    splits = split(notes)
    
    
    
    
    # Create the AI
    training_data, validation_data, test_data = load_data()
    net = Network([127, 1000, 5000, 10385])


    net.large_weight_initializer()
    # Train 
    net.SGD(training_data, 30, 500, 0.1, monitor_evaluation_accuracy=True, evaluation_data=validation_data)
    
    # This was meant to test every section in the current piece and return a list of dances, but I didn't get to that point. 
    net.save("Music_Editor\CurrentNetwork.json")
    dances = []
    for i in [1]:
        dances.append(net.feedforward(i))
    print(dances)


run("Music_Editor/Music/FullSongs/Mario.mid")
"""
import Trainer
training_data, validation_data, test_data = Trainer.load_data_wrapper()
import Network

# For every beat in the eight avaliable:
# What is playing in each 16th
# How long is the length of the remaining note and what note is it playing (Maybe smth different depending on how the AI reacts)

net = Network.Network([256, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
"""