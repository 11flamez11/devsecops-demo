# DevSecOps Security Demo

## Тестирование Security Gate

### Сценарий 1: С уязвимостями
1. Добавьте `src/vulnerable_code.py`
2. Создайте Pull Request
3. GitHub Actions заблокирует мерж

### Сценарий 2: Без уязвимостей
1. Удалите `src/vulnerable_code.py`
2. GitHub Actions разрешит мерж