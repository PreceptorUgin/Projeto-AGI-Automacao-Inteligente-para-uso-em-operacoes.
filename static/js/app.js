async function fetchLogs() {
  const res = await fetch('/api/logs');
  const logs = await res.json();

  const container = document.querySelector('.logs-top');
  container.innerHTML = logs.join('<br>');
}

setInterval(fetchLogs, 2000);
