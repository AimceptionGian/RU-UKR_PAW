import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('verarbeitete_ausruestung.csv')
df['Month'] = pd.to_datetime(df['Month'])
df['Equipment'] = df['Equipment'].str.replace('"', '')
df['Losses'] = pd.to_numeric(df['Losses'], errors='coerce')
df['Cumulative_Losses'] = df.groupby('Equipment')['Losses'].cumsum()

plt.figure(figsize=(12, 8))
sns.lineplot(data=df, x='Month', y='Cumulative_Losses', hue='Equipment', marker='o')
plt.title('Kumulative Verluste nach Ausrüstungsart über die Monate', fontsize=16)
plt.xlabel('Monat', fontsize=14)
plt.ylabel('Kumulative Verluste', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Ausrüstungsart', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
