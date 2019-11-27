import csv
from datetime import date
import calendar
import locale
import pandas as pd

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
my_date = date.today()
day = calendar.day_name[my_date.weekday()]

score = [0, 5, 10]
mood = ['Mécontent', 'Moyen', 'Heureux']
#df = pd.DataFrame(index=['Monday','Tuesday','Wednesday','Thursday','Friday'], columns=['Score', 'Mood'])
#df = pd.read_pickle('doc/Week_Template.csv')

def frameReset():
    #df = pd.read_csv('doc/Week_Template.csv')
    data = {
        'Day' : ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
        'Score': [0, 0, 0, 0, 0],
        'Mood': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
        'Comment': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty']
    }
    #df = pd.DataFrame(index=['Monday','Tuesday','Wednesday','Thursday','Friday'], columns=['Day','Score', 'Mood'])
    df = pd.DataFrame(data, dtype=str)
    #df.Mood.apply(str)
    df.to_csv('doc/Week_Template.csv')
    return df


def frameSave(df):
    df.to_csv('doc/data.csv')

def frameUpdate(day,mood):
    if day.lower() == 'lundi':
        df = frameReset()
        frameSave(df)
        #df = pd.read_csv('doc/Week_Template.csv', index_col='Day')

    df = pd.read_csv('doc/data.csv', index_col='Day')
    if mood.lower() == 'Content':
        score = 10
    elif mood.lower() == 'Couci-couca':
        score = 5
    else:
        score = 0
        value = ""
        while not value:
            value = input("Veuillez insérer un commentaire :(")

        df.at[day, 'Comment'] = value

    df.at[day, 'Score'] = score
    df.at[day, 'Mood'] = mood
    print(df)
    frameSave(df)


#frameUpdate(day, 'Mecontent')