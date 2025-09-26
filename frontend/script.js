const API = "http://127.0.0.1:8000/api/users";

// Функція для завантаження користувачів
async function loadUsers() {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/users/");
    const users = await res.json();

    const list = document.getElementById("users");
    list.innerHTML = "";
    users.forEach(u => {
      const li = document.createElement("li");
      li.textContent = `${u.name} (${u.email})`;
      list.appendChild(li);
    });
  } catch (e) {
    console.error("Помилка:", e);
  }
}

// Функція для створення користувача
async function addUser() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  const res = await fetch("http://127.0.0.1:8000/api/users/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email })
  });

  if (res.ok) {
    loadUsers();
  } else {
    alert("Помилка при додаванні користувача!");
  }
}

// Подія при натисканні кнопки "Додати"
document.getElementById("addUser").addEventListener("click", addUser);
document.addEventListener("DOMContentLoaded", loadUsers);