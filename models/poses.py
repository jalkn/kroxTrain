movement_patterns = {
    "mobility": {
    1: "frog", 
    2: "saddle",
    3: "pigeon",
    4: "sit forward fold",
    5: "lizard flex arm",
    6: "lizard extend arm",
    7: "sit crashing arm",
    8: "single leg forward bend",
    9: "seated straddle",
    10: "puppy dog",  # Corrected spelling
    11: "sumo squat",
    12: "butterfly",
    13: "half-kneeling hip flexor stretch",
    14: "90/90 stretch",
    15: "dorsiflexion/plantarflexion ankle",
    16: "figure 4 stretch (seated/supine)", # Added
    17: "dragon pose",
    18: "shoulder dislocations",
    19: "thoracic spine rotations",
    20: "cat-cow",
    21: "supine spinal twist",
    22: "child's pose",
    23: "happy baby",
    24: "deep squat",
    25: "couch stretch",
    26: "standing hip circles", # Added
    27: "leg swings (forward/backward/sideways)", # Added
    28: "arm circles (forward/backward)", # Added
    29: "world's greatest stretch",
    30: "supine stretch",
    31: "thread the needle pose",  # Added - good shoulder and thoracic mobility
    32: "pretzel stretch", # Added - targets glutes and outer hips
    33: "knee hugs", # Added - gentle warm-up for hips and lower back
    34: "seated spinal twist", # Added - variation on supine spinal twist
    35: "ankle rolls", # Added - ankle mobility
    36: "wrist circles/flexion/extension", # Added - wrist mobility
    37: "neck rotations/tilts", # Added - neck mobility (carefully)
    38: "butterfly with forward fold", # Added deeper variation
    39: "wide legged child's pose", #Added good for inner thighs/groin
    40: "reclined butterfly", #Added relaxing hip opener
    41: "bound angle pose variation with forward fold", #Added more advanced hip opener
    42: "half lord of the fishes pose", #Added good for spine rotation
    43: "sphinx pose", #Added gentle backbend
    44: "seal pose" #Added deeper backbend than sphinx
},
    "Jump": {
        1: "Air squat",
        2: "Single unders",
        3: "Jumping squat",
        4: "Single jumps",
        5: "Broad jumps",
        6: "Double unders",
        7: "Front squat",
        8: "Overhead squat",
        9: "Globet squat",
        10: "Pistol squat",
        11: 'Box Jump 20/24"',
        12: "Box step-ups"
        
    },
    "Push": {
        1: "Shoulder tap",
        2: "Push-up",
        3: "Handstand push-up",
        4: "Handstand walk",
        5: "Pike push-up",
        6: "Push press",
        7: "Shoulder press",
        8: "Push Jerk",
        9: "Bench press",
        10: "Arnold press",
        11: "Incline dumbbell press",
        12: "Decline dumbbell press",
        13: "Dumbbell flyes",
    },
    "Pull": {
        1: "Ring rows",
        2: "Kipping pull-ups",
        3: "Strict pull-ups",
        4: "Good mornings",
        5: "Pullovers",
        6: "Deadlift",
        7: "Snatch high pull",
        8: "Clean pull",
        10: "Hang power clean",
        11: "Hang clean",
        12: "Hang power snatch",
        13: "Hang snatch",
        14: "Kettlebell swings"
    },
    "Stand-Up": {
        1: "Step-up burpee",
        2: "Burpee",
        3: "Burpee to muscle up",
        4: "Burpee with jump",
        5: "Burpee with broad jump",
        5: "Muscle ups",
        7: "Burpee to Muscle ups",
        8: "Mountain climbers",
        9: "Burpee box jump over",
        10: "Burpee bar jump over",
        9: "Power Clean & Jerk",
        9: "Snatch",
        9: "ground to overhead",
        14: "Thruster"
        
        
    },
    "Stand-Up": {
    "Beginner": ["Step-up burpee", "Mountain climbers"],
    "Intermediate": ["Burpee", "Burpee with jump", "Burpee with broad jump"],
    "Advanced": ["Burpee to muscle up", "Muscle ups", "Burpee Muscle ups", "Burpee box jump over", "Burpee bar jump over"],
}
}

#example of usage
print(movement_patterns["Walk/Run"][3])  # Output: Running at steady pace
print(movement_patterns["Jump"][1])  # Output: Air squat
print(movement_patterns["Pull"][6]) # Output: Muscle ups 


for pattern, exercises in movement_patterns.items():
    print(f"\n{pattern} Pattern:")
    for move, exercise in exercises.items():
        print(f"  Movement {move}: {exercise}") 


