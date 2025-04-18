import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/full_dataset.csv")  # Make sure this file exists and is merged

# Combine features
df["features"] = df["Subjects"].fillna('') + " " + df["Hobbies"].fillna('') + " " + df["Dream Job"].fillna('')

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["features"])

# Encode labels
le = LabelEncoder()
y = le.fit_transform(df["Recommended Job Roles"])

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save all artifacts
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model trained and saved.")
