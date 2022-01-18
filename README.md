# otus-aqa
Репозиторий для домашних заданий курса https://otus.ru/lessons/avtomatizaciya-web-testirovaniya/?utm_source=github&amp;utm_medium=free&amp;utm_campaign=otus

Описание работы скрипта log_parser.py:\
Принимает на вход обязательный аргумент -p, в который необходимо указать путь к *.log файлу или директорию.
В случае указания пути к директорию, парсит все *.log файлы в нем.\
Пример запуска: python log_parser.py -p access.log

Результат работы скрипта:\
Выводит в stdout результат парсинга для каждого лога в json формате. Сохраняет результат парсинга каждого лога в файл 
{log_name}.json.