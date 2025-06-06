import pandas as pd
import numpy as np
import random
import uuid

# Set seed for reproducibility
np.random.seed(42)

# Helper functions
def generate_essay_id():
    return f"essay_{uuid.uuid4().hex[:16]}"

def generate_language():
    return random.choice(['English', 'Spanish', 'French', 'German', 'Italian', 'Romanian', 'Polish', 'Dutch', 'Turkish', 'Portuguese', 'Hindi', 'Greek'])

def generate_rater_score():
    return np.random.randint(1, 10)

def score_to_cefr(score):
    if score <= 3:
        return 'A2'
    elif score <= 6:
        return 'B1'
    elif score <= 8:
        return 'B2'
    else:
        return 'C1'

def pass_fail(score):
    return 'pass' if score >= 5 else 'fail'

# Generate synthetic dataset
n = 1000
data = []
for _ in range(n):
    essay_id = generate_essay_id()
    split = 'test'
    language = generate_language()
    
    rater_score = generate_rater_score()
    rater_cefr = score_to_cefr(rater_score)
    rater_pass = pass_fail(rater_score)
    
    auto_score = np.clip(rater_score + np.random.normal(0, 1), 1, 10)
    auto_conf = np.clip(np.random.beta(5, 1.5), 0.5, 1.0)
    auto_cefr = score_to_cefr(int(round(auto_score)))
    auto_pass = pass_fail(auto_score)

    data.append([
        essay_id, split, language,
        rater_score, rater_cefr, rater_pass,
        round(auto_score, 3), round(auto_conf, 6), auto_cefr, auto_pass
    ])

columns = [
    "public_essay_id", "split", "language", "rater_score", "rater_cefr_level", "rater_pass_fail",
    "automarker_score", "automarker_confidence", "automarker_cefr_level", "automarker_pass_fail"
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_path = "data/synthetic_autograder_data.csv"
df.to_csv(csv_path, index=False)

csv_path
