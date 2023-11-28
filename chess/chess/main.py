"""
    The code is a Python application that connects to a SQLite database, parses command line arguments,
    and performs various actions such as adding players, adding rounds with scores, shuffling players
    for duels, and printing player information.
    """
from connection import Connection
from par import Parser
from drafting import Shuffle
import sqlite3
import csv
class Aplication:
    def __init__(self,connect) -> None:
        self.connect_to_base=connect
        self.connect=Connection(connect)
        parser=Parser()
        self.arguments  = parser.parse_args()
        self.main()
    def main(self):
        match self.arguments.action:
            case 'add_player':
                #adding palyer to the table
                self.connect.add_player(self.arguments.name,self.arguments.surname)
            case 'add_round':
                #adding round with points to the table
                self.print_data()
            case 'shuffle':
                #getting duels
                dictionary=self.connect.get_players_with_points()
                shuffle=Shuffle(dictionary,self.connect_to_base)
                players=shuffle.generate_pairings()
                #print(players)
                self.connect.add_duels(players)
            case 'print_players':
                self.connect.print_players()
            case 'delete':
                self.connect.delete_player(self.arguments.id)
    def print_data(self):
        fieldnames=['id','score']
        self.scores=[]
        with open('chess//scores.csv',mode='r',newline='') as output_file:
            reader=csv.DictReader(output_file,fieldnames=fieldnames,delimiter=',')
            for row in reader:
                  self.scores.append(row)
            self.connect.post_round_score(self.scores)

if __name__=='__main__':
    with sqlite3.connect("chess//database.db")as connect:
        app=Aplication(connect)
    