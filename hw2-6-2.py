# Author MB 09/26/2021

radius = input("what is the radius")
height = input("what is the height")

radius = float(radius)
height = float(height)

sa = 2 * 3.14 * radius * height + 2 * 3.14 * radius ** 2
volume = 3.14 * radius ** 2 * height

sa2 = str(sa)
volume2 = str(volume)

print("surface area" + " " + sa2)
print("volume" + " " + volume2)