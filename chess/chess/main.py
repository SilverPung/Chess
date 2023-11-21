from connection import Connection
from par import Parser
import sqlite3
class Aplication:
    def __init__(self,connect) -> None:
        self.connect=Connection(connect)
        parser=Parser()
        self.arguments  = parser.parse_args()
        self.main()
    def main(self):
        match self.arguments.action:
            case 'add_player':
                self.connect.add_player(self.arguments.name,self.arguments.surname)
            case 'add_round':
                print("Wynik dodany")
            case 'shuffle':
                print("Zawodnicy wymieszani ",self.connect.get_players_with_points())

if __name__=='__main__':
    with sqlite3.connect("chess//test_database.db")as connect:
        app=Aplication(connect)
        #conn.add_another_round()
        #conn.add_player("Amadeusz","Krab")
        #conn.add_score_by_name("Amadeusz","Krab",1,2)
    