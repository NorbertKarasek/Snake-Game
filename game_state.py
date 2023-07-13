from random import randint

from direction import Direction
from position import Position

INITIAL_SNAKE = [Position(1, 2), Position(2, 2), Position(3, 2)]
INITIAL_DIRECTION = Direction.RIGHT

class GameState:
    def __init__(self,
                 snake,
                 direction,
                 food,
                 obstacle,
                 field_size=20):
        self.snake = snake
        self.direction = direction
        self.field_size = field_size
        self.obstacle = obstacle
        self.food = food

    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()
        self.set_random_obstacle_position()

    def next_head_position(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)

    def set_random_food_position(self):
        food_in_snake = True
        while food_in_snake:
            self.food = Position(
                randint(0, self.field_size - 1),
                randint(0, self.field_size - 1)
            )
            food_in_snake = self.food in self.snake

    def set_random_obstacle_position(self):
        obstacle_in_snake = True
        while obstacle_in_snake:
            self.obstacle = Position(
                randint(0, self.field_size - 1),
                randint(0, self.field_size - 1)
            )
            obstacle_in_snake = self.obstacle in self.snake or self.obstacle == self.food


    def can_turn(self, direction):
        new_head = self.next_head_position(direction)
        return new_head != self.snake[-2]

    def turn(self, direction):
        if self.can_turn(direction):
            self.direction = direction

    def step(self):
        initial_length = len(INITIAL_SNAKE)
        points = [len(self.snake)-initial_length]
        new_head = self.next_head_position(self.direction)

        if new_head in self.snake:
            self.set_initial_position()
            print(f"Zdoybto {points} punktów")
            return

        if new_head == self.obstacle:
            self.set_initial_position()
            print(f"Zdoybto {points} punktów")
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
            points.append(+1)
        else:
            self.snake = self.snake[1:]
