from django.contrib.auth.models import User
from movies.models import Person, Genre, Movie, MovieTheater


def test_user_table_isHealthy():
    number_of_users = len(User.objects.all())
    assert number_of_users == 1

    User.objects.create(username="thedy", password="12345")
    number_of_users = len(User.objects.all())
    assert number_of_users == 2

    user = User.objects.get(id=1)
    user.delete()
    number_of_users = len(User.objects.all())
    assert number_of_users == 1


def test_people_table_is_healthy():
    amount_of_people = len(Person.objects.all())
    assert amount_of_people == 3

    Person.objects.create(name="Al paccino")
    amount_of_people = len(Person.objects.all())
    assert amount_of_people == 4

    person = Person.objects.get(id=3)
    person.delete()
    amount_of_people = len(Person.objects.all())
    assert amount_of_people == 3


def test_movies_table_is_healthy():
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 1

    Movie.objects.create(
        title="Carrie", direction=Person.objects.create(name="Kimberly Peirce")
    )
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 2

    movie = Movie.objects.get(id=1)
    movie.delete()
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 1


def test_movies_table_is_healthy():
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 1

    Movie.objects.create(
        title="Carrie", direction=Person.objects.create(name="Kimberly Peirce")
    )
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 2

    movie = Movie.objects.get(id=1)
    movie.delete()
    number_of_movies = len(Movie.objects.all())
    assert number_of_movies == 1
