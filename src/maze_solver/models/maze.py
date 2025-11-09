from dataclasses import dataclass
from typing import Iterator
from functools import cached_property

from maze_solver.models.square import Square

# Using a Tuple (immutable) for now to represent the maze, will be changed to a List
# For an ever-growing and changing maze, like in the maze runner movie

# Something to think about
# Python’s cache requires memoized function arguments to be hashable and, therefore, immutable.

@dataclass(frozen=True)
class Maze:
    layout: tuple[Square, ...]

def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

def __getitem__(self, index: int) -> Square:
        return self.squares[index]

@cached_property
def width(self):
       return max(square.col for square in self) + 1

@cached_property
def height(self):
       return max(square.row for square in self) + 1

