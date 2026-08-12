/* Fills any <time data-current-date> on legal pages with today's date,
   formatted as "11 August 2026". The markup keeps a written-out date as a
   fallback for browsers with JavaScript turned off. */
(function () {
  var nodes = document.querySelectorAll('[data-current-date]');
  if (!nodes.length) return;

  var now = new Date();
  var text;

  try {
    text = new Intl.DateTimeFormat('en-GB', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    }).format(now);
  } catch (e) {
    return; // leave the fallback date in place
  }

  var iso = now.getFullYear() + '-' +
    String(now.getMonth() + 1).padStart(2, '0') + '-' +
    String(now.getDate()).padStart(2, '0');

  for (var i = 0; i < nodes.length; i++) {
    nodes[i].textContent = text;
    if (nodes[i].tagName === 'TIME') nodes[i].setAttribute('datetime', iso);
  }
})();
