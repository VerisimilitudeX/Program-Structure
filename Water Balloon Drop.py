#### ---- SETUP ---- ####

# --- Libraries & window --- #
import random
import pygame
pygame.init()
window = pygame.display.set_mode([800, 600])

# --- Animation variables --- #
ball_x = 0
ball_y = 0
targ_x = random.randint(100, 700)
targ_y = random.randint(100, 500)

#### ---- DRAW TARGET ---- ####

# --- Background --- #
window.fill((255, 255, 255))

# --- Target --- #
pygame.draw.circle(window, (255, 0, 0), (targ_x, targ_y), 75)
pygame.draw.circle(window, (255, 255, 255), (targ_x, targ_y), 50)
pygame.draw.circle(window, (255, 0, 0), (targ_x, targ_y), 25)


# --- Finish --- #
pygame.display.flip()

#### ---- USER GUESS ---- ####
x_speed = int(input("What is your horizontal speed guess? [1-10] "))
y_speed = int(input("What is your vertical speed guess? [1-10] "))

#### ---- MAIN LOOP ---- ####
animating = True
while ball_x < 800 and ball_y < 600 and animating:
    
    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False

    # --- Move ball --- #
    ball_x += x_speed
    ball_y += y_speed

    # --- Re-draw background --- #
    window.fill((255, 255, 255))

    # --- Re-draw target --- #
    pygame.draw.circle(window, (255, 0, 0), (targ_x, targ_y), 75)
    pygame.draw.circle(window, (255, 255, 255), (targ_x, targ_y), 50)
    pygame.draw.circle(window, (255, 0, 0), (targ_x, targ_y), 25)

    # --- Draw ball --- #
    pygame.draw.circle(window, (0, 0, 255), (int(ball_x), int(ball_y)), 25)

    # --- Finish drawing --- #
    pygame.display.flip()
    pygame.time.wait(15)
