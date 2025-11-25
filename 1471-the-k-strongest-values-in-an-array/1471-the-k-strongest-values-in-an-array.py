class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        lists = []
        arr.sort()
        m = int((n - 1) / 2)
        middle = arr[m]

        left = 0
        right = n - 1

        for i in range(k):
            if abs(arr[left] - middle) < abs(arr[right] - middle):
                lists.append(arr[right])
                right -= 1
            elif abs(arr[left] - middle) > abs(arr[right] - middle):
                lists.append(arr[left])
                left += 1
            else:
                if arr[right] > arr[left]:
                    lists.append(arr[right])
                    right  -= 1
                else:
                    lists.append(arr[left])
                    left += 1 
        return lists
