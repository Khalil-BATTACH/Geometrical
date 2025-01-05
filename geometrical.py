import turtle
import matplotlib.pyplot as plt

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a triangle
def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

# Function to draw a circle
def draw_circle(t, radius):
    t.circle(radius)

# Function to demonstrate matplotlib
def show_matplotlib_example():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]
    plt.plot(x, y, marker='o')
    plt.title("Exemple de graphique avec Matplotlib")
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.show()

# Main function to draw shapes with Turtle
def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.title("Dessiner des formes géométriques avec Turtle")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    t.speed(2)

    # Draw a square
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    draw_square(t, 100)

    # Draw a triangle
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_triangle(t, 100)

    # Draw a circle
    t.penup()
    t.goto(200, 0)
    t.pendown()
    draw_circle(t, 50)

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

    # Show matplotlib example
    show_matplotlib_example()

if __name__ == "__main__":
    main()
    