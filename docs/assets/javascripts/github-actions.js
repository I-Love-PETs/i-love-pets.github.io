(() => {
  const repoUrl = "https://github.com/I-Love-PETs/i-love-pets.github.io";

  const icon = `
    <svg class="github-actions__icon" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 .25a7.75 7.75 0 0 0-2.45 15.1c.39.07.53-.17.53-.38v-1.32c-2.17.47-2.63-1.04-2.63-1.04-.36-.9-.87-1.14-.87-1.14-.71-.49.05-.48.05-.48.78.06 1.2.81 1.2.81.7 1.19 1.83.85 2.27.65.07-.5.27-.85.5-1.04-1.73-.2-3.55-.87-3.55-3.86 0-.85.31-1.55.8-2.1-.08-.2-.35-.99.08-2.07 0 0 .66-.21 2.14.8A7.42 7.42 0 0 1 8 3.62c.66 0 1.32.09 1.94.26 1.48-1.01 2.13-.8 2.13-.8.43 1.08.16 1.87.08 2.07.5.55.8 1.25.8 2.1 0 3-.82 3.66-3.56 3.85.28.25.53.73.53 1.48v2.19c0 .21.14.46.54.38A7.75 7.75 0 0 0 8 .25Z"/>
    </svg>
  `;

  function makeButton(label, href) {
    const button = document.createElement("a");
    button.className = "github-actions__button";
    button.href = href;
    button.target = "_blank";
    button.rel = "noopener noreferrer";
    button.setAttribute("aria-label", `${label} I-Love-PETs/i-love-pets.github.io on GitHub`);
    button.innerHTML = `${icon}<span>${label}</span>`;
    return button;
  }

  function mountGitHubActions() {
    if (document.querySelector(".github-actions")) return;

    const actions = document.createElement("nav");
    actions.className = "github-actions";
    actions.setAttribute("aria-label", "GitHub repository actions");
    actions.append(
      makeButton("Star", `${repoUrl}/stargazers`),
      makeButton("Fork", `${repoUrl}/fork`)
    );

    document.body.append(actions);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountGitHubActions);
  } else {
    mountGitHubActions();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(mountGitHubActions);
  }
})();
