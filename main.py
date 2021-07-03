import arcade
import random
from player import Bird
from pipe import Pipe
from game_state import State
from game_assets import *


class Game(arcade.Window):

    def __init__(self, width, height):

    
        super().__init__(width, height, title="Super Jump!")
  
        self.sprites = None
        self.pipe_sprites = None
        self.bird = None
        
        self.background = None
       
        self.base = None
      
        self.bird_list = None
       
        self.score_board = None
      
        self.flapped = False
    
        self.score = None
    
        self.state = State.MAIN_MENU
      
        self.menus = {'start': arcade.load_texture(GET_READY_MESSAGE),
                      'gameover': arcade.load_texture(GAME_OVER),
                      'play': arcade.load_texture(PLAY_BUTTON)}

    def setup(self):
        self.score = 0
        self.score_board = arcade.SpriteList()
        self.pipe_sprites = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.background = arcade.load_texture(random.choice(BACKGROUNDS))
        self.base = arcade.load_texture(BASE)
       
        self.sprites = dict()
        self.sprites['background'] = self.background
        self.sprites['base'] = self.base
      
        self.bird = Bird(50, self.height//2, self.base.height)
        self.bird_list.append(self.bird)

      
        start_pipe1 = Pipe.random_pipe_obstacle(self.sprites, self.height)
        self.pipe_sprites.append(start_pipe1[0])
        self.pipe_sprites.append(start_pipe1[1])

    def draw_score_board(self):
        """
        Draws the score board
        """
        self.score_board.draw()

    def draw_background(self):
        """
        Draws the background.
        """
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.background.width, self.background.height,
                                      self.background, 0)

    def draw_base(self):
       
        arcade.draw_texture_rectangle(self.width//2, self.base.height//2, self.base.width, self.base.height, self.base, 0)

    def on_draw(self):

        
        
        arcade.start_render()
        
        self.draw_background()
        self.pipe_sprites.draw()
        self.draw_base()
        self.bird_list.draw()

        if self.state == State.MAIN_MENU:
           
            texture = self.menus['start']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, texture.width, texture.height, texture, 0)

        elif self.state == State.PLAYING:
          
            self.draw_score_board()

        elif self.state == State.GAME_OVER:
            
            texture = self.menus['gameover']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, texture.width, texture.height, texture, 0)
            texture = self.menus['play']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 - 100, texture.width, texture.height, texture, 0)
            self.draw_score_board()

    def on_key_release(self, symbol, modifiers):

        if symbol == arcade.key.SPACE and self.state == State.MAIN_MENU:
       
            self.state = State.PLAYING
            return
        if symbol == arcade.key.SPACE:
            self.flapped = True

    def on_mouse_press(self, x, y, button, modifiers):

        if self.state == State.GAME_OVER:
            texture = self.menus['play']
            h = self.height//2 - 100
            w = self.width//2
            if w - texture.width//2 <= x <= w + texture.width//2:
                if h - texture.height//2 <= y <= h + texture.height//2:
                    self.setup()
                    self.state = State.MAIN_MENU

    def build_score_board(self):
        
        score_length = len(str(self.score))
        score_width = 24 * score_length
        left = (self.width - score_width) // 2
        self.score_board = arcade.SpriteList()
        for s in str(self.score):
            self.score_board.append(arcade.Sprite(SCORE[s], 1, center_x=left + 12, center_y=450))
            left += 24

    def on_update(self, delta_time):

       
        self.bird_list.update_animation()

        if self.state == State.PLAYING:
            self.build_score_board()

            
            if self.flapped:
                self.bird.flap()
                self.flapped = False

            
            if self.bird.top > self.height:
                self.bird.top = self.height

           
            if self.bird.bottom <= self.base.height:
                if self.bird.change_y < 0:
                    self.bird.change_y = 0
                self.bird.bottom = self.base.height

            new_pipe = None

            
            for pipe in self.pipe_sprites:
                if pipe.right <= 0:
                    pipe.kill()
                elif len(self.pipe_sprites) == 2 and pipe.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                    new_pipe = Pipe.random_pipe_obstacle(self.sprites, self.height)

            if new_pipe:
                self.pipe_sprites.append(new_pipe[0])
                self.pipe_sprites.append(new_pipe[1])

            
            self.pipe_sprites.update()
            self.bird.update(delta_time)
            self.bird_list.update()

            if self.bird.center_x >= self.pipe_sprites[0].center_x and not self.pipe_sprites[0].scored:
                self.score += 1
            
                self.pipe_sprites[0].scored = True
                self.pipe_sprites[1].scored = True
                print(self.score)

           
            hit = arcade.check_for_collision_with_list(self.bird, self.pipe_sprites)

            if any(hit):
                self.state = State.GAME_OVER
                self.bird.die()

        elif self.state == State.GAME_OVER:
           
            self.bird.update()


def main():
    game = Game(288, 512)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
