(() => {
  const owner = "I-Love-PETs";
  const repo = "i-love-pets.github.io";
  const repoUrl = `https://github.com/${owner}/${repo}`;

  function makeLinkButton(label, href) {
    const button = document.createElement("a");
    button.className = "github-actions__button";
    button.href = href;
    button.target = "_blank";
    button.rel = "noopener noreferrer";
    button.setAttribute("aria-label", `${label} ${owner}/${repo} on GitHub`);
    button.textContent = label;
    return button;
  }

  function makeGitHubButton(type, label, width) {
    const frame = document.createElement("iframe");
    const params = new URLSearchParams({
      user: owner,
      repo,
      type,
      count: "true",
      size: "large",
    });
    frame.className = "github-actions__widget";
    frame.title = `${label} ${owner}/${repo} on GitHub`;
    frame.src = `https://ghbtns.com/github-btn.html?${params.toString()}`;
    frame.width = String(width);
    frame.height = "30";
    frame.loading = "lazy";
    frame.setAttribute("scrolling", "0");
    frame.setAttribute("frameborder", "0");
    return frame;
  }

  function mountGitHubActions() {
    if (document.querySelector(".github-actions")) return;

    const actions = document.createElement("nav");
    actions.className = "github-actions";
    actions.setAttribute("aria-label", "GitHub repository actions");
    actions.append(
      makeGitHubButton("star", "Star", 105),
      makeLinkButton("Fork", `${repoUrl}/fork`)
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
