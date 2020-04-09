# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)

        self.name = name

    def __str__(self):
        return f"The Waypoint {self.name} has a latitude of {self.lat} and a longitude of {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)

        self.difficulty = difficulty
        self.size = size

    def __str__(self):

        description = f"""
    The Geocache {self.name} has a difficulty of {self.difficulty} with the size of {self.size}

    Cordinates:

    latitude = {self.lat} 
    longitude = {self.lon}
        """

        return description



print("\nMake a new waypoint and print it out: 'Catacombs', 41.70505, -121.51521")

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f"\n {waypoint.name}, {waypoint.lat}, {waypoint.lon}")

print("\nWithout changing the following line, how can you make it print into something")
print("more human-readable?\n")
# Hint: Look up the `object.__str__` method
print(waypoint)

print("\nMake a new geocache 'Newberry Views', diff 1.5, size 2, 44.052137, -121.41556")

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
