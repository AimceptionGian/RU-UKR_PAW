import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

with open('daten.txt', 'r', encoding='utf-8') as file:
    data = file.read()

def extract_data(data):
    date_pattern = r"(\d{2}\.\d{2}\.\d{4})"
    losses_pattern = r"(\w[\w\s]*\w) — (\d+)(?: \(\+(\d+)\))?"
    
    dates = re.findall(date_pattern, data)
    losses = re.findall(losses_pattern, data)

    if len(dates) != len(losses):
        print(f"Warnung: Unterschiedliche Anzahl an Datumsangaben und Verlusten! {len(dates)} Datumsangaben und {len(losses)} Verluste.")
    
    records = []
    
    for i in range(min(len(dates), len(losses))):
        equipment, loss, increase = losses[i]
        record = {
            'Date': datetime.strptime(dates[i], "%d.%m.%Y"),
            'Equipment': equipment.strip(),
            'Losses': int(loss),
            'Increase': int(increase) if increase else 0
        }
        records.append(record)

    return pd.DataFrame(records)

df = extract_data(data)

if df.empty:
    print("Keine Daten zum Verarbeiten gefunden.")
else:
    df['Month'] = df['Date'].dt.to_period('M')

    monthly_losses = df.groupby(['Month', 'Equipment']).agg({'Losses': 'sum'}).reset_index()

    monthly_losses.to_csv('verarbeitete_daten.csv', index=False)

    plt.figure(figsize=(12, 8))
    for equipment in monthly_losses['Equipment'].unique():
        equipment_data = monthly_losses[monthly_losses['Equipment'] == equipment]
        plt.plot(equipment_data['Month'].astype(str), equipment_data['Losses'], label=equipment)

    plt.title("Verluste der russischen Ausrüstung im Jahr 2024")
    plt.xlabel("Monat")
    plt.ylabel("Verluste")
    plt.xticks(rotation=45)
    plt.legend(title="Ausrüstung", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
