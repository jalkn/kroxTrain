movement_patterns = {
    "Walk/Run": {
        1: "Walk",
        2: "Lunges",
        3: "Run",
        4: "Jumping lunges",
        5: "Broad jumping lunges",
        6: "Sprint"
    },
    "Jump": {
        1: "Air squat",
        2: "Single unders",
        3: "Jumping squat",
        4: "Single jumps",
        5: "Broad jumps",
        6: "Double unders"
    },
    "Push": {
        1: "Shoulder tap",
        2: "Push-up",
        3: "Pike push-up",
        4: "Handstand push-up",
        5: "Handstand walk"
    },
    "Pull": {
        1: "Ring rows",
        2: "Banded pull-ups",
        3: "Strict pull-ups",
        4: "Kipping pull-ups",
        5: "Muscle ups"
    },
    "Stand-Up": {
        1: "Step-up burpee",
        2: "Burpee",
        3: "Burpee to muscle up",
        4: "Burpee with jump",
        5: "Burpee with broad jump",
        
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
