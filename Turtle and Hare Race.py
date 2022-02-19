#### ---- SETUP ---- ####

# --- Libraries --- #
import random
import pygame
pygame.init()


# --- Input --- #

print("Only repeated testing will once and for all answer the age-old question: will slow and steady REALLY win the race? ")
pygame.time.wait(1000)
winner = input("Who do you think will win? turtle/hare/tie ")


# --- Window --- #

window = pygame.display.set_mode([800, 300])


# --- Animation objects --- #

track = pygame.Rect(0, 50, 800, 200)
tort = pygame.Rect(0, 85, 50, 30)
hare = pygame.Rect(0, 185, 50, 30)


#### ---- MAIN LOOP ---- ####

animating = True
while tort.x < 750 and hare.x < 750 and animating:

    # --- Event loop --- #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
            animating = False


    # --- Move racers --- #

    tort.x += 10
    hare.x += random.randint(0, 20)
    window.fill((0, 180, 0))
    pygame.draw.rect(window, (200, 180, 120), track)


    # --- Draw characters --- #

    pygame.draw.ellipse(window, (20, 140, 10), tort)
    pygame.draw.ellipse(window, (200, 200, 200), hare)


    # --- Finish drawing --- #

    pygame.display.flip()
    pygame.time.wait(40)


#### ---- AFTER LOOP ---- ####

pygame.time.wait(1000)
if hare.x > tort.x:
    print("The hare won! ")
    if winner == "hare":
        print("You guessed it right! ")
    else:
        print("Sorry, you guessed it incorrectly. ")
elif tort.x > hare.x:
    print("The tortoise won! ")
    if winner == "tortoise":
        print("You guessed it right! ")
    else:
        print("Sorry, you guessed it incorrectly. ")
else:
    print("It was a tie! ")
    if winner == "tie":
        print("You guessed it right! ")
    else:
        print("Sorry, you guessed it incorrectly. ")
