from abc import ABC, abstractmethod
import turtle
import time
from datetime import datetime
from typing import Protocol


class Digit:
    def __init__(self, value: int, position: tuple[float, float], size: float = 1.0):
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
    def __init__(self, radius: float, center: tuple[float, float] = (0, 0)):
        self.radius = radius
        self.center = center
        self.digits: list[Digit] = []
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)

