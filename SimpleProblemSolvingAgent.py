from Node import Node
from SearchAlgorithms import *
from Problem import GraphProblem


class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, problem):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.seq = []
        self.initial = problem.initial
        self.goal = problem.goal
        self.graph = problem.graph

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)
        

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, algorithm: str):
        problem = GraphProblem(self.initial, self.goal, self.graph)
        if(algorithm == 'bfgs'):
            return best_first_graph_search(problem, lambda n: problem.h(n))
        elif(algorithm == 'astar'):
            return astar_search(problem, lambda n: n.path_cost)
        elif(algorithm == 'hill'):
            return hill_climbing(problem)
        elif(algorithm == 'annealing'):
            return simulated_annealing(problem)
            


