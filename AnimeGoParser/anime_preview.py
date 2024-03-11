from dataclasses import dataclass


@dataclass
class AnimePreview:
    name: str
    russian: str
    poster: str
    rating: str
    ref: str
    ref_encoded: str
