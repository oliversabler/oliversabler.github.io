const snow = document.querySelector(".snow");
for (let i = 0; i < 36; i++) {
  const flake = document.createElement("span");
  const duration = 7 + Math.random() * 7;
  flake.textContent = "*";
  flake.style.left = `${Math.random() * 100}%`;
  flake.style.fontSize = `${10 + Math.random() * 10}px`;
  flake.style.setProperty("--drift", `${Math.random() * 80 - 40}px`);
  flake.style.setProperty("--rotation", Math.random() < 0.5 ? "-180deg" : "180deg");
  flake.style.animationDuration = `${duration}s`;
  flake.style.animationDelay = `${-Math.random() * duration}s`;
  snow.append(flake);
}
