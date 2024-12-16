# Конфигурационное управление
Домашнее задание №1
## Вариант 11
### Задание 1
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу

эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.

Эмулятор должен запускаться из реальной командной строки, а файл с

виртуальной файловой системой не нужно распаковывать у пользователя.

Эмулятор принимает образ виртуальной файловой системы в виде файла формата

tar. Эмулятор должен работать в режиме GUI.

Конфигурационный файл имеет формат ini и содержит:

• Имя пользователя для показа в приглашении к вводу.

• Имя компьютера для показа в приглашении к вводу.

• Путь к архиву виртуальной файловой системы.

• Путь к лог-файлу.

• Путь к стартовому скрипту.

Лог-файл имеет формат xml и содержит все действия во время последнего

сеанса работы с эмулятором. Для каждого действия указан пользователь.

Стартовый скрипт служит для начального выполнения заданного списка

команд из файла.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также

следующие команды:

1. tail.

2. cp.

Все функции эмулятора должны быть покрыты тестами, а для каждой из

поддерживаемых команд необходимо написать 3 теста.

---

## Эмулятор оболочки ОС с GUI

### Описание

Этот проект — эмулятор оболочки операционной системы с графическим интерфейсом (GUI). 

Он имитирует работу UNIX-подобной командной строки с поддержкой базовых команд:

- `ls` — вывод содержимого текущей директории.
  
- `cd` — переход в другую директорию.
  
- `exit` — завершение работы эмулятора.

### Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/kcatrina/Konfig1.git
   cd Konfig1
   ```

2. **Установите зависимости:**

Убедитесь, что у вас установлен Python 3, а также необходимые библиотеки. 

Если в проекте есть файл requirements.txt, выполните:
```
pip install -r requirements.txt
```

**3. Настройте config.ini:**

Укажите нужные параметры, например:
```
[Settings]
username = your_username
hostname = your_hostname
vfs_path = path/to/virtual_fs.tar
log_path = path/to/log.xml
startup_script = path/to/start.txt
```

### Запуск

Запустите эмулятор:
```
python main.py
```

### Возможности

- Выполнение базовых команд (ls, cd, exit).
  
- Логирование действий пользователя в формате XML.
  
- Автоматическое выполнение стартовых скриптов.

### Структура проекта

- main.py — основной файл запуска.
  
- config.ini — настройки эмулятора.

- ezy.tar — пример виртуальной файловой системы.

- log.xml — файл для записи логов.

- start.txt — стартовый скрипт команд.

- tests.py — тесты для проверки функциональности.
