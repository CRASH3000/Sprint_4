from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        long_name = "A" * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    # тест для проверки добавления дублирующей книги
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Harry Potter")
        assert len(collector.get_books_genre()) == 1

    # тест для проверки установки жанра книги
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.set_book_genre("Harry Potter", "Фантастика")
        assert collector.get_book_genre("Harry Potter") == "Фантастика"

    # тест для проверки получения жанра книги
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.set_book_genre("Harry Potter", "Фантастика")
        assert collector.get_book_genre("Harry Potter") == "Фантастика"

    # тест для проверки получения списка книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Dracula")
        collector.set_book_genre("Harry Potter", "Фантастика")
        collector.set_book_genre("Dracula", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Harry Potter"]
        assert collector.get_books_with_specific_genre("Ужасы") == ["Dracula"]

    # тест для проверки получения словаря books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        assert "Harry Potter" in collector.get_books_genre()

    # тест для проверки получения книг, подходящих детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Dracula")
        collector.set_book_genre("Harry Potter", "Фантастика")
        collector.set_book_genre("Dracula", "Ужасы")
        assert collector.get_books_for_children() == ["Harry Potter"]
        assert "Dracula" not in collector.get_books_for_children()

    # тест для проверки добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        assert "Harry Potter" in collector.get_list_of_favorites_books()

    # тест для проверки удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        collector.delete_book_from_favorites("Harry Potter")
        assert "Harry Potter" not in collector.get_list_of_favorites_books()

    # тест для проверки получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Dracula")
        collector.add_book_in_favorites("Harry Potter")
        collector.add_book_in_favorites("Dracula")
        assert collector.get_list_of_favorites_books() == [
            "Harry Potter",
            "Dracula",
        ]

    # тест для проверки добавления книги в избранное, если её нет в словаре books_genre
    def test_add_book_in_favorites_not_in_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Not in Genre")
        assert "Not in Genre" not in collector.get_list_of_favorites_books()

    # тест для проверки удаления книги из избранного, если её там нет
    def test_delete_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.delete_book_from_favorites("Harry Potter")
        assert "Harry Potter" not in collector.get_list_of_favorites_books()

    # тест для проверки получения книг с несуществующим жанром
    def test_get_books_with_non_existent_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.set_book_genre("Harry Potter", "Фантастика")
        assert collector.get_books_with_specific_genre("Non-Existent Genre") == []

    # тест для проверки получения книг для детей, когда книги отсутствуют
    def test_get_books_for_children_with_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    # тест для проверки, что словарь books_genre изначально пуст
    def test_get_books_genre_initially_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # тест для проверки, что у добавленной книги нет жанра
    def test_added_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        assert collector.get_book_genre("Harry Potter") == ""
