# Запуск автотестов для разных языков интерфейса
## Начало работы
### Настройка виртуального окружения

Windows:
   - cd different-languages-pytest
   - python -m venv selenium_env
   - selenium_env/bin/activate.bat
     
Linux:
   - cd different-languages-pytest
   - python3 -m venv selenium_env
   - source selenium_env/bin/activate

### Установка зависимостей:

   pip install -r requirements.txt

### Запуск тестов:

1) Тест в репозитории можно запустить командой pytest `--language=es`, тест успешно проходит.
2) Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду `time.sleep(30)` сразу после открытия ссылки. Запустите тест с параметром `--language=fr` и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".