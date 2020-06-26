from state import *
from utils import *


# For the Below implementations we have already imported a Stack class, a Queue class and a PriorityQueue class
# to help you complete the algorithms. PLEASE DO NOT ADD OR REMOVE ANY IMPORTS.

# You will also find that the GameStateHandler class (already imported) will help perform needed operations on the
# the game states. To declare a GameStateHandler simply wrap it around a GameState like such,
# handler = GameStateHandler(GameState) where GameState will be an instance of GameState.

# Below is a list of helpful functions:
# GameStateHandler.get_successors() --> returns successors of the handled state
# GameState.get_player_position() --> returns the players position in that game state as (row, col)

class SearchAlgorithms:

    @staticmethod
    def depth_first_search(goal_fn, start_state):
        # Question 1, your DFS solution should go here
        # Returns a list of actions to take to get to the solution or [] if no solution exists
        handler = GameStateHandler(start_state)

        state = start_state
        # Visited nodes
        explored = []

        # If the problem is already done
        if goal_fn(state):
            return []

        # Open stack
        open_stack = Stack()
        # Update open stack with start node
        open_stack.push(handler.get_state())
        # Taken actions
        moves = Stack()
        moves.push([])

        while not open_stack.empty():
            # Set to current node
            handler.swap_state(open_stack.pop())
            actions = moves.pop()

            if goal_fn(handler.get_state()):
                return actions

            # Add to explored
            explored.append(handler.get_state())
            for (action, successor) in handler.get_successors():
                if successor not in explored:
                    state = successor
                    move = actions + [action]
                    open_stack.push(state)
                    moves.push(move)

        return moves.pop()

    @staticmethod
    def breadth_first_search(goal_fn, start_state):
        # Question 2, your BFS solution should go here
        # Returns a list of actions to take to get to the solution or [] if no solution exists
        handler = GameStateHandler(start_state)

        state = start_state
        # Visited nodes
        explored = [state]

        # If the problem is already done
        if goal_fn(state):
            return []

        # Open Queue
        open_queue = Queue()
        # Update open stack with start node
        open_queue.push(handler.get_state())
        # Taken actions
        moves = Queue()
        moves.push([])

        while not open_queue.empty():
            actions = moves.pop()
            handler.swap_state(open_queue.pop())

            if goal_fn(handler.get_state()):
                return actions

            for (action, successor) in handler.get_successors():
                if successor not in explored:
                    explored.append(successor)
                    move = actions + [action]
                    open_queue.push(successor)
                    moves.push(move)
        return moves.pop()

    @staticmethod
    def uniform_cost_search(goal_fn, start_state, cost_fn=lambda pos: 1):
        # Question 3, your UCS solution should go here
        # Returns a list of actions to take to get to the solution or [] if no solution exists
        handler = GameStateHandler(start_state)

        state = start_state
        # Visited nodes
        explored = []

        # If the problem is already done
        if goal_fn(state):
            return explored
        # Open Queue
        open_queue = PriorityQueue()
        # Update open stack with start node
        open_queue.push(state, cost_fn(start_state.get_player_position()))

        # Taken actions
        moves = PriorityQueue()
        moves.push([], 0)

        while not open_queue.isEmpty():

            actions = moves.pop()
            handler.swap_state(open_queue.pop())

            if handler.get_state() not in explored:
                explored.append(handler.get_state())
                if goal_fn(handler.get_state()):
                    return actions

                for (action, successor) in handler.get_successors():
                    if successor not in explored:
                        move = actions + [action]
                        open_queue.push(successor, cost_fn(successor.get_player_position()))
                        moves.push(move, cost_fn(successor.get_player_position()))
        return moves.pop()

    @staticmethod
    def a_star_search(goal_fn, start_state, cost_fn=lambda pos: 1, heuristic=lambda state: 0):
        # Question 4, your A Star solution should go here
        # Returns a list of actions to take to get to the solution or [] if no solution exists
        handler = GameStateHandler(start_state)

        # Visited nodes
        explored = []

        # If the problem is already done
        if goal_fn(start_state):
            return explored
        # Open Queue
        open_queue = PriorityQueue()
        # Update open stack with start node
        open_queue.push(start_state, 0)

        # Taken actions
        moves = PriorityQueue()
        moves.push([], heuristic(start_state))

        while not open_queue.isEmpty():
            actions = moves.pop()
            handler.swap_state(open_queue.pop())

            if handler.get_state() not in explored:
                explored.append(handler.get_state())
                if goal_fn(handler.get_state()):
                    return actions

                for (action, successor) in handler.get_successors():
                    if successor not in explored:
                        move = actions + [action]
                        if heuristic(successor) is not None:
                            cost = heuristic(successor) + cost_fn(successor.get_player_position())
                        else:
                            cost = cost_fn(successor.get_player_position())
                        open_queue.push(successor, cost)
                        moves.push(move, cost)
        return moves.pop()
