const rssLink = document.querySelector('.rss-copy-button');
const rssFeed = document.querySelector('link[rel="alternate"][type="application/rss+xml"]');

if (rssLink && rssFeed) {
    const copyStatus = document.createElement('span');
    const rssIcon = rssLink.innerHTML;
    let hideStatusTimeout;

    copyStatus.className = 'rss-copy-status';
    copyStatus.setAttribute('role', 'status');
    copyStatus.setAttribute('aria-live', 'polite');
    document.body.appendChild(copyStatus);

    rssLink.title = 'Copy RSS feed URL';
    rssLink.addEventListener('click', async (event) => {
        event.preventDefault();

        const feedUrl = rssFeed.href;
        let copied = false;
        try {
            await navigator.clipboard.writeText(feedUrl);
            copied = true;
        } catch {
            const input = document.createElement('textarea');
            input.value = feedUrl;
            input.style.position = 'fixed';
            input.style.opacity = '0';
            document.body.appendChild(input);
            input.select();
            try {
                copied = document.execCommand('copy');
            } catch {
                copied = false;
            } finally {
                input.remove();
            }
        }

        const message = copied ? 'Copied!' : 'Could not copy. Please try again.';
        copyStatus.textContent = message;
        copyStatus.classList.add('visible');
        rssLink.title = message;
        rssLink.setAttribute('aria-label', message);
        rssLink.classList.toggle('copied', copied);
        rssLink.innerHTML = copied
            ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12 4 4L19 6"></path></svg>'
            : rssIcon;
        window.clearTimeout(hideStatusTimeout);
        hideStatusTimeout = window.setTimeout(() => {
            copyStatus.classList.remove('visible');
            rssLink.innerHTML = rssIcon;
            rssLink.classList.remove('copied');
            rssLink.title = 'Copy RSS feed URL';
            rssLink.setAttribute('aria-label', 'Copy RSS feed URL');
        }, 1600);
    });
}
