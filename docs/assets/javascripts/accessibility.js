(() => {
  const labels = new WeakMap();
  const observer = new ResizeObserver((entries) => {
    for (const { target } of entries) {
      const wrapper = target.closest(".md-typeset__scrollwrap");
      if (!wrapper) continue;

      if (wrapper.scrollWidth > wrapper.clientWidth) {
        wrapper.tabIndex = 0;
        wrapper.setAttribute("role", "region");
        wrapper.setAttribute("aria-label", labels.get(wrapper));
      } else {
        wrapper.removeAttribute("tabindex");
        wrapper.removeAttribute("role");
        wrapper.removeAttribute("aria-label");
      }
    }
  });

  function mountAccessibility() {
    const search = document.querySelector('.md-search[role="dialog"]');
    const searchLabel = search?.querySelector("input[aria-label]")?.getAttribute("aria-label");
    if (searchLabel && !search.hasAttribute("aria-label") && !search.hasAttribute("aria-labelledby")) {
      search.setAttribute("aria-label", searchLabel);
    }

    observer.disconnect();
    const wrappers = document.querySelectorAll(".md-content .md-typeset__scrollwrap");
    wrappers.forEach((wrapper, index) => {
      const heading = wrapper.closest("article")?.querySelector("h1")?.textContent.trim();
      labels.set(wrapper, heading ? `${heading}, scrollable table ${index + 1}` : `Scrollable table ${index + 1}`);
      observer.observe(wrapper);
      // Font loading can resize the table without resizing its scroll container.
      const table = wrapper.querySelector("table");
      if (table) observer.observe(table);
    });
  }

  // Material wraps Markdown tables when it mounts each document.
  document$.subscribe(() => requestAnimationFrame(mountAccessibility));
})();
