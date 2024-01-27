# Stephan Kotl
# MidiFuckery - Dancemaker 20000

from mido import MidiFile, tick2second, tempo2bpm, second2tick    


def listed(mid):
    global tempos
    """
    Takes a midi input, and converts it into a matrix, with every row coinsciding with a tick of a midi file
    Midi runs on ticks. Some number of ticks are in a single beat, varrying depending on the midi. 
    """
    # Some variable definitions
    track = mid.merged_track
    ret = []
    TPB = mid.ticks_per_beat
    tempo = 0
    tempos = []
    activeNotes = {}

    # Defining each poin
    from math import floor


    for i in track:

        # There are 2 ways to make a note stop playing. Either have a on note have a velocity of 0, or have a off note.
        if i.type == "note_on":
            if i.velocity == 0:
                try: 
                    activeNotes.pop(i.note)
                except KeyError:
                    pass
            else:
                activeNotes.update({i.note:i})
        
        if i.type == "note_off":
            try: 
                activeNotes.pop(i.note)
            except KeyError:
                pass
        
        extraTime = 0
        # The notes, in combination, could have a shorter overall length depending on the tempo of the current section, and why this is taken
        if i.type == "set_tempo":
            tempo = i.tempo
        
        # The time variable in the message class of a Midi File describes the amount of time passed since the last message.
        # Messages are notes on/off, tempos, time signatures, etc.
        timePlayed = i.time + extraTime
        current16ths = timePlayed / (TPB / 16)

        # If there is at least one 16th played
        if current16ths >= 1:
            num16ths = floor(current16ths)

            extraTime = current16ths - num16ths
            # Add the amount of 16ths played, and the notes that were being played in them, alongside the tempo they were played at. 
            for i in range(num16ths):
                ret.append([tempo, [i for i in activeNotes]])
        else:
            extraTime += current16ths
          

    from pickler import vectorized_result

    out = []
    
    # Final formatting before returning
    for i in ret:
        current = i[1]
        if i[1] == []:
            current = [0]
        current.sort()
        current.reverse()

        # The AI only takes decimal inputs between 0 and 1 (the way it was designed), so merging the notes played into a single float value
        summation = "0."
        for i in current:
            for v in range(3 - len(str(i))):
                summation += "0"
            summation += str(i)

        out.append([float(summation)])
    return out
        
        
    debugging = "Fun!"
            


def split(notes):
    """
    Takes a note input of [[Tempo, [Active Notes on 16th 1]], [Tempo, [Active Notes on 16th 2]], ... ]
    and splits the midi file on every 8 beats.
    """
    # Split the 16th notes into every 8 beats
    from math import floor
    beats = 8
    beatsIn16ths = (beats * 16)
    splits = floor(len(notes) / beatsIn16ths)
    
    ret = []
    
    for i in range(splits):
        ret.append(notes[(i * beatsIn16ths):((i + 1) * beatsIn16ths) - 1 ])
        
    return ret
    


        
