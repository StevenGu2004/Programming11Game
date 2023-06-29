# Compiled Using CodeSkulptor3
# https://py3.codeskulptor.org/#user308_7rSf4jIak8_10.py


# Kirby's Culinary Quest for the Lamb Sauce is a 2-player racing
# minigame that you can play with a friend. In this game, you are
# competing against your friend to survive the Gourmet Race longer than
# the other can, thus winning you the fictional world-famous lamb sauce.
# Made by Steven Gu (computer programming 11, Ms. Stusiak's class)

# Imports ======================================================================================
import simplegui, random, math

# Load images ==================================================================================
P1_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/660648490271244288/795862201624952852/kirb1spritesheet.png")
P2_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/660648490271244288/795862243094429726/kirb2spritesheet.png")
BG_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/423673672663040001/796799010459484220/BG_IMG.png")
SANIC = simplegui.load_image("https://cdn.discordapp.com/attachments/423673672663040001/797637049191759902/sanic.png")
WATCH = simplegui.load_image("https://cdn.discordapp.com/attachments/423673672663040001/797637213193633853/watch.png")
PEARL = simplegui.load_image("https://cdn.discordapp.com/attachments/423673672663040001/797637159950614558/pearl.png")
COMMA = simplegui.load_image("https://cdn.discordapp.com/attachments/565970062339604480/797981383912849458/comma.png")
OBSTACLE_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/798690374797361162/cactus_obstacle.png")
P1_HEALTH = simplegui.load_image(
    "https://media.discordapp.net/attachments/565970062339604480/799373298039390258/spritesheet.png")
P2_HEALTH = simplegui.load_image(
    "https://media.discordapp.net/attachments/565970062339604480/799376478382325790/spritesheet_3.png")
BLASTZONE = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/778014229269053441/800853888054984754/firewall.png")
P1_HURT_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/801631728002531358/damgage_taken.png")
P2_HURT_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/801631898132283432/damage_taken2.png")
MENU_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/804092690702008370/pixil-frame-0_9.png")
PLAY_BUTTON_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802031979339448320/play.png")
CONTROL_BUTTON_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802031949064962048/controls.png")
CONTROL_SCREEN_IMG = simplegui.load_image(
    "https://media.discordapp.net/attachments/565970062339604480/801929513722183690/pixil-frame-0_7.png?width=536&height=536")
BACK_BUTTON_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802031926981689375/betterback.png")
P1_WINS_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802299397580128316/p1wins.png")
P2_WINS_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802299486025285692/p2wins.png")
REMATCH_BUTTON_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802026059251056700/rematch.png")
LORE_BUTTOM_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802051165297573908/lore.png")
LORE_IMG = simplegui.load_image(
    "https://cdn.discordapp.com/attachments/565970062339604480/802062679783112724/final_lore.png")

# Sprite rows and columns ======================================================================
P_IMG_ROW = 2
P_IMG_COLUMN = 2
HP_COLUMN = 5
# HP_ROW = 1 (unused)
P_HURT_COLUMN = 2
# P_HURT_COLUMN = 1 (unused)

# Image size dictionary =============================================================================
IMG_SIZE = {P1_IMG: [100 / P_IMG_COLUMN, 100 / P_IMG_ROW],
            P2_IMG: [100 / P_IMG_COLUMN, 100 / P_IMG_ROW],
            BG_IMG: [540, 1580],
            SANIC: [512, 472],
            PEARL: [32, 32],
            WATCH: [32, 32],
            COMMA: [32, 32],
            OBSTACLE_IMG: [400, 375],
            P1_HEALTH: [185, 32],  # This image size is also the size drawn on canvas
            P2_HEALTH: [185, 32],
            BLASTZONE: [700, 242],
            P1_HURT_IMG: [100 / P_HURT_COLUMN, 50],
            P2_HURT_IMG: [100 / P_HURT_COLUMN, 50],
            PLAY_BUTTON_IMG: [64, 48],
            CONTROL_BUTTON_IMG: [64, 48],
            MENU_IMG: [50, 50],
            CONTROL_SCREEN_IMG: [536, 536],
            BACK_BUTTON_IMG: [64, 48],
            P1_WINS_IMG: [540, 540],
            P2_WINS_IMG: [540, 540],
            REMATCH_BUTTON_IMG: [72, 48],
            LORE_BUTTOM_IMG: [64, 48],
            LORE_IMG: [500, 420]}

# Load sound ===================================================================================
MENU_MUSIC = simplegui.load_sound(
    "https://cdn.discordapp.com/attachments/423673672663040001/802301225504079892/goodKirby_Air_Ride_City_Trial_8-bit_version.mp3")
GAME_BG_MUSIC = simplegui.load_sound(
    "https://cdn.discordapp.com/attachments/565970062339604480/802036178366234634/Gourmet_Race_8-Bit_Remix_-_Kirby_Super_Star.mp3")
REMATCH_MUSIC = simplegui.load_sound(
    "https://cdn.discordapp.com/attachments/565970062339604480/802042302184161280/Kirby_amazing_mirror_death_sound.mp3")
LORE_MUSIC = simplegui.load_sound(
    "https://cdn.discordapp.com/attachments/565970062339604480/802064954483802132/Gravity_Rush_OST_-_Discovery_of_Gravitation.mp3")
BUTTON_SELECTED_MUSIC = simplegui.load_sound(
    "https://cdn.discordapp.com/attachments/565970062339604480/802297640897216572/popButtonPlate_Click_Minecraft_Sound_-_Sound_Effect_for_editing_1.mp3")

# Constants ====================================================================================
# BG height is used as canvas height as well
WIDTH, HEIGHT = IMG_SIZE[BG_IMG]
FRAME_WIDTH = 800
ITEM_AMOUNT = 4
ITEM_SIZE = [50, 50]
OBSTACLE_SIZE = [550, 100]
ITEM_RADIUS = 25
OBSTACLE_TIMER = 0
PLAYER_RADIUS = 28
BLASTZONE_HEIGHT = 150
HP_COLUMN_WIDTH = 185 / HP_COLUMN  # Width of 1 heart container
P_BOUNCE = 9  # Player automatically bounces away from obstacle
INVINS_TIME = 45  # to prevent p&p_collision overwriting p&obs_collision
P_FLASH_RATE = 0.1
PLAYER_HEALTH = 5
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 125
REMATCH_MUSIC_TIME = 150
USER_INPUT_WIDTH = 211

# Global variables =============================================================================
player_size = [75, 75]  # Size on canvas
player_acceleration = 0.5
bg_pos = [FRAME_WIDTH / 2, 0]
scroll_speed = 2
items = []
obstacles = []
p1_hp_dest_center = [185 / 2, 32 / 2]
p2_hp_dest_center = [FRAME_WIDTH - 185 / 2, 32 / 2]
speed_decay = 0.925
item_spawn_time = 280
obstacle_spawn_time = 240
# Game states
game_state = 0  # Menu screen (default)
# game_state == 1: new game
# game_state == 2: controls
# game_state == 3: game over
# game_state == 4: lore page
# Music booleans and timers
menu_music = False
game_bg_music = False
rematch_music = False
lore_music = False
rematch_music_timer = 0
button_selected_music_timer = 0


# Helper functions =============================================================================
def new_game():
    global p1, p2, game_state
    p1 = Player(P1_IMG,
                [0, 0],
                player_acceleration,
                [FRAME_WIDTH / 4, HEIGHT / 4],
                P1_HEALTH,
                p1_hp_dest_center.copy(),
                P1_HURT_IMG,
                PLAYER_HEALTH)

    p2 = Player(P2_IMG,
                [0, 0],
                player_acceleration,
                [FRAME_WIDTH * 3 / 4, HEIGHT / 4],
                P2_HEALTH,
                p2_hp_dest_center.copy(),
                P2_HURT_IMG,
                PLAYER_HEALTH)

    for item in items:
        items.remove(item)

    for obstacle in obstacles:
        obstacles.remove(obstacle)

    game_state = 1


def distance(pos1, pos2):
    a = pos2[0] - pos1[0]
    b = pos2[1] - pos1[1]
    d = math.sqrt(a ** 2 + b ** 2)
    return d


def check_collision(x, y):
    collision = False
    for obstacle in obstacles:
        in_obstacle_width = (x >= obstacle.left - PLAYER_RADIUS and x <= obstacle.right + PLAYER_RADIUS)
        in_obstacle_height = (y >= obstacle.top - PLAYER_RADIUS and y <= obstacle.bottom + PLAYER_RADIUS)
        if (in_obstacle_width and in_obstacle_height):
            collision = True
    return collision


def pos_not_in_obstacle():
    # Items can't spawn inside an obstacle
    # 'Pearl' shouldn't teleport player inside obstacle
    # Using player.rad since player.rad > item.rad.
    # Plus item shouldn't spawn right next to the obstacle anyway.
    x = random.randint(PLAYER_RADIUS, FRAME_WIDTH - PLAYER_RADIUS)
    y = random.randint(PLAYER_RADIUS, HEIGHT / 2 - PLAYER_RADIUS - BLASTZONE_HEIGHT)
    while check_collision(x, y):
        x = random.randint(PLAYER_RADIUS, FRAME_WIDTH - PLAYER_RADIUS)
        y = random.randint(PLAYER_RADIUS, HEIGHT / 2 - PLAYER_RADIUS - BLASTZONE_HEIGHT)
    pos = [x, y]
    return pos


def spawn_item():
    global ITEM_IMG_DICT, item_choose, ITEM_AMOUNT, ITEM_NAME_DICT
    pos = pos_not_in_obstacle()
    spd = int(scroll_speed)
    ITEM_IMG_DICT = {0: SANIC, 1: PEARL, 2: WATCH, 3: COMMA}
    item_choose = random.randrange(ITEM_AMOUNT)

    item = Item(ITEM_IMG_DICT[item_choose], spd, pos)
    items.append(item)


def spawn_obstacle():
    x = random.randint(OBSTACLE_SIZE[0] / 2, FRAME_WIDTH - OBSTACLE_SIZE[0] / 2)
    y = - OBSTACLE_SIZE[1] / 2
    pos = [x, y]
    img = OBSTACLE_IMG
    obstacle = Obstacle(img, pos)
    obstacles.append(obstacle)


def player_collision(p1, p2):
    if p1.has_collided(p2):
        # Get p1 out of the hitbox of p2
        while p1.has_collided(p2):
            p1.pos[0] -= p1.vel[0]
            p1.pos[1] -= p1.vel[1]
            p2.pos[0] -= p2.vel[0]
            p2.pos[1] -= p2.vel[1]
        # Get angle from collision
        spd1 = math.sqrt(p1.vel[0] ** 2 + p1.vel[1] ** 2)
        spd2 = math.sqrt(p2.vel[0] ** 2 + p2.vel[1] ** 2)
        angle = math.atan2(p2.pos[1] - p1.pos[1], p2.pos[0] - p1.pos[0])  # atan2 to get quadrant
        direction = (math.cos(angle), math.sin(angle))
        # Get new velocities
        vel1x = direction[0] * spd1
        vel1y = direction[1] * spd1
        vel2x = -direction[0] * spd2
        vel2y = -direction[1] * spd2
        # Trade the two players' velocities
        p1.vel[0] = vel2x
        p1.vel[1] = vel2y
        p2.vel[0] = vel1x
        p2.vel[1] = vel1y


def spawn_button():
    global play, control, back, rematch, lore
    play = Button(PLAY_BUTTON_IMG, [FRAME_WIDTH / 2, 350])
    control = Button(CONTROL_BUTTON_IMG, [FRAME_WIDTH / 2, 500])
    back = Button(BACK_BUTTON_IMG, [FRAME_WIDTH - 92, 650])
    rematch = Button(REMATCH_BUTTON_IMG, [FRAME_WIDTH / 2, 600])
    lore = Button(LORE_BUTTOM_IMG, [FRAME_WIDTH / 2, 650])


# Classes ======================================================================================
class Player:
    def __init__(self,
                 image,
                 velocity,
                 acceleration,
                 position,
                 hp_image,
                 hp_dest_center,
                 hurt_sprite,
                 player_health):
        self.img = image
        self.vel = velocity
        self.acc = acceleration
        self.pos = position
        self.size = player_size
        self.time = 0
        self.rad = PLAYER_RADIUS
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.watch_timer = 0
        self.watch_boolean = False
        self.sanic_timer = 0
        self.sanic_boolean = False
        self.comma_timer = 0
        self.comma_boolean = False
        self.hp = PLAYER_HEALTH
        self.hp_img = hp_image
        self.collided_obstacle = False
        self.hp_dest_c = hp_dest_center
        self.invins_period = False
        self.invins_timer = 0
        self.hurt_img = hurt_sprite

    def draw(self, canvas):
        if not self.invins_period:
            width, height = IMG_SIZE[self.img]
            column = int(self.time) % P_IMG_COLUMN
            row = int(self.time) // P_IMG_ROW
            tile_center = [width / 2 + column * width,
                           height / 2 + row * height]

            canvas.draw_image(self.img,
                              tile_center,
                              IMG_SIZE[self.img],
                              self.pos,
                              self.size)
        if self.invins_period:
            width, height = IMG_SIZE[self.hurt_img]
            column = int(P_FLASH_RATE * self.invins_timer) % P_HURT_COLUMN  # adjust invins_time
            tile_center = [width / 2 + column * width, height / 2]

            canvas.draw_image(self.hurt_img,
                              tile_center,
                              IMG_SIZE[self.hurt_img],
                              self.pos,
                              self.size)

        # Health bar
        hp_width, hp_height = IMG_SIZE[self.hp_img]
        center = [hp_width / 2, hp_height / 2]

        canvas.draw_image(self.hp_img,
                          center,
                          [hp_width, hp_height],
                          self.hp_dest_c,
                          [hp_width, hp_height])

    def update(self):
        if self.up:
            self.vel[1] -= self.acc
        if self.down:
            self.vel[1] += self.acc
        if self.right:
            self.vel[0] += self.acc
        if self.left:
            self.vel[0] -= self.acc

        self.obstacle_collision()

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Slowly decaying speed
        self.vel[0] *= speed_decay
        self.vel[1] *= speed_decay
        # Player animation
        self.time += 0.25
        self.time %= P_IMG_ROW * P_IMG_COLUMN

    # For player collision
    def has_collided(self, other):
        dist = distance(self.pos, other.pos)
        return dist <= self.rad + other.rad

    def wall_collision(self):
        # Left wall
        if self.pos[0] - self.rad <= 0:
            self.vel[0] = 0
            self.pos[0] = self.rad
        # Right wall
        if self.pos[0] + self.rad >= FRAME_WIDTH:
            self.vel[0] = 0
            self.pos[0] = FRAME_WIDTH - self.rad
        # Ceiling
        if self.pos[1] - self.rad <= 0:
            self.vel[1] = 0
            self.pos[1] = self.rad

    def obstacle_collision(self):
        for obstacle in obstacles:
            if self.collides_obs_top(obstacle):
                self.vel[1] = -P_BOUNCE
                self.pos[1] = obstacle.top - self.rad

            if self.collides_obs_bottom(obstacle):
                self.vel[1] = obstacle.spd + P_BOUNCE
                self.pos[1] = obstacle.bottom + self.rad + obstacle.spd

            if self.collides_obs_left(obstacle):
                self.vel[0] = -P_BOUNCE
                self.pos[0] = obstacle.left - self.rad

            if self.collides_obs_right(obstacle):
                self.vel[0] = P_BOUNCE
                self.pos[0] = obstacle.right + self.rad

    # Player invinsible for 1 second after taking damage
    def player_invins(self):
        self.invins_timer += 1
        if self.invins_timer == INVINS_TIME:
            self.invins_period = False
            self.invins_timer = 0

    # Item effects to player
    def watch_activate(self):
        self.acc = player_acceleration / 2
        self.watch_timer += 1
        if self.watch_timer == 120:
            self.acc = player_acceleration
            self.watch_boolean = False
            self.watch_timer = 0

    def sanic_activate(self):
        self.acc = player_acceleration * 2
        self.sanic_timer += 1
        if self.sanic_timer == 120:
            self.acc = player_acceleration
            self.sanic_boolean = False
            self.sanic_timer = 0

    def comma_activate(self):
        self.acc = 0
        self.comma_timer += 1
        if self.comma_timer == 60:
            self.acc = player_acceleration
            self.comma_boolean = False
            self.comma_timer = 0

    # Player obstacle collision
    def collides_obs_left(self, obs):
        next_x = self.pos[0] + self.vel[0]
        next_in_x = self.pos[0] <= obs.left - self.rad and next_x >= obs.left - self.rad
        in_y = self.pos[1] >= obs.top - self.rad and self.pos[1] <= obs.bottom + self.rad
        return in_y and next_in_x

    def collides_obs_right(self, obs):
        next_x = self.pos[0] + self.vel[0]
        next_in_x = self.pos[0] >= obs.right + self.rad and next_x <= obs.right + self.rad
        in_y = self.pos[1] >= obs.top - self.rad and self.pos[1] <= obs.bottom + self.rad
        return in_y and next_in_x

    def collides_obs_bottom(self, obs):
        next_y = self.pos[1] + self.vel[1]
        next_in_y = self.pos[1] >= obs.bottom + self.rad and next_y <= obs.bottom + self.rad + obs.spd
        in_x = self.pos[0] >= obs.left - self.rad and self.pos[0] <= obs.right + self.rad
        return in_x and next_in_y

    def collides_obs_top(self, obs):
        next_y = self.pos[1] + self.vel[1]
        next_in_y = self.pos[1] <= obs.top - self.rad and next_y >= obs.top - self.rad
        in_x = self.pos[0] >= obs.left - self.rad and self.pos[0] <= obs.right + self.rad
        return in_x and next_in_y

    def invins_period(self):
        self.hurt_timer += 1
        if self.hurt_timer == 60:
            self.hurt = False


class Item:
    def __init__(self, image, speed, position):
        self.img = image
        self.spd = speed
        self.pos = position
        self.size = ITEM_SIZE
        self.rad = ITEM_RADIUS

    def draw(self, canvas):
        width, height = IMG_SIZE[self.img]
        canvas.draw_image(self.img,
                          [width / 2, height / 2],
                          [width, height],
                          self.pos,
                          self.size)

    def update(self):
        self.pos[1] += self.spd
        if self.pos[1] >= HEIGHT / 2 - BLASTZONE_HEIGHT:
            items.remove(self)

    # Item ability methods
    def item_ability(self, other):
        if self.img == PEARL:
            self.pearl(other)
        if self.img == WATCH:
            self.watch(other)
        if self.img == SANIC:
            self.sanic(other)
        if self.img == COMMA:
            self.comma(other)

    def pearl(self, other):
        other.pos = pos_not_in_obstacle()

    def watch(self, other):
        other.watch_boolean = True

    def sanic(self, other):
        other.sanic_boolean = True

    def comma(self, other):
        other.comma_boolean = True


class Obstacle:
    def __init__(self, image, position):
        self.img = image
        self.spd = int(scroll_speed)
        self.pos = position
        self.size = OBSTACLE_SIZE
        self.left = self.pos[0] - self.size[0] / 2
        self.right = self.pos[0] + self.size[0] / 2
        self.top = self.pos[1] - self.size[1] / 2
        self.bottom = self.pos[1] + self.size[1] / 2

    def draw(self, canvas):
        width, height = IMG_SIZE[OBSTACLE_IMG]
        canvas.draw_image(self.img,
                          [width / 2, height / 2],
                          [width, height],
                          self.pos,
                          self.size)

    def update(self):
        self.pos[1] += self.spd
        self.top += self.spd
        self.bottom += self.spd
        if self.pos[1] >= HEIGHT / 2 - BLASTZONE_HEIGHT:
            obstacles.remove(self)

    def has_collided(self, other):
        in_obstacle_width = other.pos[0] >= self.left - other.size[0] / 2 and other.pos[0] <= self.right + other.size[
            0] / 2
        in_obstacle_height = other.pos[1] >= self.top - other.size[1] / 2 and other.pos[1] <= self.bottom + other.size[
            1] / 2
        return in_obstacle_width and in_obstacle_height


class Button:
    def __init__(self, image, position):
        self.img = image
        self.pos = position
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT
        self.left = self.pos[0] - self.width / 2
        self.right = self.pos[0] + self.width / 2
        self.top = self.pos[1] - self.height / 2
        self.bottom = self.pos[1] + self.height / 2

    def draw(self, canvas):
        width, height = IMG_SIZE[self.img]
        canvas.draw_image(self.img,
                          [width / 2, height / 2],
                          [width, height],
                          self.pos,
                          [self.width, self.height])

    def is_selected(self, mouse_position):
        within_x = mouse_position[0] >= self.left and mouse_position[0] <= self.right
        within_y = mouse_position[1] >= self.top and mouse_position[1] <= self.bottom
        return within_x and within_y


# Handlers =====================================================================================
def draw_handler(canvas):
    global OBSTACLE_TIMER, game_state, menu_music, rematch_music, game_bg_music, rematch_music_timer
    # Draw the menu screen and buttons first
    if game_state == 0:
        rematch_music_timer = 0
        width, height = IMG_SIZE[MENU_IMG]
        canvas.draw_image(MENU_IMG,
                          [width / 2, height / 2],
                          [width, height],
                          [FRAME_WIDTH / 2, HEIGHT / 4],
                          [FRAME_WIDTH, HEIGHT / 2])

        # Buttons
        play.draw(canvas)
        control.draw(canvas)
        lore.draw(canvas)

        # Music
        GAME_BG_MUSIC.pause()
        REMATCH_MUSIC.pause()
        LORE_MUSIC.pause()
        menu_music = False
        if not menu_music:
            MENU_MUSIC.play()
            menu_music = True

    # New game
    if game_state == 1:
        MENU_MUSIC.pause()
        REMATCH_MUSIC.pause()
        rematch_music_timer = 0
        game_bg_music = False
        if not game_bg_music:
            GAME_BG_MUSIC.play()
            game_bg_music = True

        canvas.draw_image(BG_IMG,
                          [WIDTH / 2, HEIGHT / 2],
                          [WIDTH, HEIGHT],
                          bg_pos,
                          [FRAME_WIDTH, HEIGHT])
        bg_pos[1] += int(scroll_speed)
        bg_pos[1] %= HEIGHT / 2

        # Player lose all health if they touch the blastzone
        hp1_width, hp1_height = IMG_SIZE[p1.hp_img]
        if p1.pos[1] >= HEIGHT / 2 - BLASTZONE_HEIGHT:
            p1.hp = 0
            p1.hp_dest_c[0] -= hp1_width / 2  # Moves hp bar completely out of frame
        hp2_width, hp2_height = IMG_SIZE[p2.hp_img]
        if p2.pos[1] >= HEIGHT / 2 - BLASTZONE_HEIGHT:
            p2.hp = 0
            p2.hp_dest_c[0] += hp1_width / 2

        # Players
        p1.draw(canvas)
        p2.draw(canvas)
        p1.update()
        p2.update()
        p1.wall_collision()
        p2.wall_collision()
        player_collision(p1, p2)
        if p1.invins_period:
            p1.player_invins()
        if p2.invins_period:
            p2.player_invins()

        # Obstacles
        if OBSTACLE_TIMER >= abs(int(obstacle_spawn_time)):
            spawn_obstacle()
            OBSTACLE_TIMER = 0
        else:
            OBSTACLE_TIMER += 1

        for obstacle in obstacles:
            obstacle.draw(canvas)
            obstacle.update()

            if obstacle.has_collided(p1):
                if not p1.invins_period:
                    p1.hp_dest_c[0] -= HP_COLUMN_WIDTH
                    p1.hp -= 1
                p1.invins_period = True
            if obstacle.has_collided(p2):
                if not p2.invins_period:
                    p2.hp_dest_c[0] += HP_COLUMN_WIDTH
                    p2.hp -= 1
                p2.invins_period = True

            # Quick fix for item very occasionally spawning inside the obstacles
            for item in items:
                if obstacle.has_collided(item):
                    if item in items:
                        items.remove(item)

        # Items
        if random.randrange(abs(int(item_spawn_time))) == 0:
            spawn_item()

        for item in items:
            item.draw(canvas)
            item.update()

            if p1.has_collided(item):
                item.item_ability(p1)
                if p1.has_collided(p2):
                    p1.hp = 0  # Player gets telefraged
                if item in items:
                    items.remove(item)
            if p2.has_collided(item):
                item.item_ability(p2)
                if p2.has_collided(p1):
                    p2.hp = 0
                if item in items:
                    items.remove(item)

        # Item activations that use a timer
        if p1.watch_boolean:
            p1.watch_activate()
        if p2.watch_boolean:
            p2.watch_activate()
        if p1.sanic_boolean:
            p1.sanic_activate()
        if p2.sanic_boolean:
            p2.sanic_activate()
        if p1.comma_boolean:
            p1.comma_activate()
        if p2.comma_boolean:
            p2.comma_activate()

        # Blastzone
        bz_width, bz_height = IMG_SIZE[BLASTZONE]
        canvas.draw_image(BLASTZONE,
                          [bz_width / 2, bz_height / 2],
                          [bz_width, bz_height],
                          [FRAME_WIDTH / 2, HEIGHT / 2 - BLASTZONE_HEIGHT / 2],
                          [FRAME_WIDTH, BLASTZONE_HEIGHT])

        # Game over
        if p1.hp <= 0 or p2.hp <= 0:
            game_state = 3

    # Control screen
    if game_state == 2:
        width, height = IMG_SIZE[CONTROL_SCREEN_IMG]
        canvas.draw_image(CONTROL_SCREEN_IMG,
                          [width / 2, height / 2],
                          [width, height],
                          [FRAME_WIDTH / 2, HEIGHT / 4],
                          [FRAME_WIDTH, HEIGHT / 2])
        back.draw(canvas)
        MENU_MUSIC.pause()

    # Rematch screen
    if game_state == 3:
        for obstacle in obstacles:
            obstacles.remove(obstacle)
        for item in items:
            items.remove(item)

        if p1.hp <= 0:
            width, height = IMG_SIZE[P2_WINS_IMG]
            canvas.draw_image(P2_WINS_IMG,
                              [width / 2, height / 2],
                              [width, height],
                              [FRAME_WIDTH / 2, HEIGHT / 4],
                              [FRAME_WIDTH, HEIGHT / 2])
        if p2.hp <= 0:
            width, height = IMG_SIZE[P1_WINS_IMG]
            canvas.draw_image(P1_WINS_IMG,
                              [width / 2, height / 2],
                              [width, height],
                              [FRAME_WIDTH / 2, HEIGHT / 4],
                              [FRAME_WIDTH, HEIGHT / 2])
        rematch.draw(canvas)
        back.draw(canvas)

        GAME_BG_MUSIC.pause()
        rematch_music_timer += 1
        if rematch_music_timer <= REMATCH_MUSIC_TIME:
            rematch_music = False
            if not rematch_music:
                REMATCH_MUSIC.play()

    # Lore screen
    if game_state == 4:
        width, height = IMG_SIZE[LORE_IMG]
        canvas.draw_image(LORE_IMG,
                          [width / 2, height / 2],
                          [width, height],
                          [FRAME_WIDTH / 2, HEIGHT / 4],
                          [FRAME_WIDTH, HEIGHT / 2])
        back.draw(canvas)

        MENU_MUSIC.pause()
        lore_music = False
        if not lore_music:
            LORE_MUSIC.play()
            lore_music = True


def key_press(key):
    if key == simplegui.KEY_MAP['a']:
        p1.left = True
    if key == simplegui.KEY_MAP['d']:
        p1.right = True
    if key == simplegui.KEY_MAP['w']:
        p1.up = True
    if key == simplegui.KEY_MAP['s']:
        p1.down = True

    if key == simplegui.KEY_MAP['left']:
        p2.left = True
    if key == simplegui.KEY_MAP['right']:
        p2.right = True
    if key == simplegui.KEY_MAP['up']:
        p2.up = True
    if key == simplegui.KEY_MAP['down']:
        p2.down = True


def key_release(key):
    if key == simplegui.KEY_MAP['left']:
        p2.left = False
    if key == simplegui.KEY_MAP['right']:
        p2.right = False
    if key == simplegui.KEY_MAP['up']:
        p2.up = False
    if key == simplegui.KEY_MAP['down']:
        p2.down = False

    if key == simplegui.KEY_MAP['a']:
        p1.left = False
    if key == simplegui.KEY_MAP['d']:
        p1.right = False
    if key == simplegui.KEY_MAP['w']:
        p1.up = False
    if key == simplegui.KEY_MAP['s']:
        p1.down = False


def mouse_handler(mouse_position):
    global game_state
    if game_state == 0:
        if play.is_selected(mouse_position):
            BUTTON_SELECTED_MUSIC.play()
            new_game()
        if control.is_selected(mouse_position):
            BUTTON_SELECTED_MUSIC.play()
            game_state = 2
        if lore.is_selected(mouse_position):
            BUTTON_SELECTED_MUSIC.play()
            game_state = 4

    if game_state == 4 or game_state == 2 or game_state == 3:
        if back.is_selected(mouse_position):
            BUTTON_SELECTED_MUSIC.play()
            game_state = 0

    if game_state == 3:
        if rematch.is_selected(mouse_position):
            BUTTON_SELECTED_MUSIC.play()
            new_game()


def item_amount_handler(new_item_spawn_time):
    global item_spawn_time
    item_spawn_time = float(new_item_spawn_time)


def obstacle_amount_handler(new_obstacle_spawn_time):
    global obstacle_spawn_time
    obstacle_spawn_time = float(new_obstacle_spawn_time)


def scroll_speed_handler(new_scroll_speed):
    global scroll_speed
    scroll_speed = float(new_scroll_speed)


def p_acceleration_handler(new_player_acceleration):
    global player_acceleration
    player_acceleration = float(new_player_acceleration)


# Frame ========================================================================================
frame = simplegui.create_frame("Kirby's Culinary Quest for the Lamb Sauce", FRAME_WIDTH, HEIGHT / 2)
# Set handler functions
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.set_mouseclick_handler(mouse_handler)
frame.add_label("[Enter positive numbers.]", USER_INPUT_WIDTH)
frame.add_input("(Default: 280) Average frame per item spawn: ", item_amount_handler, USER_INPUT_WIDTH)
frame.add_input("(Default: 240) Average frame per obstacle spawn: ", obstacle_amount_handler, USER_INPUT_WIDTH)
frame.add_input("(Default: 2) Screen scroll speed: ", scroll_speed_handler, USER_INPUT_WIDTH)
frame.add_input("(Default: 0.5) Player acceleration: ", p_acceleration_handler, USER_INPUT_WIDTH)
frame.add_label("Press 'enter' for codeskulptor to recognize the entered change", USER_INPUT_WIDTH)
frame.add_label(" ", USER_INPUT_WIDTH)  # For spacing
frame.add_label("Press 'Expand' for easier screen adjustments or use 'ctrl' with '+' or '-' to zoom in or out ",
                USER_INPUT_WIDTH)
# Other functions
spawn_button()
frame.start()