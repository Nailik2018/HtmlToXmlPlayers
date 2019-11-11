import mysql.connector
import configparser
import ast

class PlayerDatabase():

    def __init__(self):
        pass

    def select_players_from_db(self):

        output = []
        db_config = configparser.ConfigParser()
        db_config.read("configurations/database.ini")
        user = ast.literal_eval(db_config.get("DATABASE", "dbuser"))
        db = ast.literal_eval(db_config.get("DATABASE", "db"))
        password = ast.literal_eval(db_config.get("DATABASE", "password"))
        db = db.split("=")
        localhost = db[1].split(";")
        db = db[2]
        localhost = localhost[0]

        db = mysql.connector.connect(
            host=localhost,
            user=user,
            passwd=password,
            database=db
        )

        mycursor = db.cursor()
        mycursor.execute("SELECT licenceNr, firstname, lastname FROM players")
        all_players = mycursor.fetchall()

        for element in all_players:
            player = {
                'licenceNr': element[0],
                'firstname': element[1],
                'lastname': element[2],
            }
            output.append(player)

        return output