import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

# === Field Drawing ===
def draw_football_field(surface):
    surface.fill((0, 100, 0))
    pygame.draw.rect(surface, (255, 255, 255), (250, 50, 1000, 1000), 10)
    for i in range(0, 700, 150):
        pygame.draw.line(surface, (255, 255, 255), (250, 50 + i), (1250, 50 + i), 2)

# === Offensive Positions ===
positions = [
    # O-Line
    ((750, 660), 0, 0),  # C
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

shotgun = [
    # Backfield
    ((750, 730), 14, 6),  # QB
    ((710, 730), 14, 6),  # RB
]

pistol = [
    # Backfield
    ((750, 720), 14, 6),  # QB
    ((750, 760), 14, 6),  # RB
]

singleback = [
    # Backfield
    ((750, 690), 14, 6),  # QB
    ((750, 750), 14, 6),  # RB
]

ten_pers = [
    #Reiciver
    ((400, 664), 14, 6),  # X
    ((1100, 664), 14, 6),  # Z
    ((545, 675), 14, 6),  # H
    ((955, 675), 14, 6)   # Y
]

eleven_pers = [
    #Reiciver
    ((400, 664), 14, 6),  # X
    ((1100, 664), 14, 6),  # Z
    ((545, 675), 14, 6),  # H
    ((840, 675), 14, 6)   # Y
]

twelve_pers = [
    #Reiciver
    ((400, 664), 14, 6),  # X
    ((1100, 664), 14, 6),  # Z
    ((660, 675), 14, 6),  # H
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

# === 3-4 Defense ===
three_four_defense = [
    # D-Line
    ((805, 630), 14, 6),  # LE
    ((760, 630), 14, 6),  # DT
    ((720, 630), 14, 6),  # RE
    # Linebackers
    ((675, 630), 14, 6),  # ROLB
    ((700, 580), 14, 6),  # MLB
    ((810, 580), 14, 6),  # MLB
    ((850, 630), 14, 6),  # LOLB
    # Secondary
    ((550, 600), 14, 6),  # SS
    ((1100, 530), 14, 6), # CB
    ((400, 530), 14, 6),  # CB
    ((750, 480), 14, 6)   # FS
]

# === 4-4 Defense ===
four_four_defense = [
    # D-Line
    ((810, 630), 14, 6),  # LE
    ((770, 630), 14, 6),  # DT
    ((730, 630), 14, 6),  # DT
    ((690, 630), 14, 6),  # RE
    # Linebackers
    ((650, 630), 14, 6),  # ROLB
    ((700, 580), 14, 6),  # MLB
    ((810, 580), 14, 6),  # MLB
    ((850, 630), 14, 6),  # LOLB
    # Secondary
    ((1100, 530), 14, 6), # CB
    ((400, 530), 14, 6),  # CB
    ((750, 480), 14, 6)   # FS
]

# === Cover 3 ===
cov_three_defense = [
    ((750, 250), 140, 3),
    ((450, 250), 140, 3),
    ((1050, 250), 140, 3),

    ((625, 500), 100, 3),
    ((875, 500), 100, 3),
    ((375, 550), 100, 3),
    ((1125, 550), 100, 3)
]

# === Motion Storage ===
motions = [[] for _ in positions]
drawing_motion = False
current_motion = []
selected_player = None

# === Routes Storage ===
routes = [[] for _ in positions]
drawing_route = False
current_route = []
selected_player = None

# === Draw Players ===
def draw_players():
    font = pygame.font.Font(None, 36)

    screen.blit(font.render("A: Action button / Move players draw routes/motions |R: Start/Finish Route |M: Start/Finish Motion |Any Key to use Buttons", True, (255, 255, 255)), (10, 10))

    pygame.draw.rect(screen, (0, 128, 255), (1300, 40, 150, 50))
    screen.blit(font.render("No Defense", True, (255, 255, 255)), (1310, 50))
    pygame.draw.rect(screen, (0, 128, 255), (50, 40, 180, 50))
    screen.blit(font.render("Clear Offense", True, (255, 255, 255)), (60, 50))

    pygame.draw.rect(screen, (0, 128, 255), (50, 120, 180, 50))
    screen.blit(font.render("Shotgun", True, (255, 255, 255)), (60, 130))
    pygame.draw.rect(screen, (0, 128, 255), (50, 200, 180, 50))
    screen.blit(font.render("Pistol", True, (255, 255, 255)), (60, 210))
    pygame.draw.rect(screen, (0, 128, 255), (50, 280, 180, 50))
    screen.blit(font.render("Singleback", True, (255, 255, 255)), (60, 290))

    pygame.draw.rect(screen, (0, 128, 255), (50, 360, 180, 50))
    screen.blit(font.render("10 Pers", True, (255, 255, 255)), (60, 370))
    pygame.draw.rect(screen, (0, 128, 255), (50, 440, 180, 50))
    screen.blit(font.render("11 Pers", True, (255, 255, 255)), (60, 450))
    pygame.draw.rect(screen, (0, 128, 255), (50, 520, 180, 50))
    screen.blit(font.render("12 Pers", True, (255, 255, 255)), (60, 530))

    pygame.draw.rect(screen, (0, 128, 255), (1300, 120, 150, 50))
    screen.blit(font.render("Nickel", True, (255, 255, 255)), (1310, 130))
    pygame.draw.rect(screen, (0, 128, 255), (1300, 200, 150, 50))
    screen.blit(font.render("4-3", True, (255, 255, 255)), (1320, 210))
    pygame.draw.rect(screen, (0, 128, 255), (1300, 280, 150, 50))
    screen.blit(font.render("3-4", True, (255, 255, 255)), (1320, 290))
    pygame.draw.rect(screen, (0, 128, 255), (1300, 360, 150, 50))
    screen.blit(font.render("4-4", True, (255, 255, 255)), (1320, 370))
    pygame.draw.rect(screen, (0, 128, 255), (1300, 440, 150, 50))
    screen.blit(font.render("Cover 3", True, (255, 255, 255)), (1320, 450))

    for pos, radius, width in positions:
        pygame.draw.circle(screen, (0, 0, 0), pos, radius, width)
        pygame.draw.rect(screen, (0, 0, 0), (736, 646, 28, 28), 6)
        
def draw_defense(defense):
    for pos, radius, width in defense:
        pygame.draw.circle(screen, (200, 0, 0), pos, radius, width)

def draw_routes():
    for i, route in enumerate(routes):
        if not route:
            continue
        route_start = positions[i][0]
        points = [route_start] + route
        pygame.draw.lines(screen, (173,216,230), False, points, 3)
        for pt in route:
            pygame.draw.circle(screen, (173,216,230), pt, 5)

def draw_motion():
    for i, motion in enumerate(motions):
        if not motion:
            continue
            
        motion_start = positions[i][0]
        points = [motion_start] + motion

        for j in range(len(motion) - 1):
            start = pygame.math.Vector2(motion[j])
            end = pygame.math.Vector2(motion[j + 1])
            direction = end - start
            length = direction.length()
            if direction.length() == 0:
                continue
            direction = direction.normalize()


            dash_length = 10
            num_dashes = int(length // dash_length)

            for k in range(0, num_dashes, 2):  # skip every second to make a dashed pattern
                dash_start = start + direction * (k * dash_length)
                dash_end = start + direction * ((k + 1) * dash_length)
                pygame.draw.line(screen, (173, 216, 230), dash_start, dash_end, 3)

        for pt in points:
            pygame.draw.circle(screen, (173, 216, 230), pt, 5)

        pygame.draw.circle(screen, (173, 216, 230), motion[0], 14, 6)
        positions[i] = [(motion[-1][0], motion[-1][1]), positions[i][1], positions[i][2]]

# === Game State ===
show_nickel = False
show_four_three = False
show_three_four = False
show_four_four = False
show_cov_three = False
dragging = False
drag_index = None

# === Main Game Loop ===
while running:
    screen.fill((0, 0, 0))
    draw_football_field(screen)
    draw_players()
    draw_routes()
    draw_motion()

    if show_nickel:
        draw_defense(nickel_defense)
    elif show_four_three:
        draw_defense(four_three_defense)
    elif show_three_four:
        draw_defense(three_four_defense)
    elif show_four_four:
        draw_defense(four_four_defense)
    elif show_cov_three:
        draw_defense(cov_three_defense)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            x, y = pygame.mouse.get_pos()


            # Defense buttons
            if pygame.Rect(50, 40, 180, 50). collidepoint(pygame.mouse.get_pos()):
                routes = [[] for _ in positions]
                motions = [[] for _ in positions]

            elif pygame.Rect(1300, 40, 150, 50). collidepoint(pygame.mouse.get_pos()):
                show_cov_three = False
                show_nickel = False
                show_four_four = False
                show_four_three = False
                show_three_four = False

            elif pygame.Rect(50, 120, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[5] = shotgun[0]
                positions[6] = shotgun[1]

            elif pygame.Rect(50, 200, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[5] = pistol[0]
                positions[6] = pistol[1]

            elif pygame.Rect(50, 280, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[5] = singleback[0]
                positions[6] = singleback[1]

            elif pygame.Rect(50, 360, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[7] = ten_pers[0]
                positions[8] = ten_pers[1]
                positions[9] = ten_pers[2]
                positions[10] = ten_pers[3]

            elif pygame.Rect(50, 440, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[7] = eleven_pers[0]
                positions[8] = eleven_pers[1]
                positions[9] = eleven_pers[2]
                positions[10] = eleven_pers[3]

            elif pygame.Rect(50, 520, 180, 50).collidepoint(pygame.mouse.get_pos()):
                positions[7] = twelve_pers[0]
                positions[8] = twelve_pers[1]
                positions[9] = twelve_pers[2]
                positions[10] = twelve_pers[3]


            elif pygame.Rect(1300, 120, 150, 50).collidepoint(pygame.mouse.get_pos()):
                show_nickel = True
                show_four_four = False
                show_four_three = False
                show_three_four = False

            elif pygame.Rect(1300, 200, 150, 50).collidepoint(pygame.mouse.get_pos()):
                show_nickel = False
                show_four_four = False
                show_four_three = True
                show_three_four = False
            
            elif pygame.Rect(1300, 280, 150, 50).collidepoint(pygame.mouse.get_pos()):
                show_nickel = False
                show_four_four = False
                show_four_three = False
                show_three_four = True
            
            elif pygame.Rect(1300, 360, 150, 50).collidepoint(pygame.mouse.get_pos()):
                show_nickel = False
                show_four_four = True
                show_four_three = False
                show_three_four = False

            elif pygame.Rect(1300, 440, 150, 50).collidepoint(pygame.mouse.get_pos()):
                show_cov_three = True
                show_nickel = False
                show_four_four =False
                show_four_three = False
                show_three_four = False

            elif event.key == pygame.K_a:
                if drawing_route and selected_player is not None:
                    current_route.append((x, y))
                elif drawing_motion and selected_player is not None:
                    current_motion.append((x, y))
                else:
                    for i, (pos, radius, width) in enumerate(positions):
                        dx, dy = x - pos[0], y - pos[1]
                        if (dx**2 + dy**2)**0.5 <= radius:
                            selected_player = i
                            dragging = True
                            drag_index = i
                            break

            elif event.key == pygame.K_r:
                x, y = pygame.mouse.get_pos()
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
                        routes[selected_player] = current_route
                    drawing_route = False
                    selected_player = None
                    current_route = []

            elif event.key == pygame.K_m:
                x, y = pygame.mouse.get_pos()
                if not drawing_motion:
                    for i, (pos, radius, width) in enumerate(positions):
                        dx, dy = x - pos[0], y - pos[1]
                        if (dx**2 + dy**2)**0.5 <= radius:
                            drawing_motion = True
                            selected_player = i 
                            current_motion = [pos]
                            break
                else:
                    if selected_player is not None:
                        motions[selected_player] = current_motion
                    drawing_motion = False
                    selected_player = None
                    current_motion = []

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
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
