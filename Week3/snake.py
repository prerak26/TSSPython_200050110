import pygame, sys, time, random

#initial game variables
score = 0

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
new_direction = direction

#Parameters for food
food_pos = [random.randrange(1,int(frame_size_x/10))*10,random.randrange(1,int(frame_size_y/10))*10]
food_present = False

check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors

# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    global direction
    global new_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                new_direction = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                new_direction = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                new_direction = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                new_direction = 'RIGHT'
    
    #to check that it doesn't change direction abruptly
    if new_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if new_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if new_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if new_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    












def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    global score
    global food_present
    # Code for making the snake move in the expected direction
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10







    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1] :
        score = score + 1
        food_present = False
    else:
        snake_body.pop()





    # End the game if the snake collides with the wall or with itself. 
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()






def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_present
    global food_pos
    
    if not food_present:
        food_pos = [random.randrange(1,frame_size_x//10)*10,random.randrange(1,frame_size_y//10)*10]
        print(food_pos)
    food_present=True


def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if pos == 1:
        score_rect.midtop = (int(frame_size_x/10), 15)
    else:
        score_rect.midtop = (int(frame_size_x/2), int(frame_size_y/1.25))
    game_window.blit(score_surface, score_rect)





def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    for pos in snake_body:
        # Snake body
        pygame.draw.rect(game_window, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    show_score(1, (255,255,255), 'arial', 20)
    pygame.draw.rect(game_window,(255,255,255), pygame.Rect(food_pos[0], food_pos[1], 10, 10))




def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, (255,0,0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (int(frame_size_x/2), int(frame_size_y/4))
    game_window.fill((0,0,0))
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0,(255,0,0), 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()






# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    update_snake()
    create_food()
    game_window.fill((0,0,0))
    update_screen()
    pygame.display.update()
    # To set the speed of the screen
    fps_controller.tick(25)
    
create_food()