import discord
from discord import Embed, Color
import urllib
import sqlite3
from sqlite3 import Error
from time import gmtime, strftime
import sys

DB_FILE = 'monopoloy.db'
CONN = sqlite3.connect('monopoloy.db')
CURSOR = CONN.cursor()

def create_connection(DB_FILE):
    
    try:
        CONN = sqlite3.connect(DB_FILE)
        print('Connected to the database...')
        return CONN
    except Error as e:
        print(e)

    return None


def get_current_game_id(DB_FILE):
    curr = CONN.cursor()
    curr.execute("SELECT MAX(id) AS LastID FROM games")
    gameID = 0

    rows = curr.fetchall()

    for row in rows:
        gameID = row[0]
    
    if gameID == None:
        gameID = 0
    else:
        gameID = gameID + 1

    return gameID


def create_new_game_channel(DB_FILE, userid, player2_id, player3_id, player4_id):

    date = strftime("%Y-%d-%m", gmtime())

    query = 'INSERT INTO games (player1_id, player2_id, player3_id, player4_id,date_started) VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\');'.format(userid, player2_id, player3_id, player4_id, date)

    curr = CONN.cursor()
    curr.execute(query)
    CONN.commit()

    return None