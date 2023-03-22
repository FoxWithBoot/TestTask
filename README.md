# TestTask

## Задание
Необходимо разработать HTTP сервис для работы с импортируемыми данными.
Должна быть реализована загрузка данных в формате csv (напр. датасеты с Kaggle). Структура файлов неизвестна и может изменяться от файла к файлу.
Помимо загрузки файлов необходимо реализовать следующий функционал:
• Получение списка файлов с информацией о колонках
• Возможность получения данных из конкретного файла с опциональными фильтрацией и сортировкой по одному или нескольким столбцам

Использовать рекомендуется любой из языков: python, C++, C#,  можно применять любые библиотеки, фреймворки, базы данных и все, что покажется необходимым.

Дополнительно можно реализовать:
• Покрытие исходного кода тестами
• Авторизацию пользователя
• Дополнительные эндпойнты, напр. удаление ранее загруженного файла
• Dockerfile для запуска сервиса в Docker
• прочее

## Использованные инструменты
Python, Django, Django Rest Framework, Pandas, drf-yasg.

## API
![2023-03-22_17-00-02](https://user-images.githubusercontent.com/63101721/226928342-63793f15-92a5-4b72-9e9c-2ac05d0e1bb9.png)

## Развертывание
Локальное развертывание.
1. Подготовить основу проекта (создать папку, создать виртуальное окружение и тд.).
2. Клонировать репозиторий.
3. Установить необходимые библиотеки.
4. В командной строке прописать: python manage.py runserver
