"""
River Crossing Puzzle Solver
Solves the classic farmer, fox, goose, and grain puzzle using BFS (Breadth-First Search)
"""

from collections import deque
from typing import Set, Tuple, List

class RiverCrossingPuzzle:
    def __init__(self):
        # State representation: (left_side, right_side, boat_location)
        # Each side is a frozenset of items: 'farmer', 'fox', 'goose', 'grain'
        self.initial_state = (
            frozenset(['farmer', 'fox', 'goose', 'grain']),  # Left side
            frozenset(),                                      # Right side
            'left'                                            # Boat location
        )
        self.goal_state = (
            frozenset(),                                      # Left side
            frozenset(['farmer', 'fox', 'goose', 'grain']),  # Right side
            'right'                                           # Boat location
        )
    
    def is_valid_state(self, left: frozenset, right: frozenset) -> bool:
        """Check if a state is valid (no rule violations)"""
        # Check left side
        if 'fox' in left and 'goose' in left and 'farmer' not in left:
            return False  # Fox and goose alone
        if 'goose' in left and 'grain' in left and 'farmer' not in left:
            return False  # Goose and grain alone
        
        # Check right side
        if 'fox' in right and 'goose' in right and 'farmer' not in right:
            return False  # Fox and goose alone
        if 'goose' in right and 'grain' in right and 'farmer' not in right:
            return False  # Goose and grain alone
        
        return True
    
    def get_next_states(self, state: Tuple) -> List[Tuple]:
        """Generate all valid next states from current state"""
        left, right, boat = state
        next_states = []
        
        if boat == 'left':
            # Farmer moves from left to right
            items_on_left = left - {'farmer'}
            
            # Farmer goes alone
            new_left = left - {'farmer'}
            new_right = right | {'farmer'}
            if self.is_valid_state(new_left, new_right):
                next_states.append((new_left, new_right, 'right'))
            
            # Farmer takes one item
            for item in items_on_left:
                new_left = left - {'farmer', item}
                new_right = right | {'farmer', item}
                if self.is_valid_state(new_left, new_right):
                    next_states.append((new_left, new_right, 'right'))
        else:
            # Farmer moves from right to left
            items_on_right = right - {'farmer'}
            
            # Farmer goes alone
            new_left = left | {'farmer'}
            new_right = right - {'farmer'}
            if self.is_valid_state(new_left, new_right):
                next_states.append((new_left, new_right, 'left'))
            
            # Farmer takes one item
            for item in items_on_right:
                new_left = left | {'farmer', item}
                new_right = right - {'farmer', item}
                if self.is_valid_state(new_left, new_right):
                    next_states.append((new_left, new_right, 'left'))
        
        return next_states
    
    def solve_bfs(self) -> List[Tuple]:
        """Solve using Breadth-First Search"""
        queue = deque([(self.initial_state, [self.initial_state])])
        visited = {self.initial_state}
        
        while queue:
            current_state, path = queue.popleft()
            
            if current_state == self.goal_state:
                return path
            
            for next_state in self.get_next_states(current_state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [next_state]))
        
        return []  # No solution found
    
    def format_state(self, state: Tuple) -> str:
        """Format state for display"""
        left, right, boat = state
        left_str = ', '.join(sorted(left)) if left else 'empty'
        right_str = ', '.join(sorted(right)) if right else 'empty'
        boat_str = f"[BOAT at {boat}]"
        return f"Left: {{{left_str}}} | Right: {{{right_str}}} {boat_str}"
    
    def print_solution(self, path: List[Tuple]):
        """Print the solution in a readable format"""
        if not path:
            print("No solution found!")
            return
        
        print("=" * 80)
        print("SOLUTION FOUND!")
        print("=" * 80)
        print(f"\nTotal moves: {len(path) - 1}\n")
        
        for i, state in enumerate(path):
            print(f"Step {i}: {self.format_state(state)}")
        
        print("\n" + "=" * 80)

def main():
    puzzle = RiverCrossingPuzzle()
    print("Solving the River Crossing Puzzle...")
    print("Rules:")
    print("1. The fox cannot be left alone with the goose")
    print("2. The goose cannot be left alone with the grain")
    print("3. The boat can only hold the farmer and one other item\n")
    
    solution = puzzle.solve_bfs()
    puzzle.print_solution(solution)
    
    # Print moves in a concise format
    if solution:
        print("\nMove Summary:")
        for i in range(len(solution) - 1):
            current = solution[i]
            next_state = solution[i + 1]
            
            left_now, right_now, boat_now = current
            left_next, right_next, boat_next = next_state
            
            if boat_now == 'left':
                moved_items = left_now - left_next
                moved_str = ' and '.join(sorted(moved_items))
                print(f"Move {i + 1}: Farmer takes {moved_str} → Right")
            else:
                moved_items = right_now - right_next
                moved_str = ' and '.join(sorted(moved_items))
                print(f"Move {i + 1}: Farmer takes {moved_str} → Left")

if __name__ == '__main__':
    main()