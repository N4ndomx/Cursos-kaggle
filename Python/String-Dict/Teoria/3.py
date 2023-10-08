claim = "Pluto is a planet!"
planet = 'Pluto'

print(claim.upper())
print(claim.lower())
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('planet'))

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, '', month, '', day)

print('/'.join([month, day, year]))

print(' 👏 '.join([word.upper() for word in words]))

print(planet + ', we miss you.')

position = 9

print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)