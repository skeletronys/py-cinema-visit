from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cinema_cleaner)
