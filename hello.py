import os
def main():
	username=os.getenv('USERNAME')
	dist="C:/Users/"+username+"/Downloads"
	print(dist)
main()