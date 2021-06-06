# -*- coding: utf-8 -*-
from dataclasses import dataclass

from src.domain.collection import Collection


@dataclass(frozen=True)
class Wallet:
    id: int
    name: str


@dataclass(frozen=True)
class Wallets(Collection[Wallet]):
    values = [Wallet]
