import React, { useEffect, useState } from "react";
import { getMenu } from "../services/api";

function Menu() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getMenu()
      .then(data => setItems(data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Завантаження меню...</p>;

  return (
    <div>
      <h1>Меню</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name} — {item.price}€</li>
        ))}
      </ul>
    </div>
  );
}

export default Menu;
