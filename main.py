# 1. Set working directory
import os
os.chdir("e:\Artin_sahand\Spinner-20241130T144346Z-001\Spinner")
# 2. Import pygame
import pygame
# 3. initialize pygame
pygame.init()
# 4. Set the screen mode
size = (512, 512)
screen = pygame.display.set_mode((size))
# 5. Set the title
pygame.display.set_caption("Spinner")
# 6. Load the spinner image
spinner_image = pygame.image.load("spinner.jpg")
# 7. Fit the spinner to 80% of the screen
spinner_image = pygame.transform.scale(spinner_image, (int(size[0]*0.8), int(size[1] *0.8)))
# 8. Get the rect of the fidget spinner image
# get_rect() returns the specified rectangular area of a given picture as a new Picture object.
spinner_rect = spinner_image.get_rect()
print(spinner_rect)

# 9. Center the rect on the center of screen
spinner_rect.center = (size[0]//2, size[1]//2)
print(spinner_rect)
# 13. Set the spin angle
spin_angle = 0

# 10. Set the spin speed
spin_speed = 15
# 19. Creates a new Clock object that can be used to track an amount of time.
clock =pygame.time.Clock()
fbs =  60
# 21. Add background music
from pygame import mixer
mixer.music.load("Leila Forouhar - Nafasam.mp3")
mixer.music.play(-1)
# 16. Set the font and size for the message
font = pygame.font.Font("freesansbold.ttf", 30)
# 11. Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            spin_speed = 15

        # Left click = 1, Middle click = 2, Right click = 3, Mouse wheel up = 4, Mouse wheel down = 5

    # 12. Set screen color
    screen.fill((255, 255, 255))
    # 14. Rotate the fidget spinner
    spin_angle += spin_speed
    rotated_image = pygame.transform.rotate(spinner_image, spin_angle)
    rotated_rect = rotated_image.get_rect(center = spinner_rect.center)
    # 15. Draw the fidget spinner
    screen.blit(rotated_image, rotated_rect)
    # 17. If fidget spinner stops, Render the message "tap on screen to spin"
    if spin_speed <= 0:
        message = font.render("Tap on screen to spin", True, (0, 0, 0))
        message_rect = message.get_rect(center = (size[0]//2, size[1]//2))
        screen.blit(message , message_rect)
    else:
        spin_speed -= 0.01
        
    # 18. Update the display
    pygame.display.flip()
    # 20. Limit to 60 frames per second
    clock.tick(fbs)
# 22. Exit pygame
    