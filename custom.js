// The head script resolves the saved preference before the first paint.
const themeToggle = document.querySelector('.theme-toggle');
let themePreference = window.siteThemePreference || 'light';

function applyTheme() {
    document.documentElement.dataset.theme = themePreference;
    if (themeToggle) {
        const label = themePreference === 'dark' ? 'light mode' : 'dark mode';
        themeToggle.title = label;
        themeToggle.setAttribute('aria-label', label);
        themeToggle.innerHTML = themePreference === 'dark'
            ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"></path></svg>'
            : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.9 13A9 9 0 0 1 11 3.1 9 9 0 1 0 20.9 13Z"></path></svg>';
    }
    document.querySelector('iframe.giscus-frame')?.contentWindow.postMessage(
        { giscus: { setConfig: { theme: themePreference } } }, 'https://giscus.app'
    );
}

applyTheme();
window.addEventListener('storage', event => {
    if (event.key !== 'picoPreferredColorScheme' && event.key !== null) return;
    themePreference = ['light', 'dark'].includes(event.newValue) ? event.newValue : 'light';
    applyTheme();
});
themeToggle?.addEventListener('click', () => {
    themePreference = themePreference === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('picoPreferredColorScheme', themePreference); }
    catch { /* The selected theme still works when storage is unavailable. */ }
    applyTheme();
});

const menuToggle = document.getElementById('menu-toggle');
const headerMenu = document.getElementById('header-menu');
function closeMenu(returnFocus = false) {
    if (!menuToggle || !headerMenu) return;
    headerMenu.classList.remove('active');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', '展开导航菜单');
    if (returnFocus) menuToggle.focus();
}
menuToggle?.addEventListener('click', () => {
    const open = headerMenu.classList.toggle('active');
    menuToggle.setAttribute('aria-expanded', String(open));
    menuToggle.setAttribute('aria-label', open ? '收起导航菜单' : '展开导航菜单');
});
window.matchMedia('(max-width: 1025px)').addEventListener('change', () => closeMenu());
document.addEventListener('click', event => {
    if (!event.target.closest('.header-nav')) closeMenu();
});
document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    if (headerMenu?.classList.contains('active')) closeMenu(true);
});

const rssLink = document.querySelector('.rss-copy-button');
const rssFeed = document.querySelector('link[rel="alternate"][type="application/rss+xml"]');
if (rssLink && rssFeed) {
    const copyStatus = document.createElement('span');
    const rssIcon = rssLink.innerHTML;
    let hideStatusTimeout;
    copyStatus.className = 'rss-copy-status';
    copyStatus.setAttribute('role', 'status');
    document.body.appendChild(copyStatus);
    rssLink.addEventListener('click', async () => {
        let copied = false;
        try {
            await navigator.clipboard.writeText(rssFeed.href);
            copied = true;
        } catch {
            const input = document.createElement('textarea');
            input.value = rssFeed.href;
            input.style.position = 'fixed';
            input.style.opacity = '0';
            document.body.appendChild(input);
            input.select();
            try { copied = document.execCommand('copy'); } catch { copied = false; }
            input.remove();
            rssLink.focus();
        }
        copyStatus.textContent = copied ? 'Copied!' : 'Could not copy. Please try again or open the feed below.';
        if (!copied) {
            const link = document.createElement('a');
            link.href = rssFeed.href;
            link.textContent = 'Open RSS feed';
            copyStatus.append(' ', link);
        }
        copyStatus.classList.add('visible');
        rssLink.classList.toggle('copied', copied);
        rssLink.innerHTML = copied
            ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 4 4L19 6"></path></svg>'
            : rssIcon;
        window.clearTimeout(hideStatusTimeout);
        hideStatusTimeout = window.setTimeout(() => {
            copyStatus.classList.remove('visible');
            rssLink.innerHTML = rssIcon;
            rssLink.classList.remove('copied');
        }, copied ? 1800 : 8000);
    });
}
