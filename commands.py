from typing import Tuple

from exceptions import MoveParamsReadError, MoveParamsSetError
from abstracts import Rotatable, Movable
from utils import Vector


class Move:
    """Класс движения объекта по прямой."""

    def __init__(self, m: Movable) -> None:
        self.m = m

    def _read_params(self) -> Tuple[Vector, Vector]:
        try:
            position = self.m.get_position()
            velocity = self.m.get_velocity()
        except Exception as e:
            raise MoveParamsReadError(f"Can't read params for moving object[{self.m}]") from e

        return position, velocity

    def execute(self) -> None:
        position, velocity = self._read_params()
        new_position = position + velocity

        try:
            self.m.set_position(new_position)
        except Exception as e:
            raise MoveParamsSetError(f"Can't set params for moving object[{self.m}]") from e


class Rotate:
    """Класс поворота объекта."""

    def __init__(self, r: Rotatable) -> None:
        self.r = r

    def execute(self):
        new_direction = (
            (self.r.get_direction() + self.r.get_angular_velocity())
            % self.r.get_directions_number()
        )
        self.r.set_direction(new_direction)
