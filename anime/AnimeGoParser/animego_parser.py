import requests
from pyquery import PyQuery as pq

from anime.AnimeGoParser.anime import Anime
from anime.AnimeGoParser.anime_preview import AnimePreview


class AnimeGoParser:
    def __init__(self, base_url=r'https://animego.org'):
        self.base_url = base_url

    def search_anime(self, name: str, first=False, search_ref='/search/anime?q='):
        response = pq(url=self.base_url + search_ref + name)
        animes = response('.animes-grid-item')
        if not animes:
            return None

        if first:
            return AnimePreview(*self.get_preview_data(next(animes.items())))
        res = [AnimePreview(*self.get_preview_data(anime)) for anime in animes.items()]
        return res

    def get_preview_data(self, anime: pq):
        params = (self.get_name, self.get_russian, self.get_poster, self.get_rating, self.get_ref)
        return (param(anime) for param in params)

    def get_anime_data(self, preview: AnimePreview):
        if not preview or requests.get(preview.ref).status_code != 200:
            return None
        page = pq(url=preview.ref)
        parsed_data = [data.text() for data in page('.anime-info .col-6').items()]
        anime_data = dict()
        for i in range(0, len(parsed_data), 2):
            anime_data[parsed_data[i]] = parsed_data[i + 1]

        type_ = ''
        episodes = ''
        status = ''
        genre = ''
        release = ''
        studio = ''
        age_restriction = ''
        duration = ''
        for key, value in anime_data.items():
            if key == 'Тип':
                type_ = value
            elif key == 'Эпизоды':
                episodes = value
            elif key == 'Статус':
                status = value
            elif key == 'Жанр':
                genre = value
            elif key == 'Выпуск':
                release = value
            elif key == 'Студия':
                studio = value
            elif key == 'Возрастные ограничения':
                age_restriction = value
            elif key == 'Длительность':
                duration = value

        description = page('.description').text()
        screens = [self.base_url + screen.attr('href') for screen in
                   page('.screenshots-block .screenshots-item').items()]
        trailer_html = page('.video-block .video-item')
        trailer = {'href': trailer_html.attr('href'), 'data-original': trailer_html.attr('data-original')}

        poster = page('.anime-poster img').attr('srcset').split()[0]

        return Anime(preview.name, preview.russian, preview.poster, preview.rating, preview.ref, poster, type_, episodes,
                     status, genre, release, studio, age_restriction, duration, description, screens, trailer)

    def get_name(self, anime: pq):
        name = anime('.text-gray-dark-6').text()
        return name

    def get_russian(self, anime: pq):
        russian = anime('.h5').text()
        return russian

    def get_poster(self, anime: pq):
        poster = anime('.anime-grid-lazy').attr('data-original')
        return poster

    def get_rating(self, anime: pq):
        rating = anime('.p-rate-flag__text').text().replace(',', '.')
        return float(rating)

    def get_ref(self, anime: pq):
        ref = anime('.h5 a').attr('href')
        return ref
