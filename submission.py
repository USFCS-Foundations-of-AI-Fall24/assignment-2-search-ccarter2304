## Carmen Carter
## CS 386

from mars_planner import RoverState, action_list, mission_complete, move_to_sample_goal, remove_sample, return_to_charger
from search_algorithms import breadth_first_search, depth_first_search
from routefinder import a_star, map_state, sld, h1, read_mars_graph
from Graph import Graph

if __name__=="__main__" :
    # ### mars_planner.py
    # ## Pre-problem decompositon
    s = RoverState()
    print("Pre Problem Decomposition")
    print("------------------------------------------------------------")
    print("-------------------Breath-First Search----------------------")
    breadth_first_search(s, action_list, mission_complete)
    print("-------------------Depth-First Search-----------------------")
    depth_first_search(s, action_list, mission_complete)
    print("-------------------Depth-Limited Search---------------------")
    depth_first_search(s, action_list, mission_complete, limit=7)
    print("------------------------------------------------------------")
    print("Post Problem Decomposition")
    print("------------------------------------------------------------")
    print("-------------------Breath-First Search----------------------")
    pds = RoverState()
    breadth_first_search(pds, action_list, move_to_sample_goal)
    pds_rs = RoverState(loc="sample")
    print("************************************************************")
    breadth_first_search(pds_rs, action_list, remove_sample)
    print("************************************************************")
    pds_rc = RoverState(loc="station", holding_sample=False, moved_to_station=True, sample_extracted=True)
    breadth_first_search(pds_rc, action_list, return_to_charger)
    print("------------------------------------------------------------")
    print("-------------------Depth-First Search-----------------------")
    pds = RoverState()
    depth_first_search(pds, action_list, move_to_sample_goal)
    print("************************************************************")
    pds_rs = RoverState(loc="sample")
    depth_first_search(pds_rs, action_list, remove_sample)
    print("************************************************************")
    pds_rc = RoverState(loc="station", holding_sample=False, moved_to_station=True, sample_extracted=True)
    depth_first_search(pds_rc, action_list, return_to_charger)
    print("------------------------------------------------------------")
    print("-------------------Depth-Limited Search---------------------")
    pdl = RoverState()
    depth_first_search(pdl, action_list, move_to_sample_goal, limit=2)
    pdl_rs = RoverState(loc="sample")
    print("************************************************************")
    depth_first_search(pdl_rs, action_list, remove_sample, limit=4)
    print("************************************************************")
    pdl_rc = RoverState(loc="station", holding_sample=False, moved_to_station=True, sample_extracted=True)
    depth_first_search(pdl_rc, action_list, return_to_charger, limit=2)

    ### A*
    print("----------------------------A *-----------------------------")
    a_star_graph = read_mars_graph("MarsMap.txt")
    start_state = "8,8"
    s = map_state(start_state)
    s.mars_graph = a_star_graph
    result_b = a_star(s.location, sld, s.is_goal)
    print("************************************************************")
    print("State Count: ", result_b)
    print("************************************************************")

    ###UCS
    print("---------------------------UCS------------------------------")
    print("************************************************************")
    result = a_star(s.location, h1, s.is_goal)
    print("State Count: ", result)
    print("************************************************************")



