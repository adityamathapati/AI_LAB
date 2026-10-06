
import random

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)
    moves = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]
    for dr, dc, move in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[n_idx] = (
                new_state[n_idx],
                new_state[zero_idx],
            )
            neighbors.append((tuple(new_state), move))
    return neighbors


def make_random_state(steps=10):
    current = goal_state
    for _ in range(steps):
        neighbors = [n for n, m in get_neighbors(current)]
        current = random.choice(neighbors)
    return current


def dls(current_state, path, depth, visited):
    if current_state == goal_state:
        return path
    if depth <= 0:
        return None
    visited.add(current_state)
    for neighbor, move in get_neighbors(current_state):
        if neighbor not in visited:
            result = dls(neighbor, path + [move], depth - 1, visited)
            if result is not None:
                return result
    visited.remove(current_state)
    return None


def idfs(start_state, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        result = dls(start_state, [], depth, visited)
        if result is not None:
            return result
    return None


initial_state = make_random_state()
print("Random Initial State:", initial_state)
print("IDFS Path:", idfs(initial_state))
