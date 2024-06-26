import turtle as t
import random as rand
import time as time1

t.setup(1200, 800)
t.hideturtle()
t_field = t.Turtle()

t_field.hideturtle()
t_field.speed(0)
t_field.width(2)
t_field.color('blue')

# Поле гравця
t_field.penup()
t_field.goto(-400, 150)
t_field.pendown()

for i in range(4):
    t_field.forward(300)
    t_field.right(90)

t_field.penup()
t_field.goto(-400, 150)
t_field.pendown()


def draw_lines():
    t_field.forward(30)
    t_field.right(90)
    t_field.forward(300)
    t_field.left(90)
    t_field.forward(30)
    t_field.left(90)
    t_field.forward(300)
    t_field.right(90)


for i in range(5):
    draw_lines()

t_field.goto(-100, 150)
t_field.right(90)

for i in range(5):
    draw_lines()

# Поле бота
t_field.penup()
t_field.goto(80, 150)
t_field.pendown()

t_field.left(90)

for i in range(4):
    t_field.forward(300)
    t_field.right(90)

for i in range(5):
    draw_lines()

t_field.right(90)
for i in range(5):
    draw_lines()

t_text = t.Turtle()
t_text.color('black')
t_text.hideturtle()


def draw_text(x, y, text, type):
    t_text.speed(0)
    t_text.penup()
    t_text.goto(x, y)
    t_text.pendown()
    t_text.write(text, font=("Arial", type, "bold"))
    t_text.hideturtle()

t_how_to_build = t.Turtle()
t_how_to_build.hideturtle()


def draw_how_to_build(x, y, text, type):
    t_how_to_build.speed(0)
    t_how_to_build.penup()
    t_how_to_build.goto(x, y)
    t_how_to_build.pendown()
    t_how_to_build.write(text, font=("Arial", type, "bold"))


# Нумерація клітинок поля гравця
draw_text(-390, 150, 'A', 14)
draw_text(-360, 150, 'B', 14)
draw_text(-330, 150, 'C', 14)
draw_text(-300, 150, 'D', 14)
draw_text(-270, 150, 'E', 14)
draw_text(-240, 150, 'F', 14)
draw_text(-210, 150, 'G', 14)
draw_text(-180, 150, 'H', 14)
draw_text(-150, 150, 'I', 14)
draw_text(-120, 150, 'J', 14)

draw_text(-415, 125, '1', 14)
draw_text(-415, 95, '2', 14)
draw_text(-415, 65, '3', 14)
draw_text(-415, 35, '4', 14)
draw_text(-415, 5, '5', 14)
draw_text(-415, -25, '6', 14)
draw_text(-415, -55, '7', 14)
draw_text(-415, -85, '8', 14)
draw_text(-415, -115, '9', 14)
draw_text(-420, -145, '10', 14)

# Нумерація клітинок поля бота
draw_text(90, 150, 'A', 14)
draw_text(120, 150, 'B', 14)
draw_text(150, 150, 'C', 14)
draw_text(180, 150, 'D', 14)
draw_text(210, 150, 'E', 14)
draw_text(240, 150, 'F', 14)
draw_text(270, 150, 'G', 14)
draw_text(300, 150, 'H', 14)
draw_text(330, 150, 'I', 14)
draw_text(360, 150, 'J', 14)

draw_text(65, 125, '1', 14)
draw_text(65, 95, '2', 14)
draw_text(65, 65, '3', 14)
draw_text(65, 35, '4', 14)
draw_text(65, 5, '5', 14)
draw_text(65, -25, '6', 14)
draw_text(65, -55, '7', 14)
draw_text(65, -85, '8', 14)
draw_text(65, -115, '9', 14)
draw_text(60, -145, '10', 14)

# Флот гравця
t_text.color('blue')
draw_text(-345, -230, 'Ваш флот', 25)

# Флот бота
t_text.color('red')
draw_text(112, -230, 'Флот опонента', 25)

t_circle = t.Turtle()
t_circle.hideturtle()


def draw_dot(x,y):
    t_circle.speed(0)
    t_circle.penup()
    t_circle.color('black')
    t_circle.goto(x+15, y-15)
    t_circle.pendown()
    t_circle.dot(10)
    
t_cross = t.Turtle()
t_cross.hideturtle()

def draw_cross(x,y):
    t_cross.speed(0)
    t_cross.color('red')
    t_cross.width(3)
    t_cross.penup()
    t_cross.goto(x,y)
    t_cross.pendown()
    t_cross.right(45)
    t_cross.forward(42.42)
    t_cross.right(135)
    t_cross.penup()
    t_cross.forward(30)
    t_cross.pendown()
    t_cross.right(135)
    t_cross.forward(42.42)
    t_cross.left(135)
    t_cross.penup()
    t_cross.forward(30)
    t_cross.pendown()
    t_cross.right(180)

t_ships = t.Turtle()
t_surround = t.Turtle()
t_surround.hideturtle()
t_ships.hideturtle()

def surround_1_deck_ship(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    t_surround.color('black')
    for i in range(4):
        t_surround.forward(30)
        t_surround.right(90)


def surround_2_deck_ship_width(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    t_surround.color('black')
    for i in range(2):
        t_surround.forward(60)
        t_surround.right(90)
        t_surround.forward(30)
        t_surround.right(90)
    

def surround_2_deck_ship_lenght(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    t_surround.color('black')
    for i in range(2):
        t_surround.forward(30)
        t_surround.right(90)
        t_surround.forward(60)
        t_surround.right(90)

def surround_3_deck_ship_width(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    t_surround.color('black')
    for i in range(2):
        t_surround.forward(90)
        t_surround.right(90)
        t_surround.forward(30)
        t_surround.right(90)

def surround_3_deck_ship_lenght(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    for i in range(2):
        t_surround.forward(30)
        t_surround.right(90)
        t_surround.forward(90)
        t_surround.right(90)

def surround_4_deck_ship_width(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    for i in range(2):
        t_surround.forward(120)
        t_surround.right(90)
        t_surround.forward(30)
        t_surround.right(90)

def surround_4_deck_ship_lenght(x,y):
    t_surround.speed(0)
    t_surround.width(4)
    t_surround.penup()
    t_surround.goto(x, y)
    t_surround.pendown()
    for i in range(2):
        t_surround.forward(30)
        t_surround.right(90)
        t_surround.forward(120)
        t_surround.right(90)


def draw_single_deck_ship(x, y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(4):
        t_ships.forward(30)
        t_ships.right(90)
    t_ships.hideturtle()
    

def draw_double_deck_ship_width(x, y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(60)
        t_ships.right(90)
        t_ships.forward(30)
        t_ships.right(90)
    for i in range(4):
        t_ships.forward(30)
        t_ships.right(90)
    t_ships.hideturtle()


def draw_double_deck_ship_lenght(x, y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(30)
        t_ships.right(90)
        t_ships.forward(60)
        t_ships.right(90)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    

def draw_triple_deck_ship_width(x,y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(90)
        t_ships.right(90)
        t_ships.forward(30)
        t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.right(180)
    

def draw_triple_deck_ship_lenght(x,y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(30)
        t_ships.right(90)
        t_ships.forward(90)
        t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    
    
def draw_four_deck_ship_width(x,y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(120)
        t_ships.right(90)
        t_ships.forward(30)
        t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    for i in range(2):
        t_ships.right(90)
        t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(120)
    t_ships.right(180)
    

def draw_four_deck_ship_lenght(x,y, penup_down):
    t_ships.speed(0)
    t_ships.width(4)
    t_ships.penup()
    t_ships.goto(x, y)
    if penup_down == 'up':
        t_ships.penup()
    else:
        t_ships.pendown()
    t_ships.color('black')
    for i in range(2):
        t_ships.forward(30)
        t_ships.right(90)
        t_ships.forward(120)
        t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.left(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    t_ships.forward(90)
    t_ships.right(90)
    t_ships.forward(30)
    t_ships.right(90)
    
    t_ships.left(90)
    

t_draw_victory = t.Turtle()
t_draw_whos_turn = t.Turtle()
t_draw_whos_turn.hideturtle()
t_draw_victory.hideturtle()

def draw_turn(x,y, text, type):
    t_draw_whos_turn.speed(0)
    t_draw_whos_turn.penup()
    t_draw_whos_turn.goto(x, y)
    t_draw_whos_turn.pendown()
    t_draw_whos_turn.write(text, font=("Arial", type, "bold"))

def draw_victory(x,y, text, type, color):
    t_draw_victory.color(color)
    t_draw_victory.speed(0)
    t_draw_victory.penup()
    t_draw_victory.goto(x, y)
    t_draw_victory.pendown()
    t_draw_victory.write(text, font=("Arial", type, "bold"))

t_draw_inability = t.Turtle()
t_draw_inability.hideturtle()

def unable_to_build_ship(x,y, text, type):
    t_draw_inability.speed(0)
    t_draw_inability.penup()
    t_draw_inability.color('red')
    t_draw_inability.goto(x, y)
    t_draw_inability.pendown()
    t_draw_inability.write(text, font=("Arial", type, "bold"))
    t_draw_inability.hideturtle()


t_button = t.Turtle()
t_button.hideturtle()

def choice_bottom():
    t_button.hideturtle()
    t_button.speed(0)
    t_button.width(3)
    t_button.penup()
    t_button.goto(-40,200)
    t_button.pendown()
    for i in range(2):
        t_button.forward(60)
        t_button.right(90)
        t_button.forward(30)
        t_button.right(90)
    t_button.forward(30)
    t_button.right(90)
    t_button.forward(30)
    t_button.penup()
    t_button.goto(-30,177)
    t_button.pendown()
    t_button.right(180)
    for i in range(2):
        t_button.forward(15)
        t_button.right(90)
        t_button.forward(8)
        t_button.right(90)
    t_button.forward(8)
    t_button.right(90)
    t_button.forward(8)
    t_button.penup()
    t_button.goto(-3,188)
    t_button.pendown()
    for i in range(2):
        t_button.forward(15)
        t_button.right(90)
        t_button.forward(8)
        t_button.right(90)
    t_button.forward(8)
    t_button.right(90)
    t_button.forward(8)

draw_choice = t.Turtle()
draw_choice.hideturtle()

draw_directory = 'none'

first_button = t.Turtle()
first_button.hideturtle()

second_button = t.Turtle()
second_button.hideturtle()


def set_direct_vertical(x,y):
    global draw_directory
    global draw_choice
    global may_draw_button
    if may_draw_button == True:
        may_draw_button = False
        draw_directory = 'vertical'
        print(draw_directory)
        draw_choice.penup()
        draw_choice.goto(-40,200)
        draw_choice.pendown()
        draw_choice.speed(9)
        draw_choice.width(3)
        draw_choice.color('green')
        for i in range(4):
            draw_choice.forward(30)
            draw_choice.right(90)
        draw_choice.clear()
        draw_choice.hideturtle()
        may_draw_button = True
    

def set_direct_gorizontal(x,y):
    global draw_directory
    global draw_choice
    global may_draw_button
    if may_draw_button == True:
        may_draw_button = False
        draw_directory = 'gorizontal'
        print(draw_directory)
        draw_choice.penup()
        draw_choice.goto(-10,200)
        draw_choice.pendown()
        draw_choice.speed(9)
        draw_choice.width(3)
        draw_choice.color('green')
        for i in range(4):
            draw_choice.forward(30)
            draw_choice.right(90)
        draw_choice.clear()
        draw_choice.hideturtle()
        may_draw_button = True



first_button.onclick(set_direct_gorizontal)
second_button.onclick(set_direct_vertical)

single_deck_ships = 0

double_deck_ships = 0

triple_deck_ships = 0

four_deck_ships = 0

coordinates_of_cells_1field = []

coordinates_of_cells_0field = []


list_status_cells_1field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

list_status_cells_0field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

cell0_x = -400
cell0_y = 150

cell1_x = 80
cell1_y = 150

cell_x = -400
cell_y = 150


player_turn = 'player'

# player field
for i in range(10):
    coordinates_of_cells_0field.append([])
    for j in range(10):
        coordinates_of_cells_0field[i].append([cell0_x, cell0_y])
        cell0_x += 30
    cell0_x = -400
    cell0_y -= 30

# bot field
for i in range(10):
    coordinates_of_cells_1field.append([])
    for j in range(10):
        coordinates_of_cells_1field[i].append([cell1_x, cell1_y])
        cell1_x += 30
    cell1_x = 80
    cell1_y -= 30




game_stage = 'Розстановка однопалубних кораблів'

select_ship_directory = False

draw_turn(-305, 270 , "Натисніть на клітинку для побудови однопалубних кораблів", 15)

list_cord_around_cell_1deck = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

list_cord_around_cell_2deck_width_right_to_left = [[-1,0],[-1,1],[0,1],[1,1],[2,1],[2,0],[2,-1],[1,-1],[0,-1],[-1,-1]]

list_cord_around_cell_2deck_width_left_to_right = [[-2,0],[-2,1],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-2,-1]]

list_cord_around_cell_2deck_lenght_left_to_right = [[-1,2],[0,2],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

list_cord_around_cell_2deck_lenght_right_to_left = [[-1,0],[-1,-1],[-1,-2],[0,-2],[1,-2],[1,-1],[1,0],[1,1],[0,1],[-1,1],]

list_cord_around_cell_3deck_width_left_to_right = [[-3,0],[-3,1],[-3,-1],[-2,1],[-2,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,1],[1,0],[1,-1]]

list_cord_around_cell_3deck_width_right_to_left = [[-1,0],[-1,1],[0,1],[1,1],[2,1],[3,1],[3,0],[3,-1],[2,-1],[1,-1],[0,-1],[-1,-1]]

list_cord_around_cell_3deck_width_mid = [[-2,0],[-2,1],[-2,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,1],[2,1],[2,0],[2,-1],[1,-1]]

list_cord_around_cell_3deck_lenght_right_to_left = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[1,-2],[1,-3],[0,-3],[-1,-3],[-1,-1],[-1,-2]]

list_cord_around_cell_3deck_lenght_left_to_right = [[-1,3],[0,3],[1,3],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[-1,2]]

list_cord_around_cell_3deck_lenght_mid = [[-1,2],[0,2],[1,2],[1,1],[1,0],[1,-1],[1,-2],[0,-2],[-1,-2],[-1,-1],[-1,0],[-1,1]]


list_cord_around_cell_4deck_width_left_to_right = [[-4,0],[-4,1],[-3,1],[-2,1],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-2,-1],[-3,-1],[-4,-1]]

list_cord_around_cell_4deck_width_right_to_left = [[-1,1],[0,1],[1,1],[2,1],[3,1],[4,1],[4,0],[4,-1],[3,-1],[2,-1],[1,-1],[0,-1],[-1,-1],[-1,0]]

list_cord_around_cell_4deck_width_mid_right = [[-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[2,0],[2,-1],[1,-1],[0,-1],[-1,-1],[-2,-1],[-3,-1],[-3,0]]

list_cord_around_cell_4deck_width_mid_left = [[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],[3,0],[3,-1],[2,-1],[1,-1],[0,-1],[-1,-1],[-2,-1],[-2,0]]

list_cord_around_cell_4deck_lenght_left_to_right = [[-1,4],[0,4],[1,4],[1,3],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[-1,2],[-1,3]]

list_cord_around_cell_4deck_lenght_right_to_left = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[1,-2],[1,-3],[1,-4],[0,-4],[-1,-4],[-1,-3],[-1,-2],[-1,-1],[-1,0]]

list_cord_around_cell_4deck_lenght_mid_right = [[-1,0],[-1,1],[-1,-1],[-1,-2],[-1,-3],[0,-3],[1,-3],[1,-2],[1,-1],[1,0],[1,1],[1,2],[0,2],[-1,2]]


list_cord_around_cell_4deck_lenght_mid_left = [[-1,0],[-1,1],[-1,-1],[-1,-2],[0,-2],[1,-2],[1,-1],[1,0],[1,1],[1,2],[1,3],[0,3],[-1,3],[-1,2],[-1,1]]

########

list_cord_around_cell_2deck_width = [[-1,0],[-1,1],[0,1],[1,1],[2,1],[2,0],[2,-1],[1,-1],[0,-1],[-1,-1]]

list_cord_around_cell_2deck_lenght = [[-1,0],[-1,1],[-1,2],[0,2],[1,2],[1,1],[0,-1],[-1,-1],[1,0],[1,1],[1,-1]]

list_cord_around_cell_3deck_width = [[-1,0],[-1,1],[0,1],[1,1],[2,1],[3,1],[3,0],[3,-1],[2,-1],[1,-1],[0,-1],[-1,-1]]

list_cord_around_cell_3deck_lenght = [[-1,0],[-1,1],[-1,2],[-1,3],[0,3],[1,3],[1,2],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[0,-1]]

list_cord_around_cell_4deck_width = [[-1,0],[-1,1],[-1,-1],[0,1],[1,1],[2,1],[3,1],[4,1],[4,0],[4,-1],[3,-1],[2,-1],[1,-1],[0,-1]]

list_cord_around_cell_4deck_lenght = [[0,4],[-1,0],[-1,1],[-1,2],[-1,3],[-1,4],[1,0],[1,1],[1,2],[1,3],[1,4],[0,-1],[-1,-1],[1,-1]]


#########
coordinates_around_cell_1deck =  [[-30,0],[-30,30],[0,30],[30,30],[30,0],[30,-30],[0,-30],[-30,-30]]

coordinates_around_cell_2deck_width_right_to_left = [[-30,0],[-30,30],[0,30],[30,30],[60,30],[60,0],[60,-30],[30,-30],[0,-30],[-30,-30]]

coordinates_around_cell_2deck_width_left_to_right = [[-60,0],[-60,30],[-30,30],[0,30],[30,30],[30,0],[30,-30],[0,-30],[-30,-30],[-60,-30]]

coordinates_around_cell_2deck_lenght_right_to_left = [[-30,0],[-30,30],[-30,60],[0,60],[30,60],[0,-30],[-30,-30],[30,0],[30,30],[30,-30],]

coordinates_around_cell_2deck_lenght_left_to_right = [[-30,0],[-30,-30],[-30,-60],[0,-60],[30,-60],[30,-30],[30,0],[30,30],[0,30],[-30,30],]

coordinates_around_cell_3deck_width_left_to_right = [[-90,0],[-90,30],[-90,-30],[-60,30],[-60,-30],[-30,30],[-30,-30],[0,30],[0,-30],[30,30],[30,0],[30,-30]]

coordinates_around_cell_3deck_width_right_to_left = [[-30,0],[-30,30],[0,30],[30,30],[60,30],[90,30],[90,0],[90,-30],[60,-30],[30,-30],[0,-30],[-30,-30]]

coordinates_around_cell_3deck_width_mid = [[-60,0],[-60,30],[-60,-30],[-30,30],[-30,-30],[0,30],[0,-30],[30,30],[60,30],[60,0],[60,-30],[30,-30]]

coordinates_around_cell_3deck_lenght_right_to_left = [[-30,0],[-30,30],[0,30],[30,30],[30,0],[30,-30],[30,-60],[30,-90],[0,-90],[-30,-90],[-30,-30],[-30,-60]]

coordinates_around_cell_3deck_lenght_left_to_right = [[-30,90],[0,90],[30,90],[30,60],[30,30],[30,0],[30,-30],[0,-30],[-30,-30],[-30,0],[-30,30],[-30,60]]

coordinates_around_cell_3deck_lenght_mid = [[-30,60],[0,60],[30,60],[30,30],[30,0],[30,-30],[30,-60],[0,-60],[-30,-60],[-30,-30],[-30,0],[-30,30]]

coordinates_around_cell_4deck_width_left_to_right = [[-120,0],[-120,30],[-90,30],[-60,30],[-30,30],[0,30],[30,30],[30,0],[30,-30],[0,-30],[-30,-30],[-60,-30],[-90,-30],[-120,-30]]

coordinates_around_cell_4deck_width_right_to_left = [[-30,30],[0,30],[30,30],[60,30],[90,30],[120,30],[120,0],[120,-30],[90,-30],[60,-30],[30,-30],[0,-30],[-30,-30],[-30,0]]

coordinates_around_cell_4deck_width_mid_right = [[-90,30],[-60,30],[-30,30],[0,30],[30,30],[60,30],[60,0],[60,-30],[30,-30],[0,-30],[-30,-30],[-60,-30],[-90,-30],[-90,0]]

coordinates_around_cell_4deck_width_mid_left = [[-60,30],[-30,30],[0,30],[30,30],[60,30],[90,30],[90,0],[90,-30],[60,-30],[30,-30],[0,-30],[-30,-30],[-60,-30],[-60,0]]

coordinates_around_cell_4deck_lenght_left_to_right = [[-30,120],[0,120],[30,120],[30,90],[30,60],[30,30],[30,0],[30,-30],[0,-30],[-30,-30],[-30,0],[-30,30],[-30,60],[-30,90]]

coordinates_around_cell_4deck_lenght_right_to_left = [[-30,30],[0,30],[30,30],[30,0],[30,-30],[30,-60],[30,-90],[30,-120],[0,-120],[-30,-120],[-30,-90],[-30,-60],[-30,-30],[-30,0]]

coordinates_around_cell_4deck_lenght_mid_right = [[-30,90],[0,90],[30,90],[30,60],[30,30],[30,0],[30,-30],[30,-60],[0,-60],[-30,-60],[-30,-30],[-30,0],[-30,30],[-30,60]]

coordinates_around_cell_4deck_lenght_mid_left = [[-30,0],[-30,30],[-30,60],[0,60],[30,60],[30,30],[30,0],[30,-30],[30,-60],[30,-90],[0,-90],[-30,-90],[-30,-60],[-30,-30]]

##################

cords_of_311_hit_1 = []
cords_of_311_hit_2 = []
cords_of_311_hit_3 = []

cords_of_312_hit_1 = []
cords_of_312_hit_2 = []
cords_of_312_hit_3 = []

cords_of_321_hit_1 = []
cords_of_321_hit_2 = []
cords_of_321_hit_3 = []
cords_of_321_hit_1_zero_ind = []
cords_of_321_hit_2_zero_ind = []
cords_of_321_hit_3_zero_ind = []

cords_of_322_hit_1 = []
cords_of_322_hit_2 = []
cords_of_322_hit_3 = []
cords_of_322_hit_1_zero_ind = []
cords_of_322_hit_2_zero_ind = []
cords_of_322_hit_3_zero_ind = []

cords_of_421_hit_1 = []
cords_of_421_hit_1_zero_indX = []
cords_of_421_hit_1_zero_indY = []
cords_of_421_hit_1_zero_indXY = []
cords_of_421_hit_2 = []
cords_of_421_hit_2_zero_indX = []
cords_of_421_hit_2_zero_indY = []
cords_of_421_hit_2_zero_indXY = []


cords_of_422_hit_1 = []
cords_of_422_hit_1_zero_indX = []
cords_of_422_hit_1_zero_indY = []
cords_of_422_hit_2 = []
cords_of_422_hit_2_zero_indX = []
cords_of_422_hit_2_zero_indY = []

cords_of_423_hit_1 = []
cords_of_423_hit_1_zero_indX = []
cords_of_423_hit_1_zero_indY = []
cords_of_423_hit_2 = []
cords_of_423_hit_2_zero_indX = []
cords_of_423_hit_2_zero_indY = []

cords_of_411_hit_1 = []
cords_of_411_hit_1_zero_indX = []
cords_of_411_hit_1_zero_indY = []
cords_of_411_hit_2 = []
cords_of_411_hit_2_zero_indX = []
cords_of_411_hit_2_zero_indY = []

cords_of_412_hit_1 = []
cords_of_412_hit_1_zero_indX = []
cords_of_412_hit_1_zero_indY = []
cords_of_412_hit_2 = []
cords_of_412_hit_2_zero_indX = []
cords_of_412_hit_2_zero_indY = []

cords_of_413_hit_1 = []
cords_of_413_hit_1_zero_indX = []
cords_of_413_hit_1_zero_indY = []
cords_of_413_hit_2 = []
cords_of_413_hit_2_zero_indX = []
cords_of_413_hit_2_zero_indY = []

cords_of_521_hit_1 = []
cords_of_521_hit_1_zero_indX = []
cords_of_521_hit_1_zero_indY = []

cords_of_522_hit_1 = []
cords_of_522_hit_1_zero_indX = []
cords_of_522_hit_1_zero_indY = []

cords_of_523_hit_1 = []
cords_of_523_hit_1_zero_indX = []
cords_of_523_hit_1_zero_indY = []

cords_of_524_hit_1 = []
cords_of_524_hit_1_zero_indX = []
cords_of_524_hit_1_zero_indY = []

cords_of_511_hit_1 = []
cords_of_511_hit_1_zero_indX = []
cords_of_511_hit_1_zero_indY = []

cords_of_512_hit_1 = []
cords_of_512_hit_1_zero_indX = []
cords_of_512_hit_1_zero_indY = []

cords_of_513_hit_1 = []
cords_of_513_hit_1_zero_indX = []
cords_of_513_hit_1_zero_indY = []

cords_of_514_hit_1 = []
cords_of_514_hit_1_zero_indX = []
cords_of_514_hit_1_zero_indY = []


double_deck_311_hits_1 = 0
double_deck_311_hits_2 = 0
double_deck_311_hits_3 = 0

double_deck_312_hits_1 = 0
double_deck_312_hits_2 = 0 
double_deck_312_hits_3 = 0

double_deck_321_hits_1 = 0
double_deck_321_hits_2 = 0
double_deck_321_hits_3 = 0


double_deck_322_hits_1 = 0
double_deck_322_hits_2 = 0
double_deck_322_hits_3 = 0

triple_deck_421_hits_1 = 0
triple_deck_421_hits_2 = 0

triple_deck_422_hits_1 = 0
triple_deck_422_hits_2 = 0

triple_deck_423_hits_1 = 0
triple_deck_423_hits_2 = 0

triple_deck_411_hits_1 = 0
triple_deck_411_hits_2 = 0

triple_deck_412_hits_1 = 0
triple_deck_412_hits_2 = 0

triple_deck_413_hits_1 = 0
triple_deck_413_hits_2 = 0

four_deck_521_hits_1 = 0
four_deck_522_hits_1 = 0
four_deck_523_hits_1 = 0
four_deck_524_hits_1 = 0

four_deck_511_hits_1 = 0
four_deck_512_hits_1 = 0
four_deck_513_hits_1 = 0
four_deck_514_hits_1 = 0


may_draw_single_deck_ships = True
may_draw_double_deck_ships = False
may_draw_triple_deck_ships = False
may_draw_four_deck_ships = False

double_deck_hits_player = 0
bot_four_deck_hits = 0

drowned_ships_player = 0
drowned_ships_bot = 0

may_draw_ships = True
may_draw_button = True
may_draw_cross = True
may_draw_dot = True
may_count_hit = True

draw_cross_permited = True
draw_dot_permited = True


ind_x11 = None
ind_y11 = None

def bot_pick_1deck_or_empty_cell():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_311_hits_1
    global double_deck_311_hits_2
    global double_deck_312_hits_1
    global ind_x11
    global ind_y11
    global double_deck_312_hits_2
    global double_deck_311_hits_3
    global double_deck_312_hits_3
    global double_deck_321_hits_1
    global double_deck_322_hits_1
    global double_deck_321_hits_2
    global double_deck_322_hits_2
    global double_deck_321_hits_3
    global double_deck_322_hits_3
    global triple_deck_421_hits_1
    global triple_deck_422_hits_1
    global triple_deck_423_hits_1
    global triple_deck_411_hits_1
    global triple_deck_412_hits_1
    global triple_deck_413_hits_1
    global triple_deck_421_hits_2
    global triple_deck_422_hits_2
    global triple_deck_423_hits_2
    global triple_deck_411_hits_2
    global triple_deck_412_hits_2
    global triple_deck_413_hits_2
    global four_deck_521_hits_1
    global four_deck_522_hits_1
    global four_deck_523_hits_1
    global four_deck_524_hits_1
    global four_deck_511_hits_1
    global four_deck_512_hits_1
    global four_deck_513_hits_1
    global four_deck_514_hits_1
    global may_draw_dot
    global may_draw_cross
    global draw_cross_permited
    global draw_dot_permited
    while drowned_ships_bot != 10:
        # print(drowned_ships_bot,'amount of drowned ships')
        ind_x = rand.randint(0,9)
        ind_y = rand.randint(0,9)
        cord = coordinates_of_cells_0field[ind_y][ind_x]
        draw_dot_permited = False
        draw_cross_permited = False
        if list_status_cells_0field[ind_y][ind_x] == 1 or list_status_cells_0field[ind_y][ind_x] == 0 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9 and list_status_cells_0field[ind_y][ind_x] != 8 and list_status_cells_0field[ind_y][ind_x] != 2:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            print(ind_y,ind_x)
            print(cord)
            if list_status_cells_0field[ind_y][ind_x] == 0 or list_status_cells_0field[ind_y][ind_x] == 1:
                draw_dot(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 3
                player_turn = 'player'
                t_draw_whos_turn.clear()
                draw_turn(-68, 270 , "Хід гравця", 15)
                if player_turn == 'player':
                    draw_dot_permited = True
                    draw_cross_permited = True
                    player_pick()
                draw_dot_permited = True
                draw_cross_permited = True
        elif list_status_cells_0field[ind_y][ind_x] == 2 and list_status_cells_0field[ind_y][ind_x] != 3:
            list_status_cells_0field[ind_y][ind_x] = 8
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            draw_cross(cord[0],cord[1])
            for i in list_cord_around_cell_1deck:
                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
            for j in coordinates_around_cell_1deck:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
            drowned_ships_bot += 1

            

        elif list_status_cells_0field[ind_y][ind_x] == 311 and list_status_cells_0field[ind_y][ind_x] != 3:
            ind_x11 = ind_x
            ind_y11 = ind_y
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            if cords_of_double_deck_ship_lenght_1_player[0] == [cord[0],cord[1]]:
                cords_of_311_hit_1.extend([cord[0],cord[1],0])
                draw_cross(cord[0],cord[1])
                double_deck_311_hits_1 += 1
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_lenght_1_player[2] += 1
                if cords_of_double_deck_ship_lenght_1_player[2] == 1:
                    print(list_status_cells_0field[ind_y-1][ind_x])
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_311_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]-30)
                        double_deck_311_hits_1 += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_1_player[2] += 1
                        if cords_of_double_deck_ship_lenght_1_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_311_hits_1 = 0 
                            bot_pick_1deck_or_empty_cell()


            elif cords_of_double_deck_ship_lenght_2_player[0] == [cord[0],cord[1]]:
                cord = coordinates_of_cells_0field[ind_y][ind_x]
                cords_of_311_hit_2.extend([cord[0],cord[1],0])
                draw_cross(cord[0],cord[1])
                double_deck_311_hits_2 += 1
                double_deck_311_hits_2 = 1
                cords_of_double_deck_ship_lenght_2_player[2] += 1
                list_status_cells_0field[ind_y][ind_x] = 8
                if cords_of_double_deck_ship_lenght_2_player[2] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_311_hit_2[2] += 1
                        cords_of_311_hit_2[2] = 1
                        print(cords_of_311_hit_2[2],'sasdasdsadasd')
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]-30)
                        double_deck_311_hits_2 += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_2_player[2] += 1
                        if cords_of_double_deck_ship_lenght_2_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')  
                            drowned_ships_bot += 1  
                            double_deck_311_hits_2 = 0
                            bot_pick_1deck_or_empty_cell() 

                                    

            elif cords_of_double_deck_ship_lenght_3_player[0] == [cord[0],cord[1]]:
                cord = coordinates_of_cells_0field[ind_y][ind_x]
                cords_of_311_hit_3.extend([cord[0],cord[1],0])
                draw_cross(cord[0],cord[1])
                double_deck_311_hits_3 += 1
                double_deck_311_hits_3 = 1
                cords_of_double_deck_ship_lenght_3_player[2] += 1
                list_status_cells_0field[ind_y][ind_x] = 8
                if cords_of_double_deck_ship_lenght_3_player[2] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_311_hit_3[2] += 1
                        cords_of_311_hit_3[2] = 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]-30)
                        double_deck_311_hits_3 += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_3_player[2] += 1
                        if cords_of_double_deck_ship_lenght_3_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_311_hits_3 = 0
                            bot_pick_1deck_or_empty_cell() 


        elif list_status_cells_0field[ind_y][ind_x] == 312 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y                                  
            if cords_of_double_deck_ship_lenght_1_player[1] == [cord[0],cord[1]]:
                cords_of_double_deck_ship_lenght_1_player[2] += 1
                draw_cross(cord[0],cord[1])
                double_deck_312_hits_1 += 1
                cords_of_312_hit_1.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8   
                if cords_of_double_deck_ship_lenght_1_player[2] == 1:
                    print('ffffffffffffffffffffffffffffffffffffffffffffff')
                    print(list_status_cells_0field[ind_y-1][ind_x])
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_312_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        double_deck_312_hits_1 += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_1_player[2] += 1
                        if cords_of_double_deck_ship_lenght_1_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8           
                            for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_312_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_double_deck_ship_lenght_2_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                cords_of_double_deck_ship_lenght_2_player[2] += 1
                cords_of_312_hit_2.extend([cord[0],cord[1],0])
                double_deck_312_hits_2 += 1
                list_status_cells_0field[ind_y][ind_x] = 8  
                if cords_of_double_deck_ship_lenght_2_player[2] == 1:
                    print('ffffffffffffffffffffffffffffffffffffffffffffff')
                    print(list_status_cells_0field[ind_y-1][ind_x])
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_312_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        double_deck_312_hits_2 += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_2_player[2] += 1
                        if cords_of_double_deck_ship_lenght_2_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8           
                            for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])                              
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_312_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_double_deck_ship_lenght_3_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                cords_of_double_deck_ship_lenght_3_player[2] += 1
                cords_of_312_hit_3.extend([cord[0],cord[1],0])
                double_deck_312_hits_3 += 1
                list_status_cells_0field[ind_y][ind_x] = 8  
                if cords_of_double_deck_ship_lenght_3_player[2] == 1:
                    print('ffffffffffffffffffffffffffffffffffffffffffffff')
                    print(list_status_cells_0field[ind_y-1][ind_x])
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_312_hit_3[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        double_deck_312_hits_3 += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_double_deck_ship_lenght_3_player[2] += 1
                        if cords_of_double_deck_ship_lenght_3_player[2] == 2:
                            for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8           
                            for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_312_hits_3 = 0
                            bot_pick_1deck_or_empty_cell()

        elif list_status_cells_0field[ind_y][ind_x] == 321 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_double_deck_ship_width_1_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_321_hits_1 += 1
                cords_of_321_hit_1.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_1_player[2] += 1
                if cords_of_double_deck_ship_width_1_player[2] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_321_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        cords_of_321_hit_1_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_321_hit_1_zero_ind[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            player_pick()
                    else:
                        draw_cross(cord[0]+30,cord[1])
                        double_deck_321_hits_1 += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 8
                        cords_of_double_deck_ship_width_1_player[2] += 1
                        cords_of_double_deck_ship_width_1_player[2] = 2 
                        if cords_of_double_deck_ship_width_1_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_321_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()
            
            elif cords_of_double_deck_ship_width_2_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_321_hits_2 += 1
                cords_of_321_hit_2.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_2_player[2] += 1
                if cords_of_double_deck_ship_width_2_player[2] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_321_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        cords_of_321_hit_2_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_321_hit_2_zero_ind[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]+30,cord[1])
                        double_deck_321_hits_2 += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 8
                        cords_of_double_deck_ship_width_2_player[2] += 1
                        if cords_of_double_deck_ship_width_2_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_321_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_double_deck_ship_width_3_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_321_hits_3 += 1
                cords_of_321_hit_3.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_3_player[2] += 1
                if cords_of_double_deck_ship_width_3_player[2] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])
                        cords_of_321_hit_3[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        cords_of_321_hit_3_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_321_hit_3_zero_ind[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            player_pick()
                    else:
                        draw_cross(cord[0]+30,cord[1])
                        double_deck_321_hits_3 += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 8
                        cords_of_double_deck_ship_width_3_player[2] += 1
                        if cords_of_double_deck_ship_width_3_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_321_hits_3 = 0
                            bot_pick_1deck_or_empty_cell()
                    
                    

                    
        elif list_status_cells_0field[ind_y][ind_x] == 322 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_double_deck_ship_width_1_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_322_hits_1 += 1
                cords_of_322_hit_1.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_1_player[2] += 1
                if cords_of_double_deck_ship_width_1_player[2] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_322_hit_1[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        cords_of_322_hit_1_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0]+30,cord[1])
                        cords_of_322_hit_1_zero_ind[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()       
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_double_deck_ship_width_1_player[2] += 1
                        if cords_of_double_deck_ship_width_1_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_322_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()



            elif cords_of_double_deck_ship_width_2_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_322_hits_2 += 1
                cords_of_322_hit_2.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_2_player[2] += 1
                if cords_of_double_deck_ship_width_2_player[2] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_322_hit_2[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        cords_of_322_hit_2_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0]+30,cord[1])
                        cords_of_322_hit_2_zero_ind[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()       
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_double_deck_ship_width_2_player[2] += 1
                        if cords_of_double_deck_ship_width_2_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_322_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()


            elif cords_of_double_deck_ship_width_3_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                double_deck_322_hits_3 += 1
                cords_of_322_hit_3.extend([cord[0],cord[1],0])
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_double_deck_ship_width_3_player[2] += 1
                if cords_of_double_deck_ship_width_3_player[2] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_322_hit_3[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        cords_of_322_hit_3_zero_ind.extend([cord[0],cord[1],0])
                        draw_dot(cord[0]+30,cord[1])
                        cords_of_322_hit_3_zero_ind[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()       
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_double_deck_ship_width_3_player[2] += 1
                        if cords_of_double_deck_ship_width_3_player[2] == 2:
                            for i in list_cord_around_cell_2deck_width_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                    list_status_cells_0field[ind_y][ind_x] = 8
                            for j in coordinates_around_cell_2deck_width_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            double_deck_322_hits_3 = 0
                            bot_pick_1deck_or_empty_cell()


        elif list_status_cells_0field[ind_y][ind_x] == 421 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_width_1_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                triple_deck_421_hits_1 += 1
                cords_of_421_hit_1.extend([cord[0],cord[1],0])
                cords_of_421_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
                cords_of_421_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_triple_deck_ship_width_1_player[3] += 1
                if cords_of_triple_deck_ship_width_1_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])  
                        cords_of_421_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30) 
                        cords_of_421_hit_1_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30)  
                        cords_of_421_hit_1_zero_indY[2] += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]+30,cord[1])
                        list_status_cells_0field[ind_y][ind_x+1] = 8
                        cords_of_triple_deck_ship_width_1_player[3] += 1
                        if list_status_cells_0field[ind_y][ind_x+2] == 423:
                            draw_cross(cord[0]+60,cord[1])
                            list_status_cells_0field[ind_y][ind_x+2] = 8
                            cords_of_triple_deck_ship_width_1_player[3] += 1
                            cords_of_triple_deck_ship_width_1_player[3] = 3
                            if cords_of_triple_deck_ship_width_1_player[3] == 3:
                                for i in list_cord_around_cell_3deck_width_right_to_left:
                                    if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                        list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                for j in coordinates_around_cell_3deck_width_right_to_left:
                                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                                        for i in list_status_cells_0field:
                                            print(i)
                                        print(' ')
                                drowned_ships_bot += 1
                                triple_deck_421_hits_1 = 0
                                bot_pick_1deck_or_empty_cell()

            elif cords_of_triple_deck_ship_width_2_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                triple_deck_421_hits_2 += 1
                cords_of_421_hit_2.extend([cord[0],cord[1],0])
                cords_of_421_hit_2_zero_indY.extend([cord[0],cord[1],0]) 
                cords_of_421_hit_2_zero_indX.extend([cord[0],cord[1],0]) 
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_triple_deck_ship_width_2_player[3] += 1
                if cords_of_triple_deck_ship_width_2_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1])  
                        cords_of_421_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30) 
                        cords_of_421_hit_2_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30)  
                        cords_of_421_hit_2_zero_indY[2] += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]+30,cord[1])
                        list_status_cells_0field[ind_y][ind_x+1] = 8
                        cords_of_triple_deck_ship_width_2_player[3] += 1
                        if list_status_cells_0field[ind_y][ind_x+2] == 423:
                            draw_cross(cord[0]+60,cord[1])
                            list_status_cells_0field[ind_y][ind_x+2] = 8
                            cords_of_triple_deck_ship_width_2_player[3] += 1
                            cords_of_triple_deck_ship_width_2_player[3] = 3
                            if cords_of_triple_deck_ship_width_2_player[3] == 3:
                                for i in list_cord_around_cell_3deck_width_right_to_left:
                                    if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                        list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                for j in coordinates_around_cell_3deck_width_right_to_left:
                                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                                        for i in list_status_cells_0field:
                                            print(i)
                                        print(' ')
                                drowned_ships_bot += 1
                                triple_deck_421_hits_2 = 0
                                bot_pick_1deck_or_empty_cell()


        elif list_status_cells_0field[ind_y][ind_x] == 422 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_width_1_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                triple_deck_422_hits_1 += 1
                cords_of_422_hit_1.extend([cord[0],cord[1],0])
                cords_of_422_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
                cords_of_422_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_triple_deck_ship_width_1_player[3] += 1
                if cords_of_triple_deck_ship_width_1_player[3] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)  
                        cords_of_422_hit_1[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30) 
                        cords_of_422_hit_1_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_triple_deck_ship_width_1_player[3] += 1
                        if list_status_cells_0field[ind_y][ind_x+1] == 423:
                            draw_cross(cord[0]+30,cord[1])
                            list_status_cells_0field[ind_y][ind_x+1] = 8
                            cords_of_triple_deck_ship_width_1_player[3] += 1
                            cords_of_triple_deck_ship_width_1_player[3] = 3
                            if cords_of_triple_deck_ship_width_1_player[3] == 3:
                                for i in list_cord_around_cell_3deck_width_mid:
                                    if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                        list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                for j in coordinates_around_cell_3deck_width_mid:
                                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                                        for i in list_status_cells_0field:
                                            print(i)
                                        print(' ')
                                drowned_ships_bot += 1
                                triple_deck_422_hits_1 = 0
                                bot_pick_1deck_or_empty_cell()

            elif cords_of_triple_deck_ship_width_2_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                triple_deck_422_hits_2 += 1
                cords_of_422_hit_2.extend([cord[0],cord[1],0])
                cords_of_422_hit_2_zero_indY.extend([cord[0],cord[1],0]) 
                cords_of_422_hit_2_zero_indX.extend([cord[0],cord[1],0]) 
                list_status_cells_0field[ind_y][ind_x] = 8
                cords_of_triple_deck_ship_width_2_player[3] += 1
                if cords_of_triple_deck_ship_width_2_player[3] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)  
                        cords_of_422_hit_2[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30) 
                        cords_of_422_hit_2_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_triple_deck_ship_width_2_player[3] += 1
                        if list_status_cells_0field[ind_y][ind_x+1] == 423:
                            draw_cross(cord[0]+30,cord[1])
                            list_status_cells_0field[ind_y][ind_x+1] = 8
                            cords_of_triple_deck_ship_width_2_player[3] += 1
                            cords_of_triple_deck_ship_width_2_player[3] = 3
                            if cords_of_triple_deck_ship_width_2_player[3] == 3:
                                for i in list_cord_around_cell_3deck_width_mid:
                                    if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                        list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                                for j in coordinates_around_cell_3deck_width_mid:
                                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                                        for i in list_status_cells_0field:
                                            print(i)
                                        print(' ')
                                drowned_ships_bot += 1
                                triple_deck_422_hits_2 = 0
                                bot_pick_1deck_or_empty_cell()


        elif list_status_cells_0field[ind_y][ind_x] == 423 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_width_1_player[2] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_423_hits_1 += 1
                cords_of_423_hit_1.extend([cord[0],cord[1],0])
                cords_of_423_hit_1_zero_indY.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_width_1_player[3] += 1
                if cords_of_triple_deck_ship_width_1_player[3] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_423_hit_1[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30)
                        cords_of_423_hit_1_zero_indY[2] += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_triple_deck_ship_width_1_player[3] += 1
                        draw_cross(cord[0]-60,cord[1])
                        list_status_cells_0field[ind_y][ind_x-2] = 8
                        cords_of_triple_deck_ship_width_1_player[3] += 1
                        cords_of_triple_deck_ship_width_1_player[3] = 3
                        if cords_of_triple_deck_ship_width_1_player[3] == 3:
                            for i in list_cord_around_cell_3deck_width_left_to_right:
                                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                            for j in coordinates_around_cell_3deck_width_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_423_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()
        
            elif cords_of_triple_deck_ship_width_2_player[2] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_423_hits_2 += 1
                cords_of_423_hit_2.extend([cord[0],cord[1],0])
                cords_of_423_hit_2_zero_indY.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_width_2_player[3] += 1
                if cords_of_triple_deck_ship_width_2_player[3] == 1:
                    if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_423_hit_2[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]-30)
                        cords_of_423_hit_2_zero_indY[2] += 1
                        list_status_cells_0field[ind_y+1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0]-30,cord[1])
                        list_status_cells_0field[ind_y][ind_x-1] = 8
                        cords_of_triple_deck_ship_width_2_player[3] += 1
                        draw_cross(cord[0]-60,cord[1])
                        list_status_cells_0field[ind_y][ind_x-2] = 8
                        cords_of_triple_deck_ship_width_2_player[3] += 1
                        cords_of_triple_deck_ship_width_2_player[3] = 3
                        if cords_of_triple_deck_ship_width_2_player[3] == 3:
                            for i in list_cord_around_cell_3deck_width_left_to_right:
                                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                            for j in coordinates_around_cell_3deck_width_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_423_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()






        elif list_status_cells_0field[ind_y][ind_x] == 411 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_lenght_1_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_411_hits_1 += 1
                cords_of_411_hit_1.extend([cord[0],cord[1],0])
                cords_of_411_hit_1_zero_indY.extend([cord[0],cord[1],0])
                cords_of_411_hit_1_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_1_player[3] += 1
                if cords_of_triple_deck_ship_lenght_1_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_411_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_411_hit_1_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_411_hit_1_zero_indY[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]-30)
                        list_status_cells_0field[ind_y+1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        draw_cross(cord[0],cord[1]-60)
                        list_status_cells_0field[ind_y+2][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        cords_of_triple_deck_ship_lenght_1_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_411_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_triple_deck_ship_lenght_2_player[0] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_411_hits_2 += 1
                cords_of_411_hit_2.extend([cord[0],cord[1],0])
                cords_of_411_hit_2_zero_indY.extend([cord[0],cord[1],0])
                cords_of_411_hit_2_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_2_player[3] += 1
                if cords_of_triple_deck_ship_lenght_2_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_411_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                        draw_dot(cord[0],cord[1]+30)
                        cords_of_411_hit_2_zero_indX[2] += 1
                        list_status_cells_0field[ind_y-1][ind_x] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_411_hit_2_zero_indY[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]-30)
                        list_status_cells_0field[ind_y+1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        draw_cross(cord[0],cord[1]-60)
                        list_status_cells_0field[ind_y+2][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        cords_of_triple_deck_ship_lenght_2_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_411_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()



        elif list_status_cells_0field[ind_y][ind_x] == 412 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_lenght_1_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_412_hits_1 += 1
                cords_of_412_hit_1.extend([cord[0],cord[1],0])
                cords_of_412_hit_1_zero_indY.extend([cord[0],cord[1],0])
                cords_of_412_hit_1_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_1_player[3] += 1
                if cords_of_triple_deck_ship_lenght_1_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_412_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_412_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        draw_cross(cord[0],cord[1]-30)
                        list_status_cells_0field[ind_y+1][ind_x11] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        cords_of_triple_deck_ship_lenght_1_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_mid:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_mid:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_412_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_triple_deck_ship_lenght_2_player[1] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_412_hits_2 += 1
                cords_of_412_hit_2.extend([cord[0],cord[1],0])
                cords_of_412_hit_2_zero_indY.extend([cord[0],cord[1],0])
                cords_of_412_hit_2_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_2_player[3] += 1
                if cords_of_triple_deck_ship_lenght_2_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_412_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_412_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        draw_cross(cord[0],cord[1]-30)
                        list_status_cells_0field[ind_y+1][ind_x11] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        cords_of_triple_deck_ship_lenght_2_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_mid:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_mid:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_412_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()

                        
        elif list_status_cells_0field[ind_y][ind_x] == 413 and list_status_cells_0field[ind_y][ind_x] != 3 and list_status_cells_0field[ind_y][ind_x] != 9:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            if cords_of_triple_deck_ship_lenght_1_player[2] == [cord[0],cord[1]]:    
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_413_hits_1 += 1
                cords_of_413_hit_1.extend([cord[0],cord[1],0])
                cords_of_413_hit_1_zero_indY.extend([cord[0],cord[1],0])
                cords_of_413_hit_1_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_1_player[3] += 1
                if cords_of_triple_deck_ship_lenght_1_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_413_hit_1[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_413_hit_1_zero_indX[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick() 
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        draw_cross(cord[0],cord[1]+60)
                        list_status_cells_0field[ind_y-2][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_1_player[3] += 1
                        cords_of_triple_deck_ship_lenght_1_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])                
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_413_hits_1 = 0
                            bot_pick_1deck_or_empty_cell()

            elif cords_of_triple_deck_ship_lenght_2_player[2] == [cord[0],cord[1]]:
                draw_cross(cord[0],cord[1])
                list_status_cells_0field[ind_y][ind_x] = 8
                triple_deck_413_hits_2 += 1
                cords_of_413_hit_2.extend([cord[0],cord[1],0])
                cords_of_413_hit_2_zero_indY.extend([cord[0],cord[1],0])
                cords_of_413_hit_2_zero_indX.extend([cord[0],cord[1],0])
                cords_of_triple_deck_ship_lenght_2_player[3] += 1
                if cords_of_triple_deck_ship_lenght_2_player[3] == 1:
                    if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                        draw_dot(cord[0]-30,cord[1]) 
                        cords_of_413_hit_2[2] += 1
                        list_status_cells_0field[ind_y][ind_x-1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick()
                    elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                        draw_dot(cord[0]+30,cord[1]) 
                        cords_of_413_hit_2_zero_indX[2] += 1
                        list_status_cells_0field[ind_y][ind_x+1] = 3
                        player_turn = 'player'
                        t_draw_whos_turn.clear()
                        draw_turn(-68, 270 , "Хід гравця", 15)
                        if player_turn == 'player':
                            draw_dot_permited = True
                            draw_cross_permited = True
                            player_pick() 
                    else:
                        draw_cross(cord[0],cord[1]+30)
                        list_status_cells_0field[ind_y-1][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        draw_cross(cord[0],cord[1]+60)
                        list_status_cells_0field[ind_y-2][ind_x] = 8
                        cords_of_triple_deck_ship_lenght_2_player[3] += 1
                        cords_of_triple_deck_ship_lenght_2_player[3] = 3
                        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
                            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                                if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                    draw_dot(cord[0]+j[0],cord[1]+j[1])                 
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                            drowned_ships_bot += 1
                            triple_deck_413_hits_2 = 0
                            bot_pick_1deck_or_empty_cell()    


        elif list_status_cells_0field[ind_y][ind_x] == 521 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            four_deck_521_hits_1 += 1
            cords_of_521_hit_1.extend([cord[0],cord[1],0])
            cords_of_521_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
            cords_of_521_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            list_status_cells_0field[ind_y][ind_x] = 8
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                    draw_dot(cord[0]-30,cord[1])  
                    cords_of_521_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x-1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]+30) 
                    cords_of_521_hit_1_zero_indX[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]-30)  
                    cords_of_521_hit_1_zero_indY[2] += 1
                    list_status_cells_0field[ind_y+1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0]+30,cord[1])
                    list_status_cells_0field[ind_y][ind_x+1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]+60,cord[1])
                    list_status_cells_0field[ind_y][ind_x+2] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]+90,cord[1])
                    list_status_cells_0field[ind_y][ind_x+3] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_width_right_to_left:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_width_right_to_left:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_521_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()
                

        elif list_status_cells_0field[ind_y][ind_x] == 522 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            four_deck_522_hits_1 += 1
            cords_of_522_hit_1.extend([cord[0],cord[1],0])
            cords_of_522_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
            cords_of_522_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            list_status_cells_0field[ind_y][ind_x] = 8
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]+30)  
                    cords_of_522_hit_1[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]-30) 
                    cords_of_522_hit_1_zero_indX[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0]-30,cord[1])
                    list_status_cells_0field[ind_y][ind_x-1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]+30,cord[1])
                    list_status_cells_0field[ind_y][ind_x+1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]+60,cord[1])
                    list_status_cells_0field[ind_y][ind_x+2] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_width_mid_left:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_width_mid_left:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_522_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()


        elif list_status_cells_0field[ind_y][ind_x] == 523 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            four_deck_523_hits_1 += 1
            cords_of_523_hit_1.extend([cord[0],cord[1],0])
            cords_of_523_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
            cords_of_523_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            list_status_cells_0field[ind_y][ind_x] = 8
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]+30)  
                    cords_of_523_hit_1[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]-30) 
                    cords_of_523_hit_1_zero_indX[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0]-30,cord[1])
                    list_status_cells_0field[ind_y][ind_x-1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]+30,cord[1])
                    list_status_cells_0field[ind_y][ind_x+1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]-60,cord[1])
                    list_status_cells_0field[ind_y][ind_x-2] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_width_mid_right:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_width_mid_right:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_523_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()
                
                            
        elif list_status_cells_0field[ind_y][ind_x] == 524 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1]) 
            four_deck_524_hits_1 += 1
            cords_of_524_hit_1.extend([cord[0],cord[1],0])
            cords_of_524_hit_1_zero_indY.extend([cord[0],cord[1],0]) 
            cords_of_524_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            list_status_cells_0field[ind_y][ind_x] = 8
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]+30)
                    cords_of_524_hit_1[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]-30 <= 150 and cord[1]-30 >= -120 and list_status_cells_0field[ind_y+1][ind_x] != 3 and list_status_cells_0field[ind_y+1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]-30)
                    cords_of_524_hit_1_zero_indY[2] += 1
                    list_status_cells_0field[ind_y+1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0]-30,cord[1])
                    list_status_cells_0field[ind_y][ind_x-1] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]-60,cord[1])
                    list_status_cells_0field[ind_y][ind_x-2] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0]-90,cord[1])
                    list_status_cells_0field[ind_y][ind_x-3] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_width_left_to_right:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_width_left_to_right:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_524_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()

        elif list_status_cells_0field[ind_y][ind_x] == 511 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            list_status_cells_0field[ind_y][ind_x] = 8
            four_deck_511_hits_1 += 1
            cords_of_511_hit_1.extend([cord[0],cord[1],0])
            cords_of_511_hit_1_zero_indY.extend([cord[0],cord[1],0])
            cords_of_511_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                    draw_dot(cord[0]-30,cord[1]) 
                    cords_of_511_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x-1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0] >= -400 and cord[0] <= -130 and cord[1]+30 <= 150 and cord[1]+30 >= -120 and list_status_cells_0field[ind_y-1][ind_x] != 3 and list_status_cells_0field[ind_y-1][ind_x] != 9:
                    draw_dot(cord[0],cord[1]+30)
                    cords_of_511_hit_1_zero_indX[2] += 1
                    list_status_cells_0field[ind_y-1][ind_x] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                    draw_dot(cord[0]+30,cord[1]) 
                    cords_of_511_hit_1_zero_indY[2] += 1
                    list_status_cells_0field[ind_y][ind_x+1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0],cord[1]-30)
                    list_status_cells_0field[ind_y+1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]-60)
                    list_status_cells_0field[ind_y+2][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]-90)
                    list_status_cells_0field[ind_y+3][ind_x] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_lenght_left_to_right:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_lenght_right_to_left:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_511_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()
                
        elif list_status_cells_0field[ind_y][ind_x] == 512 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            list_status_cells_0field[ind_y][ind_x] = 8
            four_deck_512_hits_1 += 1
            cords_of_512_hit_1.extend([cord[0],cord[1],0])
            cords_of_512_hit_1_zero_indY.extend([cord[0],cord[1],0])
            cords_of_512_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                    draw_dot(cord[0]-30,cord[1]) 
                    cords_of_512_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x-1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                    draw_dot(cord[0]+30,cord[1]) 
                    cords_of_512_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x+1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0],cord[1]+30)
                    list_status_cells_0field[ind_y-1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]-30)
                    list_status_cells_0field[ind_y+1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]-60)
                    list_status_cells_0field[ind_y+2][ind_x] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4 
                    if bot_four_deck_hits == 4:
                        # bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_lenght_mid_left:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_lenght_mid_left:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_512_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()

        elif list_status_cells_0field[ind_y][ind_x] == 513 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            list_status_cells_0field[ind_y][ind_x] = 8
            four_deck_513_hits_1 += 1
            cords_of_513_hit_1.extend([cord[0],cord[1],0])
            cords_of_513_hit_1_zero_indY.extend([cord[0],cord[1],0])
            cords_of_513_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:
                if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                    draw_dot(cord[0]-30,cord[1]) 
                    cords_of_513_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x-1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                    draw_dot(cord[0]+30,cord[1]) 
                    cords_of_513_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x+1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                else:
                    draw_cross(cord[0],cord[1]-30)
                    list_status_cells_0field[ind_y+1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]+30)
                    list_status_cells_0field[ind_y-1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]+60)
                    list_status_cells_0field[ind_y-2][ind_x] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_lenght_mid_right:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_lenght_mid_right:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_513_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()
                        

        elif list_status_cells_0field[ind_y][ind_x] == 514 and list_status_cells_0field[ind_y][ind_x] != 3:
            cord = coordinates_of_cells_0field[ind_y][ind_x]
            ind_x11 = ind_x
            ind_y11 = ind_y 
            draw_cross(cord[0],cord[1])
            list_status_cells_0field[ind_y][ind_x] = 8
            four_deck_514_hits_1 += 1
            cords_of_514_hit_1.extend([cord[0],cord[1],0])
            cords_of_514_hit_1_zero_indY.extend([cord[0],cord[1],0])
            cords_of_514_hit_1_zero_indX.extend([cord[0],cord[1],0]) 
            bot_four_deck_hits += 1
            if bot_four_deck_hits == 1:  
                if cord[0]-30 >= -400 and cord[0]-30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x-1] != 3 and list_status_cells_0field[ind_y][ind_x-1] != 9:
                    draw_dot(cord[0]-30,cord[1]) 
                    cords_of_514_hit_1[2] += 1
                    list_status_cells_0field[ind_y][ind_x-1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()
                elif cord[0]+30 >= -400 and cord[0]+30 <= -130 and cord[1] <= 150 and cord[1] >= -120 and list_status_cells_0field[ind_y][ind_x+1] != 3 and list_status_cells_0field[ind_y][ind_x+1] != 9:
                    draw_dot(cord[0]+30,cord[1]) 
                    cords_of_514_hit_1_zero_indX[2] += 1
                    list_status_cells_0field[ind_y][ind_x+1] = 3
                    player_turn = 'player'
                    t_draw_whos_turn.clear()
                    draw_turn(-68, 270 , "Хід гравця", 15)
                    if player_turn == 'player':
                        draw_dot_permited = True
                        draw_cross_permited = True
                        player_pick()     
                else:
                    draw_cross(cord[0],cord[1]+30)
                    list_status_cells_0field[ind_y-1][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]+60)
                    list_status_cells_0field[ind_y-2][ind_x] = 8
                    bot_four_deck_hits += 1
                    draw_cross(cord[0],cord[1]+90)
                    list_status_cells_0field[ind_y-3][ind_x] = 8
                    bot_four_deck_hits += 1
                    bot_four_deck_hits = 4
                    if bot_four_deck_hits == 4:
                        bot_four_deck_hits = 0
                        for i in list_cord_around_cell_4deck_lenght_right_to_left:
                            if ind_y+i[1] >= 0 and ind_y+i[1] < len(list_status_cells_0field) and ind_x+i[0] >= 0 and ind_x+i[0] < len(list_status_cells_0field):
                                list_status_cells_0field[ind_y+i[1]][ind_x+i[0]] = 9
                        for j in coordinates_around_cell_4deck_lenght_left_to_right:
                            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                                draw_dot(cord[0]+j[0],cord[1]+j[1])    
                                for i in list_status_cells_0field:
                                    print(i)
                                print(' ')
                        drowned_ships_bot += 1
                        four_deck_514_hits_1 = 0
                        bot_pick_1deck_or_empty_cell()
    else:
        t_draw_whos_turn.clear()
        draw_victory(-112, 270 , "Перемога бота!", 20, 'goldenrod')   
#FUNCTIONS OF TURNS
            
def second_bot_pick_2deckLenght_311_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_311_hits_1
    global cords_of_311_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_311_hit_1[0] >= -400 and cords_of_311_hit_1[0] <= -130 and cords_of_311_hit_1[1]+30 <= 150 and cords_of_311_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_311_hit_1[0],cords_of_311_hit_1[1]+30)
        cords_of_311_hit_1[2] = 2
        double_deck_311_hits_1 = 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_311_hit_1[0],cords_of_311_hit_1[1]-30)
        cords_of_311_hit_1[2] += 1
        double_deck_311_hits_1 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_double_deck_ship_lenght_1_player[2] += 1
        if cords_of_double_deck_ship_lenght_1_player[2] == 2:
            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cords_of_311_hit_1[0]+j[0],cords_of_311_hit_1[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            double_deck_311_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_2deckLenght_311_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global ind_x11
    global ind_y11
    global double_deck_311_hits_1
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_311_hit_1[0],cords_of_311_hit_1[1]-30)
    double_deck_311_hits_1 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_1_player[2] += 1
    if cords_of_double_deck_ship_lenght_1_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cords_of_311_hit_1[0]+j[0],cords_of_311_hit_1[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_311_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def first_bot_pick_2deckLenght_312_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_312_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(cord)
    draw_cross(cords_of_312_hit_1[0],cords_of_312_hit_1[1]+30)
    print(cords_of_312_hit_1[0],cords_of_312_hit_1[1])
    double_deck_312_hits_1 += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_1_player[2] += 1
    if cords_of_double_deck_ship_lenght_1_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8           
        for j in coordinates_around_cell_2deck_lenght_right_to_left:
            if cords_of_312_hit_1[0]+j[0] >= -400 and cords_of_312_hit_1[0]+j[0] <= -130 and cords_of_312_hit_1[1]+j[1] <= 150 and cords_of_312_hit_1[1]+j[1] >= -120:
                draw_dot(cords_of_312_hit_1[0]+j[0],cords_of_312_hit_1[1]+j[1])                                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_312_hits_1 = 0
        bot_pick_1deck_or_empty_cell()
# 2 двопалубний корабель
def second_bot_pick_2deckLenght_311_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_311_hits_2
    global cords_of_311_hit_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_311_hit_2[0] >= -400 and cords_of_311_hit_2[0] <= -130 and cords_of_311_hit_2[1]+30 <= 150 and cords_of_311_hit_2[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_311_hit_2[0],cords_of_311_hit_2[1]+30)
        cords_of_311_hit_2[2] = 2
        double_deck_311_hits_2 = 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_311_hit_2[0],cords_of_311_hit_2[1]-30)
        cords_of_311_hit_2[2] += 1
        double_deck_311_hits_2 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_double_deck_ship_lenght_2_player[2] += 1
        if cords_of_double_deck_ship_lenght_2_player[2] == 2:
            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cords_of_311_hit_2[0]+j[0],cords_of_311_hit_2[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            double_deck_311_hits_2 = 0
            bot_pick_1deck_or_empty_cell()
            
def third_bot_pick_2deckLenght_311_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global ind_x11
    global ind_y11
    global double_deck_311_hits_2
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_311_hit_2[0],cords_of_311_hit_2[1]-30)
    double_deck_311_hits_2 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_2_player[2] += 1
    if cords_of_double_deck_ship_lenght_2_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cords_of_311_hit_2[0]+j[0],cords_of_311_hit_2[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_311_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def first_bot_pick_2deckLenght_312_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_312_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(cord)
    draw_cross(cords_of_312_hit_2[0],cords_of_312_hit_2[1]+30)
    print(cords_of_312_hit_2[0],cords_of_312_hit_2[1])
    double_deck_312_hits_2 += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_2_player[2] += 1
    if cords_of_double_deck_ship_lenght_2_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8           
        for j in coordinates_around_cell_2deck_lenght_right_to_left:
            if cords_of_312_hit_2[0]+j[0] >= -400 and cords_of_312_hit_2[0]+j[0] <= -130 and cords_of_312_hit_2[1]+j[1] <= 150 and cords_of_312_hit_2[1]+j[1] >= -120:
                draw_dot(cords_of_312_hit_2[0]+j[0],cords_of_312_hit_2[1]+j[1])                                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_312_hits_2 = 0
        bot_pick_1deck_or_empty_cell()
# 3 двопалубний корабель
def second_bot_pick_2deckLenght_311_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_311_hits_3
    global cords_of_311_hit_3
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_311_hit_3[0] >= -400 and cords_of_311_hit_3[0] <= -130 and cords_of_311_hit_3[1]+30 <= 150 and cords_of_311_hit_3[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_311_hit_3[0],cords_of_311_hit_3[1]+30)
        cords_of_311_hit_3[2] = 2
        double_deck_311_hits_3 = 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_311_hit_3[0],cords_of_311_hit_3[1]-30)
        cords_of_311_hit_3[2] += 1
        double_deck_311_hits_3 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_double_deck_ship_lenght_3_player[2] += 1
        if cords_of_double_deck_ship_lenght_3_player[2] == 2:
            for i in list_cord_around_cell_2deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cords_of_311_hit_3[0]+j[0],cords_of_311_hit_3[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ') 
            drowned_ships_bot += 1
            double_deck_311_hits_3 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_2deckLenght_311_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global ind_x11
    global ind_y11
    global double_deck_311_hits_3
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_311_hit_3[0],cords_of_311_hit_3[1]-30)
    double_deck_311_hits_3 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_3_player[2] += 1
    if cords_of_double_deck_ship_lenght_3_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cords_of_311_hit_3[0]+j[0],cords_of_311_hit_3[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_311_hits_3 = 0
        bot_pick_1deck_or_empty_cell()
        
def first_bot_pick_2deckLenght_312_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_312_hits_3
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(cord)
    draw_cross(cords_of_312_hit_3[0],cords_of_312_hit_3[1]+30)
    print(cords_of_312_hit_3[0],cords_of_312_hit_3[1])
    double_deck_312_hits_3 += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_double_deck_ship_lenght_3_player[2] += 1
    if cords_of_double_deck_ship_lenght_3_player[2] == 2:
        for i in list_cord_around_cell_2deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8           
        for j in coordinates_around_cell_2deck_lenght_right_to_left:
            if cords_of_312_hit_3[0]+j[0] >= -400 and cords_of_312_hit_3[0]+j[0] <= -130 and cords_of_312_hit_3[1]+j[1] <= 150 and cords_of_312_hit_3[1]+j[1] >= -120:
                draw_dot(cords_of_312_hit_3[0]+j[0],cords_of_312_hit_3[1]+j[1])                                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_312_hits_3 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_321_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_321_hit_1[0] >= -400 and cords_of_321_hit_1[0] <= -130 and cords_of_321_hit_1[1]+30 <= 150 and cords_of_321_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_321_hit_1[0],cords_of_321_hit_1[1]+30)
        double_deck_321_hits_1 = 1
        cords_of_321_hit_1[2] = 2
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_321_hit_1[0]+30,cords_of_321_hit_1[1])
        cords_of_321_hit_1[2] += 1
        double_deck_321_hits_1 += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_double_deck_ship_width_1_player[2] += 1
        if cords_of_double_deck_ship_width_1_player[2] == 2:
            for i in list_cord_around_cell_2deck_width_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_width_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            double_deck_321_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_2deckWidth_321_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_321_hit_1[0]+30,cords_of_321_hit_1[1])
    cords_of_321_hit_1[2] += 1
    double_deck_321_hits_1 += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    cords_of_double_deck_ship_width_1_player[2] += 1
    if cords_of_double_deck_ship_width_1_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_321_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_322_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_322_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_322_hit_1[0]-30,cords_of_322_hit_1[1])
    cords_of_322_hit_1[2] += 1
    double_deck_322_hits_1 += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    cords_of_double_deck_ship_width_1_player[2] += 1
    if cords_of_double_deck_ship_width_1_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_322_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_321_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_321_hit_2[0] >= -400 and cords_of_321_hit_2[0] <= -130 and cords_of_321_hit_2[1]+30 <= 150 and cords_of_321_hit_2[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_321_hit_2[0],cords_of_321_hit_2[1]+30)
        cords_of_321_hit_2[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_321_hit_2[0]+30,cords_of_321_hit_2[1])
        cords_of_321_hit_2[2] += 1
        double_deck_321_hits_2 += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_double_deck_ship_width_2_player[2] += 1
        if cords_of_double_deck_ship_width_2_player[2] == 2:
            for i in list_cord_around_cell_2deck_width_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_width_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            double_deck_321_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_2deckWidth_321_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_321_hit_2[0]+30,cords_of_321_hit_2[1])
    cords_of_321_hit_2[2] += 1
    double_deck_321_hits_2 += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    cords_of_double_deck_ship_width_2_player[2] += 1
    if cords_of_double_deck_ship_width_2_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_321_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_322_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_322_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_322_hit_2[0]-30,cords_of_322_hit_2[1])
    cords_of_322_hit_2[2] += 1
    double_deck_322_hits_2 += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    cords_of_double_deck_ship_width_2_player[2] += 1
    if cords_of_double_deck_ship_width_2_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_322_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_321_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_3
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_321_hit_3[0] >= -400 and cords_of_321_hit_3[0] <= -130 and cords_of_321_hit_3[1]+30 <= 150 and cords_of_321_hit_3[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_321_hit_3[0],cords_of_321_hit_3[1]+30)
        cords_of_321_hit_3[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_321_hit_3[0]+30,cords_of_321_hit_3[1])
        cords_of_321_hit_3[2] += 1
        double_deck_321_hits_3 += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_double_deck_ship_width_3_player[2] += 1
        if cords_of_double_deck_ship_width_3_player[2] == 2:
            for i in list_cord_around_cell_2deck_width_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                    list_status_cells_0field[ind_y11][ind_x11] = 8
            for j in coordinates_around_cell_2deck_width_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            double_deck_321_hits_3 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_2deckWidth_321_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_321_hits_3
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_321_hit_3[0]+30,cords_of_321_hit_3[1])
    cords_of_321_hit_3[2] += 1
    double_deck_321_hits_3 += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    cords_of_double_deck_ship_width_3_player[2] += 1
    if cords_of_double_deck_ship_width_3_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_321_hits_3 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_2deckWidth_322_3():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global double_deck_322_hits_3
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cords_of_322_hit_3[0]-30,cords_of_322_hit_3[1])
    cords_of_322_hit_3[2] += 1
    double_deck_322_hits_3 += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    cords_of_double_deck_ship_width_3_player[2] += 1
    if cords_of_double_deck_ship_width_3_player[2] == 2:
        for i in list_cord_around_cell_2deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                list_status_cells_0field[ind_y11][ind_x11] = 8
        for j in coordinates_around_cell_2deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        double_deck_322_hits_3 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_421_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_421_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_421_hit_1[0] >= -400 and cords_of_421_hit_1[0] <= -130 and cords_of_421_hit_1[1]+30 <= 150 and cords_of_421_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_421_hit_1[0],cords_of_421_hit_1[1]+30)
        cords_of_421_hit_1[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()

    else:
        draw_cross(cord[0]+30,cord[1])
        triple_deck_421_hits_1 += 1 
        cords_of_421_hit_1[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_triple_deck_ship_width_1_player[3] += 1
        if list_status_cells_0field[ind_y11][ind_x11+2] == 423:
            draw_cross(cord[0]+60,cord[1])
            triple_deck_421_hits_1 += 1 
            cords_of_421_hit_1[2] += 1
            list_status_cells_0field[ind_y11][ind_x11+2] = 8
            cords_of_triple_deck_ship_width_1_player[3] += 1
            cords_of_triple_deck_ship_width_1_player[3] = 3
            if cords_of_triple_deck_ship_width_1_player[3] == 3:
                for i in list_cord_around_cell_3deck_width_right_to_left:
                    if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                        list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                for j in coordinates_around_cell_3deck_width_right_to_left:
                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                        for i in list_status_cells_0field:
                            print(i)
                        print(' ')
                drowned_ships_bot += 1
                triple_deck_421_hits_1 = 0
                bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_421_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_421_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_421_hit_2[0] >= -400 and cords_of_421_hit_2[0] <= -130 and cords_of_421_hit_2[1]+30 <= 150 and cords_of_421_hit_2[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_421_hit_2[0],cords_of_421_hit_2[1]+30)
        cords_of_421_hit_2[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]+30,cord[1])
        triple_deck_421_hits_2 += 1 
        cords_of_421_hit_2[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_triple_deck_ship_width_2_player[3] += 1
        if list_status_cells_0field[ind_y11][ind_x11+2] == 423:
            draw_cross(cord[0]+60,cord[1])
            triple_deck_421_hits_2 += 1 
            cords_of_421_hit_2[2] += 1
            list_status_cells_0field[ind_y11][ind_x11+2] = 8
            cords_of_triple_deck_ship_width_2_player[3] += 1
            cords_of_triple_deck_ship_width_2_player[3] = 3
            if cords_of_triple_deck_ship_width_2_player[3] == 3:
                for i in list_cord_around_cell_3deck_width_right_to_left:
                    if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                        list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
                for j in coordinates_around_cell_3deck_width_right_to_left:
                    if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                        draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                        for i in list_status_cells_0field:
                            print(i)
                        print(' ')
                drowned_ships_bot += 1
                triple_deck_421_hits_2 = 0
                bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_421_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_421_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    cords_of_triple_deck_ship_width_1_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    triple_deck_421_hits_1 += 1 
    cords_of_421_hit_1[2] += 1
    draw_cross(cord[0]+60,cord[1])
    triple_deck_421_hits_1 += 1 
    cords_of_421_hit_1[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+2] = 8
    cords_of_triple_deck_ship_width_1_player[3] += 1
    cords_of_triple_deck_ship_width_1_player[3] = 3
    if cords_of_triple_deck_ship_width_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_421_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_421_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_421_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    cords_of_triple_deck_ship_width_2_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    triple_deck_421_hits_2 += 1 
    cords_of_421_hit_2[2] += 1
    draw_cross(cord[0]+60,cord[1])
    triple_deck_421_hits_2 += 1 
    cords_of_421_hit_2[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+2] = 8
    cords_of_triple_deck_ship_width_2_player[3] += 1
    cords_of_triple_deck_ship_width_2_player[3] = 3
    if cords_of_triple_deck_ship_width_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_421_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_422_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_1_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_422_hits_1 += 1 
    cords_of_422_hit_1[2] += 1
    if cords_of_422_hit_1[0]-60 >= -400 and cords_of_422_hit_1[0]-60 <= -130 and cords_of_422_hit_1[1] <= 150 and cords_of_422_hit_1[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11-2] != 3 and list_status_cells_0field[ind_y11][ind_x11-2] != 9:
        draw_dot(cord[0]-60,cord[1]) 
        cords_of_422_hit_1[2] += 1
        print('ffffffffffffffffffffffffffffff',cords_of_422_hit_1[2],triple_deck_422_hits_1)
        list_status_cells_0field[ind_y11][ind_x11-2] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]+30,cord[1])
        cords_of_triple_deck_ship_width_1_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        triple_deck_422_hits_1 += 1 
        cords_of_422_hit_1[2] += 1
        cords_of_triple_deck_ship_width_1_player[3] = 3
        if cords_of_triple_deck_ship_width_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_422_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_422_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_2_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_422_hits_2 += 1 
    cords_of_422_hit_2[2] += 1
    if cords_of_422_hit_2[0]-60 >= -400 and cords_of_422_hit_2[0]-60 <= -130 and cords_of_422_hit_2[1] <= 150 and cords_of_422_hit_2[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11-2] != 3 and list_status_cells_0field[ind_y11][ind_x11-2] != 9:
        draw_dot(cord[0]-60,cord[1]) 
        cords_of_422_hit_2[2] += 1
        list_status_cells_0field[ind_y11][ind_x11-2] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]+30,cord[1])
        cords_of_triple_deck_ship_width_2_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        triple_deck_422_hits_2 += 1 
        cords_of_422_hit_2[2] += 1
        cords_of_triple_deck_ship_width_2_player[3] = 3
        if cords_of_triple_deck_ship_width_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_422_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_422_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    cords_of_triple_deck_ship_width_1_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    triple_deck_422_hits_1 += 1 
    cords_of_422_hit_1[2] += 1
    cords_of_triple_deck_ship_width_1_player[3] = 3
    if cords_of_triple_deck_ship_width_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                              
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_422_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_422_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    cords_of_triple_deck_ship_width_2_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    triple_deck_422_hits_2 += 1 
    cords_of_422_hit_2[2] += 1
    cords_of_triple_deck_ship_width_2_player[3] = 3
    if cords_of_triple_deck_ship_width_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_422_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_422_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]+30,cord[1])
    triple_deck_422_hits_1 += 1 
    cords_of_422_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    cords_of_triple_deck_ship_width_1_player[3] += 1
    if cords_of_422_hit_1_zero_indX[0]+60 >= -400 and cords_of_422_hit_1_zero_indX[0]+60 <= -130 and cords_of_422_hit_1_zero_indX[1] <= 150 and cords_of_422_hit_1_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+2] != 3 and list_status_cells_0field[ind_y11][ind_x11+2] != 9:
        draw_dot(cord[0]+60,cord[1])
        cords_of_422_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+2] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        triple_deck_422_hits_1 += 1 
        cords_of_422_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        cords_of_triple_deck_ship_width_1_player[3] += 1
        draw_cross(cord[0]+30,cord[1])
        triple_deck_422_hits_1 += 1 
        cords_of_422_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_triple_deck_ship_width_1_player[3] += 1
        cords_of_triple_deck_ship_width_1_player[3] = 3
        if cords_of_triple_deck_ship_width_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_422_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_422_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]+30,cord[1])
    triple_deck_422_hits_2 += 1 
    cords_of_422_hit_2_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    cords_of_triple_deck_ship_width_2_player[3] += 1
    if cords_of_422_hit_2_zero_indX[0]+60 >= -400 and cords_of_422_hit_2_zero_indX[0]+60 <= -130 and cords_of_422_hit_2_zero_indX[1] <= 150 and cords_of_422_hit_2_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+2] != 3 and list_status_cells_0field[ind_y11][ind_x11+2] != 9:
        draw_dot(cord[0]+60,cord[1])
        cords_of_422_hit_2_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+2] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        triple_deck_422_hits_2 += 1 
        cords_of_422_hit_2_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        cords_of_triple_deck_ship_width_2_player[3] += 1
        draw_cross(cord[0]+30,cord[1])
        triple_deck_422_hits_2 += 1 
        cords_of_422_hit_2_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        cords_of_triple_deck_ship_width_2_player[3] += 1
        cords_of_triple_deck_ship_width_2_player[3] = 3
        if cords_of_triple_deck_ship_width_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                                           
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_422_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_422_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]-30,cord[1])
    triple_deck_422_hits_1 += 1 
    cords_of_422_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    cords_of_triple_deck_ship_width_1_player[3] += 1
    cords_of_triple_deck_ship_width_1_player[3] = 3
    if cords_of_triple_deck_ship_width_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_422_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_422_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_422_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]-30,cord[1])
    triple_deck_422_hits_2 += 1 
    cords_of_422_hit_2_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    cords_of_triple_deck_ship_width_2_player[3] += 1
    cords_of_triple_deck_ship_width_2_player[3] = 3
    if cords_of_triple_deck_ship_width_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                                               
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_422_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_423_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_423_hit_1[0]+30 >= -400 and cords_of_423_hit_1[0]+30 <= -130 and cords_of_423_hit_1[1] <= 150 and cords_of_423_hit_1[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_423_hit_1[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        cords_of_triple_deck_ship_width_1_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        triple_deck_423_hits_1 += 1 
        cords_of_423_hit_1[2] += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        triple_deck_423_hits_1 += 1 
        cords_of_423_hit_1[2] += 1
        cords_of_triple_deck_ship_width_1_player[3] += 1
        if cords_of_triple_deck_ship_width_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_423_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_423_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_423_hit_2[0]+30 >= -400 and cords_of_423_hit_2[0]+30 <= -130 and cords_of_423_hit_2[1] <= 150 and cords_of_423_hit_2[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_423_hit_2[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        cords_of_triple_deck_ship_width_2_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        triple_deck_423_hits_2 += 1 
        cords_of_423_hit_2[2] += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        triple_deck_423_hits_2 += 1 
        cords_of_423_hit_2[2] += 1
        cords_of_triple_deck_ship_width_2_player[3] += 1
        if cords_of_triple_deck_ship_width_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_423_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_423_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_1_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_423_hits_1 += 1 
    cords_of_423_hit_1[2] += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    triple_deck_423_hits_1 += 1 
    cords_of_423_hit_1[2] += 1
    cords_of_triple_deck_ship_width_1_player[3] += 1
    if cords_of_triple_deck_ship_width_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_423_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_423_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_2_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_423_hits_2 += 1 
    cords_of_423_hit_2[2] += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    triple_deck_423_hits_2 += 1 
    cords_of_423_hit_2[2] += 1
    cords_of_triple_deck_ship_width_2_player[3] += 1
    if cords_of_triple_deck_ship_width_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_423_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_423_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_423_hit_1_zero_indY[0]+30 >= -400 and cords_of_423_hit_1_zero_indY[0]+30 <= -130 and cords_of_423_hit_1_zero_indY[1] <= 150 and cords_of_423_hit_1_zero_indY[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_423_hit_1_zero_indY[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        cords_of_triple_deck_ship_width_1_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        triple_deck_423_hits_1 += 1 
        cords_of_423_hit_1_zero_indY[2] += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        triple_deck_423_hits_1 += 1 
        cords_of_423_hit_1_zero_indY[2] += 1
        cords_of_triple_deck_ship_width_1_player[3] += 1
        if cords_of_triple_deck_ship_width_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_423_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckWidth_423_2_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_423_hit_2_zero_indY[0]+30 >= -400 and cords_of_423_hit_2_zero_indY[0]+30 <= -130 and cords_of_423_hit_2_zero_indY[1] <= 150 and cords_of_423_hit_2_zero_indY[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_423_hit_2_zero_indY[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        cords_of_triple_deck_ship_width_2_player[3] += 1
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        triple_deck_423_hits_2 += 1 
        cords_of_423_hit_2_zero_indY[2] += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        triple_deck_423_hits_2 += 1 
        cords_of_423_hit_2_zero_indY[2] += 1
        cords_of_triple_deck_ship_width_2_player[3] += 1
        if cords_of_triple_deck_ship_width_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_423_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_423_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_1_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_423_hits_1 += 1 
    cords_of_423_hit_1_zero_indY[2] += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    triple_deck_423_hits_1 += 1 
    cords_of_423_hit_1_zero_indY[2] += 1
    cords_of_triple_deck_ship_width_1_player[3] += 1
    if cords_of_triple_deck_ship_width_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_423_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckWidth_423_2_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_423_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    cords_of_triple_deck_ship_width_2_player[3] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    triple_deck_423_hits_2 += 1 
    cords_of_423_hit_2_zero_indY[2] += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    triple_deck_423_hits_2 += 1 
    cords_of_423_hit_2_zero_indY[2] += 1
    cords_of_triple_deck_ship_width_2_player[3] += 1
    if cords_of_triple_deck_ship_width_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_423_hits_2 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckLenght_411_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_1
    global cords_of_411_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_411_hit_1[0] >= -400 and cords_of_411_hit_1[0] <= -130 and cords_of_411_hit_1[1]+30 <= 150 and cords_of_411_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_411_hit_1[0],cords_of_411_hit_1[1]+30)
        cords_of_411_hit_1[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_411_hit_1[0],cords_of_411_hit_1[1]-30)
        cords_of_411_hit_1[2] += 1
        triple_deck_411_hits_1 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        draw_cross(cords_of_411_hit_1[0],cords_of_411_hit_1[1]-60)
        cords_of_411_hit_1[2] += 1
        triple_deck_411_hits_1 += 1
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        cords_of_triple_deck_ship_lenght_1_player[3] = 3
        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_411_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_411_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_411_hit_2[0] >= -400 and cords_of_411_hit_2[0] <= -130 and cords_of_411_hit_2[1]+30 <= 150 and cords_of_411_hit_2[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_411_hit_2[0],cords_of_411_hit_2[1]+30)
        cords_of_411_hit_2[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_411_hit_2[0],cords_of_411_hit_2[1]-30)
        cords_of_411_hit_2[2] += 1
        triple_deck_411_hits_2 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        draw_cross(cords_of_411_hit_2[0],cords_of_411_hit_2[1]-60)
        cords_of_411_hit_2[2] += 1
        triple_deck_411_hits_2 += 1
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        cords_of_triple_deck_ship_lenght_2_player[3] = 3
        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_411_hits_2 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_3deckLenght_411_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_1
    global cords_of_411_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_1[0],cords_of_411_hit_1[1]-30)
    cords_of_411_hit_1[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    draw_cross(cords_of_411_hit_1[0],cords_of_411_hit_1[1]-60)
    cords_of_411_hit_1[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    cords_of_triple_deck_ship_lenght_1_player[3] = 3
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckLenght_411_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_2[0],cords_of_411_hit_2[1]-30)
    cords_of_411_hit_2[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    draw_cross(cords_of_411_hit_2[0],cords_of_411_hit_2[1]-60)
    cords_of_411_hit_2[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    cords_of_triple_deck_ship_lenght_2_player[3] = 3
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_2 = 0
        bot_pick_1deck_or_empty_cell()


def second_bot_pick_3deckLenght_411_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_411_hit_1_zero_indX[0]+30 >= -400 and cords_of_411_hit_1_zero_indX[0]+30 <= -130 and cords_of_411_hit_1_zero_indX[1] <= 150 and cords_of_411_hit_1_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cords_of_411_hit_1_zero_indX[0]+30,cords_of_411_hit_1_zero_indX[1])
        cords_of_411_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_411_hit_1_zero_indX[0],cords_of_411_hit_1_zero_indX[1]-30)
        cords_of_411_hit_1_zero_indX[2] += 1
        triple_deck_411_hits_1 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        draw_cross(cords_of_411_hit_1_zero_indX[0],cords_of_411_hit_1_zero_indX[1]-60)
        cords_of_411_hit_1_zero_indX[2] += 1
        triple_deck_411_hits_1 += 1
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        cords_of_triple_deck_ship_lenght_1_player[3] = 3
        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_411_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_411_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_411_hit_2_zero_indX[0]+30 >= -400 and cords_of_411_hit_2_zero_indX[0]+30 <= -130 and cords_of_411_hit_2_zero_indX[1] <= 150 and cords_of_411_hit_2_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cords_of_411_hit_2_zero_indX[0]+30,cords_of_411_hit_2_zero_indX[1])
        cords_of_411_hit_2_zero_indX[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cords_of_411_hit_2_zero_indX[0],cords_of_411_hit_2_zero_indX[1]-30)
        cords_of_411_hit_2_zero_indX[2] += 1
        triple_deck_411_hits_2 += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        draw_cross(cords_of_411_hit_2_zero_indX[0],cords_of_411_hit_2_zero_indX[1]-60)
        cords_of_411_hit_2_zero_indX[2] += 1
        triple_deck_411_hits_2 += 1
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        cords_of_triple_deck_ship_lenght_2_player[3] = 3
        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_411_hits_2 = 0
            bot_pick_1deck_or_empty_cell() 
    

def third_bot_pick_3deckLenght_411_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_1_zero_indX[0],cords_of_411_hit_1_zero_indX[1]-30)
    cords_of_411_hit_1_zero_indX[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    draw_cross(cords_of_411_hit_1_zero_indX[0],cords_of_411_hit_1_zero_indX[1]-60)
    cords_of_411_hit_1_zero_indX[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    cords_of_triple_deck_ship_lenght_1_player[3] = 3
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def third_bot_pick_3deckLenght_411_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_2_zero_indX[0],cords_of_411_hit_2_zero_indX[1]-30)
    cords_of_411_hit_2_zero_indX[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    draw_cross(cords_of_411_hit_2_zero_indX[0],cords_of_411_hit_2_zero_indX[1]-60)
    cords_of_411_hit_2_zero_indX[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    cords_of_triple_deck_ship_lenght_2_player[3] = 3
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_2 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_411_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_1_zero_indY[0],cords_of_411_hit_1_zero_indY[1]-30)
    cords_of_411_hit_1_zero_indY[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    draw_cross(cords_of_411_hit_1_zero_indY[0],cords_of_411_hit_1_zero_indY[1]-60)
    cords_of_411_hit_1_zero_indY[2] += 1
    triple_deck_411_hits_1 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    cords_of_triple_deck_ship_lenght_1_player[3] = 3
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 


def second_bot_pick_3deckLenght_411_2_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_411_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cords_of_411_hit_2_zero_indY[0],cords_of_411_hit_2_zero_indY[1]-30)
    cords_of_411_hit_2_zero_indY[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    draw_cross(cords_of_411_hit_2_zero_indY[0],cords_of_411_hit_2_zero_indY[1]-60)
    cords_of_411_hit_2_zero_indY[2] += 1
    triple_deck_411_hits_2 += 1
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    cords_of_triple_deck_ship_lenght_2_player[3] = 3
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_411_hits_2 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_412_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_412_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]+30)
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    triple_deck_412_hits_1 += 1 
    cords_of_412_hit_1[2] += 1
    if cords_of_412_hit_1[0] >= -400 and cords_of_412_hit_1[0] <= -130 and cords_of_412_hit_1[1]+60 <= 150 and cords_of_412_hit_1[1]+60 >= -120 and list_status_cells_0field[ind_y11-2][ind_x11] != 3 and list_status_cells_0field[ind_y11-2][ind_x11] != 9:
        draw_dot(cords_of_412_hit_1[0],cords_of_412_hit_1[1]+60)
        cords_of_412_hit_1[2] += 1
        list_status_cells_0field[ind_y11-2][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]-30)
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        triple_deck_412_hits_1 += 1 
        cords_of_412_hit_1[2] += 1
        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_412_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_3deckLenght_412_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_412_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]+30)
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    triple_deck_412_hits_2 += 1 
    cords_of_412_hit_2[2] += 1
    if cords_of_412_hit_2[0] >= -400 and cords_of_412_hit_2[0] <= -130 and cords_of_412_hit_2[1]+60 <= 150 and cords_of_412_hit_2[1]+60 >= -120 and list_status_cells_0field[ind_y11-2][ind_x11] != 3 and list_status_cells_0field[ind_y11-2][ind_x11] != 9:
        draw_dot(cords_of_412_hit_2[0],cords_of_412_hit_2[1]+60)
        cords_of_412_hit_2[2] += 1
        list_status_cells_0field[ind_y11-2][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]-30)
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        triple_deck_412_hits_2 += 1 
        cords_of_412_hit_2[2] += 1
        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_mid:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_mid:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_412_hits_2 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckLenght_412_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_412_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    triple_deck_412_hits_1 += 1 
    cords_of_412_hit_1[2] += 1
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_412_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def third_bot_pick_3deckLenght_412_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_412_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    triple_deck_412_hits_2 += 1 
    cords_of_412_hit_2[2] += 1
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_mid:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_mid:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_412_hits_2 = 0
        bot_pick_1deck_or_empty_cell()
    
def second_bot_pick_3deckLenght_413_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_413_hit_1[0] >= -400 and cords_of_413_hit_1[0] <= -130 and cords_of_413_hit_1[1]-30 <= 150 and cords_of_413_hit_1[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_413_hit_1[0],cords_of_413_hit_1[1]-30)
        cords_of_413_hit_1[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        cords_of_triple_deck_ship_lenght_1_player[3] = 3
        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_413_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 


def second_bot_pick_3deckLenght_413_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_413_hit_2[0] >= -400 and cords_of_413_hit_2[0] <= -130 and cords_of_413_hit_2[1]-30 <= 150 and cords_of_413_hit_2[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_413_hit_2[0],cords_of_413_hit_2[1]-30)
        cords_of_413_hit_2[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        cords_of_triple_deck_ship_lenght_2_player[3] = 3
        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_413_hits_2 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_3deckLenght_413_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    cords_of_triple_deck_ship_lenght_1_player[3] = 3
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_413_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 
    
def third_bot_pick_3deckLenght_413_2():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    cords_of_triple_deck_ship_lenght_2_player[3] = 3
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])               
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_413_hits_2 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_413_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_413_hit_1_zero_indX[0] >= -400 and cords_of_413_hit_1_zero_indX[0] <= -130 and cords_of_413_hit_1_zero_indX[1]-30 <= 150 and cords_of_413_hit_1_zero_indX[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_413_hit_1_zero_indX[0],cords_of_413_hit_1_zero_indX[1]-30)
        cords_of_413_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_1_player[3] += 1
        cords_of_triple_deck_ship_lenght_1_player[3] = 3
        if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])               
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_413_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def second_bot_pick_3deckLenght_413_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_2
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_413_hit_2_zero_indX[0] >= -400 and cords_of_413_hit_2_zero_indX[0] <= -130 and cords_of_413_hit_2_zero_indX[1]-30 <= 150 and cords_of_413_hit_2_zero_indX[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_413_hit_2_zero_indX[0],cords_of_413_hit_2_zero_indX[1]-30)
        cords_of_413_hit_2_zero_indX[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        cords_of_triple_deck_ship_lenght_2_player[3] += 1
        cords_of_triple_deck_ship_lenght_2_player[3] = 3
        if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
            for i in list_cord_around_cell_3deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_3deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])                 
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            triple_deck_413_hits_2 = 0
            bot_pick_1deck_or_empty_cell() 


def third_bot_pick_3deckLenght_413_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_1_player[3] += 1
    cords_of_triple_deck_ship_lenght_1_player[3] = 3
    if cords_of_triple_deck_ship_lenght_1_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_413_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def third_bot_pick_3deckLenght_413_2_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global triple_deck_413_hits_2
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    cords_of_triple_deck_ship_lenght_2_player[3] += 1
    cords_of_triple_deck_ship_lenght_2_player[3] = 3
    if cords_of_triple_deck_ship_lenght_2_player[3] == 3:
        for i in list_cord_around_cell_3deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_3deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])                
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        triple_deck_413_hits_2 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_4deckWidth_521_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_521_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_521_hit_1[0] >= -400 and cords_of_521_hit_1[0] <= -130 and cords_of_521_hit_1[1]+30 <= 150 and cords_of_521_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_521_hit_1[0],cords_of_521_hit_1[1]+30)
        cords_of_521_hit_1[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+2] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+90,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+3] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_521_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_521_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_521_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0]+60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11+2] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0]+90,cord[1])
    list_status_cells_0field[ind_y11][ind_x11+3] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_width_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_width_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_521_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_522_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_522_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    four_deck_522_hits_1 += 1 
    cords_of_522_hit_1[2] += 1
    if cords_of_522_hit_1[0]-60 >= -400 and cords_of_522_hit_1[0]-60 <= -130 and cords_of_522_hit_1[1] <= 150 and cords_of_522_hit_1[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11-2] != 3 and list_status_cells_0field[ind_y11][ind_x11-2] != 9:
        draw_dot(cord[0]-60,cord[1]) 
        cords_of_522_hit_1[2] += 1
        list_status_cells_0field[ind_y11][ind_x11-2] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+2] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_522_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_522_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_522_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    four_deck_522_hits_1 += 1 
    cords_of_522_hit_1[2] += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+2] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_522_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_522_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_522_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]+30,cord[1])
    four_deck_522_hits_1 += 1 
    cords_of_522_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0]+60,cord[1])
    four_deck_522_hits_1 += 1 
    cords_of_522_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+2] = 8
    bot_four_deck_hits += 1
    if cords_of_522_hit_1_zero_indX[0]+90 >= -400 and cords_of_522_hit_1_zero_indX[0]+90 <= -130 and cords_of_522_hit_1_zero_indX[1] <= 150 and cords_of_522_hit_1_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+3] != 3 and list_status_cells_0field[ind_y11][ind_x11+3] != 9:
        draw_dot(cord[0]+90,cord[1])
        cords_of_522_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+3] = 3
        print(four_deck_522_hits_1,cords_of_522_hit_1_zero_indX[2])
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+2] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_522_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_522_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_522_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]-30,cord[1])   
    four_deck_522_hits_1 += 1 
    cords_of_522_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_width_mid_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_width_mid_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_522_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_523_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_523_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1[2] += 1
    draw_cross(cord[0]-60,cord[1])
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1[2] += 1
    if cords_of_523_hit_1[0]-90 >= -400 and cords_of_523_hit_1[0]-90 <= -130 and cords_of_523_hit_1[1] <= 150 and cords_of_523_hit_1[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11-3] != 3 and list_status_cells_0field[ind_y11][ind_x11-3] != 9:
        draw_dot(cord[0]-90,cord[1]) 
        cords_of_523_hit_1[2] += 1
        list_status_cells_0field[ind_y11][ind_x11-3] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_523_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_523_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_523_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]+30,cord[1])
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1[2] += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_523_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_523_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_523_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]-30,cord[1])
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0]-60,cord[1])
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    bot_four_deck_hits += 1
    if cords_of_523_hit_1_zero_indX[0]-90 >= -400 and cords_of_523_hit_1_zero_indX[0]-90 <= -130 and cords_of_523_hit_1_zero_indX[1] <= 150 and cords_of_523_hit_1_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11-3] != 3 and list_status_cells_0field[ind_y11][ind_x11-3] != 9:
        draw_dot(cord[0]-90,cord[1])
        cords_of_523_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+3] = 3
        print(four_deck_523_hits_1,cords_of_523_hit_1_zero_indX[2])
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]+30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11+1] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_mid_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_mid_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_523_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_523_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_523_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0]+30,cord[1])   
    four_deck_523_hits_1 += 1 
    cords_of_523_hit_1_zero_indX[2] += 1
    list_status_cells_0field[ind_y11][ind_x11+1] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_width_mid_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_width_mid_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_523_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_524_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_524_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_524_hit_1[0]+30 >= -400 and cords_of_524_hit_1[0]+30 <= -130 and cords_of_524_hit_1[1] <= 150 and cords_of_524_hit_1[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_524_hit_1[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-90,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-3] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_524_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_524_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_524_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    draw_cross(cord[0]-90,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-3] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_524_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckWidth_524_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_524_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_524_hit_1_zero_indY[0]+30 >= -400 and cords_of_524_hit_1_zero_indY[0]+30 <= -130 and cords_of_524_hit_1_zero_indY[1] <= 150 and cords_of_524_hit_1_zero_indY[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cord[0]+30,cord[1]) 
        cords_of_524_hit_1_zero_indY[2] += 1
        list_status_cells_0field[ind_y11][ind_x11+1] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0]-30,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-1] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-60,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-2] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0]-90,cord[1])
        list_status_cells_0field[ind_y11][ind_x11-3] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_width_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_width_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_524_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckWidth_524_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_524_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0]-30,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-1] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    draw_cross(cord[0]-60,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-2] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    draw_cross(cord[0]-90,cord[1])
    list_status_cells_0field[ind_y11][ind_x11-3] = 8
    four_deck_524_hits_1 += 1
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_width_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_width_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_524_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckLenght_511_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_511_hits_1
    global cords_of_511_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_511_hit_1[0] >= -400 and cords_of_511_hit_1[0] <= -130 and cords_of_511_hit_1[1]+30 <= 150 and cords_of_511_hit_1[1]+30 >= -120 and list_status_cells_0field[ind_y11-1][ind_x11] != 3 and list_status_cells_0field[ind_y11-1][ind_x11] != 9:
        draw_dot(cords_of_511_hit_1[0],cords_of_511_hit_1[1]+30)
        cords_of_511_hit_1[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]-30)
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-60)
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-90)
        list_status_cells_0field[ind_y11+3][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_511_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_4deckLenght_511_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_511_hits_1
    global cords_of_511_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-60)
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-90)
    list_status_cells_0field[ind_y11+3][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_511_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_4deckLenght_511_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_511_hits_1
    global cords_of_511_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_511_hit_1_zero_indX[0]+30 >= -400 and cords_of_511_hit_1_zero_indX[0]+30 <= -130 and cords_of_511_hit_1_zero_indX[1] <= 150 and cords_of_511_hit_1_zero_indX[1] >= -120 and list_status_cells_0field[ind_y11][ind_x11+1] != 3 and list_status_cells_0field[ind_y11][ind_x11+1] != 9:
        draw_dot(cords_of_511_hit_1_zero_indX[0]+30,cords_of_511_hit_1_zero_indX[1])
        cords_of_511_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11-1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]-30)
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-60)
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-90)
        list_status_cells_0field[ind_y11+3][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_left_to_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_right_to_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_511_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_4deckLenght_511_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_511_hits_1
    global cords_of_511_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-60)
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-90)
    list_status_cells_0field[ind_y11+3][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_511_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_4deckLenght_511_1_zeroY():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_511_hits_1
    global cords_of_511_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-60)
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-90)
    list_status_cells_0field[ind_y11+3][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_left_to_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_right_to_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_511_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_4deckLenght_512_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_512_hits_1
    global cords_of_512_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]+30)
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    four_deck_512_hits_1 += 1 
    cords_of_512_hit_1[2] += 1
    if cords_of_512_hit_1[0] >= -400 and cords_of_512_hit_1[0] <= -130 and cords_of_512_hit_1[1]+60 <= 150 and cords_of_512_hit_1[1]+60 >= -120 and list_status_cells_0field[ind_y11-2][ind_x11] != 3 and list_status_cells_0field[ind_y11-2][ind_x11] != 9:
        draw_dot(cords_of_512_hit_1[0],cords_of_512_hit_1[1]+60)
        cords_of_512_hit_1[2] += 1
        list_status_cells_0field[ind_y11-2][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-30)
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]-60)
        list_status_cells_0field[ind_y11+2][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4 
        if bot_four_deck_hits == 4:
            # bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_mid_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_mid_left:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_512_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_4deckLenght_512_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_512_hits_1
    global cords_of_512_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]-60)
    list_status_cells_0field[ind_y11+2][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4 
    if bot_four_deck_hits == 4:
        # bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_mid_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_mid_left:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_512_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckLenght_513_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_513_hits_1
    global cords_of_513_hit_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]+30)
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    four_deck_513_hits_1 += 1 
    cords_of_513_hit_1[2] += 1
    draw_cross(cord[0],cord[1]+60)
    bot_four_deck_hits += 1
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    four_deck_513_hits_1 += 1 
    cords_of_513_hit_1[2] += 1
    if cords_of_513_hit_1[0] >= -400 and cords_of_513_hit_1[0] <= -130 and cords_of_513_hit_1[1]+90 <= 150 and cords_of_513_hit_1[1]+90 >= -120 and list_status_cells_0field[ind_y11-3][ind_x11] != 3 and list_status_cells_0field[ind_y11-3][ind_x11] != 9:
        draw_dot(cords_of_513_hit_1[0],cords_of_513_hit_1[1]+90)
        cords_of_513_hit_1[2] += 1
        list_status_cells_0field[ind_y11-3][ind_x11] = 3
        print(cords_of_513_hit_1[2],four_deck_513_hits_1)
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]-30)
        list_status_cells_0field[ind_y11+1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_mid_right:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_mid_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_513_hits_1 = 0
            bot_pick_1deck_or_empty_cell() 

def third_bot_pick_4deckLenght_513_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_513_hits_1
    global cords_of_513_hit_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    draw_cross(cord[0],cord[1]-30)
    list_status_cells_0field[ind_y11+1][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_mid_right:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_mid_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_513_hits_1 = 0
        bot_pick_1deck_or_empty_cell() 

def second_bot_pick_4deckLenght_514_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_514_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_514_hit_1[0] >= -400 and cords_of_514_hit_1[0] <= -130 and cords_of_514_hit_1[1]-30 <= 150 and cords_of_514_hit_1[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_514_hit_1[0],cords_of_514_hit_1[1]-30)
        cords_of_514_hit_1[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+90)
        list_status_cells_0field[ind_y11-3][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])    
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_514_hits_1 = 0
            bot_pick_1deck_or_empty_cell()
        
def third_bot_pick_4deckLenght_514_1():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_514_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]+90)
    list_status_cells_0field[ind_y11-3][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])    
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_514_hits_1 = 0
        bot_pick_1deck_or_empty_cell()

def second_bot_pick_4deckLenght_514_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_514_hits_1
    global ind_x11
    global ind_y11
    global draw_cross_permited
    global draw_dot_permited
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    print(list_status_cells_0field[ind_y11][ind_x11])
    if cords_of_514_hit_1_zero_indX[0] >= -400 and cords_of_514_hit_1_zero_indX[0] <= -130 and cords_of_514_hit_1_zero_indX[1]-30 <= 150 and cords_of_514_hit_1_zero_indX[1]-30 >= -120 and list_status_cells_0field[ind_y11+1][ind_x11] != 3 and list_status_cells_0field[ind_y11+1][ind_x11] != 9:
        draw_dot(cords_of_514_hit_1_zero_indX[0],cords_of_514_hit_1_zero_indX[1]-30)
        cords_of_514_hit_1_zero_indX[2] += 1
        list_status_cells_0field[ind_y11+1][ind_x11] = 3
        player_turn = 'player'
        t_draw_whos_turn.clear()
        draw_turn(-68, 270 , "Хід гравця", 15)
        if player_turn == 'player':
            draw_dot_permited = True
            draw_cross_permited = True
            player_pick()
    else:
        draw_cross(cord[0],cord[1]+30)
        list_status_cells_0field[ind_y11-1][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+60)
        list_status_cells_0field[ind_y11-2][ind_x11] = 8
        bot_four_deck_hits += 1
        draw_cross(cord[0],cord[1]+90)
        list_status_cells_0field[ind_y11-3][ind_x11] = 8
        bot_four_deck_hits += 1
        bot_four_deck_hits = 4
        if bot_four_deck_hits == 4:
            bot_four_deck_hits = 0
            for i in list_cord_around_cell_4deck_lenght_right_to_left:
                if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                    list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
            for j in coordinates_around_cell_4deck_lenght_left_to_right:
                if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                    draw_dot(cord[0]+j[0],cord[1]+j[1])    
                    for i in list_status_cells_0field:
                        print(i)
                    print(' ')
            drowned_ships_bot += 1
            four_deck_514_hits_1 = 0
            bot_pick_1deck_or_empty_cell()

def third_bot_pick_4deckLenght_514_1_zeroX():
    global double_deck_hits_player 
    global bot_four_deck_hits
    global list_status_cells_0field
    global player_turn
    global drowned_ships_bot
    global four_deck_514_hits_1
    global ind_x11
    global ind_y11
    cord = coordinates_of_cells_0field[ind_y11][ind_x11]
    draw_cross(cord[0],cord[1]+30)
    list_status_cells_0field[ind_y11-1][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]+60)
    list_status_cells_0field[ind_y11-2][ind_x11] = 8
    bot_four_deck_hits += 1
    draw_cross(cord[0],cord[1]+90)
    list_status_cells_0field[ind_y11-3][ind_x11] = 8
    bot_four_deck_hits += 1
    bot_four_deck_hits = 4
    if bot_four_deck_hits == 4:
        bot_four_deck_hits = 0
        for i in list_cord_around_cell_4deck_lenght_right_to_left:
            if ind_y11+i[1] >= 0 and ind_y11+i[1] < len(list_status_cells_0field) and ind_x11+i[0] >= 0 and ind_x11+i[0] < len(list_status_cells_0field):
                list_status_cells_0field[ind_y11+i[1]][ind_x11+i[0]] = 9
        for j in coordinates_around_cell_4deck_lenght_left_to_right:
            if cord[0]+j[0] >= -400 and cord[0]+j[0] <= -130 and cord[1]+j[1] <= 150 and cord[1]+j[1] >= -120:
                draw_dot(cord[0]+j[0],cord[1]+j[1])    
                for i in list_status_cells_0field:
                    print(i)
                print(' ')
        drowned_ships_bot += 1
        four_deck_514_hits_1 = 0
        bot_pick_1deck_or_empty_cell()


def player_move(x, y):
    global draw_directory 
    global player_turn
    global single_deck_ships
    global double_deck_ships
    global triple_deck_ships
    global four_deck_ships
    global game_stage
    global select_ship_directory
    global may_draw_single_deck_ships
    global may_draw_double_deck_ships
    global may_draw_triple_deck_ships
    global may_draw_four_deck_ships
    global status_of_cell
    global player_double_deck_ships_lenght
    global player_double_deck_ships_width
    global player_triple_deck_ships_width
    global player_triple_deck_ships_lenght
    global player_turn
    global may_draw_ships
    global draw_cross_permited
    global draw_dot_permited
    for row_ind in range(len(coordinates_of_cells_0field)):
        for cell_ind in range(len(coordinates_of_cells_0field[row_ind])):
            cord = coordinates_of_cells_0field[row_ind][cell_ind]
            if cord[0] < x and x < cord[0] + 30 and cord[1] > y and y > cord[1] - 30:                  
                    if may_draw_single_deck_ships == True:
                        if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2:
                            unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці", 15)
                        elif list_status_cells_0field[row_ind][cell_ind] == 0 and may_draw_ships == True:
                            may_draw_ships = False
                            t_draw_inability.clear()
                            draw_single_deck_ship(cord[0], cord[1], 'down')
                            single_deck_ships += 1
                            list_status_cells_0field[row_ind][cell_ind] = 2
                            for i in list_cord_around_cell_1deck:
                                if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                    list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                            for i in list_status_cells_0field:
                                print(i)
                            print(' ')
                            print(single_deck_ships)
                            may_draw_ships = True

                        if single_deck_ships == 4:
                            may_draw_single_deck_ships = False
                            may_draw_double_deck_ships = True
                            t_draw_whos_turn.clear()
                            first_button.showturtle()
                            second_button.showturtle()
                            

                            first_button.shapesize(1.3)
                            first_button.shape('square')
                            first_button.color('white')
                            first_button.penup()
                            first_button.goto(5,185)

                            second_button.shapesize(1.3)
                            second_button.shape('square')
                            second_button.color('white')
                            second_button.penup()
                            second_button.goto(-25, 185)

                            choice_bottom()
                            draw_how_to_build(-165, 210, 'Оберіть, як саме ви хочете поставити корабель', 10)
                            

                            draw_turn(-400, 270, "Натисніть на клітинку, де ви хочете побудувати початок двопалубних кораблів\n\t\t(Розстановка йде зліва на право\зверху вниз)", 15)
                    if may_draw_single_deck_ships == False and may_draw_double_deck_ships == True:
                        if draw_directory == 'vertical':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif row_ind == 9 or list_status_cells_0field[row_ind + 1][cell_ind] == 2 or list_status_cells_0field[row_ind + 1][cell_ind] == 311 or list_status_cells_0field[row_ind + 1][cell_ind] == 312:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 1][cell_ind] == 1 or list_status_cells_0field[row_ind + 1][cell_ind] == 321 or list_status_cells_0field[row_ind + 1][cell_ind] == 322 or row_ind == 9:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:

                                if row_ind + 1 >= 0 and row_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind + 1][cell_ind] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_double_deck_ship_lenght(cord[0], cord[1], 'down')
                                    double_deck_ships += 1
                                    player_double_deck_ships_lenght += 1
                                    if player_double_deck_ships_lenght == 1:
                                        cords_of_double_deck_ship_lenght_1_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_lenght_1_player.append([cord[0],cord[1]-30])
                                        cords_of_double_deck_ship_lenght_1_player.append(0)
                                        print(cords_of_double_deck_ship_lenght_1_player)
                                    elif player_double_deck_ships_lenght == 2:
                                        cords_of_double_deck_ship_lenght_2_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_lenght_2_player.append([cord[0],cord[1]-30])
                                        cords_of_double_deck_ship_lenght_2_player.append(0)
                                        print(cords_of_double_deck_ship_lenght_2)
                                    elif player_double_deck_ships_lenght == 3:
                                        cords_of_double_deck_ship_lenght_3_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_lenght_3_player.append([cord[0],cord[1]-30])
                                        cords_of_double_deck_ship_lenght_3_player.append(0)
                                        print(cords_of_double_deck_ship_lenght_3_player)
                                    # print(cell_ind)
                                    list_status_cells_0field[row_ind][cell_ind] = 311
                                    list_status_cells_0field[row_ind+1][cell_ind] = 312
                                    for i in list_cord_around_cell_2deck_lenght:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    may_draw_ships = True
                        elif draw_directory == 'gorizontal':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif cell_ind == 9 or list_status_cells_0field[row_ind][cell_ind + 1] == 2 or list_status_cells_0field[row_ind][cell_ind + 1] == 311 or list_status_cells_0field[row_ind][cell_ind + 1] == 312:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 1] == 1 or list_status_cells_0field[row_ind][cell_ind + 1] == 321 or list_status_cells_0field[row_ind][cell_ind + 1] == 322 or cell_ind == 9:
                                unable_to_build_ship(-250, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:

                                if cell_ind + 1 >= 0 and cell_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind][cell_ind + 1] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_double_deck_ship_width(cord[0], cord[1], 'down')
                                    print(cell_ind)
                                    double_deck_ships += 1
                                    player_double_deck_ships_width += 1
                                    if player_double_deck_ships_width == 1:
                                        cords_of_double_deck_ship_width_1_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_width_1_player.append([cord[0]+30,cord[1]])
                                        cords_of_double_deck_ship_width_1_player.append(0)
                                        print(cords_of_double_deck_ship_width_1_player)
                                    elif player_double_deck_ships_width == 2:
                                        cords_of_double_deck_ship_width_2_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_width_2_player.append([cord[0]+30,cord[1]])
                                        cords_of_double_deck_ship_width_2_player.append(0)
                                        print(cords_of_double_deck_ship_width_2_player)
                                    elif player_double_deck_ships_width == 3:
                                        cords_of_double_deck_ship_width_3_player.append([cord[0],cord[1]])                        
                                        cords_of_double_deck_ship_width_3_player.append([cord[0]+30,cord[1]])
                                        cords_of_double_deck_ship_width_3_player.append(0)
                                        print(cords_of_double_deck_ship_width_3_player)
                                    list_status_cells_0field[row_ind][cell_ind] = 321
                                    list_status_cells_0field[row_ind][cell_ind+1] = 322
                                    for i in list_cord_around_cell_2deck_width:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    may_draw_ships = True
                    ###############
                    
                        if double_deck_ships == 3:
                            may_draw_double_deck_ships = False
                            may_draw_triple_deck_ships = True
                            t_draw_whos_turn.clear()
                            draw_turn(-400, 270, "Натисніть на клітинку, де ви хочете побудувати початок трьопалубних кораблів\n\t\t(Розстановка йде зліва на право\зверху вниз)", 15)

                    if may_draw_double_deck_ships == False and may_draw_triple_deck_ships == True:
                        if draw_directory == 'vertical':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif row_ind == 9 or row_ind == 8:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 2][cell_ind] == 2 or list_status_cells_0field[row_ind + 2][cell_ind] == 311 or list_status_cells_0field[row_ind + 2][cell_ind] == 312 or list_status_cells_0field[row_ind + 2][cell_ind] == 321 or list_status_cells_0field[row_ind + 2][cell_ind] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 2][cell_ind] == 411 or list_status_cells_0field[row_ind + 2][cell_ind] == 412 or list_status_cells_0field[row_ind + 2][cell_ind] == 413 or list_status_cells_0field[row_ind + 2][cell_ind] == 421 or list_status_cells_0field[row_ind + 2][cell_ind] == 422 or list_status_cells_0field[row_ind + 2][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322 or list_status_cells_0field[row_ind][cell_ind] == 411 or list_status_cells_0field[row_ind][cell_ind] == 412 or list_status_cells_0field[row_ind][cell_ind] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 2][cell_ind] == 1 or row_ind == 9 or list_status_cells_0field[row_ind][cell_ind] == 421 or list_status_cells_0field[row_ind][cell_ind] == 422 or list_status_cells_0field[row_ind][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:

                                if row_ind + 1 >= 0 and row_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind + 2][cell_ind] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_triple_deck_ship_lenght(cord[0], cord[1], 'down')
                                    print(cell_ind)
                                    triple_deck_ships += 1
                                    player_triple_deck_ships_lenght += 1
                                    if player_triple_deck_ships_lenght == 1:
                                        cords_of_triple_deck_ship_lenght_1_player.append([cord[0],cord[1]])
                                        cords_of_triple_deck_ship_lenght_1_player.append([cord[0],cord[1]-30])
                                        cords_of_triple_deck_ship_lenght_1_player.append([cord[0],cord[1]-60])
                                        cords_of_triple_deck_ship_lenght_1_player.append(0)
                                        print(cords_of_triple_deck_ship_lenght_1_player)
                                    elif player_triple_deck_ships_lenght == 2:
                                        cords_of_triple_deck_ship_lenght_2_player.append([cord[0],cord[1]])
                                        cords_of_triple_deck_ship_lenght_2_player.append([cord[0],cord[1]-30])
                                        cords_of_triple_deck_ship_lenght_2_player.append([cord[0],cord[1]-60])
                                        cords_of_triple_deck_ship_lenght_2_player.append(0)
                                        print(cords_of_triple_deck_ship_lenght_2_player)

                                    list_status_cells_0field[row_ind][cell_ind] = 411
                                    list_status_cells_0field[row_ind+1][cell_ind] = 412
                                    list_status_cells_0field[row_ind+2][cell_ind] = 413
                                    for i in list_cord_around_cell_3deck_lenght:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    may_draw_ships = True
                        
                        elif draw_directory == 'gorizontal':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif cell_ind == 8 or cell_ind == 9:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322 or list_status_cells_0field[row_ind][cell_ind] == 411 or list_status_cells_0field[row_ind][cell_ind] == 412 or list_status_cells_0field[row_ind][cell_ind] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 421 or list_status_cells_0field[row_ind][cell_ind] == 422 or list_status_cells_0field[row_ind][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 2] == 2 or list_status_cells_0field[row_ind][cell_ind + 2] == 311 or list_status_cells_0field[row_ind][cell_ind + 2] == 312 or list_status_cells_0field[row_ind][cell_ind + 2] == 321 or list_status_cells_0field[row_ind][cell_ind + 2] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 2] == 411 or list_status_cells_0field[row_ind][cell_ind + 2] == 412 or list_status_cells_0field[row_ind][cell_ind + 2] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 2] == 421 or list_status_cells_0field[row_ind][cell_ind + 2] == 422 or list_status_cells_0field[row_ind][cell_ind + 2] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 2] == 1 or cell_ind == 9:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:

                                if cell_ind + 1 >= 0 and cell_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind][cell_ind + 2] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_triple_deck_ship_width(cord[0], cord[1], 'down')
                                    print(cell_ind)
                                    triple_deck_ships += 1
                                    player_triple_deck_ships_width += 1
                                    if player_triple_deck_ships_width == 1:
                                        cords_of_triple_deck_ship_width_1_player.append([cord[0],cord[1]])
                                        cords_of_triple_deck_ship_width_1_player.append([cord[0]+30,cord[1]])
                                        cords_of_triple_deck_ship_width_1_player.append([cord[0]+60,cord[1]])
                                        cords_of_triple_deck_ship_width_1_player.append(0)
                                        print(cords_of_triple_deck_ship_width_1_player)
                                    elif player_triple_deck_ships_width == 2:
                                        cords_of_triple_deck_ship_width_2_player.append([cord[0],cord[1]])
                                        cords_of_triple_deck_ship_width_2_player.append([cord[0]+30,cord[1]])
                                        cords_of_triple_deck_ship_width_2_player.append([cord[0]+60,cord[1]])
                                        cords_of_triple_deck_ship_width_2_player.append(0)
                                        print(cords_of_triple_deck_ship_width_2_player)

                                    list_status_cells_0field[row_ind][cell_ind] = 421
                                    list_status_cells_0field[row_ind][cell_ind+1] = 422
                                    list_status_cells_0field[row_ind][cell_ind+2] = 423
                                    for i in list_cord_around_cell_3deck_width:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    may_draw_ships = True
                    ##########
                        if triple_deck_ships == 2:
                            may_draw_triple_deck_ships = False
                            may_draw_four_deck_ships = True
                            t_draw_whos_turn.clear()
                            draw_turn(-400, 270, "Натисніть на клітинку, де ви хочете побудувати початок чотирьохпалубних кораблів\n\t\t(Розстановка йде зліва на право\зверху вниз)", 15)
                    
                    if may_draw_triple_deck_ships == False and may_draw_four_deck_ships == True:
                        if draw_directory == 'vertical':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312 or list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif row_ind == 9 or row_ind == 8 or row_ind == 7:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 411 or list_status_cells_0field[row_ind][cell_ind] == 412 or list_status_cells_0field[row_ind][cell_ind] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 421 or list_status_cells_0field[row_ind][cell_ind] == 422 or list_status_cells_0field[row_ind][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 3][cell_ind] == 2 or list_status_cells_0field[row_ind + 2][cell_ind] == 2 or list_status_cells_0field[row_ind + 2][cell_ind] == 311 or list_status_cells_0field[row_ind + 3][cell_ind] == 311:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 3][cell_ind] == 312 or list_status_cells_0field[row_ind + 2][cell_ind] == 312 or list_status_cells_0field[row_ind + 3][cell_ind] == 321 or list_status_cells_0field[row_ind + 2][cell_ind] == 321 or list_status_cells_0field[row_ind + 3][cell_ind] == 322 or list_status_cells_0field[row_ind + 3][cell_ind] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 3][cell_ind] == 411 or list_status_cells_0field[row_ind + 2][cell_ind] == 411 or list_status_cells_0field[row_ind + 3][cell_ind] == 412 or list_status_cells_0field[row_ind + 2][cell_ind] == 412 or list_status_cells_0field[row_ind + 3][cell_ind] == 413 or list_status_cells_0field[row_ind + 2][cell_ind] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind + 3][cell_ind] == 421 or list_status_cells_0field[row_ind + 2][cell_ind] == 421 or list_status_cells_0field[row_ind + 3][cell_ind] == 422 or list_status_cells_0field[row_ind + 2][cell_ind] == 422 or list_status_cells_0field[row_ind + 3][cell_ind] == 423 or list_status_cells_0field[row_ind + 2][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)

                            elif list_status_cells_0field[row_ind + 3][cell_ind] == 1 or row_ind == 9 or list_status_cells_0field[row_ind + 2][cell_ind] == 1:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:
                    
                                if row_ind + 1 >= 0 and row_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind + 3][cell_ind] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_four_deck_ship_lenght(cord[0], cord[1], 'down')
                                    print(cell_ind)
                                    four_deck_ships += 1
                                    list_status_cells_0field[row_ind][cell_ind] = 511
                                    list_status_cells_0field[row_ind+1][cell_ind] = 512
                                    list_status_cells_0field[row_ind+2][cell_ind] = 513
                                    list_status_cells_0field[row_ind+3][cell_ind] = 514
                                    for i in list_cord_around_cell_4deck_lenght:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    may_draw_ships = True

                        elif draw_directory == 'gorizontal':
                            t_draw_inability.clear()
                            if list_status_cells_0field[row_ind][cell_ind] == 1 or list_status_cells_0field[row_ind][cell_ind] == 2 or list_status_cells_0field[row_ind][cell_ind] == 311 or list_status_cells_0field[row_ind][cell_ind] == 312 or list_status_cells_0field[row_ind][cell_ind] == 321 or list_status_cells_0field[row_ind][cell_ind] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif cell_ind == 8 or cell_ind == 9 or cell_ind == 7:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 411 or list_status_cells_0field[row_ind][cell_ind] == 412 or list_status_cells_0field[row_ind][cell_ind] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 421 or list_status_cells_0field[row_ind][cell_ind] == 422 or list_status_cells_0field[row_ind][cell_ind] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 3] == 2 or list_status_cells_0field[row_ind][cell_ind + 2] == 2 or list_status_cells_0field[row_ind][cell_ind + 2] == 311 or list_status_cells_0field[row_ind][cell_ind + 3] == 311:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 3] == 312 or list_status_cells_0field[row_ind][cell_ind + 2] == 312 or list_status_cells_0field[row_ind][cell_ind + 3] == 321 or list_status_cells_0field[row_ind][cell_ind + 2] == 321 or list_status_cells_0field[row_ind][cell_ind + 3] == 322 or list_status_cells_0field[row_ind][cell_ind + 2] == 322:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 3] == 411 or list_status_cells_0field[row_ind][cell_ind + 2] == 411 or list_status_cells_0field[row_ind][cell_ind + 3] == 412 or list_status_cells_0field[row_ind][cell_ind + 2] == 412 or list_status_cells_0field[row_ind][cell_ind + 3] == 413 or list_status_cells_0field[row_ind][cell_ind + 2] == 413:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 3] == 421 or list_status_cells_0field[row_ind][cell_ind + 2] == 421 or list_status_cells_0field[row_ind][cell_ind + 3] == 422 or list_status_cells_0field[row_ind][cell_ind + 2] == 422 or list_status_cells_0field[row_ind][cell_ind + 3] == 423 or list_status_cells_0field[row_ind][cell_ind + 2] == 423:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind + 3] == 1 or cell_ind == 9 or list_status_cells_0field[row_ind][cell_ind + 2] == 1:
                                unable_to_build_ship(-240, 230, "Ви не можете поставити корабель у цій клітинці!", 15)
                            elif list_status_cells_0field[row_ind][cell_ind] == 0:

                                if cell_ind + 1 >= 0 and cell_ind + 1 < len(list_status_cells_0field) and list_status_cells_0field[row_ind][cell_ind + 3] != 1 and may_draw_ships == True:
                                    may_draw_ships = False
                                    t_draw_inability.clear()
                                    draw_four_deck_ship_width(cord[0], cord[1], 'down')
                                    print(cell_ind)
                                    four_deck_ships += 1
                                    list_status_cells_0field[row_ind][cell_ind] = 521
                                    list_status_cells_0field[row_ind][cell_ind+1] = 522
                                    list_status_cells_0field[row_ind][cell_ind+2] = 523
                                    list_status_cells_0field[row_ind][cell_ind+3] = 524
                                    for i in list_cord_around_cell_4deck_width:
                                        if row_ind+i[1] >= 0 and row_ind+i[1] < len(list_status_cells_0field) and cell_ind+i[0] >= 0 and cell_ind+i[0] < len(list_status_cells_0field):
                                            list_status_cells_0field[row_ind+i[1]][cell_ind+i[0]] = 1
                                    for i in list_status_cells_0field:
                                        print(i)
                                    print(' ')
                                    first_button.hideturtle()
                                    second_button.hideturtle()
                                    may_draw_ships = True


                        if four_deck_ships == 1:   
                            may_draw_four_deck_ships = False               
                            bot_move()
                            if player_turn == 'player' and draw_cross_permited != False and draw_dot_permited != False:
                                t.onscreenclick(player_pick)
                                player_turn = 'bot'
                            



                            
                
                            
triple_deck_hits = 0    

status_of_cell = 0

bot_single_deck_ships = 0

bot_double_deck_ships = 0

bot_double_deck_ships_lenght = 0

bot_double_deck_ships_width = 0

bot_triple_deck_ships_lenght = 0

bot_triple_deck_ships_width = 0


bot_triple_deck_ships = 0

bot_four_deck_ships = 0

double_deck_hits_width = 0

double_deck_hits_lenght = 0

triple_deck_hits_width = 0

triple_deck_hits_lenght = 0

four_deck_hits = 0

cords_of_double_deck_ship_lenght_1 = []

cords_of_double_deck_ship_lenght_2 = []

cords_of_double_deck_ship_lenght_3 = []

cords_of_double_deck_ship_width_1 = []

cords_of_double_deck_ship_width_2 = []

cords_of_double_deck_ship_width_3 = []

cords_of_triple_deck_ship_lenght_1 = []

cords_of_triple_deck_ship_lenght_2 = []

cords_of_triple_deck_ship_width_1 = []

cords_of_triple_deck_ship_width_2 = []



player_double_deck_ships_lenght = 0 

player_double_deck_ships_width = 0

cords_of_double_deck_ship_lenght_1_player = []

cords_of_double_deck_ship_lenght_2_player = []

cords_of_double_deck_ship_lenght_3_player = []

cords_of_double_deck_ship_width_1_player = []

cords_of_double_deck_ship_width_2_player = []

cords_of_double_deck_ship_width_3_player = []

cords_of_triple_deck_ship_lenght_1_player = []

cords_of_triple_deck_ship_lenght_2_player = []

cords_of_triple_deck_ship_width_1_player = []

cords_of_triple_deck_ship_width_2_player = []

player_triple_deck_ships_lenght = 0 

player_triple_deck_ships_width = 0







def bot_move():
    global bot_single_deck_ships
    global bot_double_deck_ships
    global bot_triple_deck_ships
    global bot_four_deck_ships
    global status_of_cell
    global bot_double_deck_ships_lenght
    global bot_double_deck_ships_width
    global bot_triple_deck_ships_lenght
    global bot_triple_deck_ships_width
    t_button.clear()
    t_draw_whos_turn.clear()
    t_how_to_build.clear()
    draw_turn(-170, 270 , "Йде розстановка кораблів бота", 15)
    while bot_single_deck_ships != 4:
        x_ind = rand.randint(0,9)
        y_ind = rand.randint(0,9)
        if list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2:
            cord = coordinates_of_cells_1field[y_ind][x_ind]
            print(y_ind,x_ind)
            print(cord)
            draw_single_deck_ship(cord[0],cord[1],'up')
            bot_single_deck_ships += 1
            list_status_cells_1field[y_ind][x_ind] = 2
            for i in list_cord_around_cell_1deck:
                if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                    list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
            for i in list_status_cells_1field:
                print(i)
            print(' ')
    
    if bot_single_deck_ships == 4:
        while bot_double_deck_ships != 3:
            x_ind = rand.randint(0,9)
            y_ind = rand.randint(0,9)
            ship_direction = rand.randint(1,2)
            if list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and ship_direction == 1 and y_ind < 9:
                if list_status_cells_1field[y_ind + 1][x_ind] != 1 and list_status_cells_1field[y_ind + 1][x_ind] != 2  and list_status_cells_1field[y_ind+1][x_ind] != 311 and list_status_cells_1field[y_ind+1][x_ind] != 312:
                    if list_status_cells_1field[y_ind+1][x_ind] != 321 and list_status_cells_1field[y_ind+1][x_ind] != 322:
                        cord = coordinates_of_cells_1field[y_ind][x_ind]
                        draw_double_deck_ship_lenght(cord[0],cord[1],'up')
                        bot_double_deck_ships += 1
                        bot_double_deck_ships_lenght += 1
                        if bot_double_deck_ships_lenght == 1:
                            cords_of_double_deck_ship_lenght_1.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_lenght_1.append([cord[0],cord[1]-30])
                            cords_of_double_deck_ship_lenght_1.append(0)
                            print(cords_of_double_deck_ship_lenght_1)
                        elif bot_double_deck_ships_lenght == 2:
                            cords_of_double_deck_ship_lenght_2.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_lenght_2.append([cord[0],cord[1]-30])
                            cords_of_double_deck_ship_lenght_2.append(0)
                            print(cords_of_double_deck_ship_lenght_2)
                        elif bot_double_deck_ships_lenght == 3:
                            cords_of_double_deck_ship_lenght_3.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_lenght_3.append([cord[0],cord[1]-30])
                            cords_of_double_deck_ship_lenght_3.append(0)
                            print(cords_of_double_deck_ship_lenght_3)

                        list_status_cells_1field[y_ind][x_ind] = 311
                        list_status_cells_1field[y_ind+1][x_ind] = 312
                        status_of_cell = 1
                        for i in list_cord_around_cell_2deck_lenght:
                            if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                        # for i in list_status_cells_1field:
                        #     print(i)
                        # print(' ')


            elif list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and ship_direction == 2 and x_ind < 9:
                if list_status_cells_1field[y_ind][x_ind + 1] != 1 and list_status_cells_1field[y_ind][x_ind + 1] != 2  and list_status_cells_1field[y_ind][x_ind + 1] != 311 and list_status_cells_1field[y_ind][x_ind + 1] != 312:
                    if list_status_cells_1field[y_ind][x_ind + 1] != 321 and list_status_cells_1field[y_ind][x_ind + 1] != 322:
                        cord = coordinates_of_cells_1field[y_ind][x_ind]
                        print(y_ind,x_ind, ' ', y_ind, x_ind+1)
                        # print(cord)
                        # print(ship_direction)
                        draw_double_deck_ship_width(cord[0],cord[1],'up')
                        bot_double_deck_ships += 1
                        bot_double_deck_ships_width += 1
                        if bot_double_deck_ships_width == 1:
                            cords_of_double_deck_ship_width_1.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_width_1.append([cord[0]+30,cord[1]])
                            cords_of_double_deck_ship_width_1.append(0)
                            print(cords_of_double_deck_ship_width_1)
                        elif bot_double_deck_ships_width == 2:
                            cords_of_double_deck_ship_width_2.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_width_2.append([cord[0]+30,cord[1]])
                            cords_of_double_deck_ship_width_2.append(0)
                            print(cords_of_double_deck_ship_width_2)
                        elif bot_double_deck_ships_width == 3:
                            cords_of_double_deck_ship_width_3.append([cord[0],cord[1]])                        
                            cords_of_double_deck_ship_width_3.append([cord[0]+30,cord[1]])
                            cords_of_double_deck_ship_width_3.append(0)
                            print(cords_of_double_deck_ship_width_3)
    

                        list_status_cells_1field[y_ind][x_ind] = 321
                        list_status_cells_1field[y_ind][x_ind+1] = 322
                        status_of_cell = 1
                        for i in list_cord_around_cell_2deck_width:
                            if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                        # for i in list_status_cells_1field:
                        #     print(i)
                        # print(' ')

    if bot_double_deck_ships == 3:
        while bot_triple_deck_ships != 2:
            x_ind = rand.randint(0,9)
            y_ind = rand.randint(0,9)
            ship_direction = rand.randint(1,2)
            if list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and ship_direction == 1 and y_ind < 8:
                if list_status_cells_1field[y_ind][x_ind] != 411 and list_status_cells_1field[y_ind][x_ind] != 412 and list_status_cells_1field[y_ind][x_ind] != 413 and list_status_cells_1field[y_ind][x_ind] != 421 and list_status_cells_1field[y_ind][x_ind] != 422 and list_status_cells_1field[y_ind][x_ind] != 423:
                    if list_status_cells_1field[y_ind + 2][x_ind] != 1 and list_status_cells_1field[y_ind + 2][x_ind] != 2 and list_status_cells_1field[y_ind+2][x_ind] != 311 and list_status_cells_1field[y_ind+2][x_ind] != 312 and list_status_cells_1field[y_ind+2][x_ind] != 411 and list_status_cells_1field[y_ind+2][x_ind] != 412 and list_status_cells_1field[y_ind+2][x_ind] != 413:
                        if list_status_cells_1field[y_ind+2][x_ind] != 321 and list_status_cells_1field[y_ind+2][x_ind] != 322 and list_status_cells_1field[y_ind+2][x_ind] != 421 and list_status_cells_1field[y_ind+2][x_ind] != 422 and list_status_cells_1field[y_ind+2][x_ind] != 423:
                                cord = coordinates_of_cells_1field[y_ind][x_ind]
                                print(y_ind,x_ind)
                                print(cord)
                                print(ship_direction)
                                draw_triple_deck_ship_lenght(cord[0],cord[1],'up')
                                bot_triple_deck_ships += 1
                                bot_triple_deck_ships_lenght += 1
                                if bot_triple_deck_ships_lenght == 1:
                                    cords_of_triple_deck_ship_lenght_1.append([cord[0],cord[1]])
                                    cords_of_triple_deck_ship_lenght_1.append([cord[0],cord[1]-30])
                                    cords_of_triple_deck_ship_lenght_1.append([cord[0],cord[1]-60])
                                    cords_of_triple_deck_ship_lenght_1.append(0)
                                    print(cords_of_triple_deck_ship_lenght_1)
                                elif bot_triple_deck_ships_lenght == 2:
                                    cords_of_triple_deck_ship_lenght_2.append([cord[0],cord[1]])
                                    cords_of_triple_deck_ship_lenght_2.append([cord[0],cord[1]-30])
                                    cords_of_triple_deck_ship_lenght_2.append([cord[0],cord[1]-60])
                                    cords_of_triple_deck_ship_lenght_2.append(0)
                                    print(cords_of_triple_deck_ship_lenght_2)

                                list_status_cells_1field[y_ind][x_ind] = 411
                                list_status_cells_1field[y_ind+1][x_ind] = 412
                                list_status_cells_1field[y_ind+2][x_ind] = 413
                                status_of_cell = 1
                                for i in list_cord_around_cell_3deck_lenght:
                                    if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                        list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                                for i in list_status_cells_1field:
                                    print(i)
                                print(' ')

            elif list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and ship_direction == 2 and x_ind < 8:
                if list_status_cells_1field[y_ind][x_ind] != 411 and list_status_cells_1field[y_ind][x_ind] != 412 and list_status_cells_1field[y_ind][x_ind] != 413 and list_status_cells_1field[y_ind][x_ind] != 421 and list_status_cells_1field[y_ind][x_ind] != 422 and list_status_cells_1field[y_ind][x_ind] != 423:
                    if list_status_cells_1field[y_ind][x_ind + 2] != 1 and list_status_cells_1field[y_ind][x_ind + 2] != 2 and list_status_cells_1field[y_ind][x_ind + 2] != 311 and list_status_cells_1field[y_ind][x_ind + 2] != 312 and list_status_cells_1field[y_ind][x_ind + 2] != 411 and list_status_cells_1field[y_ind][x_ind + 2] != 412 and list_status_cells_1field[y_ind][x_ind +2] != 413:
                        if list_status_cells_1field[y_ind][x_ind + 2] != 321 and list_status_cells_1field[y_ind][x_ind + 2] != 322 and list_status_cells_1field[y_ind][x_ind + 2] != 421 and list_status_cells_1field[y_ind][x_ind + 2] != 422 and list_status_cells_1field[y_ind][x_ind + 2] != 423:
                            cord = coordinates_of_cells_1field[y_ind][x_ind]
                            print(y_ind,x_ind)
                            print(cord)
                            print(ship_direction)
                            draw_triple_deck_ship_width(cord[0],cord[1],'up')
                            bot_triple_deck_ships += 1
                            bot_triple_deck_ships_width += 1
                            if bot_triple_deck_ships_width == 1:
                                cords_of_triple_deck_ship_width_1.append([cord[0],cord[1]])                        
                                cords_of_triple_deck_ship_width_1.append([cord[0]+30,cord[1]])
                                cords_of_triple_deck_ship_width_1.append([cord[0]+60,cord[1]])
                                cords_of_triple_deck_ship_width_1.append(0)
                                print(cords_of_triple_deck_ship_width_1)
                            elif bot_triple_deck_ships_width == 2:
                                cords_of_triple_deck_ship_width_2.append([cord[0],cord[1]])                        
                                cords_of_triple_deck_ship_width_2.append([cord[0]+30,cord[1]])
                                cords_of_triple_deck_ship_width_2.append([cord[0]+60,cord[1]])
                                cords_of_triple_deck_ship_width_2.append(0)
                                print(cords_of_triple_deck_ship_width_2)

                            list_status_cells_1field[y_ind][x_ind] = 421
                            list_status_cells_1field[y_ind][x_ind+1] = 422
                            list_status_cells_1field[y_ind][x_ind+2] = 423
                            status_of_cell = 1
                            for i in list_cord_around_cell_3deck_width:
                                if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                    list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                            for i in list_status_cells_1field:
                                print(i)
                            print(' ')
    if bot_triple_deck_ships == 2:
        while bot_four_deck_ships != 1:
            x_ind = rand.randint(0,9)
            y_ind = rand.randint(0,9)
            ship_direction = rand.randint(1,2)
            if list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and list_status_cells_1field[y_ind][x_ind] != 521 and list_status_cells_1field[y_ind][x_ind] != 522 and list_status_cells_1field[y_ind][x_ind] != 523 and list_status_cells_1field[y_ind][x_ind] != 524 and ship_direction == 1 and y_ind < 7:
                if list_status_cells_1field[y_ind][x_ind] != 411 and list_status_cells_1field[y_ind][x_ind] != 412 and list_status_cells_1field[y_ind][x_ind] != 413 and list_status_cells_1field[y_ind][x_ind] != 421 and list_status_cells_1field[y_ind][x_ind] != 422 and list_status_cells_1field[y_ind][x_ind] != 423 and list_status_cells_1field[y_ind][x_ind] != 511 and list_status_cells_1field[y_ind][x_ind] != 512 and list_status_cells_1field[y_ind][x_ind] != 513 and list_status_cells_1field[y_ind][x_ind] != 514:
                    if list_status_cells_1field[y_ind + 2][x_ind] != 1 and list_status_cells_1field[y_ind + 3][x_ind]!= 1 and list_status_cells_1field[y_ind + 2][x_ind] != 2 and list_status_cells_1field[y_ind + 3][x_ind]!= 2 and list_status_cells_1field[y_ind + 2][x_ind] != 311 and list_status_cells_1field[y_ind + 3][x_ind]!= 311 and list_status_cells_1field[y_ind + 2][x_ind] != 312 and list_status_cells_1field[y_ind + 3][x_ind]!= 312 and list_status_cells_1field[y_ind + 2][x_ind] != 321 and list_status_cells_1field[y_ind + 3][x_ind]!= 322 and list_status_cells_1field[y_ind + 2][x_ind] != 411 and list_status_cells_1field[y_ind + 3][x_ind]!= 411 and list_status_cells_1field[y_ind + 2][x_ind] != 412 and list_status_cells_1field[y_ind + 3][x_ind]!= 412 and list_status_cells_1field[y_ind + 2][x_ind] != 413 and list_status_cells_1field[y_ind + 3][x_ind]!= 413:
                        if list_status_cells_1field[y_ind + 2][x_ind] != 421 and list_status_cells_1field[y_ind + 3][x_ind]!= 421 and list_status_cells_1field[y_ind + 2][x_ind] != 422 and list_status_cells_1field[y_ind + 3][x_ind]!= 422 and list_status_cells_1field[y_ind + 2][x_ind] != 423 and list_status_cells_1field[y_ind + 3][x_ind]!= 423:
                            if list_status_cells_1field[y_ind + 2][x_ind] != 511 and list_status_cells_1field[y_ind + 3][x_ind] != 511 and list_status_cells_1field[y_ind + 2][x_ind] != 512 and list_status_cells_1field[y_ind + 3][x_ind] != 512 and list_status_cells_1field[y_ind + 2][x_ind] != 513 and list_status_cells_1field[y_ind + 3][x_ind] != 513 and list_status_cells_1field[y_ind + 2][x_ind] != 514 and list_status_cells_1field[y_ind + 3][x_ind] != 514:
                                if list_status_cells_1field[y_ind + 2][x_ind] != 521 and list_status_cells_1field[y_ind + 3][x_ind] != 521 and list_status_cells_1field[y_ind + 2][x_ind] != 522 and list_status_cells_1field[y_ind + 3][x_ind] != 522 and list_status_cells_1field[y_ind + 2][x_ind] != 523 and list_status_cells_1field[y_ind + 3][x_ind] != 523 and list_status_cells_1field[y_ind + 2][x_ind] != 524 and list_status_cells_1field[y_ind + 3][x_ind] != 524:
                                    cord = coordinates_of_cells_1field[y_ind][x_ind]
                                    print(y_ind,x_ind)
                                    print(cord)
                                    print(ship_direction)
                                    draw_four_deck_ship_lenght(cord[0],cord[1],'up')
                                    bot_four_deck_ships += 1
                                    list_status_cells_1field[y_ind][x_ind] = 511
                                    list_status_cells_1field[y_ind+1][x_ind] = 512
                                    list_status_cells_1field[y_ind+2][x_ind] = 513
                                    list_status_cells_1field[y_ind+3][x_ind] = 514
                                    status_of_cell = 1
                                    for i in list_cord_around_cell_4deck_lenght:
                                        if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                                    for i in list_status_cells_1field:
                                        print(i)
                                    print(' ')
            elif list_status_cells_1field[y_ind][x_ind] != 1 and list_status_cells_1field[y_ind][x_ind] != 2 and list_status_cells_1field[y_ind][x_ind] != 311 and list_status_cells_1field[y_ind][x_ind] != 312 and list_status_cells_1field[y_ind][x_ind] != 321 and list_status_cells_1field[y_ind][x_ind] != 322 and list_status_cells_1field[y_ind][x_ind] != 521 and list_status_cells_1field[y_ind][x_ind] != 522 and list_status_cells_1field[y_ind][x_ind] != 523 and list_status_cells_1field[y_ind][x_ind] != 524 and ship_direction == 2 and x_ind < 7 :
                if list_status_cells_1field[y_ind][x_ind] != 411 and list_status_cells_1field[y_ind][x_ind] != 412 and list_status_cells_1field[y_ind][x_ind] != 413 and list_status_cells_1field[y_ind][x_ind] != 421 and list_status_cells_1field[y_ind][x_ind] != 422 and list_status_cells_1field[y_ind][x_ind] != 423 and list_status_cells_1field[y_ind][x_ind] != 511 and list_status_cells_1field[y_ind][x_ind] != 512 and list_status_cells_1field[y_ind][x_ind] != 513 and list_status_cells_1field[y_ind][x_ind] != 514:
                    if list_status_cells_1field[y_ind][x_ind + 2] != 1 and list_status_cells_1field[y_ind][x_ind + 3]!= 1 and list_status_cells_1field[y_ind][x_ind + 2] != 2 and list_status_cells_1field[y_ind][x_ind + 3]!= 2 and list_status_cells_1field[y_ind][x_ind + 2] != 311 and list_status_cells_1field[y_ind][x_ind + 3]!= 311 and list_status_cells_1field[y_ind][x_ind + 2] != 312 and list_status_cells_1field[y_ind][x_ind + 3]!= 312 and list_status_cells_1field[y_ind][x_ind + 2] != 321 and list_status_cells_1field[y_ind][x_ind + 3]!= 322 and list_status_cells_1field[y_ind][x_ind + 2] != 411 and list_status_cells_1field[y_ind][x_ind + 3]!= 411 and list_status_cells_1field[y_ind][x_ind + 2] != 412 and list_status_cells_1field[y_ind][x_ind + 3]!= 412 and list_status_cells_1field[y_ind][x_ind + 2] != 413 and list_status_cells_1field[y_ind][x_ind + 3]!= 413:
                        if list_status_cells_1field[y_ind][x_ind + 2] != 421 and list_status_cells_1field[y_ind][x_ind + 3]!= 421 and list_status_cells_1field[y_ind][x_ind + 2] != 422 and list_status_cells_1field[y_ind][x_ind + 3]!= 422 and list_status_cells_1field[y_ind][x_ind + 2] != 423 and list_status_cells_1field[y_ind][x_ind + 3]!= 423:
                            if list_status_cells_1field[y_ind][x_ind + 2] != 511 and list_status_cells_1field[y_ind][x_ind + 3] != 511 and list_status_cells_1field[y_ind][x_ind + 2] != 512 and list_status_cells_1field[y_ind][x_ind + 3] != 512 and list_status_cells_1field[y_ind][x_ind + 2] != 513 and list_status_cells_1field[y_ind][x_ind + 3] != 513 and list_status_cells_1field[y_ind][x_ind + 2] != 514 and list_status_cells_1field[y_ind][x_ind + 3] != 514:
                                if list_status_cells_1field[y_ind][x_ind + 2] != 521 and list_status_cells_1field[y_ind][x_ind + 3] != 521 and list_status_cells_1field[y_ind][x_ind + 2] != 522 and list_status_cells_1field[y_ind][x_ind + 3] != 522 and list_status_cells_1field[y_ind][x_ind + 2] != 523 and list_status_cells_1field[y_ind][x_ind + 3] != 523 and list_status_cells_1field[y_ind][x_ind + 2] != 524 and list_status_cells_1field[y_ind][x_ind + 3] != 524:
                                    cord = coordinates_of_cells_1field[y_ind][x_ind]
                                    print(y_ind,x_ind)
                                    print(cord)
                                    print(ship_direction)
                                    draw_four_deck_ship_width(cord[0],cord[1],'up')
                                    bot_four_deck_ships += 1
                                    list_status_cells_1field[y_ind][x_ind] = 521
                                    list_status_cells_1field[y_ind][x_ind+1] = 522
                                    list_status_cells_1field[y_ind][x_ind+2] = 523
                                    list_status_cells_1field[y_ind][x_ind+3] = 524
                                    status_of_cell = 1
                                    for i in list_cord_around_cell_4deck_width:
                                        if y_ind+i[1] >= 0 and y_ind+i[1] < len(list_status_cells_1field) and x_ind+i[0] >= 0 and x_ind+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[y_ind+i[1]][x_ind+i[0]] = 1
                                    for i in list_status_cells_1field:
                                        print(i)
                                    print(' ')

    t_draw_whos_turn.clear()
    draw_turn(-125, 270 , "Гра почалася! Ваш хід", 15)

def player_pick(x,y):
    global double_deck_hits_width
    global double_deck_hits_lenght
    global triple_deck_hits
    global four_deck_hits
    global player_turn
    global drowned_ships_player 
    global double_deck_311_hits_1
    global cords_of_311_hit_1
    global double_deck_311_hits_2
    global cords_of_311_hit_2
    global double_deck_311_hits_3
    global double_deck_312_hits_3
    global double_deck_312_hits_1
    global double_deck_312_hits_2
    global double_deck_321_hits_1
    global double_deck_322_hits_1
    global double_deck_321_hits_2
    global double_deck_322_hits_2
    global double_deck_321_hits_3
    global double_deck_322_hits_3
    global triple_deck_421_hits_1
    global triple_deck_422_hits_1
    global triple_deck_423_hits_1
    global triple_deck_411_hits_1
    global triple_deck_412_hits_1
    global triple_deck_413_hits_1
    global triple_deck_421_hits_2
    global triple_deck_422_hits_2
    global triple_deck_423_hits_2
    global triple_deck_411_hits_2
    global triple_deck_412_hits_2
    global triple_deck_413_hits_2
    global four_deck_521_hits_1
    global four_deck_522_hits_1
    global four_deck_523_hits_1
    global four_deck_524_hits_1
    global four_deck_511_hits_1
    global four_deck_512_hits_1
    global four_deck_513_hits_1
    global four_deck_514_hits_1
    global may_count_hit
    global draw_cross_permited
    global draw_dot_permited
    global may_draw_cross
    if drowned_ships_player != 10:
        print(drowned_ships_player,'-Drowned ships')
        for row_ind2 in range(len(coordinates_of_cells_1field)):
                for cell_ind2 in range(len(coordinates_of_cells_1field[row_ind2])):
                    cord2 = coordinates_of_cells_1field[row_ind2][cell_ind2]
                    if cord2[0] < x and x < cord2[0] + 30 and cord2[1] > y and y > cord2[1] - 30:
                        if list_status_cells_1field[row_ind2][cell_ind2] == 9:
                            unable_to_build_ship(-210, 230, "Ця клітинка вже зайнята, оберіть іншу", 15)
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 3:
                            unable_to_build_ship(-210, 230, "Ця клітинка вже зайнята, оберіть іншу", 15)
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 8:
                            unable_to_build_ship(-210, 230, "Ця клітинка вже зайнята, оберіть іншу", 15)
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 2 and draw_cross_permited == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            draw_cross(cord2[0],cord2[1])
                            drowned_ships_player += 1
                            surround_1_deck_ship(cord2[0],cord2[1])
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            t_draw_inability.clear()                            
                            for i in list_cord_around_cell_1deck:
                                if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                    list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                            for j in coordinates_around_cell_1deck:
                                if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                    draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                for i in list_status_cells_1field:
                                    print(i)
                                print(' ')
                            draw_dot_permited = True
                            draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 1 and draw_dot_permited == True or list_status_cells_1field[row_ind2][cell_ind2] == 0 and draw_dot_permited == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 3
                            draw_dot_permited = False
                            draw_dot(cord2[0],cord2[1])
                            t_draw_whos_turn.clear()
                            draw_turn(-50, 270 , "Хід бота", 15)
                            player_turn = 'bot'
                            time1.sleep(1)
                            if player_turn == 'bot':
                                draw_dot_permited = False
                                draw_cross_permited = False
                                if double_deck_311_hits_1 == 0 and double_deck_312_hits_1 == 0 and double_deck_311_hits_2 == 0 and double_deck_312_hits_2 == 0 and double_deck_311_hits_3 == 0 and double_deck_312_hits_3 == 0 and double_deck_321_hits_1 == 0 and double_deck_322_hits_1 == 0 and double_deck_321_hits_2 == 0 and double_deck_322_hits_2 == 0 and double_deck_321_hits_3 == 0 and double_deck_322_hits_3 == 0 and triple_deck_421_hits_1 == 0 and triple_deck_422_hits_1 == 0 and triple_deck_423_hits_1 == 0 and triple_deck_411_hits_1 == 0 and triple_deck_412_hits_1 == 0 and triple_deck_413_hits_1 == 0 and triple_deck_421_hits_2 == 0 and triple_deck_422_hits_2 == 0 and triple_deck_423_hits_2 == 0 and triple_deck_411_hits_2 == 0 and triple_deck_412_hits_2 == 0 and triple_deck_413_hits_2 == 0 and four_deck_521_hits_1 == 0 and four_deck_522_hits_1 == 0 and four_deck_523_hits_1 == 0 and four_deck_524_hits_1 == 0 and four_deck_511_hits_1 == 0 and four_deck_512_hits_1 == 0 and four_deck_513_hits_1 == 0 and four_deck_514_hits_1 == 0:
                                    bot_pick_1deck_or_empty_cell()

                                elif double_deck_311_hits_1 == 1 and cords_of_311_hit_1[2] == 1:
                                    second_bot_pick_2deckLenght_311_1()
                                elif double_deck_311_hits_1 == 1 and cords_of_311_hit_1[2] == 2:
                                    third_bot_pick_2deckLenght_311_1()
                                    double_deck_311_hits_1 = 0

                                elif double_deck_311_hits_2 == 1 and cords_of_311_hit_2[2] == 1:
                                    second_bot_pick_2deckLenght_311_2()
                                elif double_deck_311_hits_2 == 1 and cords_of_311_hit_2[2] == 2:
                                    third_bot_pick_2deckLenght_311_2()
                                    double_deck_311_hits_2 = 0


                                elif double_deck_311_hits_3 == 1 and cords_of_311_hit_3[2] == 1:
                                    second_bot_pick_2deckLenght_311_3()
                                elif double_deck_311_hits_3 == 1 and cords_of_311_hit_3[2] == 2:
                                    third_bot_pick_2deckLenght_311_3()
                                    double_deck_311_hits_3 = 0


                                elif double_deck_312_hits_1 == 1 and cords_of_312_hit_1[2] == 1:
                                    first_bot_pick_2deckLenght_312_1()
                                    double_deck_312_hits_1 = 0



                                elif double_deck_312_hits_2 == 1 and cords_of_312_hit_2[2] == 1:
                                    first_bot_pick_2deckLenght_312_2()
                                    double_deck_312_hits_2 = 0



                                elif double_deck_312_hits_3 == 1 and cords_of_312_hit_3[2] == 1:
                                    first_bot_pick_2deckLenght_312_3()
                                    double_deck_312_hits_3 = 0


                                elif double_deck_321_hits_1 == 1 and cords_of_321_hit_1[2] == 1:
                                    second_bot_pick_2deckWidth_321_1()
                                elif double_deck_321_hits_1 == 1 and cords_of_321_hit_1[2] == 2:
                                    third_bot_pick_2deckWidth_321_1()
                                    double_deck_321_hits_1 = 0
                                elif double_deck_321_hits_1 == 1 and cords_of_321_hit_1_zero_ind[2] == 1:
                                    third_bot_pick_2deckWidth_321_1()
                                    double_deck_321_hits_1 = 0

                                
                                elif double_deck_322_hits_1 == 1 and cords_of_322_hit_1[2] == 1:
                                    second_bot_pick_2deckWidth_322_1()
                                    double_deck_322_hits_1 = 0
                                elif double_deck_322_hits_1 == 1 and cords_of_322_hit_1_zero_ind[2] == 1:
                                    second_bot_pick_2deckWidth_322_1()
                                    double_deck_322_hits_1 = 0


                                elif double_deck_321_hits_2 == 1 and cords_of_321_hit_2[2] == 1:
                                    second_bot_pick_2deckWidth_321_2()
                                    double_deck_321_hits_2 = 0
                                elif double_deck_321_hits_2 == 1 and cords_of_321_hit_2[2] == 2:
                                    third_bot_pick_2deckWidth_321_2()
                                    double_deck_321_hits_2 = 0
                                elif double_deck_321_hits_2 == 1 and cords_of_321_hit_2_zero_ind[2] == 1:
                                    third_bot_pick_2deckWidth_321_2()
                                    double_deck_321_hits_2 = 0

                                
                                elif double_deck_322_hits_2 == 1 and cords_of_322_hit_2[2] == 1:
                                    second_bot_pick_2deckWidth_322_2()
                                    double_deck_322_hits_2 = 0
                                elif double_deck_322_hits_2 == 1 and cords_of_322_hit_2_zero_ind[2] == 1:
                                    second_bot_pick_2deckWidth_322_2()
                                    double_deck_322_hits_2 = 0

                                
                                elif double_deck_321_hits_3 == 1 and cords_of_321_hit_3[2] == 1:
                                    second_bot_pick_2deckWidth_321_3()
                                    double_deck_321_hits_3 = 0
                                elif double_deck_321_hits_3 == 1 and cords_of_321_hit_3[2] == 2:
                                    third_bot_pick_2deckWidth_321_3()
                                    double_deck_321_hits_3 = 0
                                elif double_deck_321_hits_3 == 1 and cords_of_321_hit_3_zero_ind[2] == 1:
                                    third_bot_pick_2deckWidth_321_3()
                                    double_deck_321_hits_3 = 0


                                elif double_deck_322_hits_3 == 1 and cords_of_322_hit_3[2] == 1:
                                    second_bot_pick_2deckWidth_322_3()
                                    double_deck_322_hits_3 = 0
                                elif double_deck_322_hits_3 == 1 and cords_of_322_hit_3_zero_ind[2] == 1:
                                    second_bot_pick_2deckWidth_322_3()
                                    double_deck_322_hits_3 = 0


                                elif triple_deck_421_hits_1 == 1 and cords_of_421_hit_1[2] == 1:
                                    second_bot_pick_3deckWidth_421_1()
                                    triple_deck_421_hits_1 = 0
                                elif triple_deck_421_hits_1 == 1 and cords_of_421_hit_1[2] == 2:
                                    third_bot_pick_3deckWidth_421_1()
                                    triple_deck_421_hits_1 = 0
                                elif triple_deck_421_hits_1 == 1 and cords_of_421_hit_1_zero_indX[2] == 1:
                                    third_bot_pick_3deckWidth_421_1()
                                    triple_deck_421_hits_1 = 0
                                elif triple_deck_421_hits_1 == 1 and cords_of_421_hit_1_zero_indY[2] == 1:
                                    third_bot_pick_3deckWidth_421_1()
                                    triple_deck_421_hits_1 = 0

                                elif triple_deck_421_hits_2 == 1 and cords_of_421_hit_2[2] == 1:
                                    second_bot_pick_3deckWidth_421_2()
                                    triple_deck_421_hits_2 = 0
                                elif triple_deck_421_hits_2 == 1 and cords_of_421_hit_2[2] == 2:
                                    third_bot_pick_3deckWidth_421_2()
                                    triple_deck_421_hits_2 = 0
                                elif triple_deck_421_hits_2 == 1 and cords_of_421_hit_2_zero_indX[2] == 1:
                                    third_bot_pick_3deckWidth_421_2()
                                    triple_deck_421_hits_2 = 0
                                elif triple_deck_421_hits_2 == 1 and cords_of_421_hit_2_zero_indY[2] == 1:
                                    third_bot_pick_3deckWidth_421_2()
                                    triple_deck_421_hits_2 = 0
                            

                                elif triple_deck_422_hits_1 == 1 and cords_of_422_hit_1[2] == 1:
                                    second_bot_pick_3deckWidth_422_1()
                                    triple_deck_422_hits_1 = 0
                                elif triple_deck_422_hits_1 == 2 and cords_of_422_hit_1[2] == 3:
                                    third_bot_pick_3deckWidth_422_1()
                                    triple_deck_422_hits_1 = 0
                                elif triple_deck_422_hits_1 == 1 and cords_of_422_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_3deckWidth_422_1_zeroX()
                                    triple_deck_422_hits_1 = 0
                                elif triple_deck_422_hits_1 == 2 and cords_of_422_hit_1_zero_indX[2] == 3:
                                    third_bot_pick_3deckWidth_422_1_zeroX()
                                    triple_deck_422_hits_1 = 0

                                elif triple_deck_422_hits_2 == 1 and cords_of_422_hit_2[2] == 1:
                                    second_bot_pick_3deckWidth_422_2()
                                    triple_deck_422_hits_2 = 0
                                elif triple_deck_422_hits_2 == 2 and cords_of_422_hit_2[2] == 3:
                                    third_bot_pick_3deckWidth_422_2()
                                    triple_deck_422_hits_2 = 0
                                elif triple_deck_422_hits_2 == 1 and cords_of_422_hit_2_zero_indX[2] == 1:
                                    second_bot_pick_3deckWidth_422_2_zeroX()
                                    triple_deck_422_hits_2 = 0
                                elif triple_deck_422_hits_2 == 2 and cords_of_422_hit_2_zero_indX[2] == 3:
                                    third_bot_pick_3deckWidth_422_2_zeroX()
                                    triple_deck_422_hits_2 = 0


                                elif triple_deck_423_hits_1 == 1 and cords_of_423_hit_1[2] == 1:
                                    second_bot_pick_3deckWidth_423_1()
                                    triple_deck_423_hits_1 = 0
                                elif triple_deck_423_hits_1 == 1 and cords_of_423_hit_1[2] == 2:
                                    third_bot_pick_3deckWidth_423_1()
                                    triple_deck_423_hits_1 = 0
                                elif triple_deck_423_hits_1 == 1 and cords_of_423_hit_1_zero_indY[2] == 1:
                                    second_bot_pick_3deckWidth_423_1_zeroY()
                                    triple_deck_423_hits_1 = 0
                                elif triple_deck_423_hits_1 == 1 and cords_of_423_hit_1_zero_indY[2] == 2:
                                    second_bot_pick_3deckWidth_423_1_zeroY()
                                    triple_deck_423_hits_1 = 0

                                elif triple_deck_423_hits_2 == 1 and cords_of_423_hit_2[2] == 1:
                                    second_bot_pick_3deckWidth_423_2()
                                    triple_deck_423_hits_2 = 0
                                elif triple_deck_423_hits_2 == 1 and cords_of_423_hit_2[2] == 2:
                                    third_bot_pick_3deckWidth_423_2()
                                    triple_deck_423_hits_2 = 0
                                elif triple_deck_423_hits_2 == 1 and cords_of_423_hit_2_zero_indY[2] == 1:
                                    second_bot_pick_3deckWidth_423_2_zeroY()
                                    triple_deck_423_hits_2 = 0
                                elif triple_deck_423_hits_2 == 1 and cords_of_423_hit_2_zero_indY[2] == 2:
                                    second_bot_pick_3deckWidth_423_2_zeroY()
                                    triple_deck_423_hits_2 = 0

                                
                                elif triple_deck_411_hits_1 == 1 and cords_of_411_hit_1[2] == 1:
                                    second_bot_pick_3deckLenght_411_1()
                                    triple_deck_411_hits_1 = 0
                                elif triple_deck_411_hits_1 == 1 and cords_of_411_hit_1[2] == 2:
                                    third_bot_pick_3deckLenght_411_1()
                                    triple_deck_411_hits_1 = 0
                                elif triple_deck_411_hits_1 == 1 and cords_of_411_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_3deckLenght_411_1_zeroX()
                                    triple_deck_411_hits_1 = 0
                                elif triple_deck_411_hits_1 == 1 and cords_of_411_hit_1_zero_indX[2] == 2:
                                    third_bot_pick_3deckLenght_411_1_zeroX()
                                    triple_deck_411_hits_1 = 0
                                elif triple_deck_411_hits_1 == 1 and cords_of_411_hit_1_zero_indY[2] == 1:
                                    second_bot_pick_3deckLenght_411_1_zeroY()
                                    triple_deck_411_hits_1 = 0

                                elif triple_deck_411_hits_2 == 1 and cords_of_411_hit_2[2] == 1:
                                    second_bot_pick_3deckLenght_411_2()
                                    triple_deck_411_hits_2 = 0
                                elif triple_deck_411_hits_2 == 1 and cords_of_411_hit_2[2] == 2:
                                    third_bot_pick_3deckLenght_411_2()
                                    triple_deck_411_hits_2 = 0
                                elif triple_deck_411_hits_2 == 1 and cords_of_411_hit_2_zero_indX[2] == 1:
                                    second_bot_pick_3deckLenght_411_2_zeroX()
                                    triple_deck_411_hits_2 = 0
                                elif triple_deck_411_hits_2 == 1 and cords_of_411_hit_2_zero_indX[2] == 2:
                                    third_bot_pick_3deckLenght_411_2_zeroX()
                                    triple_deck_411_hits_2 = 0
                                elif triple_deck_411_hits_2 == 1 and cords_of_411_hit_2_zero_indY[2] == 1:
                                    second_bot_pick_3deckLenght_411_2_zeroY()
                                    triple_deck_411_hits_2 = 0


                                elif triple_deck_412_hits_1 == 1 and cords_of_412_hit_1[2] == 1:
                                    second_bot_pick_3deckLenght_412_1()
                                    triple_deck_412_hits_1 = 0
                                elif triple_deck_412_hits_1 == 2 and cords_of_412_hit_1[2] == 3:
                                    third_bot_pick_3deckLenght_412_1()
                                    triple_deck_412_hits_1 = 0
                                elif triple_deck_412_hits_2 == 1 and cords_of_412_hit_2[2] == 1:
                                    second_bot_pick_3deckLenght_412_2()
                                    triple_deck_412_hits_2 = 0
                                elif triple_deck_412_hits_2 == 2 and cords_of_412_hit_2[2] == 3:
                                    third_bot_pick_3deckLenght_412_2()
                                    triple_deck_412_hits_2 = 0


                                elif triple_deck_413_hits_1 == 1 and cords_of_413_hit_1[2] == 1:
                                    second_bot_pick_3deckLenght_413_1()
                                    triple_deck_413_hits_1 = 0
                                elif triple_deck_413_hits_1 == 1 and cords_of_413_hit_1[2] == 2:
                                    third_bot_pick_3deckLenght_413_1()
                                    triple_deck_413_hits_1 = 0
                                elif triple_deck_413_hits_1 == 1 and cords_of_413_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_3deckLenght_413_1_zeroX()
                                    triple_deck_413_hits_1 = 0
                                elif triple_deck_413_hits_1 == 1 and cords_of_413_hit_1_zero_indX[2] == 2:
                                    third_bot_pick_3deckLenght_413_1_zeroX()
                                    triple_deck_413_hits_1 = 0

                                elif triple_deck_413_hits_2 == 1 and cords_of_413_hit_2[2] == 1:
                                    second_bot_pick_3deckLenght_413_2()
                                    triple_deck_413_hits_2 = 0
                                elif triple_deck_413_hits_2 == 1 and cords_of_413_hit_2[2] == 2:
                                    third_bot_pick_3deckLenght_413_2()
                                    triple_deck_413_hits_2 = 0
                                elif triple_deck_413_hits_2 == 1 and cords_of_413_hit_2_zero_indX[2] == 1:
                                    second_bot_pick_3deckLenght_413_2_zeroX()
                                    triple_deck_413_hits_2 = 0
                                elif triple_deck_413_hits_2 == 1 and cords_of_413_hit_2_zero_indX[2] == 2:
                                    third_bot_pick_3deckLenght_413_2_zeroX()
                                    triple_deck_413_hits_2 = 0

                                elif four_deck_521_hits_1 == 1 and cords_of_521_hit_1[2] == 1:
                                    second_bot_pick_4deckWidth_521_1()
                                    four_deck_521_hits_1 = 0
                                elif four_deck_521_hits_1 == 1 and cords_of_521_hit_1[2] == 2:
                                    third_bot_pick_4deckWidth_521_1()
                                    four_deck_521_hits_1 = 0
                                elif four_deck_521_hits_1 == 1 and cords_of_521_hit_1_zero_indX[2] == 1:
                                    third_bot_pick_4deckWidth_521_1()
                                    four_deck_521_hits_1 = 0
                                elif four_deck_521_hits_1 == 1 and cords_of_521_hit_1_zero_indY[2] == 1:
                                    third_bot_pick_4deckWidth_521_1()
                                    four_deck_521_hits_1 = 0

                                elif four_deck_522_hits_1 == 1 and cords_of_522_hit_1[2] == 1:
                                    second_bot_pick_4deckWidth_522_1()
                                    four_deck_522_hits_1 = 0
                                elif four_deck_522_hits_1 == 2 and cords_of_522_hit_1[2] == 3:
                                    third_bot_pick_4deckWidth_522_1()
                                    four_deck_522_hits_1 = 0
                                elif four_deck_522_hits_1 == 1 and cords_of_522_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_4deckWidth_522_1_zeroX()
                                    four_deck_522_hits_1 = 0
                                elif four_deck_522_hits_1 == 3 and cords_of_522_hit_1_zero_indX[2] == 4:
                                    third_bot_pick_4deckWidth_522_1_zeroX()
                                    four_deck_522_hits_1 = 0

                                elif four_deck_523_hits_1 == 1 and cords_of_523_hit_1[2] == 1:
                                    second_bot_pick_4deckWidth_523_1()
                                    four_deck_523_hits_1 = 0
                                elif four_deck_523_hits_1 == 3 and cords_of_523_hit_1[2] == 4:
                                    third_bot_pick_4deckWidth_523_1()
                                    four_deck_523_hits_1 = 0
                                elif four_deck_523_hits_1 == 1 and cords_of_523_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_4deckWidth_523_1_zeroX()
                                    four_deck_523_hits_1 = 0
                                elif four_deck_523_hits_1 == 3 and cords_of_523_hit_1_zero_indX[2] == 4:
                                    third_bot_pick_4deckWidth_523_1_zeroX()
                                    four_deck_523_hits_1 = 0

                                elif four_deck_524_hits_1 == 1 and cords_of_524_hit_1[2] == 1:
                                    second_bot_pick_4deckWidth_524_1()
                                    four_deck_524_hits_1 = 0
                                elif four_deck_524_hits_1 == 1 and cords_of_524_hit_1[2] == 2:
                                    third_bot_pick_4deckWidth_524_1()
                                    four_deck_524_hits_1 = 0
                                elif four_deck_524_hits_1 == 1 and cords_of_524_hit_1_zero_indY[2] == 1:
                                    second_bot_pick_4deckWidth_524_1_zeroY()
                                    four_deck_524_hits_1 = 0
                                elif four_deck_524_hits_1 == 1 and cords_of_524_hit_1_zero_indY[2] == 2:
                                    third_bot_pick_4deckWidth_524_1_zeroY()
                                    four_deck_524_hits_1 = 0

                                elif four_deck_511_hits_1 == 1 and cords_of_511_hit_1[2] == 1:
                                    second_bot_pick_4deckLenght_511_1()
                                    four_deck_511_hits_1 = 0
                                elif four_deck_511_hits_1 == 1 and cords_of_511_hit_1[2] == 2:
                                    third_bot_pick_4deckLenght_511_1()
                                    four_deck_511_hits_1 = 0
                                elif four_deck_511_hits_1 == 1 and cords_of_511_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_4deckLenght_511_1_zeroX()
                                    four_deck_511_hits_1 = 0
                                elif four_deck_511_hits_1 == 1 and cords_of_511_hit_1_zero_indX[2] == 2:
                                    third_bot_pick_4deckLenght_511_1_zeroX()
                                    four_deck_511_hits_1 = 0
                                elif four_deck_511_hits_1 == 1 and cords_of_511_hit_1_zero_indY[2] == 1:
                                    second_bot_pick_4deckLenght_511_1_zeroY()
                                    four_deck_511_hits_1 = 0

                                elif four_deck_512_hits_1 == 1 and cords_of_512_hit_1[2] == 1:
                                    second_bot_pick_4deckLenght_512_1()
                                    four_deck_512_hits_1 = 0
                                elif four_deck_512_hits_1 == 2 and cords_of_512_hit_1[2] == 3:
                                    third_bot_pick_4deckLenght_512_1()
                                    four_deck_512_hits_1 = 0

                                elif four_deck_513_hits_1 == 1 and cords_of_513_hit_1[2] == 1:
                                    second_bot_pick_4deckLenght_513_1()
                                    four_deck_513_hits_1 = 0
                                elif four_deck_513_hits_1 == 3 and cords_of_513_hit_1[2] == 4:
                                    third_bot_pick_4deckLenght_513_1()
                                    four_deck_513_hits_1 = 0

                                elif four_deck_514_hits_1 == 1 and cords_of_514_hit_1[2] == 1:
                                    second_bot_pick_4deckLenght_514_1()
                                    four_deck_514_hits_1 = 0
                                elif four_deck_514_hits_1 == 1 and cords_of_514_hit_1[2] == 2:
                                    third_bot_pick_4deckLenght_514_1()
                                    four_deck_514_hits_1 = 0
                                elif four_deck_514_hits_1 == 1 and cords_of_514_hit_1_zero_indX[2] == 1:
                                    second_bot_pick_4deckLenght_514_1_zeroX()
                                    four_deck_514_hits_1 = 0
                                elif four_deck_514_hits_1 == 1 and cords_of_514_hit_1_zero_indX[2] == 2:
                                    third_bot_pick_4deckLenght_514_1_zeroX()
                                    four_deck_514_hits_1 = 0



                            t_draw_inability.clear()

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 321 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_double_deck_ship_width_1[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_1[2] += 1
                                    may_count_hit = False
                                    if cords_of_double_deck_ship_width_1[2] == 2 :
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_width_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_width_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True

                            elif cords_of_double_deck_ship_width_2[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_2[2] += 1
                                    may_count_hit = False
                                    print(cords_of_double_deck_ship_width_2[2])
                                    if cords_of_double_deck_ship_width_2[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_width_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_2deck_width_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                            elif cords_of_double_deck_ship_width_3[0] == [cord2[0],cord2[1]] and draw_cross_permited == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_3[2] += 1
                                    may_count_hit = False
                                    print(cords_of_double_deck_ship_width_3[2])
                                    if cords_of_double_deck_ship_width_3[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_width_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_width_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 322 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_double_deck_ship_width_1[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                print('111111111111111111')
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_1[2] += 1
                                    may_count_hit = False
                                    print(cords_of_double_deck_ship_width_1[2])
                                    if cords_of_double_deck_ship_width_1[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0]-30,cord2[1])
                                        for i in list_cord_around_cell_2deck_width_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):                          
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_width_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])     
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                            elif cords_of_double_deck_ship_width_2[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                print('2222222222222222')
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_2[2] += 1
                                    may_count_hit = False
                                    print(cords_of_double_deck_ship_width_2[2])
                                    if cords_of_double_deck_ship_width_2[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0]-30,cord2[1])
                                        for i in list_cord_around_cell_2deck_width_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_width_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])     
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                            elif cords_of_double_deck_ship_width_3[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                print('333333333333333333')
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_width_3[2] += 1
                                    may_count_hit = False
                                    print(cords_of_double_deck_ship_width_3[2])
                                    list_status_cells_1field[row_ind2][cell_ind2] = 8
                                    if cords_of_double_deck_ship_width_3[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_width(cord2[0]-30,cord2[1])
                                        for i in list_cord_around_cell_2deck_width_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_width_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                print(row_ind2+i[1],cell_ind2+i[0])     
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 311 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8 
                            if cords_of_double_deck_ship_lenght_1[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_1[2] += 1
                                    may_count_hit = False
                                    if cords_of_double_deck_ship_lenght_1[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_double_deck_ship_lenght_2[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_2[2] += 1
                                    may_count_hit = False
                                    list_status_cells_1field[row_ind2][cell_ind2] = 8
                                    if cords_of_double_deck_ship_lenght_2[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_double_deck_ship_lenght_3[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_3[2] += 1
                                    may_count_hit = False
                                    list_status_cells_1field[row_ind2][cell_ind2] = 8
                                    if cords_of_double_deck_ship_lenght_3[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_2deck_lenght_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8
                                        for j in coordinates_around_cell_2deck_lenght_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 312 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8                                  
                            if cords_of_double_deck_ship_lenght_1[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_1[2] += 1
                                    may_count_hit = False
                                    if cords_of_double_deck_ship_lenght_1[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1]+30)
                                        for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8           
                                        for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                 
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_double_deck_ship_lenght_2[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_2[2] += 1
                                    may_count_hit = False
                                    if cords_of_double_deck_ship_lenght_2[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1]+30)
                                        for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9    
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8    
                                        for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                 
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_double_deck_ship_lenght_3[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_double_deck_ship_lenght_3[2] += 1
                                    may_count_hit = False
                                    if cords_of_double_deck_ship_lenght_3[2] == 2:
                                        drowned_ships_player += 1
                                        surround_2_deck_ship_lenght(cord2[0],cord2[1]+30)
                                        for i in list_cord_around_cell_2deck_lenght_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9     
                                                list_status_cells_1field[row_ind2][cell_ind2] = 8    
                                        for j in coordinates_around_cell_2deck_lenght_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                 
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 421 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_width_1[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_1[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_3deck_width_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                           
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                                    
                            elif cords_of_triple_deck_ship_width_2[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_2[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_3deck_width_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                           
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 422 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_width_1[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_1[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0]-30,cord2[1])
                                        for i in list_cord_around_cell_3deck_width_mid:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_mid:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                               
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_triple_deck_ship_width_2[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_2[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0]-30,cord2[1])
                                        for i in list_cord_around_cell_3deck_width_mid:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_mid:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                                               
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 423 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_width_1[2] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_1[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0]-60,cord2[1])
                                        for i in list_cord_around_cell_3deck_width_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_triple_deck_ship_width_2[2] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_width_2[3] += 1
                                    may_count_hit = False
                                    if cords_of_triple_deck_ship_width_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_width(cord2[0]-60,cord2[1])
                                        for i in list_cord_around_cell_3deck_width_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_width_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
        
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 411 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_lenght_1[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_1[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_1)
                                    if cords_of_triple_deck_ship_lenght_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_3deck_lenght_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_triple_deck_ship_lenght_2[0] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_2[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_2)
                                    if cords_of_triple_deck_ship_lenght_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1])
                                        for i in list_cord_around_cell_3deck_lenght_left_to_right:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_right_to_left:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 412 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_lenght_1[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_1[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_1)
                                    if cords_of_triple_deck_ship_lenght_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1]+30)
                                        for i in list_cord_around_cell_3deck_lenght_mid:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_mid:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_triple_deck_ship_lenght_2[1] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_2[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_2)
                                    if cords_of_triple_deck_ship_lenght_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1]+30)
                                        for i in list_cord_around_cell_3deck_lenght_mid:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_mid:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 413 and draw_cross_permited == True and may_draw_cross == True:
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            if cords_of_triple_deck_ship_lenght_1[2] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_1[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_1)
                                    if cords_of_triple_deck_ship_lenght_1[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1]+60)
                                        for i in list_cord_around_cell_3deck_lenght_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                 
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True
                            elif cords_of_triple_deck_ship_lenght_2[2] == [cord2[0],cord2[1]] and draw_cross_permited == True and may_draw_cross == True:
                                draw_cross_permited = False
                                draw_dot_permited = False
                                may_draw_cross = False
                                draw_cross(cord2[0],cord2[1])
                                t_draw_inability.clear()
                                if may_count_hit == True:
                                    cords_of_triple_deck_ship_lenght_2[3] += 1
                                    may_count_hit = False
                                    print(cords_of_triple_deck_ship_lenght_2)
                                    if cords_of_triple_deck_ship_lenght_2[3] == 3:
                                        drowned_ships_player += 1
                                        surround_3_deck_ship_lenght(cord2[0],cord2[1]+60)
                                        for i in list_cord_around_cell_3deck_lenght_right_to_left:
                                            if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                                list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                        for j in coordinates_around_cell_3deck_lenght_left_to_right:
                                            if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                                draw_dot(cord2[0]+j[0],cord2[1]+j[1])                 
                                                for i in list_status_cells_1field:
                                                    print(i)
                                                print(' ')
                                    may_count_hit = True
                                    may_draw_cross = True
                                    draw_dot_permited = True
                                    draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 521 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_width(cord2[0],cord2[1])
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_width_right_to_left:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_width_right_to_left:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 522 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_width(cord2[0]-30,cord2[1])
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_width_mid_left:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_width_mid_left:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ') 
                                may_count_hit = True  
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True
                        
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 523 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_width(cord2[0]-60,cord2[1])
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_width_mid_right:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_width_mid_right:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 524 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_width(cord2[0]-90,cord2[1])
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_width_left_to_right:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_width_left_to_right:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True
                        ####
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 511 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_lenght(cord2[0],cord2[1])
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_lenght_left_to_right:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_lenght_right_to_left:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 512 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_lenght(cord2[0],cord2[1]+30)
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_lenght_mid_left:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_lenght_mid_left:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True
                        
                        elif list_status_cells_1field[row_ind2][cell_ind2] == 513 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_lenght(cord2[0],cord2[1]+60)
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_lenght_mid_right:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_lenght_mid_right:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True

                        elif list_status_cells_1field[row_ind2][cell_ind2] == 514 and draw_cross_permited == True and may_draw_cross == True:
                            draw_cross_permited = False
                            draw_dot_permited = False
                            may_draw_cross = False
                            t_draw_inability.clear()
                            list_status_cells_1field[row_ind2][cell_ind2] = 8
                            draw_cross(cord2[0],cord2[1])
                            if may_count_hit == True:
                                four_deck_hits += 1
                                may_count_hit = False
                                if four_deck_hits == 4:
                                    four_deck_hits = 0
                                    surround_4_deck_ship_lenght(cord2[0],cord2[1]+90)
                                    drowned_ships_player += 1
                                    for i in list_cord_around_cell_4deck_lenght_right_to_left:
                                        if row_ind2+i[1] >= 0 and row_ind2+i[1] < len(list_status_cells_1field) and cell_ind2+i[0] >= 0 and cell_ind2+i[0] < len(list_status_cells_1field):
                                            list_status_cells_1field[row_ind2+i[1]][cell_ind2+i[0]] = 9
                                    for j in coordinates_around_cell_4deck_lenght_left_to_right:
                                        if cord2[0]+j[0] >= 80 and cord2[0]+j[0] <= 350 and cord2[1]+j[1] <= 150 and cord2[1]+j[1] >= -120:
                                            draw_dot(cord2[0]+j[0],cord2[1]+j[1])    
                                            for i in list_status_cells_1field:
                                                print(i)
                                            print(' ')
                                may_count_hit = True
                                may_draw_cross = True
                                draw_dot_permited = True
                                draw_cross_permited = True
    if drowned_ships_player == 10:
        t_draw_whos_turn.clear()
        t_draw_inability.clear()
        draw_victory(-120, 270 , "Перемога Гравця!", 20, 'goldenrod')
    

t.onscreenclick(player_move)


t.done()
