primes = [2, 3, 5, 7]
print(primes)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)
print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])

print(planets[0:3])
print(planets[3:])
print(planets[1:-1])
print(planets[-3:])

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], 
]
print(hands)

my_favourite_things = [32, 'raindrops on roses', help]
print(my_favourite_things)