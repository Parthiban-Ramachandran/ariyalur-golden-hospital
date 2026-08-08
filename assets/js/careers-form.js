/* ---------------------------------------------------------------------------
   Careers application form.

   The site is static HTML with no backend, so until the form is given a real
   endpoint there is nowhere for an application to go. Letting the browser
   "submit" to nothing would reload the page and silently lose whatever the
   applicant typed, which is worse than having no form at all — so the submit
   is blocked and the applicant is pointed at reception instead.

   The guard keys off the form's own action attribute: set a real URL on the
   <form> and this stops interfering by itself, with no change needed here.
   --------------------------------------------------------------------------- */
(function () {
  var forms = document.querySelectorAll('[data-careers-form]');

  Array.prototype.forEach.call(forms, function (form) {
    var status = form.querySelector('[data-form-status]');

    form.addEventListener('submit', function (event) {
      var action = (form.getAttribute('action') || '').trim();

      // A real endpoint is configured — let the submission through untouched.
      if (action !== '' && action !== '#') return;

      event.preventDefault();
      if (!status) return;

      status.hidden = false;
      status.textContent =
        'Online applications are not connected yet, so this form cannot be sent. ' +
        'Please call reception on 04329 222530, or bring your CV and certificates ' +
        'to the hospital. Sorry for the inconvenience.';
      status.focus();
    });
  });
})();
