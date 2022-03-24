from abc import ABC, abstractmethod


class Anime(ABC):

    @abstractmethod
    def print_info(self):
        ...


class Adventures(Anime):
    adventures = ['Бездомный Бог', 'Стальной Алхимик', 'Наруто']

    def print_info(self):
        return self.adventures


class Fantasy(Anime):
    fantasy = ['Атака Титанов', 'Мастер меча онлайн', 'Сделанно в Бездне']

    def print_info(self):
        return self.fantasy


class Drama(Anime):
    drama = ['Домекано', 'Токийский гуль', 'Убийца Акаме']

    def print_info(self):
        return self.drama


def result(name):
    return name.print_info()


animeAdventures = Adventures()
animeFantasy = Fantasy()
animeDrama = Drama()

print(result(animeAdventures))
print(result(animeFantasy))
print(result(animeDrama))
