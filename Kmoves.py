# to solve this problem we use bacltracking
# it works by exploring all different paths!
def moves(arr, start, finish, k):
    # case if we are out of the bounds - we return false
    def is_valid(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0])

    def helper(x, y, steps_left):
        # case where we cant continue moving from the current point
        if not is_valid(x, y) or arr[x][y] == 1 or steps_left < 0:
            return False

        if (x, y) == finish:
            return True

        # we use bacltrack to mark the cell as visited
        saved_value = arr[x][y]
        arr[x][y] = -1

        # go to all possible moves: up, down, left, right
        for val1, val2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if helper(x + val1, y + val2, steps_left - 1):
                # if the target is reachable we return true
                arr[x][y] = saved_value
                return True

        # Revert the vlaue...
        arr[x][y] = saved_value

        return False

    return helper(start[0], start[1], k)

if __name__ == '__main__':
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    start = (0, 0)
    target = (2, 2)
    k = 6

    result = moves(grid, start, target, k)
    if result:
        print(f"it is possible to reach the target from the starting point in {k} steps .")
    else:
        print(f"it is not possible to reach the target from the starting point in {k} steps .")
