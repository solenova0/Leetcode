class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0 
        j = 0  
        count = 0
        while i < len(trainers) and j < len(players):
            if players[j] <= trainers[i]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
        return count