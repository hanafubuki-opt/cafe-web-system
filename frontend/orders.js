const form = document.getElementById("orderForm");
const list = document.getElementById("ordersList");
let orders = [];

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const customer = document.getElementById("customer").value;
  const item = document.getElementById("item").value;
  const comment = document.getElementById("comment").value;

  orders.push({ customer, item, comment });
  renderOrders();
  form.reset();
});

function renderOrders() {
  list.innerHTML = "";
  orders.forEach(o => {
    const li = document.createElement("li");
    li.textContent = `${o.customer} замовив "${o.item}" (${o.comment})`;
    list.appendChild(li);
  });
}
