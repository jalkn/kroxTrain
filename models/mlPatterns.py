import tensorflow as tf
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Data loading and preprocessing (placeholder)
# Assume X_train, y_train, X_val, y_val are defined here.
# Also assume vocab_size, embedding_dim, hidden_units, 
# max_sequence_length, and epochs are defined.


# Movement patterns (using lists for easier indexing)
movement_patterns = {
    "Walk/Run": ["Walk", "Lunges", "Run", "Jumping lunges", "Broad jumping lunges", "Sprint"],
    "Jump": ["Air squat", "Single unders", "Jumping squat", "Single jumps", "Broad jumps", "Double unders"],
    "Push": ["Shoulder tap", "Push-up", "Pike push-up", "Handstand push-up", "Handstand walk"],
    "Pull": ["Ring rows", "Banded pull-ups", "Strict pull-ups", "Kipping pull-ups", "Muscle ups"],
    "Stand-Up": ["Step-up burpee", "Burpee", "Burpee to muscle up", "Burpee with jump", "Burpee with broad jump"],
}

# Flatten the movement patterns and create mappings
all_exercises = [ex for group in movement_patterns.values() for ex in group]
label_encoder = LabelEncoder()
label_encoder.fit(all_exercises)

# Convert y_train and y_val to numerical labels
y_train_encoded = np.array([[label_encoder.transform([ex])[0] for ex in seq] for seq in y_train])
y_val_encoded = np.array([[label_encoder.transform([ex])[0] for ex in seq] for seq in y_val])


# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim),  # Input is user features
    tf.keras.layers.LSTM(units=hidden_units),  # Encoder
    tf.keras.layers.RepeatVector(n=max_sequence_length),  # Prepare for decoder
    tf.keras.layers.LSTM(units=hidden_units, return_sequences=True),  # Decoder
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=len(all_exercises), activation='softmax'))  # Output
])


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# One-hot encode the target sequences
def one_hot_encode(sequences, num_classes):
    encoded = np.zeros((sequences.shape[0], sequences.shape[1], num_classes), dtype=np.float32)
    for i, seq in enumerate(sequences):
        for j, val in enumerate(seq):
            encoded[i, j, val] = 1.0
    return encoded

y_train_onehot = one_hot_encode(y_train_encoded, len(all_exercises))
y_val_onehot = one_hot_encode(y_val_encoded, len(all_exercises))


model.fit(X_train, y_train_onehot, epochs=epochs, validation_data=(X_val, y_val_onehot))


# Generate predictions and decode
predictions = model.predict(X_val)
predicted_sequences = np.argmax(predictions, axis=-1)
decoded_predictions = [[label_encoder.inverse_transform([ex])[0] for ex in seq] for seq in predicted_sequences]

# ... (evaluate decoded_predictions) ..