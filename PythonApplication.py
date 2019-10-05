import logging
import logstash
import sys
import time
from random import randint




game_logger = logging.getLogger('python-logstash-logger')
game_logger.setLevel(logging.INFO)
game_logger.addHandler(logstash.LogstashHandler('13.58.80.59', 5959, version=1))



def randomPlay():
    return randint(0,2)


def main():

 #Game play between 2 player#
    #List all player 1 choice 
    for i in range(30):
        player1 = randomPlay()
        if player1 == 0:
            extra = {'player1Choice' : 'Rock'}
            game_logger.info('outcome', extra=extra)
        elif player1 == 1:
            extra = {'player1Choice' : 'Paper'}
            game_logger.info('outcome', extra=extra)
        elif player1 == 2:
            extra = {'player1Choice' : 'Scissors'}
            game_logger.info('outcome', extra=extra)
            
     #List all player 2 choice               
        player2 = randomPlay()
        if player2 == 0:
            extra = {'player2Choice' : 'Rock'}
            game_logger.info('outcome', extra=extra)
        elif player2 == 1:
            extra = {'player2Choice' : 'Paper'}
            game_logger.info('outcome', extra=extra)
        elif player2 == 2:
            extra = {'player2Choice' : 'Scissors'}
            game_logger.info('outcome', extra=extra)
    
        #Warining if collison occur
        if player1 == player2:
            game_logger.warning('Detected collision of Player Choice')
            extra = {'win' : 'tie'}
            game_logger.info('outcome', extra=extra)
            
         #Listing all possible out come               
        if player1 == 0 and player2 == 1:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 0 and player2 == 2:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)
        if player1 == 1 and player2 == 0:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)
        if player1 == 1 and player2 == 2:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 2 and player2 == 0:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 2 and player2 == 1:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)

   


main()