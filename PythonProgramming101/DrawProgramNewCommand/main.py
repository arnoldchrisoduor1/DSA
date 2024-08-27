import turtle

def main():
    filename = input("Please enter the drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()

    with open(filename, "r") as file:
        # Read the first command to start processing
        command = file.readline().strip()

        # Process commands from the file
        while command != "":
            if command == "goto":
                x = float(file.readline())
                y = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.goto(x, y)

            elif command == "circle":
                radius = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.circle(radius)

            elif command == "beginfill":
                color = file.readline().strip()
                t.fillcolor(color)
                t.begin_fill()

            elif command == "endfill":
                t.end_fill()

            elif command == "penup":
                t.penup()

            elif command == "pendown":
                t.pendown()

            else:
                print("Unknown command found in file:", command)

            # Read the next command
            command = file.readline().strip()

    # Complete the drawing
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
