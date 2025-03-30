from abc import ABC, abstractmethod
import turtle
import time
from datetime import datetime
from typing import Protocol


class Digit:
    def init(self, value: int, position: tuple[float, float], size: float = 1.0):
        self.value = value
        self.position = position
        self.size = size
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)

    def draw(self) -> None:
        self._turtle.penup()
        self._turtle.goto(self.position)
        self._turtle.color("black")
        font_size = int(20 * self.size)
        self._turtle.write(str(self.value), align="center", font=("Arial", font_size, "normal"))


class ClockFace:
    def init(self, radius: float, center: tuple[float, float] = (0, 0)):
        self.radius = radius
        self.center = center
        self.digits: list[Digit] = []
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)

    def setup(self) -> None:
        import math
        for hour in range(1, 13):
            angle = math.radians(30 * (3 - hour))
            x = self.center[0] + (self.radius * 0.85) * math.cos(angle)
            y = self.center[1] + (self.radius * 0.85) * math.sin(angle)
            digit = Digit(hour, (x, y), size=1.2)
            self.digits.append(digit)

    def draw(self) -> None:
        self._turtle.penup()
        self._turtle.goto(self.center[0], self.center[1] - self.radius)
        self._turtle.pendown()
        self._turtle.circle(self.radius)
        for _ in range(12):
            self._turtle.penup()
            self._turtle.goto(self.center[0], self.center[1])
            self._turtle.setheading(_ * 30)
            self._turtle.forward(self.radius * 0.9)
            self._turtle.pendown()
            self._turtle.forward(self.radius * 0.1)
        for digit in self.digits:
            digit.draw()


class Hand:
    def init(self, length: float, width: float, color: str, center: tuple[float, float] = (0, 0)):
        self.length = length
        self.width = width
        self.color = color
        self.center = center
        self.angle = 0
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)

    def draw(self) -> None:
        self._turtle.clear()
        self._turtle.penup()
        self._turtle.goto(self.center)
        self._turtle.pensize(self.width)
        self._turtle.color(self.color)
        self._turtle.setheading(90 - self.angle)
        self._turtle.pendown()
        self._turtle.forward(self.length)

    def update(self, angle: float) -> None:
        self.angle = angle
        self.draw()
