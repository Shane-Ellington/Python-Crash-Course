#6-11 practice prompt
## Make a dictionary of three cities
### List countries, facts, and populations

cities = {
    'houston': {
        'state': 'texas',
        'population': '2.3 million',
        'fact': 'named after first president of texas',
    },
    'raleigh': {
        'state': 'north carolina',
        'population': '477 thousand',
        'fact': 'home of first public park in north carolina',
    },
    'seattle': {
        'state': 'washington',
        'population': '750 thousand',
        'fact': 'birthplace of starbucks',
    }
}

for city, city_info, in cities.items():
    state = f"{city_info['state']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"
    print(f"City: {city.title()}")
    print(f"State: {state.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFun Fact: {fact.title()}")