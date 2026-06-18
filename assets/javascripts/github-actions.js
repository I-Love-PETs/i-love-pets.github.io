(() => {
  const owner = "I-Love-PETs";
  const repo = "i-love-pets.github.io";
  const repoUrl = `https://github.com/${owner}/${repo}`;

  function makeButton(label, href, kind) {
    const button = document.createElement("a");
    button.className = `github-actions__button github-actions__button--${kind}`;
    button.href = href;
    button.target = "_blank";
    button.rel = "noopener noreferrer";
    button.setAttribute("aria-label", `${label} ${owner}/${repo} on GitHub`);
    button.title = `${label} ${owner}/${repo} on GitHub`;
    button.textContent = label;
    return button;
  }

  function mountGitHubActions() {
    if (document.querySelector(".github-actions")) return;

    const actions = document.createElement("nav");
    actions.className = "github-actions";
    actions.setAttribute("aria-label", "GitHub repository actions");
    actions.append(
      makeButton("Star", repoUrl, "star"),
      makeButton("Fork", `${repoUrl}/fork`, "fork")
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
