document.addEventListener("DOMContentLoaded", () => {
    fetch("sites.txt")
        .then(response => response.text())
        .then(text => {
            const lines = text.split('\n').filter(line => line.trim() !== "");
            const navLinks = document.getElementById("nav-links");
            for (let i = 0; i < lines.length; i += 2) {
                const siteName = lines[i].trim();
                const siteURL = lines[i + 1].trim();
                const listItem = document.createElement("li");
                listItem.className = "nav-item";
                const link = document.createElement("a");
                link.className = "nav-link";
                link.href = "#";
                link.textContent = siteName;
                link.addEventListener("click", () => loadSite(siteURL));
                listItem.appendChild(link);
                navLinks.appendChild(listItem);
            }
        });
});

function loadSite(url) {
    const card = document.getElementById("content-card");
    const frame = document.getElementById("content-frame");
    const fallback = document.getElementById("fallback");
    const directLink = document.getElementById("direct-link");

    card.style.opacity = "1";
    card.style.transition = "opacity 1s";
    card.style.opacity = "0";
    
    setTimeout(() => {
        frame.src = url;
        directLink.href = url;
        fallback.classList.add("d-none");
        frame.classList.remove("d-none");
        
        frame.onload = () => {
            card.style.opacity = "1";
        };
        frame.onerror = () => {
            fallback.classList.remove("d-none");
            frame.classList.add("d-none");
            card.style.opacity = "1";
        };
    }, 1000);
}
