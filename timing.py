import time

def calculate_time(func):
	def wrapper():
		x = time.time()		# save first time as x, before start of function
		func()
		print(f'Total time {time.time() - x}')
	return wrapper

"""
Caculate Time

Calculate the time to execute any given function

Parameter
--------
func
	Any given function

Return
-------
wrapper
	that print out the time it take for that function to run

Example
----------------
function is  time.sleep(2)
Total time 2.001
"""

@calculate_time
def func():		# tester function, to see if it acurate
	return time.sleep(2)

#@calculate_time
#def hello():
#	print("hello professor and grader, have a great day")

# hello()
func()
