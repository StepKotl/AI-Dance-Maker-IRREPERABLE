# Stephan Kotl
# MidiInput - dataFilter

from basic_pitch.inference import predict
import os


inp = "Music_Editor\Music\Midi\Raw"
out = "Scripts"

# For every wav file
total = len(os.listdir(inp))
for i, mid in enumerate(os.listdir(inp)):
    # Loading bar
    print(f"{i+1}/{total} Done | {round((i+1)/total)}% Done                                                              ", end = "\r")

    # convert it
    model_output, midi_data, note_events = predict(f"{inp}\{mid}")
    # and save it
    midi_data.write(f"Music_Editor\Music\Midi\Clipped\{mid[0:len(mid) - 4]}.mid")

print(len(os.listdir(inp)))

