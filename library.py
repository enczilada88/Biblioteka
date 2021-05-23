import random
from datetime import date


class Movie:
    def __init__(self, title: str, year: int, genre: int) -> str:
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.views = 0

    def __str__(self)-> str:
        return f"{self.title} ({self.year})"

    def play(self)-> str:
        self.views += 1
        return print(self)


class Series(Movie):
    def __init__(self, season: int, episode: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} - {self.season}{self.episode}"


class LibraryAll:
    def __init__(self):
        self.library_database = [
            Movie(title="Movie 1", year="2001", genre="horror"),
            Movie(title="Movie 2", year="2019", genre="fantazy"),
            Movie(title="Movie 3", year="2012", genre="drama"),
            Movie(title="Movie 4", year="2012", genre="thriller"),
            Series(title="Series 1", year="2011", genre="comedy", season="S01", episode="E01"),
            Series(title="Series 2", year="2011", genre="animated", season="S01", episode="E05"),
            Series(title="Series 3", year="2011", genre="documentary", season="S03", episode="E03")
        ]

    def get_movies(self):
        self.movies_only = [item for item in self.library_database if (isinstance(item, Movie) and not isinstance(item, Series))]
        return sorted(self.movies_only, key=lambda movie: movie.title)

    def get_series(self):
        self.series_only = [item for item in self.library_database if isinstance(item, Series)]
        return sorted(self.series_only, key=lambda series: series.title)

    def search(self, keyword):
        keyword=input("What movie are you searching for in Library?-provide title & check the status:")
        for item in self.library_database:
            if item.title == keyword:
                return item


    def generate_views(self):
        self.library_database[random.randint(0, len(self.library_database)-1)].views += random.randint(100, 1000)
        return True

    def top_titles(self, content_type=None, top_counter=3):
        if content_type == None:
            return sorted(self.library_database, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Movie":
            self.movies_only = [item for item in self.library_database if (isinstance(item, Movie) and not isinstance(item, Series))]
            return sorted(self.movies_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Series":
            self.series_only = [item for item in self.library_database if isinstance(item, Series)]
            return sorted(self.series_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        else:
            return 0


if __name__ == "__main__":
    print('--**' * 150)
    print("\n Welcome to Movies and Series Library!\n")
    print('--**' * 150)

# get.movies
    libAll = LibraryAll()
    print("Available movies listed below:\n")
    for movie in libAll.get_movies():
        print(movie.title)

    print('--' * 100)
# get.series
    print("Available series listed below:\n")
    for series in libAll.get_series():
        print(f"{series.title} {series.season}{series.episode}")
    print('--' * 100)
# search
    print("Check below if the movie is available in Library:\n")
    print(libAll.search("Movie 1"))

    print('--' * 100)
# generate.view
    print("Generate_views():\n")
    for i in range(10):
        libAll.generate_views()
# top titles
    print(f"The most popular movies  of {date.today()}:\n")
    for item in libAll.top_titles(content_type="Movie", top_counter=3):
        print(f"{item.title}: {item.views}")
    print('-' * 100)

    print(f"The most popular series of {date.today()}:\n")
    for item in libAll.top_titles(content_type="Series", top_counter=3):
        print(f"{item.title}: {item.views}")
    print('-' * 100)
