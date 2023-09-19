squares = [n**2 for n in range(10)]
print(squares)


squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

[32 for planet in planets]
