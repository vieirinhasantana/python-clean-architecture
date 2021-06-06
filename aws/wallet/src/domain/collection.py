from typing import Generic, TypeVar
from dataclasses import dataclass

T = TypeVar('T')


@dataclass(frozen=True)
class Collection(Generic[T]):
    values: [T]

    def map(self, func) -> map:
        return map(func, self.values)
