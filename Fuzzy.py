import numpy as np
import random

def fuzzy_set(distance):
	if distance < 0:
		return "left"
	elif distance > 0:
		return "right"
	else:
		return "straight"

def fuzzy_rule(left, right):
	turn = 0.0
	dr_dl = right - left
	direction = fuzzy_set(dr_dl)

	if direction == "left":
		if dr_dl < -8:
			turn = -15
		else:
			turn = 5 * dr_dl
	elif direction == "right":	
		if dr_dl > 8:
			turn = 15
		else:
			turn = 5 * dr_dl
	else:	# straight
		turn = 0

	return turn

def process(left, right): 
	return fuzzy_rule(left, right)
	