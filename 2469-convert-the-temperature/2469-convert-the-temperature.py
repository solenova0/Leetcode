class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahr = celsius * 1.80 + 32.00
        kelv = celsius + 273.15
        return [round(kelv , 5), round(fahr , 5)]
        