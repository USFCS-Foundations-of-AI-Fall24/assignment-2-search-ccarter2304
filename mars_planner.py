## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search #, iterative_deepening_search


class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, charged=False, holding_tool=False, moved_to_station=False):
        self.loc = loc
        self.sample_extracted = sample_extracted
        self.holding_sample = holding_sample
        self.charged=charged
        self.prev = None
        self.holding_tool = holding_tool
        self.moved_to_station = moved_to_station

    ## you do this.
    def __eq__(self, other):
        return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.charged == other.charged and self.holding_tool == other.holding_tool and self.moved_to_station == other.moved_to_station)


    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" + f"Holding Tool? {self.holding_tool}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2

def move_to_station(state) :
    r2 = deepcopy(state)
    r2.moved_to_station = True
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here
def pick_up_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state) :
    r2 = deepcopy(state)
    r2.sample_extracted = True
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "battery" : #and dropped_tool_at_station:
        r2.charged = True
    r2.prev = state
    return r2

action_list = [move_to_sample, pick_up_tool, drop_tool, use_tool,
               pick_up_sample, move_to_station,
               drop_sample,  move_to_battery, charge]

def battery_goal(state) :
    return state.loc == "battery"
## add your goals here.
def charge_goal(state) :
    return state.charged == True and state.moved_to_station == True

def sample_station_goal(state) :
    return state.sample_extracted == True and state.holding_sample == False
## returns True if we are at the battery, charged, and the sample is at the station.
def mission_complete(state) :
    if (battery_goal(state) and
        charge_goal(state) and
       sample_station_goal(state)):
        return True
    else :
        return False

def move_to_sample_goal(state) :
    return (state.loc == "sample" and state.sample_extracted == False
            and state.holding_sample == False and state.charged == False and
            state.holding_tool == False and state.moved_to_station == False)

def remove_sample(state) :
    return (state.sample_extracted == True and state.holding_sample == False
            and state.charged == False and state.loc == "station")

def return_to_charger(state) :
    return (state.moved_to_station == True and state.loc == "battery")

if __name__=="__main__" :
    s = RoverState()
    result_bfs = breadth_first_search(s, action_list, mission_complete)
    result_dfs = depth_first_search(s, action_list, mission_complete)
    result_dls = depth_first_search(s, action_list, mission_complete, limit=7)

    ### Problem Decomposition
    # pds = RoverState()
    # result_pds = breadth_first_search(pds, action_list, move_to_sample_goal)
    # pds_rs = RoverState(loc="sample")
    # result_rs = breadth_first_search(pds_rs, action_list, remove_sample)
    # pds_rc = RoverState(loc="station", holding_sample=False, moved_to_station=True, sample_extracted=True)
    # result_rc = breadth_first_search(pds_rc, action_list, return_to_charger)

    # pds = RoverState()
    # result_pds = depth_first_search(pds, action_list, move_to_sample_goal, limit=2)
    # pds_rs = RoverState(loc="sample")
    # result_rs = depth_first_search(pds_rs, action_list, remove_sample, limit=4)
    # pds_rc = RoverState(loc="station", holding_sample=False, moved_to_station=True, sample_extracted=True)
    # result_rc = depth_first_search(pds_rc, action_list, return_to_charger, limit=2)







