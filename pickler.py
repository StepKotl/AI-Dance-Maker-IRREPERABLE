# Stephan Kotl
# MidiInput - pickler


file = []
import os
import pickle
import numpy as np
from mido import MidiFile
from midiFuckery import *


def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    
    e = np.zeros((10385, 1))
    e[j] = 1.0
    return e



def pickled():
    # For every midi training file
    training = []
    for v, midi in enumerate(os.listdir("Music_Editor/Music/Midi/Raw")):
        mid = MidiFile(f"Music_Editor/Music/Midi/Raw/{midi}")

        # take the notes from the split version of the file
        for i, notes in enumerate(split(listed(mid))):
            
            # Split it and format it so the AI can read it
            file.append(tuple([np.array(notes), len(file)]))

            # 
            training.append(tuple([np.array(notes), vectorized_result(len(file))]))
    
    from math import floor
    from random import shuffle
    # Randomize the files (Although it changes how the AI trains, it's better than having everything in order so the AI finds a basic pattern that we don't want it to have)
    shuffle(file)
    shuffle(training)

    splitPoint = floor(len(file) / 2)
    # Take some random validation and test_data values. 
    validation_data = file[: splitPoint]
    test_data = file[splitPoint :]

    
    
    # Save the training data in a pickle file to be loaded at a later time. 
    with open("Music_Editor/Music/Midi/trainingData.pkl", "wb") as f:
        pickle.dump([training, validation_data, test_data], f)
        


