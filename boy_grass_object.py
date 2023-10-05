from pico2d import *


class Grass:
    def __int__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running

    running = True


def update_world():
    pass


def render_world():
    clear_canvas()
    update_canvas()
    open_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
