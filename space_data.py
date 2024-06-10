import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_info = []
    
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else None
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else None
            planet_info.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
            print(f"Planet: {name}, Mass: {mass} x 10^24 kg, Orbit Period: {orbit_period} days")
    
    heaviest_planet = max(planet_info, key=lambda x: x['mass'])
    print(f"\nThe heaviest planet is {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} x 10^24 kg.")

fetch_planet_data()
