from dataclasses import dataclass

from AnimeGoParser.anime_preview import AnimePreview


@dataclass
class Anime(AnimePreview):
    better_poster: str
    type: str
    episodes: str
    status: str
    genre: str
    release: str
    studio: str
    age_restriction: str
    duration: str
    description: str
    screens: list[str]
    trailer: str
