const logBox = document.getElementById("log");

async function loadLogs() {
  try {
    const res = await fetch("/api/logs");
    const data = await res.json();

    logBox.textContent = data.join("\n");
    logBox.scrollTop = logBox.scrollHeight;
  } catch (err) {
    logBox.textContent = "Erro ao carregar logs";
    console.error(err);
  }
}

setInterval(loadLogs, 1000);
loadLogs();
