#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:42:54 2021

@author: thiagofreitas
"""


""" MCTS bot - When the game is in phase 1, this bot uses Monte Carlo Tree Search algorithm
to explore game tree asymmetrically, based on a calculated UCB1 value... """

from api import State, util
import random


class bot:

    def __init__(self, time_limit):
        self.time_limit = time_limit

    def get_move(self, state):

        # See if we're player 1 or 2
        player = state.whose_turn()

        # Get a list of all legal moves
        moves = state.moves()

        # Sometimes many moves have the same, highest score, and we'd like the bot to pick a random one.
        # Shuffling the list of moves ensures that.
        random.shuffle(moves)

        for move in moves:



class Node:

    def __init__(self, state, parent=None):
        self.visits = 1
        self.reward = 0.0
        self.state = state
        self.children = []
        self.parent = parent

    def add_child(self, child_state):
        child = Node(child_state, self)
        self.children.append(child)

    def update(self, reward):
        self.reward += reward
        self.visits += 1

    def fully_expanded(self):
        if len(self.children) == self.state.num_moves:
            return True
        return False


