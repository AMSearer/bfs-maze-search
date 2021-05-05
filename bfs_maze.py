import time
from collections import deque

class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location, path=None):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
        self.path = path or []

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('\033[96m*\x1b[0m', end=' ')   # print a blue *
                else:
                    print(self.grid[r][c], end=' ')      # prints a space or wall
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        possibleMoves = []
        position = self.location
        posx = self.location[0]
        posy = self.location[1]

        # Check North (x-1, y)
        if self.grid[posx - 1][posy] == " ":
            possibleMoves += ['N']

        # Check South (x+1, y)
        if self.grid[posx + 1][posy] == " ":
            possibleMoves += ['S']

        # Check East (x, y+1)
        if self.grid[posx][posy+1] == " ":
            possibleMoves += ['E']

        # Check West (x, y-1)
        if self.grid[posx][posy-1] == " ":
            possibleMoves += ['W']

        return possibleMoves


    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        position = self.location
        posx = self.location[0]
        posy = self.location[1]
        if (move == 'N'):
            return Maze(self.grid, (posx - 1, posy), self.path + [move])
        elif (move == 'S'):
            return Maze(self.grid, (posx + 1, posy), self.path + [move])
        elif (move == 'E'):
            return Maze(self.grid, (posx, posy+1), self.path + [move])
        elif (move == 'W'):
            return Maze(self.grid, (posx, posy-1), self.path + [move])

class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        print("start")
        q = deque()
        closedList = []
        q.append(maze)



        while q:  # Will be False if q is empty
            #pop next state
            state = q.popleft()

            #check if goal
            if state.location == goal.location:
                # return path to goal
                return state.path

            #else generate list of moves and add child states to queue
            else:
                closedList += [state.location]
                moves = state.moves()
                for move in moves:
                    temp = state.neighbor(move)
                    if temp.location not in closedList:
                        q.append(temp)




def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.50)
        maze.display()


if __name__ == '__main__':
    main()