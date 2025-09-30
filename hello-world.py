#This program wil write Hello World!


#This function tells the computer to print "Hello World"
def PrintHelloWorld():
	print("Hello World!")

#This defines our main() function for our program
def main():
	PrintHelloWorld()

#When we run the program, this executes first: Python has a failsafe to allow us to write complicated programs
if __name__=="__main__":
	main()