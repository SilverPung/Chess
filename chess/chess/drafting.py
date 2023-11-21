class Shuffle:
    def __init__(self, players) -> None:
        self.sorted_players = [{"id": id, "score": score} for id, score in players.items()]
        print(self.sorted_players)

    def generate_pairings(self):
        # Step 1: Sort players by score in descending order
        self.sorted_players = sorted(self.sorted_players, key=lambda x: x['score'], reverse=True)

        # Step 2: Initialize pairings list
        pairings = []

        # Step 3: Generate pairings
        for i in range(0, len(self.sorted_players) - 1, 2):
            player1 = self.sorted_players[i]
            player2 = self.find_opponent(player1, self.sorted_players[i + 1:], pairings)

            pairings.append((player1['id'], player2['id']))

        # Step 4: Repeat if necessary (odd number of players)
        if len(self.sorted_players) % 2 != 0:
            # Handle the remaining player
            remaining_player = self.sorted_players[-1]
            opponent = self.find_opponent(remaining_player, self.sorted_players[:-1], pairings)
            pairings.append((remaining_player['id'], opponent['id']))

        return pairings

    def find_opponent(self, player, opponents, pairings):
        for opponent in opponents:
            if opponent['id'] not in [p[0] for p in pairings] and \
                    opponent['id'] not in [p[1] for p in pairings] and \
                    player['id'] not in [p[0] for p in pairings] and \
                    player['id'] not in [p[1] for p in pairings]:
                return opponent

# Example usage: