import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()
running = True

# === Field Drawing ===
def draw_football_field(surface):
    surface.fill((0, 100, 0))
    pygame.draw.rect(surface, (255, 255, 255), (250, 50, 1000, 700), 10)
    for i in range(0, 700, 150):
        pygame.draw.line(surface, (255, 255, 255), (250, 50 + i), (1250, 50 + i), 2)

# === Offensive Positions ===
positions = [
    # O-Line
    ((750, 660), 14, 6),  # C
    ((720, 662), 14, 6),  # LG
    ((780, 662), 14, 6),  # RG
    ((810, 664), 14, 6),  # RT
    ((690, 664), 14, 6),  # LT
    # Backfield
    ((750, 730), 14, 6),  # QB
    ((710, 730), 14, 6),  # RB
    # Reiciver
    ((400, 664), 14, 6),  # X
    ((1100, 664), 14, 6),  # Z
    ((545, 675), 14, 6),  # H
    ((840, 675), 14, 6)   # Y
]

# === Nickel Defense ===
nickel_defense = [
    # D-Line
    ((850, 630), 14, 6),  # LE
    ((790, 630), 14, 6),  # DT
    ((735, 630), 14, 6),  # DT
    ((675, 630), 14, 6),  # RE
    # Linebackers
    ((700, 580), 14, 6),  # MLB
    ((810, 580), 14, 6),  # MLB
    # Secondary
    ((550, 600), 14, 6),  # NB
    ((920, 620), 14, 6),  # SS
    ((1100, 530), 14, 6), # CB
    ((400, 530), 14, 6),  # CB
    ((750, 480), 14, 6)   # FS
]

# === 4-3 Defense ===
four_three_defense = [
    # D-Line
    ((850, 630), 14, 6),  # LE
    ((790, 630), 14, 6),  # DT
    ((735, 630), 14, 6),  # DT
    ((675, 630), 14, 6),  # RE
    # Linebackers
    ((680, 580), 14, 6),  # ROLB
    ((760, 580), 14, 6),  # MLB
    ((840, 580), 14, 6),  # LOLB
    # Secondary
    ((550, 600), 14, 6),  # SS
    ((1100, 530), 14, 6), # CB
    ((400, 530), 14, 6),  # CB
    ((750, 480), 14, 6)   # FS
]

# === Routes Storage ===
routes = [[] for _ in positions]
drawing_route = False
current_route = []
selected_player = None

# === Draw Players ===
def draw_players():
    font = pygame.font.Font(None, 36)
    pygame.draw.rect(screen, (0, 128, 255), (1300, 120, 100, 50))
    screen.blit(font.render("Nickel", True, (255, 255, 255)), (1310, 130))
    pygame.draw.rect(screen, (0, 128, 255), (1300, 200, 100, 50))
    screen.blit(font.render("4-3", True, (255, 255, 255)), (1320, 210))

    for pos, radius, width in positions:
        pygame.draw.circle(screen, (0, 0, 0), pos, radius, width)

def draw_defense(defense):
    for pos, radius, width in defense:
        pygame.draw.circle(screen, (200, 0, 0), pos, radius, width)

def draw_routes():
    for i, route in enumerate(routes):
        if not route:
            continue
        start = positions[i][0]
        points = [start] + route
        pygame.draw.lines(screen, (0, 0, 255), False, points, 3)
        for pt in route:
            pygame.draw.circle(screen, (0, 0, 255), pt, 5)

# === Game State ===
show_nickel = False
show_four_three = False
dragging = False
drag_index = None

# === Main Game Loop ===
while running:
    screen.fill((0, 0, 0))
    draw_football_field(screen)
    draw_players()
    draw_routes()

    if show_nickel:
        draw_defense(nickel_defense)
    elif show_four_three:
        draw_defense(four_three_defense)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Defense buttons
            if pygame.Rect(1300, 120, 100, 50).collidepoint(event.pos):
                show_nickel = True
                show_four_three = False

            elif pygame.Rect(1300, 200, 100, 50).collidepoint(event.pos):
                show_four_three = True
                show_nickel = False

            elif event.button == 1:  # Left click
                if drawing_route and selected_player is not None:
                    current_route.append((x, y))
                else:
                    for i, (pos, radius, width) in enumerate(positions):
                        dx, dy = x - pos[0], y - pos[1]
                        if (dx**2 + dy**2)**0.5 <= radius:
                            dragging = True
                            drag_index = i
                            break

            elif event.button == 3:  # Right click
                if not drawing_route:
                    for i, (pos, radius, width) in enumerate(positions):
                        dx, dy = x - pos[0], y - pos[1]
                        if (dx**2 + dy**2)**0.5 <= radius:
                            drawing_route = True
                            selected_player = i
                            current_route = [pos]
                            break
                else:
                    if selected_player is not None:
                        routes[selected_player] = current_route[:]
                    drawing_route = False
                    selected_player = None
                    current_route = []

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                drag_index = None

        elif event.type == pygame.MOUSEMOTION:
            if dragging and drag_index is not None:
                x, y = event.pos
                _, radius, width = positions[drag_index]
                positions[drag_index] = ((x, y), radius, width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
