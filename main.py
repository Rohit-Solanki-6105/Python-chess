import pygame
from data.classes.Board import Board
import tkinter as tk
from tkinter import messagebox

def win(winner):
# Create a Tkinter window
	root = tk.Tk()
# Hide the main window
	root.withdraw()
# Display the message box
	messagebox.showinfo("Winner",winner,)
# Destroy the Tkinter window
	root.destroy()


pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
logo = pygame.image.load('chess_logo.png')
pygame.display.set_icon(logo)
title = pygame.display.set_caption('R Chess')
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()


font = pygame.font.SysFont('Arial', 32)

    
 
# create a text surface object,
# on which text is drawn on it.

if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
		if board.is_in_checkmate('black'): # If black is in checkmate
			# text = font.render('White wins!', True)
			# screen.blit(font.render('White wins!', True,(255,244,200)), (20, 50))
			win("White wins!")
			pygame.display.update()
			print('White wins!')
			running = False
		elif board.is_in_checkmate('white'): # If white is in checkmate
			win("Black wins!")
			print('Black wins!')
			running = False
		# Draw the board
		draw(screen)