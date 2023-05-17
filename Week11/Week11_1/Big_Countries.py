"""
A country can be said as being big if it is:
    Big in terms of population.
    Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:
    Population is greater than 250 million.
    Area is larger than 3 million square km.

Also, create a method which compares a country's population density to another country object. 
Return a string in the following format:
{country} has a {smaller / larger} population density than {other_country}
Examples
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

Notes

    Population density is calculated by dividing the population by the area.
    Area is given in square km.
    The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a 
    string and the other two inputs are integers.
"""


class Country:
    def __init__(self, name_of_country, population, size_in_km2) -> None:
        self.name_of_country = name_of_country
        self.population = population
        self.size_in_km2 = size_in_km2
        self.is_big = self.population > 250000000 or self.size_in_km2 > 3000000

    def compare_pd(self, other_country):
        self.other_country = other_country
        population_densit_1 = self.population / self.size_in_km2
        population_densit_2 = other_country.population / other_country.size_in_km2

        if population_densit_1 > population_densit_2:
            return f"{self.name_of_country} has a larger population density than {other_country.name_of_country}"
        elif population_densit_1 < population_densit_2:
            return f"{self.other_country} has a larger population density than {other_country.name_of_country}"
        return f"{self.name_of_country} has the same population density as {other_country.name_of_country}"
    
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)
print(andorra.is_big)
print(andorra.compare_pd(australia))
