const rssLink = document.querySelector('.menu-item[href$="#rss"]');
const rssFeed = document.querySelector('link[rel="alternate"][type="application/rss+xml"]');

if (rssLink && rssFeed) {
    const originalLabel = rssLink.textContent;

    rssLink.title = '复制订阅链接';
    rssLink.addEventListener('click', async (event) => {
        event.preventDefault();

        const feedUrl = rssFeed.href;
        try {
            await navigator.clipboard.writeText(feedUrl);
        } catch {
            const input = document.createElement('textarea');
            input.value = feedUrl;
            input.style.position = 'fixed';
            input.style.opacity = '0';
            document.body.appendChild(input);
            input.select();
            document.execCommand('copy');
            input.remove();
        }

        rssLink.textContent = '已复制';
        window.setTimeout(() => {
            rssLink.textContent = originalLabel;
        }, 1600);
    });
}
