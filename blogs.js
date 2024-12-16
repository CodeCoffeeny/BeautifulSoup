const blogFiles = [
    "blogposts/blog1.txt"
]; // Update this list when new files are added.

async function fetchBlogPosts() {
    const container = document.getElementById('blog-container');

    for (const file of blogFiles) {
        try {
            const response = await fetch(file);
            if (!response.ok) {
                console.error(`Failed to load ${file}`);
                continue;
            }

            const text = await response.text();
            const posts = text.split(/^(Blog Post.*)$/m).filter(Boolean);

            posts.forEach((content, index) => {
                if (content.startsWith('Blog Post')) {
                    const card = document.createElement('div');
                    card.className = 'col-12';
                    card.innerHTML = `
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">${content}</h5>
                                <p class="card-text">${posts[index + 1]?.trim() || ''}</p>
                            </div>
                        </div>
                    `;
                    container.appendChild(card);
                }
            });
        } catch (error) {
            console.error(`Error processing file ${file}:`, error);
        }
    }
}

fetchBlogPosts();