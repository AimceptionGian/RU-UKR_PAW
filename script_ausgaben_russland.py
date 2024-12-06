import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('russland_militaerausgaben.csv')

fig, ax1 = plt.subplots()

ax1.set_xlabel('Jahr')
ax1.set_ylabel('Anteil am BIP (%)', color='tab:blue')
ax1.bar(df['Jahr'], df['Anteil_am_BIP'], color='tab:blue', alpha=0.6, label='Anteil am BIP (%)')  
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Ausgaben (Mrd USD)', color='tab:green')
ax2.plot(df['Jahr'], df['Absolut_in_Mrd_USD'], color='tab:green', marker='o', label='Ausgaben (Mrd USD)')
ax2.tick_params(axis='y', labelcolor='tab:green')

ax1.set_ylim(0, df['Anteil_am_BIP'].max() * 1.1)  

ax1.set_xticks(df['Jahr'])
ax1.set_xticklabels(df['Jahr'], rotation=45) 

plt.title('Anteil am BIP und absolute Ausgaben (in Mrd USD)')
fig.tight_layout()

plt.savefig('ausgaben_bip_gesamt_linie_und_balken.png')

plt.show()
