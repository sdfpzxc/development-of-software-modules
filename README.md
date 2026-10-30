# backend-starter · МДК.01.01 «Разработка программных модулей»

Мой репозиторий на всю дисциплину. В нём будет собран сервис: код, тесты,
миграции, стенд. Здесь же лежат конспекты занятий и файлы, которые
раздавались на парах. Папки занятий появляются по ходу курса, забирать их
из шаблона вы будете сами, это описано в задании каждого занятия.

## Что понадобится

Python 3.12 и git. На Windows при установке Python отметьте галочку
*Add Python to PATH*. Проверить, что стоят:

| | macOS / Linux | Windows |
|---|---|---|
| Python | `python3 --version` | `py --version` |
| git | `git --version` | `git --version` |

## Что где лежит

### 📚 Домашние работы (по занятиям)

| № | Тема занятия | Перейти к файлам |
| :---: | :--- | :--- |
| **01** | Вводное: что такое backend | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_01 |
| **02** | Окружение, модули и пакеты | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_02 |
| **03** | Практикум «Сборка проекта» | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_03 |
| **04** | Практикум «Младший разработчик: первая неделя» | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_04 |
| **05** | Проверка типов до запуска | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_05 |
| **06** | Проверка типов: Pylance и mypy | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_06 |
| **07** | Докстринги в VS Code: генератор и проверка | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lesson_07 |

### 📁 Дополнительные материалы

| Раздел | Перейти к файлам |
| :--- | :--- |
| **Документация** | https://github.com/sdfpzxc/development-of-software-modules/tree/main/docs |
| **Лекции** | https://github.com/sdfpzxc/development-of-software-modules/tree/main/lectures |
| **Материалы** | https://github.com/sdfpzxc/development-of-software-modules/tree/main/materials |

## Как сдавать

Все задания сдаются в ветку `main`. Отдельную ветку для задания создавать
не нужно, Pull Request открывать тоже не нужно. Кладёте работу в папку
занятия, коммитите в `main` и отправляете на GitHub. Сообщение коммита
начинается с номера задания: `hw-06: проверка типов`.
Срок — до начала следующего занятия.

Всё делается кнопками в VS Code:

| Что нужно | Где посмотреть |
|---|---|
| отобрать файлы и закоммитить | [изменения и коммиты](docs/git/README.md#3-изменения-и-коммиты) |
| отправить коммиты на GitHub | [отправить на GitHub](docs/git/README.md#отправить-на-github) |
| забрать правки с GitHub, разобрать конфликт | [pull и fetch](docs/git/README.md#8-совместная-работа-pull-и-fetch) |

Полная версия разбора со всеми экранами — [docs/git/FULL.md](docs/git/FULL.md).

## Правила

- Сервис должен подниматься на чужом компьютере из скачанного репозитория,
  это проверяется на защите.
- ИИ можно после собственной попытки: разобрать ошибку, предложить тесты,
  поправить документацию. Вставленный код вы объясняете на review.
- На диагностике, контрольных и экзамене ИИ и поиск закрыты.
