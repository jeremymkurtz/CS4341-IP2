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
            best_first_graph_search(problem, lambda n: problem.h(n))
        elif(algorithm == 'astar'):
            astar_search(problem)
        elif(algorithm == 'hill'):
            hill_climbing(problem)
        elif(algorithm == 'anneal'):
            simulated_annealing(problem)
            

def best_first_graph_search(problem, f, display=False):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""
        f = memoize(f, 'f')
        node = Node(problem.initial)
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                if display:
                    print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
        return None

def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)


