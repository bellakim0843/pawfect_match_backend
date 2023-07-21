import strawberry
import typing


@strawberry.type
class Movie:
    title: str
    year: int
    rating: int


movies_db = [
    Movie(title="Inside Out", year=2016, rating=9),
]


@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> typing.List[Movie]:
        return movies_db

    @strawberry.field
    def movie(self, movie_pk: int) -> Movie:
        return movies_db[movie_pk - 1]


schema = strawberry.Schema(query=Query)
