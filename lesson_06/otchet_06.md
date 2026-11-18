# Отчёт · Проверка типов: Pylance и mypy

**Студент:** Геращенко Ксения, группа 9/2-РПО-25/3
**Номер в журнале:** 3, вариант шага 4: 1

Работа выполнена на втором архиве проекта «Отчёт кафе»
(`lesson_06/otchet-kafe-start`), глава 4.3.

## 1. Редактор до настройки

В корне проекта создан файл `proba.py` с двумя неверными вызовами:
`format_title(40)` и `format_kopeks("1250")`. Выбран интерпретатор
из окружения проекта, внизу справа окна написано `.venv (__.venv (3.12.12))`.

![proba.py в режиме off](img/06-01-off.png)

В режиме `off` в файле подчёркнуто ___ аргументов. Ошибки типов в этом
режиме не показываются, аннотации идут только в подсказки.

## 2. Включение режима basic

Настройка `python.analysis.typeCheckingMode` выбрана на вкладке Workspace,
поэтому VS Code записал её в файл `.vscode/settings.json` внутри проекта.

![settings.json с режимом basic](img/06-02-settings.png)

## 3. Ошибки в редакторе

После смены режима в `proba.py` подчёркнуты 40 и "1250". На вкладке
после имени файла стоит цифра 2.

![Подчёркнутые аргументы в proba.py](img/06-03-squiggle.png)

Сообщение над `40`:

![Сообщение Pylance над 40](img/06-04-hover.png)

Pylance называет тип переданного значения `Literal[40]`. Параметр `text`
функции `format_title` ожидает тип `str`. Правило, по которому
выдано сообщение, называется `reportArgumentType`.

## 4. Моя ошибка и панель Problems

Мой вариант — 1. В `proba.py` добавлен вызов `, он стоит
Мой вариант — 1. В `proba.py` добавлен вызов `, он стоит
в строке 4. Функция объявлена в модуле `app.utils.formatter`, её подпись:
`def format_kopeks(kopeks: int) -> str`.

![Панель Problems с тремя ошибками](img/06-05-problems.png)

В панели Problems у `proba.py` 2 ошибки. Моя ошибка стоит
на месте `[Ln 4, Col 22]`, её короткая причина в конце сообщения:
`"str" is not assignable to "int"`.

## 5. Четыре режима на одном файле

Файл `rezhimy.py` проверен во всех четырёх режимах.
Число сообщений в панели Problems:

| Режим | Сообщений |
|---|---|
| `off` | 1 |
| `basic` | 2 |
| `standard` | 3 |
| `strict` | 9 |

![rezhimy.py в режиме strict](img/06-06-strict.png)

Только в `standard` и `strict` появилось сообщение про переменную
`label`: `"label" is possibly unbound`. После опыта возвращён режим `basic`.

## 6. Ошибки в терминале

Версия mypy: `1.15.0 (compiled: yes)`. Команда `mypy proba.py` закончилась строкой
`Found  **2** errors in **1** file (checked **1** source file)`.

![mypy proba.py с ошибками](img/06-07-mypy-errors.png)

Строка с моей ошибкой: ` **Argument 1 to "format_kopeks" has incompatible type "str"; expected "int"** [**arg-type**]`.
В сообщении mypy параметр назван `Argument 1`, а Pylance называл его `kopeks`.

## 7. Исправление

Исправленные вызовы:

| Было | Стало |
|---|---|
| `format_title(40)` | `format_title(" Итог ")` |
| `format_kopeks("1250")` | `format_kopeks(125000)` |

После сохранения файла проверка повторена.

![mypy без ошибок](img/06-08-mypy-success.png)

`mypy proba.py`: `Success: no issues found in 1 source file`.
`mypy app`: `Success: no issues found in 15 source files`.

## 8. Проект без аннотаций

На первом архиве mypy вывел `Found 17 errors in 10 files`.
У всех ошибок код `no-untyped-def`. Ошибки появились потому, что в `pyproject.toml`
включён параметр `disallow_untyped_defs`.

![mypy на первом архиве](img/06-09-bez-tipov.png)

Первая строка списка: `app\domain\order.py:11: error: Function is missing a return type annotation [no-untyped-def]`.

## 9. Какой тип видит проверка

![Тип bounds в редакторе и в терминале](img/06-10-tip.png)

Pylance при наведении на `bounds` показал `tuple[int, int]`. mypy в строке
`reveal_type` вывел `uple[builtins.int, builtins.int]`.

## 10. Итог

Если Pylance ошибок не показывает, а mypy показывает, первым делом
проверяю, сохранён ли файл на диске (Pylance проверяет текст в редакторе на лету, а mypy читает только сохранённые файлы).

Не получилось: ничего

ИИ: не использовался 
