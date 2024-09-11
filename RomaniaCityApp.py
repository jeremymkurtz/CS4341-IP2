from RomaniaMap import romania_map
from SimpleProblemSolvingAgent import *
from Problem import Problem, GraphProblem


class RomaniaProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
    
    def actions(self, state):
        return romania_map.get(state)
    
    def result(self, state, action):
        return romania_map.get(action)
    
    def goal_test(self, state): 
        return state == self.goal
    
    def path_cost(self, c, state1, action, state2):
        return romania_map.get(state1, state2)

def are_valid_cities(city1, city2):
    print("Here are all the possible Romania cities that can be traveled:")
    locations = romania_map.locations
    print('\n[' + ', '.join(["'" + item + "'" for item in locations]) + ']\n')
    
    while True:
        city1 = input("Please enter the origin city: ")
        while city1 not in locations:
            city1 = input("Could not find " + city1 + ", please try again: ")
        city2 = input("\nPlease enter the destination city: ")
        while city2 not in locations:
            city2 = input("\nCould not find " + city2 + ", please try again: ")
        if city1 == city2:
            print("\nThe same city can't be both origin and destination. Please try again. ")
        else:
            return city1, city2
        
def printWithArrows(path: list) -> None:
    for i, item in enumerate(path):
        print(item, end='')
        if i != len(path) - 1:
            print(" → ", end='')
    print()
        
def use_algorithms(city1, city2):
    switchCities = 'yes'
    while(switchCities == 'yes'):
        problem = GraphProblem(city1, city2, romania_map)
        SPSA = SimpleProblemSolvingAgentProgram(problem)
        
        print("\nGreedy Best-First Search")
        # Use Greedy Best-First Search
        gbfs = SPSA.search(algorithm="bfgs")
        print("Total Cost:", gbfs.path_cost)
        gbfs = gbfs.solution()
        gbfs.insert(0, city1)
        printWithArrows(gbfs)
        
        print("\nA* Search")
        # Use A* Search
        astar = SPSA.search(algorithm="astar")
        print("Total Cost:", astar.path_cost)
        astar = astar.solution()
        astar.insert(0, city1)
        printWithArrows(astar)
        
        print("\nHill Climbing Search")
        # Use Hill Climbing Search
        hill_climbing = SPSA.search(algorithm="hill")
        print("Total Cost:", hill_climbing.path_cost)
        hill_climbing = hill_climbing.solution()
        hill_climbing.insert(0, city1)
        printWithArrows(hill_climbing)
        
        print("\nSimulated Annealing Search")
        # Use Simulated Annealing
        annealing = SPSA.search(algorithm="annealing")
        print("Total Cost:", annealing.path_cost)
        annealing = annealing.solution()
        annealing.insert(0, city1)
        printWithArrows(annealing)
        
        switchCities = input("\nWould you like to find the best path between the other two cities? " )
        if(switchCities == 'yes'):
            temp=city1
            city1=city2
            city2=temp
        else:
            print("\nThank You for Using Our App")
            break
        
    pass

    
def main():
    city1, city2 = are_valid_cities(city1=None, city2=None)
    use_algorithms(city1, city2)
    pass


if __name__ == '__main__':
    main()
    
