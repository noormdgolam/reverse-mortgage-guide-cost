document.addEventListener('DOMContentLoaded', () => {
    // Register Service Worker
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then(registration => {
          console.log('ServiceWorker registration successful');
        }, err => {
          console.log('ServiceWorker registration failed: ', err);
        });
      });
    }

    // Enforce external link security (noopener noreferrer)
    const currentDomain = window.location.hostname;
    document.querySelectorAll('a').forEach(link => {
        if (link.hostname && link.hostname !== currentDomain && link.hostname !== "") {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});
