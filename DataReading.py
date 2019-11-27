import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('doc/data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(row[0])
        y.append(row[2])

plt.plot(x, y, marker='o', label='Mood')
plt.xlabel('Jours Ouvrés')
plt.ylabel('Humeur')
plt.title('Evolution de votre mood (Semaine 32)')
plt.legend()
plt.show()