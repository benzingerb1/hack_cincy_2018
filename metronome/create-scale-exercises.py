from api.models import Exercise

# Create array holding notes A-G
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# Create array holding all different scales (major, minor, pentatonic, myxolidian, dorian, etc)
scales = ['Major', 'Minor', 'Major Pentatonic', 'Minor Pentatonic', 'Blues', 'Myxolidian', 'Dorian']

# Outer for loop to go through each note
for note in notes:
    # Inner for loop to go through each scale
    for scale in scales:
<<<<<<< HEAD:create-scale-exercises.py
        # Within each inner loop, print out the note then the scale in order to create the title
        print(note, scale)
=======
        exerciseName = note + " " + scale
        print(exerciseName)
        e = Exercise(title=exerciseName)
        e.save()
# Inner for loop to go through each scale
# Within each inner loop, print out the title of
>>>>>>> 93d3f7d7cadbb409a1eefef776e2b459119a299e:metronome/create-scale-exercises.py

# YOU DO NOT NEED THE NOTES
