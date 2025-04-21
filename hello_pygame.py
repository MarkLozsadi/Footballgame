import pygame

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create window: width × height
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mark's Football game!")
    
    footballField = pygame.image.load("images/footballField.png").convert()
    footballField = pygame.transform.scale(footballField, (800,600))
    p1 = pygame.image.load("images/Ronaldo.png").convert_alpha()
    p1 = pygame.transform.scale(p1, (80,80))
    p2 = pygame.image.load("images/Messi.png").convert_alpha()
    p2 = pygame.transform.scale(p2,(80,80))
   
    p1_x = 100
    p1_y = 100
    p2_x = 400
    p2_y = 400
    p1_cx = p1.get_rect().center[0]
    p1_cy = p1.get_rect().center[1]
    p2_cx = p2.get_rect().center[0]
    p2_cy = p2.get_rect().center[1]

    # Main loop control flag
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    p1_x += 10
                elif event.key == pygame.K_LEFT:
                    p1_x -= 10
                elif event.key == pygame.K_UP:
                    p1_y -= 10
                elif event.key == pygame.K_DOWN:
                    p1_y += 10
        
        
        screen.blit(footballField, (0,0))  
        p1_center = ((p1_x + p1_cx), (p1_y + p1_cy))
        update_sprite(footballField, p1, p1_center, 45, )
        footballField.blit(p2, (p2_x, p2_y))    


        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()


def update_sprite(target_surf, image_surf, center_pos, angle):
    """
    Rotate image_surf by angle about its center, then blit it so that
    its center is at center_pos on target_surf.
    """
    # Rotate the image.
    rotated_image = pygame.transform.rotate(image_surf, angle)
    # Build a rect with the same center as where we want it on screen.
    new_rect = rotated_image.get_rect(center=center_pos)
    # Blit to screen.
    target_surf.blit(rotated_image, new_rect)


if __name__ == "__main__":
    main()
