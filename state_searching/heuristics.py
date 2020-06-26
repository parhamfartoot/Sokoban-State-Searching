from state import *


class Heuristics:

    # We have included above two common heuristics, manhattan distance and euclidean distance so feel free to use
    # either if needed.
    #
    # Helpful functions:
    # GameState.get_boxes() --> returns a list of (row, col) positions representing where the boxes are on the map
    # GameState.get_switches() --> returns a dictionary where the keys are the locations of the switches as (row, col) and the value
    #                              being True if the switch is on and False if off.
    # GameState.get_player_position() --> returns the current position of the player in the form (row, col)
    # GameState.get_remaining_points() --> returns a list of the positions of the remaining armory points of the map in the form (row, col)

    @staticmethod
    def manhattan_heuristic(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def euclidean_heuristic(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    @staticmethod
    def two_boxes_heuristic(state):
        # Question 5, your solution for the two boxes heuristic will go here.
        # Return a heuristic value (an integer) representing the heuristic cost of the given state.
        switch = []
        total = 0
        for sw in state.get_switches().values():
            if sw is True:
                continue
            else:
                switch.append(sw)
                for box in state.get_boxes():
                    if box in switch:
                        continue
                    else:
                        box_signed_dst = Heuristics.manhattan_signed(box, min(state.get_switches(),
                                                                              key=lambda
                                                                                  switch: Heuristics.manhattan_signed(
                                                                                  box,
                                                                                  switch)))
                        target = [0, 0]
                        if box_signed_dst[0] > 0:  # box needs to go Right
                            target[0] = box[0] - 1
                        elif box_signed_dst[0] < 0:  # box needs to go Left
                            target[0] = box[0] + 1
                        if box_signed_dst[1] > 0:  # box needs to go Up
                            target[1] = box[1] - 1
                        elif box_signed_dst[1] < 0:  # box need to go Down
                            target[1] = box[1] + 1

                        total += abs(box_signed_dst[0]) + abs(box_signed_dst[1])

    @staticmethod
    def points_only_heuristic(state):
        # Question 6, your solution for the points only heuristic will go here.
        # Return a heuristic value (an integer) representing the heuristic cost of the given state.
        pass

    def manhattan_signed(p1, p2):
        return p2[0] - p1[0], p2[1] - p1[1]
