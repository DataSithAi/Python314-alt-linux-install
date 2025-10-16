# 🐍 Установка Python 3.14.0 в ALT Linux

![Python Version](https://img.shields.io/badge/Python-3.14.0-blue?style=for-the-badge&logo=python&logoColor=white)
![ALT Linux](https://img.shields.io/badge/ALT_Linux-11.1-red?style=for-the-badge&logo=linux&logoColor=white)
![Build](https://img.shields.io/badge/Build-Success-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Подробное руководство по компиляции и установке Python 3.14.0 из исходников на ALT Workstation K 11.1**

---

## 📋 Содержание

- [Требования](#-требования)
- [Установка зависимостей](#-установка-зависимостей)
- [Загрузка исходников](#-загрузка-исходников)
- [Компиляция Python](#-компиляция-python)
- [Проверка установки](#-проверка-установки)
- [Очистка](#-очистка)
- [Начало работы](#-начало-работы)
- [Решение проблем](#-решение-проблем)

---

## 🔧 Требования

### Системные требования

- **ОС**: ALT Workstation K 11.1 (Nemorosa) или выше
- **Архитектура**: x86_64
- **Свободное место**: ~500 MB для сборки, ~150 MB после установки
- **Права**: sudo/root доступ для установки

### Уже должно быть установлено

```bash
gcc --version    # GCC компилятор
make --version   # GNU Make
```

---

## 📦 Установка зависимостей

### Шаг 1: Установка библиотек разработки

Установите все необходимые библиотеки для сборки Python:

```bash
sudo apt-get install -y gcc make zlib-devel libffi-devel libssl-devel \
    bzlib-devel libreadline-devel libsqlite3-devel wget curl \
    libncurses-devel tk-devel libgdbm-devel liblzma-devel
```

### Что устанавливается:

| Пакет | Назначение |
|-------|------------|
| `gcc`, `make` | Компилятор и система сборки |
| `zlib-devel` | Сжатие данных |
| `libffi-devel` | Foreign Function Interface |
| `libssl-devel` | SSL/TLS поддержка |
| `bzlib-devel` | Сжатие bzip2 |
| `libreadline-devel` | Интерактивная командная строка |
| `libsqlite3-devel` | Встроенная база данных |
| `libncurses-devel` | Терминальный интерфейс |
| `tk-devel` | GUI библиотека Tkinter |
| `libgdbm-devel` | База данных DBM |
| `liblzma-devel` | LZMA сжатие (xz) |

> **💡 Примечание**: Система автоматически выберет правильные пакеты:
> - `bzip2-devel` → `bzlib-devel`
> - `openssl-devel` → `libssl-devel`

### Ожидаемый результат:

```
Следующие НОВЫЕ пакеты будут установлены:
  bzlib-devel   libffi-devel   liblzma-devel     libreadline-devel  
  libssl-devel  libsqlite3-devel  libncurses-devel  tk-devel  
  ... и другие зависимости
  
0 будет обновлено, 16 новых установлено
Необходимо получить 15,8MB архивов.
```

---

## 📥 Загрузка исходников

### Шаг 2: Скачивание Python 3.14.0

```bash
# Переход в временную директорию
cd /tmp

# Загрузка исходников Python 3.14.0
wget https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tar.xz

# Распаковка архива
tar -xf Python-3.14.0.tar.xz

# Переход в директорию с исходниками
cd Python-3.14.0
```

### Проверка загрузки:

```bash
ls -lh Python-3.14.0.tar.xz
# Ожидается: ~20-25 MB
```

---

## ⚙️ Компиляция Python

### Шаг 3: Конфигурация сборки

```bash
./configure --enable-optimizations --prefix=/usr/local
```

#### Параметры конфигурации:

- `--enable-optimizations` - включает оптимизации производительности (PGO)
- `--prefix=/usr/local` - устанавливает Python в `/usr/local`

> **⚠️ Важно**: Опция `--enable-optimizations` увеличивает время сборки, но улучшает производительность на 10-20%

### Шаг 4: Компиляция

```bash
make -j$(nproc)
```

- `-j$(nproc)` использует все доступные процессорные ядра для ускорения сборки

**⏱️ Время сборки**: 5-15 минут (зависит от процессора)

### Шаг 5: Установка

```bash
sudo make altinstall
```

> **🔴 КРИТИЧЕСКИ ВАЖНО**: Используйте **только** `altinstall`, **НЕ** `install`!
> 
> - `altinstall` - устанавливает Python как `python3.14` (безопасно)
> - `install` - перезаписывает системный `python3` (может сломать систему!)

### Ожидаемый вывод установки:

```
/usr/bin/ginstall -c -m 644 ./Misc/python.man \
    /usr/local/share/man/man1/python3.14.1
...
Successfully installed pip-25.2
```

---

## ✅ Проверка установки

### Шаг 6: Тестирование Python

```bash
# Проверка версии Python
python3.14 --version
# Вывод: Python 3.14.0

# Проверка версии pip
pip3.14 --version
# Вывод: pip 25.2 from /usr/local/lib/python3.14/site-packages/pip (python 3.14)

# Расположение исполняемого файла
which python3.14
# Вывод: /usr/local/bin/python3.14

# Список установленных пакетов
python3.14 -m pip list
# Вывод:
# Package    Version
# ---------- -------
# pip        25.2
```

### Проверка основных модулей:

```bash
# Тест базовой функциональности
python3.14 -c "print('Python 3.14.0 работает отлично! ✨')"

# Проверка стандартных модулей
python3.14 -c "import sys, json, sqlite3, ssl; print('Все основные модули загружены успешно!')"

# Информация о сборке
python3.14 -c "import sys; print(f'Python {sys.version}')"
# Вывод: Python 3.14.0 (main, Oct 16 2025, 11:47:30) [GCC 13.2.1 20240128 (ALT Sisyphus 13.2.1-alt3)]

# Проверка SSL/TLS
python3.14 -c "import ssl; print(f'OpenSSL версия: {ssl.OPENSSL_VERSION}')"
# Вывод: OpenSSL версия: OpenSSL 3.3.3 11 Feb 2025

# Пути к библиотекам
python3.14 -c "import sys; print('\n'.join(sys.path))"
# Вывод:
# /usr/local/lib/python314.zip
# /usr/local/lib/python3.14
# /usr/local/lib/python3.14/lib-dynload
# /usr/local/lib/python3.14/site-packages
```

---

## 🧹 Очистка

### Шаг 7: Удаление временных файлов

После успешной установки удалите исходники:

```bash
cd ~
sudo rm -rf /tmp/Python-3.14.0*
```

Проверка очистки:

```bash
ls -la /tmp/ | grep -i python
# Вывод должен быть пустым
```

---

## 🚀 Начало работы

### Создание виртуального окружения

**Рекомендуется** всегда работать в виртуальных окружениях:

```bash
# Создайте директорию проекта
mkdir ~/myproject
cd ~/myproject

# Создайте виртуальное окружение
python3.14 -m venv venv

# Активируйте окружение
source venv/bin/activate

# Теперь 'python' указывает на Python 3.14
python --version
# Вывод: Python 3.14.0

# Обновите pip
pip install --upgrade pip

# Установите необходимые пакеты
pip install requests numpy pandas

# Деактивация окружения
deactivate
```

### Создание тестового скрипта

```python
#!/usr/bin/env python3.14
"""Тестовый скрипт для Python 3.14"""

import sys
import platform

def main():
    print(f"🐍 Python {sys.version}")
    print(f"📍 Платформа: {platform.platform()}")
    print(f"💻 Архитектура: {platform.machine()}")
    print(f"✨ Python 3.14.0 готов к работе!")

if __name__ == "__main__":
    main()
```

Сохраните как `test.py` и запустите:

```bash
python3.14 test.py
```

### Полезные алиасы (опционально)

Добавьте в `~/.bashrc`:

```bash
# Алиасы для Python 3.14
alias py314='python3.14'
alias pip314='pip3.14'
```

Применить изменения:

```bash
source ~/.bashrc
py314 --version
```

---

## 🎯 Итоговая структура установки

```
/usr/local/
├── bin/
│   ├── python3.14           # Исполняемый файл Python
│   ├── pip3.14              # Менеджер пакетов pip
│   └── idle3.14             # IDLE IDE (опционально)
├── lib/
│   ├── python3.14/          # Стандартная библиотека
│   │   ├── site-packages/   # Установленные пакеты
│   │   └── lib-dynload/     # Динамические модули
│   └── libpython3.14.so     # Динамическая библиотека
├── include/
│   └── python3.14/          # Заголовочные файлы
└── share/
    └── man/man1/            # Документация
```

---

## 📊 Сравнение версий Python

| Компонент | Системный Python | Python 3.14.0 |
|-----------|------------------|---------------|
| **Команда** | `python3` | `python3.14` |
| **Версия** | 3.12.7 | 3.14.0 |
| **Расположение** | `/usr/bin/python3` | `/usr/local/bin/python3.14` |
| **pip** | `pip` / `pip3` | `pip3.14` |
| **Управление** | Системный пакетный менеджер | Собран вручную |

> **💡 Совет**: Системный Python остаётся нетронутым и используется системными утилитами

---

## 🔍 Решение проблем

### Проблема: Не найден пакет при установке зависимостей

**Решение**: Используйте точные имена пакетов для ALT Linux:

```bash
# Поиск правильного имени пакета
apt-cache search <название> | grep -i dev

# Примеры:
apt-cache search bzip2 | grep -i dev    # найдёт bzlib-devel
apt-cache search readline | grep -i dev # найдёт libreadline-devel
```

### Проблема: Ошибка при компиляции "missing openssl"

**Решение**: Убедитесь, что установлен `libssl-devel`:

```bash
sudo apt-get install libssl-devel
./configure --enable-optimizations --prefix=/usr/local --with-openssl=/usr
make -j$(nproc)
```

### Проблема: Нет доступа при удалении временных файлов

**Решение**: Используйте `sudo`:

```bash
sudo rm -rf /tmp/Python-3.14.0*
```

### Проблема: Python 3.14 не найден после установки

**Решение**: Проверьте PATH:

```bash
echo $PATH | grep -o '/usr/local/bin'

# Если пусто, добавьте в ~/.bashrc:
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Проблема: Конфликт версий pip

**Решение**: Всегда указывайте конкретную версию:

```bash
python3.14 -m pip install <package>    # Правильно
pip3.14 install <package>               # Правильно
pip install <package>                   # Может использовать системный pip
```

---

## 📚 Дополнительные ресурсы

- [Официальная документация Python 3.14](https://docs.python.org/3.14/)
- [Что нового в Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html)
- [ALT Linux Wiki](https://www.altlinux.org/)
- [Python Developer's Guide](https://devguide.python.org/)

---

## 📝 Changelog

### Python 3.14.0 (7 октября 2025)

Основные нововведения:

- 🚀 Улучшенная производительность интерпретатора
- 🔧 Экспериментальный JIT-компилятор
- 📦 Обновлённая стандартная библиотека
- 🐛 Улучшенные сообщения об ошибках
- 🔒 Обновлённые модули безопасности

---

## ⚖️ Лицензия

Python распространяется под лицензией **PSF (Python Software Foundation License)**, которая совместима с GPL.

Данное руководство распространяется под лицензией **MIT**.

---

## 👨‍💻 Авторы

Руководство составлено на основе успешной установки Python 3.14.0 на:
- **ОС**: ALT Workstation K 11.1 (Nemorosa) x86_64
- **DE**: KDE Plasma 6.4.4 (Wayland)
- **Дата**: 16 октября 2025

---

## 🎉 Заключение

Поздравляем! Теперь у вас установлена самая свежая версия Python 3.14.0, собранная с оптимизациями специально для вашей системы ALT Linux.

**Что дальше?**

1. ✅ Создавайте виртуальные окружения для проектов
2. ✅ Устанавливайте необходимые библиотеки через pip
3. ✅ Изучайте новые возможности Python 3.14
4. ✅ Наслаждайтесь разработкой! 🐍✨

---

<div align="center">

**Сделано с ❤️ для сообщества ALT Linux**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)
![ALT Linux](https://img.shields.io/badge/Tested%20on-ALT%20Linux-red?style=flat-square&logo=linux)

</div>