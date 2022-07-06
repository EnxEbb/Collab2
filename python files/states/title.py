from states.state import State
from states.game_world import game_world


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, dt, action):
        if action['start']:
            new_state = game_world(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Game states demo.", (0, 0, 0),
                            self.game.GAME_W // 2, self.game.GAME_H // 2)
                            
