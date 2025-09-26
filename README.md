# Cafe Web System

Учбовий репозиторій для практичної роботи: вебсистема замовлень для кав'ярні.

## Мета
Створити простий прототип вебсистеми з frontend на React, backend на FastAPI та базою даних MySQL.

## Структура репозиторію
- `frontend/` — приклад React-застосунку (placeholder).
- `backend/` — приклад FastAPI сервера (placeholder).
- `db/` — SQL-схема (placeholder).
- `docs/` — документи: ТЗ, архітектура, вибір стеку.
- `README.md` — цей файл.

## Як працювати локально (швидка інструкція)
1. Ініціалізувати локальний репозиторій (якщо ще не зроблено):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Створити віддалений репозиторій на GitHub (назва наприклад `cafe-web-system`) і пов'язати:
```bash
git remote add origin https://github.com/USERNAME/cafe-web-system.git
git branch -M main
git push -u origin main
```

3. Для нової задачі створити гілку за GitHub Flow:
```bash
git checkout -b feature/назва-фічі
# після роботи
git add .
git commit -m "Опис змін"
git push origin feature/назва-фічі
```

4. Коли фічa готова — створити Pull Request у GitHub і змерджити в `main`.

## Документи
- docs/architecture.png — діаграма архітектури (вставити вручну, якщо необхідно).
- docs/technical_task.docx — ТЗ (можна згенерувати/вставити).

## Примітка
Це шаблон репозиторію для студентської практики. Ви можете змінювати структуру відповідно до вимог викладача.
