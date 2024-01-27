# Stephan Kotl
# MidiInput - Dancemaker 20000

def midInput():
    from mido import MidiFile, tempo2bpm
    from os import path
    
    
    # This entire script wasn't used, but was going to be implemented if everything in unity was done. 

    baseDir = "Music Editor/Music"
    
    # Take a input from the user
    inp = input("Name the midi file that you want to use: \n> ")
    
    # for Faster Testing, return if "t"
    if inp.lower() == "t":
        return MidiFile("Music Editor/Music/MiiChannel.mid")
    
    # Until a there is a midi file with a type of 1, keep asking for an input. 
    while True:
        inpDir = path.join(baseDir, inp) + ".mid"  
        
        if path.isfile(inpDir):
            mid = MidiFile(inpDir)
            
            if mid.type != 1:
                inp = input("The midi needs to be type 1. Try again:\n>")
            else:
                break
            
        
        else:
            inp = input("Not a valid file path, try again: \n> ")
    
    return mid
        
            
        
        
