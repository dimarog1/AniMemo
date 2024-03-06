from dataclasses import dataclass


@dataclass
class AnimePreview:
    name: str
    russian: str
    poster: str
    rating: float
    ref: str
