from connection import Connection
from par import Parser
from drafting import Shuffle
import sqlite3
import csv
class Aplication:
    def __init__(self,connect) -> None:
        self.connect=Connection(connect)
        parser=Parser()
        self.arguments  = parser.parse_args()
        #self.main()
    def main(self):
        match self.arguments.action:
            case 'add_player':
                self.connect.add_player(self.arguments.name,self.arguments.surname)
            case 'add_round':
                self.connect.post_round_score()
            case 'shuffle':
                dictionary=self.connect.get_players_with_points()
                shuffle=Shuffle(dictionary)
                players=shuffle.generate_pairings()
                print(players)
                self.connect.add_duels(players)
    def print_data(self):
        fieldnames=['id','score']
        self.scores=[]
        with open('chess//scores.csv',mode='r',newline='') as output_file:
            reader=csv.DictReader(output_file,fieldnames=fieldnames,delimiter=',')
            for row in reader:
                  self.scores.append(row)
                  print(row)
                

if __name__=='__main__':
    with sqlite3.connect("chess//test_database.db")as connect:
        app=Aplication(connect)
        app.print_data()
        #conn.add_another_round()
        #conn.add_player("Amadeusz","Krab")
        #conn.add_score_by_name("Amadeusz","Krab",1,2)
    