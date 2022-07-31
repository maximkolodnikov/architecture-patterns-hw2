from commands import Move
from utils import Vector
import pytest
from exceptions import MoveParamsReadError, MoveParamsSetError


def test_correct_move(spaceship):
    Move(spaceship).execute()
    position_after = spaceship.position

    assert position_after == Vector([5, 8])


def test_read_position_raises_error(spaceship, monkeypatch):
    def _get_position(self):
        raise Exception('Read blocked')

    monkeypatch.setattr(spaceship, 'get_position', _get_position)

    with pytest.raises(MoveParamsReadError):
        Move(spaceship).execute()


def test_read_velocity_raises_error(spaceship, monkeypatch):
    def _get_velocity(self):
        raise Exception('Read blocked')

    monkeypatch.setattr(spaceship, 'get_velocity', _get_velocity)

    with pytest.raises(MoveParamsReadError):
        Move(spaceship).execute()


def test_set_position_raises_error(spaceship, monkeypatch):
    def _set_position(self):
        raise Exception('Set blocked')

    monkeypatch.setattr(spaceship, 'set_position', _set_position)

    with pytest.raises(MoveParamsSetError):
        Move(spaceship).execute()
