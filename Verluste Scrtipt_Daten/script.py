import os
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

file_path = 'daten.txt'

if not os.path.exists(file_path):
    print(f"Die Datei {file_path} wurde nicht gefunden!")
else:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    def extract_data(data):
        date_pattern = r"(\d{2}\.\d{2}\.\d{4})"
        losses_pattern = r"([\w\s\(\)]+) — (\d+)(?: \(\+(\d+)\))?"
        personnel_pattern = r"Military personnel — aprx\. (\d+) people(?: \(\+(\d+)\))?"

        dates = re.findall(date_pattern, data)
        losses = re.findall(losses_pattern, data)
        personnel = re.findall(personnel_pattern, data)

        records = []

        for i in range(min(len(dates), len(losses), len(personnel))):
            date = datetime.strptime(dates[i], "%d.%m.%Y")
            losses_data = losses[i]
            equipment = losses_data[0].strip()
            loss = int(losses_data[1])
            increase = int(losses_data[2]) if losses_data[2] else 0
            personnel_count = int(personnel[i][0])
            personnel_increase = int(personnel[i][1]) if personnel[i][1] else 0

            record = {
                'Date': date,
                'Equipment': equipment,
                'Losses': loss,
                'Increase': increase,
                'Military Personnel': personnel_count,
                'Personnel Increase': personnel_increase
            }
            records.append(record)

        return pd.DataFrame(records)

    df = extract_data(data)

    if df.empty:
        print("Keine Daten zum Verarbeiten gefunden.")
    else:
        df['Month'] = df['Date'].dt.to_period('M')

        monthly_losses = df.groupby(['Month', 'Equipment']).agg({'Losses': 'sum'}).reset_index()

        monthly_personnel_losses = df.groupby('Month').agg({'Military Personnel': 'max'}).reset_index()

        monthly_losses.to_csv('verarbeitete_ausruestung.csv', index=False)
        monthly_personnel_losses.to_csv('verarbeitete_personen.csv', index=False)

        plt.figure(figsize=(12, 8))
        plt.plot(monthly_personnel_losses['Month'].astype(str), monthly_personnel_losses['Military Personnel'], label="Militärisches Personal")
        plt.title("Verluste des militärischen Personals im Jahr 2024")
        plt.xlabel("Monat")
        plt.ylabel("Militärisches Personal")
        plt.xticks(rotation=45)
        plt.legend(title="Verluste", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
