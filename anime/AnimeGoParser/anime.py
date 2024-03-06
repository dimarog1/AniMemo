from dataclasses import dataclass

from anime.AnimeGoParser.anime_preview import AnimePreview


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
    trailer: dict

    def copy(self, preview: AnimePreview):
        self.name = preview.name
        self.russian = preview.russian
        self.poster = preview.poster
        self.rating = preview.rating
        self.ref = preview.ref
