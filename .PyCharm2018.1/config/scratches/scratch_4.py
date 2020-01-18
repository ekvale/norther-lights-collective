""" Chirstmas Trivia 2017 """

import sys
import random

class Question:
	def __init__(self, question, answer, options):
	    self.question = question
	    self.answer = answer
	    self.options = options

	def ask(self):
		for n, option in enumerate(self.options):
			print("{} {}".format(n + 1, option))

		response = int(sys.stdin.readline().strip())
		if response == self.answer:
			print("Correct")
		else:
			print("Wrong")

questions = [
	Question("How many legs does a dog have?", 4,  ["one", "two", "three", "four", "five"]),
	Question("How many legs does a moose have?", 4,  ["one", "two", "three", "four", "five"]) ]

random.shuffle(questions)
for question in questions:
	question.ask()