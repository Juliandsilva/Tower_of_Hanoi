"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools
        self.tmodel = TOAHModel(self.number_of_stools)
        self.finished = False
        self.counter = 1

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
                
        self.tmodel.fill_first_stool(self.number_of_cheeses)

        print(self.tmodel)
        while not self.finished:
            x = input('Which stool index do you want to move a cheese from?')
            if x == 'end':
                self.finished = True
                return None
            y = input('Which stool index do you want to move the cheese to?')
            if y == 'end':
                self.finished = True
                return None
            try:
                move(self.tmodel, int(x), int(y))
                print(self.tmodel)
            except ValueError:
                print('That is an invalid move. Please try again')
            except IllegalMoveError:
                print('That is an invalid move. Please try again')


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print("Welcome to Sukhman and Julian's Tower Game! Please read and follow \
the rules below!")
    print("Rules: Your objective is to move all of the Cheeses from the first \
stool to the last stool. You will asked how many cheeses and stools you \
would like to play with. You must play with at least 1 cheese and at least \
2 stools. You move cheeses one at a time by specifying the indices of the \
stool you would like to move the top cheese from and the stool which you \
would like to move the cheese to. You cannot place a smaller cheese on top \
of a larger cheese. You also cannot move cheeses from empty or non-\
existing stools nor to non-existing stools. You may quit the game any time \
after specifying a number of cheeses and stools by inputing 'end' as a \
source or destination stool.")
    
    a = input('Enter the number of cheeses would you like to play with ')
    while not (a.isnumeric() and int(a) > 0):
        print('Please provide a valid number of cheeses')
        a = input('Enter the number of cheeses would you like to play with ')
    b = input('Enter the number of stools would you like to play with ')
    while not (b.isnumeric() and int(b) > 1):
        print('Please provide a valid number of stools')
        b = input('Enter the number of stools would you like to play with ')
    controller = ConsoleController(int(a), int(b))
    controller.play_loop()
    
    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
    
