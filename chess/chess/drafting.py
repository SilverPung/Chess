from connection import Connection
class Shuffle:
    def __init__(self, players,conn) -> None:
        self.sorted_players = [{"id": id, "score": score} for id, score in players.items()]
        #print(self.sorted_players)
        self.connect=Connection(conn)


    def generate_pairings(self):
        # Step 1: Sort players by score in descending order
        self.sorted_players = sorted(self.sorted_players, key=lambda x: x['score'], reverse=True)

        # Step 2: Initialize pairings list
        pairings = []
        draftings=[]
        temp=[]
        # Step 3: Generate pairings
        for i in range(0, int(len(self.sorted_players))):
            if self.sorted_players[i]['id']not in draftings:
                player1=self.sorted_players[i]
                player2=self.find_opponent(player1,self.sorted_players,self.connect.get_opponents(player1['id']),draftings)
                if player2==None:
                    self.connect.delete_duels()
                    player2=self.find_opponent(player1,self.sorted_players,self.connect.get_opponents(player1['id']),draftings)
                    temp.append(player2)
                    #print(draftings)
                pairings.append([player1['id'],player2])
                draftings.append(player1['id'])
                draftings.append(player2)

        print(pairings)
        return pairings

    def find_opponent(self, player, opponents, pairings, draftings):
        for opponent in opponents:
            if opponent['id'] not in pairings  and opponent['id']!=player['id'] and opponent['id']not in draftings:
                return opponent['id']

