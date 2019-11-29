import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('doc/data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if row[0] != 'Day' and row[1] != 'Score':
            x.append(row[0])
            y.append(row[1])

plt.plot(x, y, marker='o', label='Mood')
plt.xlabel('Jours Ouvrés')
plt.ylabel('Humeur')
plt.title('Evolution de votre mood (Semaine 32)')
plt.legend()
plt.show()