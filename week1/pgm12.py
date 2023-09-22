m = int(input("Enter the total percentage: "))

def gswitch(m):
    switch = {
        90 <= m <= 100: "A",
        80 <= m < 90: "B",
        70 <= m < 80: "C",
        60 <= m < 70: "D",
        50 <= m < 60: "E",
    }
    return switch.get(True, "Failed")

result = gswitch(m)
print(result)
