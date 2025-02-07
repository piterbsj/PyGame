import pygame
import Box2D
from Box2D.b2 import world


class GameWorld:
    def __init__(self):
        self.world = world(gravity=(0, -10), doSleep=True)

    def step(self, time_step, vel_iters, pos_iters):
        self.world.Step(time_step, vel_iters, pos_iters)

    def clear_forces(self):
        self.world.ClearForces()


class GameObject:
    def __init__(self, world, position, size, image_path):
        self.body = world.CreateStaticBody(
            position=position,
            shapes=Box2D.b2PolygonShape(box=size)
        )
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(position[0] * 30, 600 - position[1] * 30))

    def update(self):
        self.rect.center = (self.body.position[0] * 30, 600 - self.body.position[1] * 30)