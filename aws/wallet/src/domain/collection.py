# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Collection(Generic[T]):
    values: [T]

    def map(self, func) -> map:
        return map(func, self.values)
