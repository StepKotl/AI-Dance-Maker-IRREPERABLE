# Midi Dance Project
The goal of this project was to create a dancing avatar in Unity by inputting a MIDI input, and creating an associated dance via an AI
The input nodes were different sections of 8 bars of music, that each was associated with a different dance. 
The AI should've then taken the input, split it into 8 bar chunks, and associated it as closely as it could to an input piece, and spit out whatever
dance was associated to the selected bars
**NOTE: this was done BEFORE the AI boom in 2024**
===
There were several problems with my approach 
1. There are not enough publically available databases that have music in MIDI form associated with animations
2. The file type I used was incredibly niche and has _very_ little documentation
3. The music had to be converted from MP3 to MIDI, which can only be done via AI approximations, with automated version being very few and far between

===
If I were to do this project again:
1. I would actually learn from projects that have done this exact thing in the past, and try to see if their databases were available
2. Instead of analyzing MIDI files, I would just approximate MP3 sound waves to each other, which would likely work wonders
3. Learn Unity, and build the underlying platform so that I could test the actual output to see if that idea would even be viable
