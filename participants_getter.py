import pandas as pd

participants_file = 'participants.csv'
df = pd.read_csv(participants_file, encoding='utf-8', delimiter=';')

participant_names = df["name"].tolist()