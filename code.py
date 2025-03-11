import heapq

# Directions (Up, Down, Left, Right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    # Heuristic: Manhattan Distance
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # A* algorithm implementation
    def astar():
        open_list = []  # Priority queue
        heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))  # (f_score, g_score, position)
        came_from = {}  # To track the path
        g_score = {start: 0}  # Actual cost from start to current point
        f_score = {start: heuristic(start, end)}  # Estimated cost (f = g + h)
        
        while open_list:
            _, current_g, current = heapq.heappop(open_list)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path  # Return the found path

            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                # Ensure the neighbor is within bounds and not an obstacle
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative_g_score = current_g + 1

                    # If this path is better, update the scores
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                        heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

        return None  # Return None if no path is found

    return astar()

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Start at top-left corner
end = (4, 4)    # End at bottom-right corner

path = a_star(grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
