## Every piece of the maze is made up of squares, aka they should have information about it

from dataclasses import dataclass

from maze_solver.models.role import Role
from maze_solver.models.border import Border

@dataclass(frozen=True)
class Square:
    index: int
    row : int
    col : int
    border : Border
    role : Role