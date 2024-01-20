import turtle

def snowflake(lengthSide, depth):
	if (depth == 0):
		turtle.forward(lengthSide)
		return
	lengthSide /= 3.0
	snowflake(lengthSide, depth - 1)
	turtle.left(60)
	snowflake(lengthSide, depth - 1)
	turtle.right(120)
	snowflake(lengthSide, depth - 1)
	turtle.left(60)
	snowflake(lengthSide, depth - 1)


if __name__ == "__main__":
	turtle.speed(0)
	length = 300.0
	turtle.penup()
	turtle.backward(length/2.0)
	turtle.pendown()
	for i in range(3):
		snowflake(length, 4)
		turtle.right(120)
	turtle.mainloop()