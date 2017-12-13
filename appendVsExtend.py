'''
Code to illustrate difference between append and extend
'''

def func1(bar = []):
	 bar.append('xyz') 
	 return bar 
print(func1())

def func2(bar = []):
	 bar.extend('xyz') 
	 return bar
print(func2())
