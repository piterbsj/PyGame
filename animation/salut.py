import sys
import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN
from models.methods import load_image

class Animation:
    def __init__(self, w1, h1, k, fps, image_path, position):
        self.animation_frames = []
        self.timer = pygame.time.Clock()
        self.image = load_image(image_path)

        self.width, self.height = self.image.get_size()
        self.w, self.h = self.width / w1, self.height / h1

        row = 0
        for j in range(int(self.height / self.h)):
            for i in range(int(self.width / self.w)):
                self.animation_frames.append(self.image.subsurface(pygame.Rect(i * self.w, row, self.w, self.h)))
            row += int(self.h)

        self.counter = 0
        self.k = k
        self.fps = fps
        self.position = position

    def update(self, screen: pygame.Surface):
        screen.blit(self.animation_frames[self.counter], self.position)
        self.counter = (self.counter + 1) % self.k

    def run(self, screen: pygame.Surface):
        while True:
            for evt in pygame.event.get():
                if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                    sys.exit()

            self.update(screen)

            pygame.display.update()
            self.timer.tick(self.fps)
