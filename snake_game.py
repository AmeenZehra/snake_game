import turtle
import time
import random
import pygame  
pygame.mixer.init()

# sound effects
eat_food_sound = pygame.mixer.Sound("eat.mp3")
turn_sound = pygame.mixer.Sound("turn.wav")
collision_sound = pygame.mixer.Sound("go.wav")
level_up_sound = pygame.mixer.Sound("nxtlvl.wav")

# Screen 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#initial speed
delay = 0.15  
level = 1

# Snake
snake = turtle.Turtle()
snake.shape("circle")
snake.color("green")
snake.penup()
snake.speed(0)
snake.direction = "stop"

# Snake body 
segments = []

# Food 
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)

# Obstacles for level 2
obstacles = []

# Score
score = 0
high_score = 0

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# instructions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"
        pygame.mixer.Sound.play(turn_sound) 

def go_down():
    if snake.direction != "up":
        snake.direction = "down"
        pygame.mixer.Sound.play(turn_sound)  

def go_left():
    if snake.direction != "right":
        snake.direction = "left"
        pygame.mixer.Sound.play(turn_sound)  

def go_right():
    if snake.direction != "left":
        snake.direction = "right"
        pygame.mixer.Sound.play(turn_sound)  

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#level 2 
def setup_level_2():
    global level, obstacles
    level = 2
    obstacles = []
    positions = [(-200, 0), (-160, 0), (-120, 0), (-80, 0), (-40, 0),
                 (40, 0), (80, 0), (120, 0), (160, 0), (200, 0),
                 (0, 200), (0, 160), (0, 120), (0, 80), (0, 40),
                 (0, -40), (0, -80), (0, -120), (0, -160), (0, -200)]
    for position in positions:
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("blue")
        obstacle.penup()
        obstacle.goto(position)
        obstacles.append(obstacle)

#collisions
def check_collision_with_obstacles():
    for obstacle in obstacles:
        if snake.distance(obstacle) < 20:
            pygame.mixer.Sound.play(collision_sound)  # Play collision sound
            return True
    return False

#reset
def reset_game():
    global score, segments, level, delay
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "stop"
    
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    if level == 2:
        for obstacle in obstacles:
            obstacle.goto(1000, 1000)
        obstacles.clear()
        level = 1
    
    score = 0
    delay = 0.15  
    scoreboard.clear()
    scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Keyboard keys
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main game 
try:
    while True:
        wn.update()

        # collision with border
        if (snake.xcor() > 290 or snake.xcor() < -290 or
            snake.ycor() > 290 or snake.ycor() < -290):
            scoreboard.goto(0, 0)
            scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
            reset_game()
            time.sleep(2)
            scoreboard.clear()
            scoreboard.goto(0, 260)
            scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        # eating food
        if snake.distance(food) < 20:
            pygame.mixer.Sound.play(eat_food_sound)

            # move food at random
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # snake body segment
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("circle")
            segment.color("light green")
            segment.penup()
            segments.append(segment)

            # score
            score += 10
            if score > high_score:
                high_score = score
            scoreboard.clear()
            scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

            # Increase speed
            delay -= 0.003

            # check for next level
            if score >= 100 and level == 1:
                setup_level_2()
                pygame.mixer.Sound.play(level_up_sound)  
                scoreboard.goto(0, 0)
                scoreboard.write("Level 2", align="center", font=("Courier", 24, "normal"))
                time.sleep(2)
                scoreboard.clear()
                scoreboard.goto(0, 260)
                scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        
        if len(segments) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y)

        move()

        # collision with self
        for segment in segments:
            if segment.distance(snake) < 20:
                scoreboard.goto(0, 0)
                scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
                reset_game()
                time.sleep(2)
                scoreboard.clear()
                scoreboard.goto(0, 260)
                scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        # collision with obstacles
        if level == 2 and check_collision_with_obstacles():
            scoreboard.goto(0, 0)
            scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
            reset_game()
            time.sleep(2)
            scoreboard.clear()
            scoreboard.goto(0, 260)
            scoreboard.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)
except turtle.Terminator:
    print("Game closed.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    pygame.mixer.quit()
