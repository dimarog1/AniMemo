import requests
from pyquery import PyQuery as pq
from urllib.parse import quote

from AnimeGoParser.anime import Anime
from AnimeGoParser.anime_preview import AnimePreview


class AnimeGoParser:
    def __init__(self, base_url=r'https://animego.org'):
        self.base_url = base_url

    def search_anime_preview(self, name: str, first=False, search_ref='/search/anime?q='):
        if not name:
            return None
        response = pq(url=self.base_url + search_ref + name)
        animes = response('.animes-grid-item')
        if not animes:
            return None

        if first:
            return AnimePreview(*self.get_preview_data(next(animes.items())))
        res = [AnimePreview(*self.get_preview_data(anime)) for anime in animes.items()]
        return res

    def get_preview_data(self, anime: pq):
        params = (self.get_name_preview,
                  self.get_russian_preview,
                  self.get_poster_preview,
                  self.get_rating_preview,
                  self.get_ref_preview,
                  self.get_ref_encoded_preview)
        return (param(anime) for param in params)

    def get_anime(self, url: str):
        if not url or requests.get(url).status_code != 200:
            return None
        page = pq(url=url)
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
        trailer = trailer_html.attr('href')
        if trailer:
            trailer_id = trailer.split('/')[-1]
            if 'watch' in trailer_id:
                trailer = 'https://youtube.com/embed/' + trailer_id.split('=')[-1]
            else:
                trailer = 'https://youtube.com/embed/' + trailer_id

        poster = page('.anime-poster img').attr('srcset').split()[0]

        return Anime(self.get_name(page), self.get_russian(page), self.get_poster(page), self.get_rating(page), url,
                     quote(url), poster, type_, episodes, status, genre, release, studio, age_restriction, duration,
                     description, screens, trailer)

    def get_name(self, anime: pq):
        name = anime('.anime-title .list-unstyled').text().split('\n')[0]
        return name

    def get_russian(self, anime: pq):
        russian = anime('.anime-title h1').text()
        return russian

    def get_poster(self, anime: pq):
        poster = anime('.anime-poster img').attr('srcset').split()[0]
        return poster

    def get_rating(self, anime: pq):
        rating = anime('.itemRatingBlock .rating-value').text().replace(',', '.')
        return round(float(rating), 1)

    def get_name_preview(self, anime: pq):
        name = anime('.text-gray-dark-6').text()
        return name

    def get_russian_preview(self, anime: pq):
        russian = anime('.h5').text()
        return russian

    def get_poster_preview(self, anime: pq):
        poster = anime('.anime-grid-lazy').attr('data-original')
        return poster

    def get_rating_preview(self, anime: pq):
        rating = anime('.p-rate-flag__text').text().replace(',', '.')
        try:
            rating = round(float(rating), 1)
        except ValueError as e:
            print(e)
            print(rating)
            return 0
        return rating

    def get_ref_preview(self, anime: pq):
        ref = anime('.h5 a').attr('href')
        return ref

    def get_ref_encoded_preview(self, anime: pq):
        ref = anime('.h5 a').attr('href')
        ref_encoded = quote(ref)
        return ref_encoded


api = AnimeGoParser()
