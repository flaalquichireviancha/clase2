import pygame
import random
import sys
import os

pygame.init()
WIDTH, HEIGHT = 900, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run Adventure")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 24)

# Colors
BG_COLOR = (135, 206, 235)
BROWN = (120, 80, 40)
RED = (220, 60, 60)
WHITE = (255, 255, 255)

# Load sprites
DINO_NORMAL_IMG = pygame.image.load(os.path.join("imagenes", "Dino Normal.png")).convert_alpha()
DINO_DUCK_IMG = pygame.image.load(os.path.join("imagenes", "Dino Dunk.png")).convert_alpha()
CACTUS_IMG = pygame.image.load(os.path.join("imagenes", "Cactus.png")).convert_alpha()
ROCK_IMG = pygame.image.load(os.path.join("imagenes", "Roca.png")).convert_alpha()
BIRD_IMG = pygame.image.load(os.path.join("imagenes", "Pajaro.png")).convert_alpha()

# Scale sprites to expected sizes
DINO_NORMAL_IMG = pygame.transform.scale(DINO_NORMAL_IMG, (60, 80))
DINO_DUCK_IMG = pygame.transform.scale(DINO_DUCK_IMG, (60, 40))
CACTUS_IMG = pygame.transform.scale(CACTUS_IMG, (30, 60))
ROCK_IMG = pygame.transform.scale(ROCK_IMG, (40, 40))
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (50, 30))


def run_game():
    # Dino settings
    dino_img = DINO_NORMAL_IMG
    dino = pygame.Rect(80, HEIGHT - 120, 60, 80)
    dino_vel_y = 0
    gravity = 0.8
    jump_strength = -15
    on_ground = True
    is_ducking = False

    # Ground
    ground_y = HEIGHT - 40

    # Obstacles and birds
    obstacles = []   # list of (rect, image)
    birds = []       # list of rects
    spawn_timer = 0
    spawn_delay = 90

    # Score
    score = 0
    speed = 6

    running = True
    while running:
        clock.tick(60)
        screen.fill(BG_COLOR)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed() 

        # Jump
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:
            dino_vel_y = jump_strength
            on_ground = False

        # Duck
        if keys[pygame.K_DOWN] and on_ground:
            if not is_ducking:
                dino_img = DINO_DUCK_IMG
                dino.height = 40
                dino.y += 40
                is_ducking = True
        else:
            if is_ducking:
                dino_img = DINO_NORMAL_IMG
                dino.y -= 40
                dino.height = 80
                is_ducking = False

        # Dino physics
        dino_vel_y += gravity
        dino.y += dino_vel_y

        if dino.bottom >= ground_y:
            dino.bottom = ground_y
            dino_vel_y = 0
            on_ground = True

        # Spawn obstacles and birds
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            choice = random.choice(["cactus", "rock", "bird"])

            if choice == "cactus":
                rect = pygame.Rect(WIDTH + 20, ground_y - 60, 30, 60)
                obstacles.append((rect, CACTUS_IMG))

            elif choice == "rock":
                rect = pygame.Rect(WIDTH + 20, ground_y - 40, 40, 40)
                obstacles.append((rect, ROCK_IMG))

            else:
                # Pájaros a altura que obliga a agacharse
                y = random.choice([ground_y - 80, ground_y - 90])
                bird = pygame.Rect(WIDTH + 20, y, 50, 30)
                birds.append(bird)

            spawn_timer = 0
            if spawn_delay > 50:
                spawn_delay -= 1

        # Move obstacles
        for rect, img in obstacles[:]:
            rect.x -= speed
            if rect.right < 0:
                obstacles.remove((rect, img))
                score += 1

        # Move birds
        for bird in birds[:]:
            bird.x -= speed + 2
            if bird.right < 0:
                birds.remove(bird)
                score += 2

        # Collision
        for rect, img in obstacles:
            if dino.colliderect(rect):
                running = False

        for bird in birds:
            if dino.colliderect(bird):
                running = False

        # Increase speed
        speed = 6 + score // 20

        # Draw ground
        pygame.draw.rect(screen, BROWN, (0, ground_y, WIDTH, 40))

        # Draw dino sprite
        screen.blit(dino_img, (dino.x, dino.y))

        # Draw obstacles
        for rect, img in obstacles:
            screen.blit(img, (rect.x, rect.y))

        # Draw birds
        for bird in birds:
            screen.blit(BIRD_IMG, (bird.x, bird.y))

        # UI
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    # Game Over screen
    while True:
        screen.fill(BG_COLOR)
        over_text = FONT.render("GAME OVER", True, RED)
        score_text = FONT.render(f"Final Score: {score}", True, WHITE)
        restart_text = FONT.render("Press R to Restart", True, WHITE)

        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(score_text, (WIDTH // 2 - 110, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - 130, HEIGHT // 2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return


# Main loop
while True:
    run_game()

