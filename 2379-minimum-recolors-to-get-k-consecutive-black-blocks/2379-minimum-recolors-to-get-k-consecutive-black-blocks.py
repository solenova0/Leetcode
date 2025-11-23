class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        count = 0
        recolor = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                count += 1

            if right - left + 1 == k:
                recolor = min(recolor, count)

                if blocks[left] == 'W':
                    count -= 1
                left += 1

        return recolor