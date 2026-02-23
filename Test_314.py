# """Тестовый скрипт для Python 3.14"""

# import sys
# import platform


# def main():
#     print(f"🐍 Python {sys.version}")
#     print(f"📍 Платформа: {platform.platform()}")
#     print(f"💻 Архитектура: {platform.machine()}")
#     print(f"✨ Python 3.14.3 готов к работе!")


# if __name__ == "__main__":
#     main()


"""Тест Python 3.14.3"""

import sys
import platform


def main():
    print("=" * 60)
    print("🐍 Python Environment Info")
    print("=" * 60)
    print(f"Python версия:     {sys.version}")
    print(f"Исполняемый файл: {sys.executable}")
    print(f"Платформа:        {platform.platform()}")
    print(f"Архитектура:      {platform.machine()}")
    print(f"Префикс venv:     {sys.prefix}")
    print("=" * 60)
    print("✨ Python 3.14.3 в виртуальном окружении работает!")
    print("=" * 60)


if __name__ == "__main__":
    main()
