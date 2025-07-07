async function fetchEvents() {
  const res = await fetch("http://localhost:5000/events");
  const data = await res.json();

  const list = document.getElementById("event-list");
  list.innerHTML = "";

  data.forEach(e => {
    let text = "";
    if (e.action === "push") {
      text = `${e.author} pushed to ${e.to_branch} on ${e.timestamp}`;
    } else if (e.action === "pull_request") {
      text = `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    } else if (e.action === "merge") {
      text = `${e.author} merged branch ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    }

    const item = document.createElement("li");
    item.className = "list-group-item";
    item.innerText = text;
    list.appendChild(item);
  });
}

fetchEvents();
setInterval(fetchEvents, 15000);
