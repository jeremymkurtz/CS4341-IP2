from RomaniaMap import *

def are_valid_cities(city1, city2):
    print("Here are all the possible Romania cities that can be traveled:")
    locations = romania_map.locations
    print('[' + ', '.join(["'" + item + "'" for item in locations]) + ']')
    
    while True:
        city1 = input("Please enter the origin city: ")
        while city1 not in locations:
            city1 = input("Could not find " + city1 + ", please try again: ")
        city2 = input("Please enter the destination city: ")
        while city2 not in locations:
            city2 = input("Could not find " + city2 + ", please try again: ")
        if city1 == city2:
            print("The same city can't be both origin and destination. Please try again. ")
        else:
            return city1, city2
        
def use_algorithims(city1, city2):
    switchCities = 'yes'
    while(switchCities == 'yes'):
        print("Greedy Best-First Search")
        # Use Greedy Best-First Search
        print('\n')
        
        print("A* Search")
        # Use A* Search
        print('\n')
        
        print("Hill Climbing Search")
        # Use Hill Climbing Search
        print('\n')
        
        print("Simulated Annealing Search")
        # Use Simulated Annealing
        print('\n')
        
        switchCities = input("Would you like to find the best path between the other two cities?" )
        if(switchCities == 'yes'):
            temp=city1
            city1=city2
            city2=temp
        else:
            print("Thank You for Using Our App")
            break
        
    pass

    
def main():
    city1, city2 = are_valid_cities(city1=None, city2=None)
    use_algorithims(city1, city2)
    pass


if __name__ == '__main__':
    main()