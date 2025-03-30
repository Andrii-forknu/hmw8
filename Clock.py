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

class Theme(Protocol):
    background_color: str
    face_color: str
    digit_color: str
    hour_hand_color: str
    minute_hand_color: str
    second_hand_color: str


class LightTheme:
    background_color = "white"
    face_color = "#f0f0f0"
    digit_color = "black"
    hour_hand_color = "black"
    minute_hand_color = "blue"
    second_hand_color = "red"


class Watch(ABC):
    def init(self, theme: Theme = LightTheme()):
        self.theme = theme
        self.screen = turtle.Screen()
        self.configure_screen()

    def configure_screen(self) -> None:
        self.screen.bgcolor(self.theme.background_color)
        self.screen.title("Python Turtle Watch")
        self.screen.tracer(0)

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    def run(self, update_interval: float = 1.0) -> None:
        self.setup()
        while True:
            try:
                self.update()
                self.screen.update()
                time.sleep(update_interval)
            except (KeyboardInterrupt, turtle.Terminator):
                break


class AnalogWatch(Watch):
    def init(self, theme: Theme = LightTheme(), radius: float = 200):
        super().init(theme)
        self.radius = radius
        self.clock_face = ClockFace(radius)
        self.hour_hand = Hand(radius * 0.5, 6, theme.hour_hand_color)
        self.minute_hand = Hand(radius * 0.7, 4, theme.minute_hand_color)
        self.second_hand = Hand(radius * 0.9, 2, theme.second_hand_color)

    def setup(self) -> None:
        self.clock_face.setup()
        self.clock_face.draw()

    def update(self) -> None:
        current_time = datetime.now()
        second_angle = current_time.second * 6
        minute_angle = current_time.minute * 6 + current_time.second * 0.1
        hour_angle = (current_time.hour % 12) * 30 + current_time.minute * 0.5
        self.hour_hand.update(hour_angle)
        self.minute_hand.update(minute_angle)
        self.second_hand.update(second_angle)


def main():
    analog_clock = AnalogWatch(theme=LightTheme())
    analog_clock.run(update_interval=1.0)


if name == "main":
    main()
