import matplotlib.pyplot as plt
import csv
import datetime
import calendar
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
my_date = datetime.datetime.now()
#week = date(my_date).isocalendar()[1]
day = calendar.day_name[my_date.weekday()]

x = []
y = []


def weekly_curve(the_day):
    if the_day.lower() == 'vendredi':
        with open('doc/data.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                if row[0] != 'Day' and row[1] != 'Score':
                    x.append(row[0])
                    y.append(int(row[1]))
        plt.plot(x, y, marker='o', label='Mood')
        plt.xlabel('Jours Ouvrés')
        plt.ylabel('Humeur',)
        plt.title('Evolution de votre mood cette semaine')
        plt.legend()
        plt.show()