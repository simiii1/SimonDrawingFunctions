import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Functions Example")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Función para dibujar una estrella
def draw_star(surface, color, position, size, points=5):
    x, y = position
    outer_radius = size
    inner_radius = size // 2
    angle = math.pi / points
    
    points_list = []
    for i in range(2 * points):
        radius = outer_radius if i % 2 == 0 else inner_radius
        current_angle = i * angle - math.pi / 2
        px = x + radius * math.cos(current_angle)
        py = y + radius * math.sin(current_angle)
        points_list.append((px, py))
    
    pygame.draw.polygon(surface, color, points_list)

# Función principal
def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Limpiar pantalla
        screen.fill(WHITE)
        
        # Dibujar formas básicas
        pygame.draw.line(screen, BLACK, (50, 50), (200, 50), 3)
        pygame.draw.rect(screen, RED, (50, 100, 150, 100), 2)
        pygame.draw.circle(screen, BLUE, (125, 300), 50)
        pygame.draw.ellipse(screen, GREEN, (50, 400, 150, 80), 0)
        pygame.draw.polygon(screen, YELLOW, [(300, 50), (350, 150), (250, 150)])
        
        # Dibujar arco
        pygame.draw.arc(screen, PURPLE, (300, 200, 150, 100), 0, math.pi, 3)
        
        # Dibujar estrella personalizada
        draw_star(screen, BLACK, (375, 400), 50, 7)
        
        # Dibujar texto
        font = pygame.font.SysFont('Arial', 24)
        text = font.render("Ejemplo de Funciones de Dibujo", True, BLACK)
        screen.blit(text, (250, 500))
        
        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()