from collections import deque

def is_valid(state):
    # state: (farmer, fox, goose, grain) 
    # 0 means left bank, 1 means right bank
    farmer, fox, goose, grain = state
    
    # If fox and goose are together and farmer is away
    if fox == goose and farmer != fox:
        return False
    # If goose and grain are together and farmer is away
    if goose == grain and farmer != goose:
        return False
    
    return True

def get_next_states(state):
    farmer, fox, goose, grain = state
    next_states = []
    
    # Farmer can move alone
    next_states.append((1 - farmer, fox, goose, grain))
    
    # Farmer can take the fox
    if farmer == fox:
        next_states.append((1 - farmer, 1 - fox, goose, grain))
        
    # Farmer can take the goose
    if farmer == goose:
        next_states.append((1 - farmer, fox, 1 - goose, grain))
        
    # Farmer can take the grain
    if farmer == grain:
        next_states.append((1 - farmer, fox, goose, 1 - grain))
        
    return [s for s in next_states if is_valid(s)]

def solve():
    # Initial state: all on the left (0)
    start_state = (0, 0, 0, 0)
    # Goal state: all on the right (1)
    goal_state = (1, 1, 1, 1)
    
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    item_names = ["Farmer", "Fox", "Goose", "Grain"]
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [goal_state]
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    
    return None

def format_state(state):
    items = ["Farmer", "Fox", "Goose", "Grain"]
    left = [items[i] for i in range(4) if state[i] == 0]
    right = [items[i] for i in range(4) if state[i] == 1]
    return f"Left: {', '.join(left)} | Right: {', '.join(right)}"

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Sequence of steps to solve the puzzle:")
        for i, state in enumerate(solution):
            print(f"Step {i}: {format_state(state)}")
            if i < len(solution) - 1:
                # Determine what moved
                prev = solution[i]
                curr = solution[i+1]
                moved = []
                for j in range(1, 4):
                    if prev[j] != curr[j]:
                        moved.append(["Fox", "Goose", "Grain"][j-1])
                
                if not moved:
                    print("  -> Farmer crosses alone")
                else:
                    print(f"  -> Farmer takes the {' and '.join(moved)}")
    else:
        print("No solution found.")