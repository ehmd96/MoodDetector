import csv
import datetime
import calendar
import locale
import pandas as pd

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
my_date = datetime.datetime.now()
#week = date(my_date).isocalendar()[1]
day = calendar.day_name[my_date.weekday()]

score = [0, 5, 10]
mood = ['Mécontent', 'Moyen', 'Heureux']
#df = pd.DataFrame(index=['Monday','Tuesday','Wednesday','Thursday','Friday'], columns=['Score', 'Mood'])
#df = pd.read_pickle('doc/Week_Template.csv')

def frameReset():
    #df = pd.read_csv('doc/Week_Template.csv')
    data = {
        'Day': ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
        'Score': [0, 0, 0, 0, 0],
        'Mood': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
        'Comment': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty']
    }
    #df = pd.DataFrame(index=['Monday','Tuesday','Wednesday','Thursday','Friday'], columns=['Day','Score', 'Mood'])
    df = pd.DataFrame(data, index="Day", dtype=str)
    df.set_index('Day')
    #df.Mood.apply(str)
    df.to_csv('doc/Week_Template.csv', sep=",", index_label='Day')
    return df

def weekTemp():
    df = pd.read_csv('doc/Week_Template.csv', index_col='Day')
    return df


def frameSave(df):
    df.to_csv('doc/data.csv')

def frameUpdate(day,mood):
    if day.lower() == 'lundi':
        df = weekTemp()
        frameSave(df)
        #df = pd.read_csv('doc/Week_Template.csv', index_col='Day')

    df = pd.read_csv('doc/data.csv', index_col='Day')
    if mood.lower() == 'content':
        score = 10
    elif mood.lower() == 'couci-couca':
        score = 5
    elif mood.lower() == 'pas content':
        score = 0
        value = ""
        while not value:
            value = input("Veuillez insérer un commentaire :(")
            df.at[day, 'Comment'] = value

    df.at[day, 'Score'] = score
    df.at[day, 'Mood'] = mood
    print(df)
    frameSave(df)


#frameUpdate(day, 'Pas content')