# qa_python - Sprint 4

## Список реализованных тестов

### Добавление новых книг
- `test_add_new_book_with_long_name()` — Проверка добавления книги с именем более 40 символов.
- `test_add_new_book_duplicate()` — Проверка добавления дублирующей книги.

### Установка и получение жанров книг
- `test_set_book_genre()` — Проверка установки жанра книги.
- `test_get_book_genre()` — Проверка получения жанра книги.
- `test_added_book_has_no_genre()` — Проверка, что у добавленной книги нет жанра.

### Получение списка книг с определённым жанром
- `test_get_books_with_specific_genre()` — Проверка получения списка книг с определённым жанром.
- `test_get_books_with_non_existent_genre()` — Проверка получения книг с несуществующим жанром.

### Получение словаря books_genre
- `test_get_books_genre()` — Проверка получения словаря `books_genre`.
- `test_get_books_genre_initially_empty()` — Проверка, что словарь `books_genre` изначально пуст.

### Получение книг, подходящих детям
- `test_get_books_for_children()` — Проверка получения книг, подходящих детям.
- `test_books_for_children_excludes_age_restricted()` — Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей.
- `test_get_books_for_children_with_no_books()` — Проверка получения книг для детей, когда книги отсутствуют.

### Управление избранными книгами
- `test_add_book_in_favorites()` — Проверка добавления книги в избранное.
- `test_add_book_in_favorites_not_in_genre()` — Проверка добавления книги в избранное, если её нет в словаре `books_genre`.
- `test_delete_book_from_favorites()` — Проверка удаления книги из избранного.
- `test_delete_book_not_in_favorites()` — Проверка удаления книги из избранного, если её там нет.
- `test_get_list_of_favorites_books()` — Проверка получения списка избранных книг.