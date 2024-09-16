from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 1

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        state_count += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(state_count)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    print(state_count)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    depth_list  = {}
    closed_list = {}
    state_count = 1
    depth = 0

    search_queue.append((startState,""))
    depth_list[startState] = depth
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        state_count += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(state_count)
            return next_state
        else :
            if depth <= limit :
                successors = next_state[0].successors(action_list)
                if depth_list[next_state[0]] <= depth :
                    depth += 1
                if use_closed_list :
                    successors = [item for item in successors
                                            if item[0] not in closed_list]
                    for s in successors :
                        closed_list[s[0]] = True
                        depth_list[s[0]] = depth
                search_queue.extend(successors)
    print(state_count)

## add iterative deepening search here
#
def iterative_deepening_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    depth_list = {}
    state_count = 1
    depth = 0
    limit = 1

    search_queue.append((startState,""))
    depth_list[startState] = depth
    if use_closed_list :
        closed_list[startState] = True
    ## do DLS with appending limit until limit hits length of search_queue
    while limit <= len(search_queue) :
        ## this is a (state, "action") tuple
        while len(search_queue) > 0  :
            next_state = search_queue.pop()
            state_count += 1
            if goal_test(next_state[0]):
                print("Goal found")
                print(next_state)
                ptr = next_state[0]
                while ptr is not None :
                    ptr = ptr.prev
                    print(ptr)
                print(state_count)
                return next_state
            else :
                if depth <= limit :
                    successors = next_state[0].successors(action_list)
                    #print(depth_list[next_state[0]])
                    if depth_list[next_state[0]] <= depth:
                        depth += 1
                    if use_closed_list :
                        successors = [item for item in successors
                                            if item[0] not in closed_list]
                        for s in successors :
                            closed_list[s[0]] = True
                            depth_list[s[0]] = depth
                    search_queue.extend(successors)
        limit += 1
        depth = 0
        print(state_count)



