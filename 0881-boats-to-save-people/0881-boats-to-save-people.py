class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l ,r = 0, len(people)-1
        total_boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                total_boats += 1
                r -= 1
                l += 1
            else:
                r -= 1
                total_boats += 1
        return total_boats