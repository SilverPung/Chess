#file to cennct to database
import sqlite3
from sqlite3 import IntegrityError

class Connection():
    def __init__(self,connect) -> None:
        self.connection=connect
        self.cursor=connect.cursor()
        self.create_players()
        self.create_rounds()   
        self.create_duels() 
    def create_players(self):
        sql="""CREATE TABLE IF NOT EXISTS players(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT)"""
        self.cursor.execute(sql)
    def create_rounds(self):
        sql="""CREATE TABLE IF NOT EXISTS rounds(
                player_id INTEGER PRIMARY KEY,
                round_1 FLOAT,
                FOREIGN KEY (player_id) REFERENCES players(id))"""
        self.cursor.execute(sql)
    def create_duels(self):
        sql="""CREATE TABLE IF NOT EXISTS duels(player_id INTEGER,
        opponent_id INTEGER)"""
        self.cursor.execute(sql)
    def add_another_round(self):
        self.cursor.execute(f"PRAGMA table_info(rounds);")
        temp=len(self.cursor.fetchall())
        self.cursor.execute(f'ALTER TABLE rounds ADD COLUMN round_{temp} FLOAT')
    def add_player(self,name,surname):
        #adding players into database
        self.cursor.execute("SELECT id FROM players WHERE name=? AND surname=?",(name,surname))
        if self.cursor.fetchone()==None:
            self.cursor.execute("INSERT INTO players(name,surname) VALUES(?,?)",(name,surname))
            self.cursor.execute("SELECT id FROM players WHERE name=? AND surname=?",(name,surname))
            self.connection.commit()
            id=self.cursor.fetchone()
            self.cursor.execute("INSERT INTO rounds(player_id) VALUES(?)",(id))
    def add_score(self,id,score:float,round=1):
        try:  
            self.cursor.execute(f"UPDATE rounds SET round_{round}=? WHERE player_id=?",(score,id))
            self.connection.commit()
        except TypeError:
            print("404 brak danych")
            raise "404 brak danych"
    def add_score_by_name(self,name,surname,score:int=1,round=1):
        try: 
            self.cursor.execute("SELECT id FROM players WHERE name=? AND surname=?",(name,surname))
            self.connection.commit()
            id=self.cursor.fetchone()[0]
            self.add_score(id,score,round)
        except TypeError:
            print("404 brak danych")
    def add_duels(self,duels):
        for duel in duels:
            self.cursor.execute("INSERT INTO duels VALUES(?,?)",(duel[0],duel[1]))
    def get_number_of_rounds(self):
        self.cursor.execute(f"PRAGMA table_info(rounds);")
        columns = [column[1] for column in self.cursor.fetchall()]

        return len(columns)
    def get_players_with_points(self):
        number_of_rounds=self.get_number_of_rounds()
        self.cursor.execute("SELECT id  FROM players")
        players={}
        for id in self.cursor.fetchall():
            total=0
            for n in range(1,number_of_rounds):
                self.cursor.execute(f"SELECT round_{n} FROM rounds WHERE player_id=?",(id[0],))
                try:
                    total+=self.cursor.fetchone()[0]
                except TypeError:
                    pass
            players.update({id[0]:total})
        return players
    def get_opponents(self,id):
        opponents=[]
        self.cursor.execute(f'SELECT opponent_id FROM duels WHERE player_id={id}')
        for item in self.cursor.fetchall():
            opponents.append(item[0])
        self.cursor.execute(f'SELECT player_id FROM duels WHERE opponent_id={id}')
        for item in self.cursor.fetchall():
            opponents.append(item[0])
        return set(opponents)
    def print_players(self):
        number_of_rounds=self.get_number_of_rounds()
        self.cursor.execute("SELECT *  FROM players")
        players=[]
        for id, name ,surname in self.cursor.fetchall():
            total=0
            for n in range(1,number_of_rounds):
                self.cursor.execute(f"SELECT round_{n} FROM rounds WHERE player_id=?",(id,))
                try:
                    total+=self.cursor.fetchone()[0]
                except TypeError:
                    pass
            players.append([id,name,surname,total])
        print(players)
    def post_round_score(self,players:list):
        rounds=self.get_number_of_rounds()
        if rounds>1:
            self.add_another_round()
            rounds+=1

        #print(players)
        for player in players:
            if player['id']!='':
                self.cursor.execute(f"UPDATE rounds SET round_{rounds-1} = {player['score']} WHERE player_id={player['id']};")
        
if __name__=='__main__':
    with sqlite3.connect("chess//test_database.db")as connect:
        conn=Connection(connect)
        print(conn.print_players())
    
