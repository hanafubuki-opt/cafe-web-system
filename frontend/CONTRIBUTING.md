# CONTRIBUTING

## Strategy: GitHub Flow (спрощений)
1. `main` — завжди робоча стабільна гілка (production-ready).
2. Для кожної нової задачі створюйте гілку `feature/<коротка-назва>`.
3. Працюйте у своїй feature-гілці, робіть коміти, пуші.
4. Коли готово — створіть Pull Request у `main`.
5. Після рев'ю та тестування зливати PR у `main`.
6. Якщо знадобиться швидкий виправлення в production — створюйте `hotfix/<назва>` і робіть PR.

## Приклади команд
```bash
# Створення гілки
git checkout -b feature/login-form

# Пуш нової гілки
git push origin feature/login-form

# Забрати останні зміни з main перед початком роботи:
git checkout main
git pull origin main
git checkout -b feature/new-feature
```
