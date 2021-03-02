def calculate_apr(principal, interest_rate, years):
	if((isinstance(principal, float) or isinstance(principal,int))  and (isinstance(interest_rate, float) and interest_rate >= 0)
	 and isinstance(years, int)):
		for i in range(years):
			principal = principal*(1 + interest_rate)	#use the initial principal and update it while in the loop.
		return principal
	else :
		print("invalid parameters")	#indicate that the parameter is invalid
		return False

"""
Caculate the apr

This function caculate the apr for user with given parameters
starting principal of $500.0, interest rate of 3% for 65 years

Parameters
--------
principal: float
	Investment amount start with
interest_rate: float
	Invesment rate in decimal
years: int
	Numbers of years of investment

Return
-------
float
	The outcome of investing "principal" at "interest_rate" for "years" years
boolean
	False if the parameter is invalid
Example
-------
>>> calculate_apr(100.0, 0.1, 1)
110.00
>>> calculate_apr(2500.0, 0.05, 10)
4072.24
>>> calculate_apr(100, 0.03, 2.3)
invalid parameter
"""

print(f'The outcome of investing $500 at an interest rate of 3% for 65 years is ${calculate_apr(500.0, 0.03, 65)}')
# calculate_apr(100, 0.2, 2.5)
# print(calculate_apr(100, - 0.2, 2.5))
