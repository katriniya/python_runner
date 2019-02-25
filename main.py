import pygame, random

class Game:
    def __init__(self):
        self.widht = 500
        self.height = 200
        self.screen = pygame.display.set_mode((self.widht, self.height))
        pygame.display.set_caption('SNAKE')
        pygame.font.init()
        go_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.go_surf = go_font.render('Game over', True, pygame.Color(255, 255, 255))
        self.restart = go_font.render('Press R to restart', True, pygame.Color(255, 255, 255))


    def draw_game_over(self):
        self.screen.blit(self.go_surf, (self.widht/2.8, self.height / 3))
        self.screen.blit(self.restart, (self.widht/4, self.height / 2))

    def drawGame(self):
        go_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = go_font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        self.screen.fill((43, 43, 43))
        self.screen.blit(self.score, (game.widht - 200,  20))

        player.drawPlayer(game.screen)
        objlist[0].drawObject(game.screen)

        if player.player_y < 190:
           player.player_y +=10


        if game_over:
            game.draw_game_over()

        pygame.display.flip()

class Player:
    def __init__(self):
        self.widht = 30
        self.height = - 80
        self.player_y = game.height-10
        self.player_x = 40
        self.playerColor = pygame.Color(255, 153, 204)

    def drawPlayer(self, screen):
        pygame.draw.rect(screen, self.playerColor, pygame.Rect(self.player_x, self.player_y, self.widht, self.height))

    def jumpPlayer(self):
        self.player_y -= 90

class Object:
    def __init__(self):
        self.widht = random.randint(20, 30)
        self.height = - random.randint(20, 50)
        self.object_x = game.widht + 10
        self.object_y = game.height-10
        self.objectColor = pygame.Color(255, 204, 255)

    def drawObject(self, screen):
        pygame.draw.rect(screen, self.objectColor, pygame.Rect(self.object_x, self.object_y, self.widht, self.height))

    def updateObject(self):
        self.object_x -= 15
        self.deleteObject()

    def deleteObject(self):
        print('del')
        if self.object_x < 0:
            objlist.pop(0)


if __name__ == '__main__':
    score = 0
    game = Game()
    player = Player()
    objlist = []
    objlist.append(Object())


    game_over = False
    app_running = True

    while app_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                app_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if player.player_y == game.height-10:
                        player.jumpPlayer()
                        break

                elif event.key == pygame.K_r:
                    game_over = False
                    score = 0
                    objlist[0].__init__()

        if not game_over:
            objlist[0].updateObject()
            score += 1


        if 180 < objlist[0].object_x <= 200:
            objlist.append(Object())
            print(len(objlist))

        if (player.player_x <= objlist[0].object_x <= player.player_x + player.widht or
                player.player_x <= objlist[0].object_x + objlist[0].widht <= player.player_x + player.widht) and\
                (player.player_y + player.height <= objlist[0].object_y <= player.player_y or
             player.player_y + player.height <= objlist[0].object_y + objlist[0].height <= player.player_y):
            game_over = True

        game.drawGame()

        pygame.time.delay(100)