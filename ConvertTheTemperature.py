class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius+273.15
        farenheit = celsius*1.8 +32.00
        ans=[kelvin, farenheit]
        return ans
        