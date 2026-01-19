from pygame import *


from sprites_for_snake import *


class SpaceInvaders2:
    def __init__(self):
        # Фактическая инициализация Pygame происходит в _init_pygame().
        self._init_pygame()
        self.screen = display.set_mode((WIN_W, WIN_H))
        self.clock = time.Clock()

        # init sprites
        self.background = WorkClass(
            SRC + 'lakeside_lights.png',
            WIN_W // 2, WIN_H // 2,
            WIN_W, WIN_H
        )
        self.sssss1snake = NoGamePersona(
            SRC + 'змеюка-ргх.png',
            CRUSADERS_SIZE[1]//2, (WIN_H - CRUSADERS_SIZE[0]) // 2,
            CRUSADERS_SIZE[0],CRUSADERS_SIZE[1], STOP_V
        )
        self.sssss2snake = NoGamePersona(
            SRC + 'змеюка-ргх.png',
            WIN_W - (CRUSADERS_SIZE[1] // 2), (WIN_H - CRUSADERS_SIZE[0] ) // 2,
            CRUSADERS_SIZE[0],CRUSADERS_SIZE[1], STOP_V
        )
        self.ball = Ball(
            SRC + 'кольцокотла.png',
            WIN_W // 2, WIN_H // 2,
            SNITCH[0],SNITCH[1],1
        )

    # продолжение вышеописанного класса

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        init()
        display.set_caption('Космические приключения')

    def _handle_input(self):
        for e in event.get():
            if e.type == QUIT or (
                    e.type == KEYDOWN and e.key == K_ESCAPE
            ):
                quit()
        keys = key.get_pressed()

        if keys[K_RIGHT]:
            self.sssss1snake.move_right()
        elif keys[K_LEFT]:
            self.sssss1snake.move_left()
        if keys[K_UP]:
            self.sssss1snake.move_up()
        if keys[K_DOWN]:
            self.sssss1snake.move_down()


        if keys[K_d]:
            self.sssss2snake.move_right()
        elif keys[K_a]:
            self.sssss2snake.move_left()
        if keys[K_w]:
            self.sssss2snake.move_up()
        if keys[K_s]:
            self.sssss2snake.move_down()

    def _process_game_logic(self):
        self.ball.move()
        if sprite.collide_mask(self.ball, self.sssss1snake):
            self.ball.velocity = self.ball.velocity.reflect(self.sssss1snake.velocity)
            self.ball.left_turn = False
        if sprite.collide_rect(self.ball, self.sssss2snake):
            self.ball.velocity = self.ball.velocity.reflect(self.sssss2snake.velocity)
            self.ball.left_turn = True


    def _draw(self):
        self.background.draw(self.screen)
        self.sssss1snake.rotate()
        self.sssss1snake.draw(self.screen)
        self.sssss2snake.rotate()
        self.sssss2snake.draw(self.screen)
        self.ball.draw(self.screen)
        self.clock.tick(FPS)
        display.update()


game = SpaceInvaders2()
game.main_loop()

