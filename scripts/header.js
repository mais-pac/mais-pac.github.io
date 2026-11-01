/* Keep anchored content clear of the persistent navigation, including wrapped mobile links. */
(() => {
  const start = () => {
    const bar = document.querySelector('.site-header, .handout-bar');
    if (!bar) return;
    const update = () => {
      const height = Math.ceil(bar.getBoundingClientRect().height);
      document.documentElement.style.setProperty('--header-offset', height + 'px');
    };
    update();
    if ('ResizeObserver' in window) new ResizeObserver(update).observe(bar);
    else window.addEventListener('resize', update);
    window.addEventListener('load', update, { once: true });
    if (document.fonts) document.fonts.ready.then(update);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
