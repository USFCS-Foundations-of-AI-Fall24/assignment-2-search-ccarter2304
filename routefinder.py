from operator import indexOf
from queue import PriorityQueue

from Graph import Graph, Node, Edge

import math


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'
    #
    def successor(self):
        #current_location = self.location
        successors = []
        graph_file = read_mars_graph("MarsMap.txt")
        self.mars_graph = graph_file
        location = self.location.__str__()
        location = location.replace('(', '').replace(')', '')
        neighbors = self.mars_graph.get_edges(Node(location))
        for neighbor in neighbors:
            successors.append(neighbor.dest)
        return successors

def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    state_count = 1
    g = 0
    ## Create map state for the start state and add to search queue
    start_map = map_state(start_state)
    start_map.g = g
    start_map.h = heuristic_fn(start_state)
    start_map.f = start_map.g + start_map.h
    f = start_map.f
    search_queue.put(start_map)
    if use_closed_list :
        closed_list[start_state] = True
    while search_queue.qsize() > 0 :
        current_state = search_queue.get()
        c_map = map_state(current_state)
        successors = c_map.successor()
        if use_closed_list:
            successors = [item for item in successors
                         if item not in closed_list]
            for successor in successors :
                closed_list[successor] = True
                s_map = map_state(successor)
                s_map.g = g + 1
                s_map.h = heuristic_fn(successor)
                s_map.f = s_map.g + s_map.h
                search_queue.put(s_map)
            state_count += len(successors)
        g += 1
    return state_count

    ## you do the rest.
    ## g - += 1
    ## h - sld or h1

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    state_cords = state.split(',')
    return math.sqrt((int(state_cords[0]) - 1)^2 + (int(state_cords[1]) - 1)^2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    try :
        f = open(filename, 'r')
        file_graph = Graph()
        file_lines = f.readlines()
        for line in file_lines:
            g = line.split()
            node = g[0].replace(":", "")
            node = Node(node)
            file_graph.add_node(node)
            i = 1
            while i < len(g):
                edge = Edge(node, g[i])
                file_graph.add_edge(edge)
                i += 1
        return file_graph
    except FileNotFoundError as e:
        print(e)



if __name__=="__main__" :
    a_star_graph = read_mars_graph("MarsMap.txt")
    start_state = "8,8"
    s = map_state(start_state)
    s.mars_graph = a_star_graph
    result = a_star(s.location, h1, s.is_goal)
    print(result)
    result_b = a_star(s.location, sld, s.is_goal)
    print(result)