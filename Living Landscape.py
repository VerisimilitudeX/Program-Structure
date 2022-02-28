#### ---- SET UP ---- ####

# Set up libraries
import pygame
pygame.init()

# Open window
window = pygame.display.set_mode([800, 600])

# Animation variables
sun_pos = -10
green = 200
blue = 250
color_max = 200

#### ---- MAIN LOOP ---- ####

# Main animation loop
done = False
while not done:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Calculate the current sun position
    sun_pos += 1
    if sun_pos > 1000:
        sun_pos = -200

    # Calculate the current sky color values
    if sun_pos < 100:
        green += 1
        blue += 1
    elif sun_pos > 700:
        green -= 1
        blue -= 1

    # Control the max and min of the sky color
    if green > 200:
        green = 200
    elif green < 0:
        green = 0
    if blue > 250:
        blue = 250
    elif blue < 50:
        blue = 50

    # Create final sky color
    sky_color = (0, green, blue)

    # Draw background layers
    window.fill(sky_color)
    pygame.draw.circle(window, (100, 250, 100), (100, 800), 600)
    pygame.draw.circle(window, (200, 250, 200), (600, 800), 600)
    pygame.draw.circle(window, (50, 150, 50), (300, 1100), 800)

    # Draw tree trunks
    trunk = pygame.Rect(300, 400, 20, 80)
    pygame.draw.rect(window, (145, 100, 0), trunk)
    trunk = pygame.Rect(100, 450, 20, 80)
    pygame.draw.rect(window, (145, 100, 0), trunk)
    trunk = pygame.Rect(700, 435, 20, 80)
    pygame.draw.rect(window, (145, 100, 0), trunk)

    # Draw tree leaves
    leaves = pygame.Rect(270, 360, 80, 90)
    pygame.draw.ellipse(window, (0, 255, 0), leaves)
    leaves = pygame.Rect(60, 410, 100, 100)
    pygame.draw.ellipse(window, (0, 255, 0), leaves)
    leaves = pygame.Rect(670, 390, 80, 100)
    pygame.draw.ellipse(window, (0, 255, 0), leaves)

    # Draw sun
    pygame.draw.circle(window, (255, 255, 0), (sun_pos, 50), 40)

    # Finish drawing
    pygame.time.wait(10)
    pygame.display.flip()
