# Using GPT-4.1

from collections import deque

# Each state: (farmer, fox, goose, grain)
# 0 = left bank, 1 = right bank

def is_valid(state):
    farmer, fox, goose, grain = state
    # If farmer is not with fox and goose are together, fox eats goose
    if fox == goose and farmer != fox:
        return False
    # If farmer is not with goose and grain are together, goose eats grain
    if goose == grain and farmer != goose:
        return False
    return True

def get_next_states(state):
    farmer, fox, goose, grain = state
    next_states = []
    # Farmer moves alone
    new_farmer = 1 - farmer
    new_state = (new_farmer, fox, goose, grain)
    if is_valid(new_state):
        next_states.append((new_state, "Farmer crosses alone"))
    # Farmer takes fox
    if farmer == fox:
        new_state = (1 - farmer, 1 - fox, goose, grain)
        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Fox"))
    # Farmer takes goose
    if farmer == goose:
        new_state = (1 - farmer, fox, 1 - goose, grain)
        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Goose"))
    # Farmer takes grain
    if farmer == grain:
        new_state = (1 - farmer, fox, goose, 1 - grain)
        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Grain"))
    return next_states

def solve():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add(start)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        for next_state, action in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
    return None

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Solution found:")
        for step, action in enumerate(solution, 1):
            print(f"{step}. {action}")
    else:
        print("No solution found.")