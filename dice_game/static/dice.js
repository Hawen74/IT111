const rollBtn = document.getElementById("rollBtn");
const restartBtn = document.getElementById("restartBtn");

const turnEl = document.getElementById("turn");
const rollEl = document.getElementById("roll");
const pointEl = document.getElementById("point");
const resultEl = document.getElementById("result");

rollBtn.addEventListener("click", async () => {
  const response = await fetch("/roll");
  const data = await response.json();

  if (data.finished && data.roll === undefined) {
    resultEl.textContent = data.message;
    return;
  }

  turnEl.textContent = `Turn: ${data.turn}`;
  rollEl.textContent = `Roll: ${data.roll}`;
  pointEl.textContent = `Point: ${data.point ?? "-"}`;
  resultEl.textContent = data.result;
})

restartBtn.addEventListener("click", async () => {
  const response = await fetch("/restart");
  const data = await response.json();

  turnEl.textContent = "Turn: 1";
  rollEl.textContent = "Roll: -";
  pointEl.textContent = "Point: -";
  resultEl.textContent = data.message;
});
