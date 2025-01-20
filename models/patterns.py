movement_patterns = {
    "Walk/Run": {
        1: "Walk", 
        2: "Lunges",
        3: "Run",
        4: "Jumping lunges",
        5: "Broad jumping lunges",
        6: "Sprint",
        7: "Overhead lunges",
        8: "Reverse Lunges",
        9: "Curtsy Lunges",
        10: "Lateral Lunges",
        11: "Walking Lunges with Rotation (Twist)",
        12: "Deficit Reverse Lunges"  
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


