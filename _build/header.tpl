<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="keywords" content="{{KEYWORDS}}">
<meta name="author" content="{{AUTHOR}}">
<meta name="theme-color" content="#0F4CB3">
<meta property="og:type" content="website">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:locale" content="en_IN">
<meta property="og:image" content="assets/logo.png">
<link rel="canonical" href="{{SLUG}}">
<link rel="icon" href="assets/web/favicon.ico" sizes="32x32">
<link rel="icon" href="assets/web/icon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="assets/web/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="assets/web/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<a class="skip-link" href="#main">Skip to main content</a>

<!-- ============================ TOP BAR ============================ -->
<div class="topbar">
  <div class="container topbar__inner">
    <ul class="topbar__list">
      <li class="topbar__item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        <span>Ariyalur, Tamil Nadu</span>
      </li>
      <li class="topbar__item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span>Emergency &amp; Casualty Open 24×7</span>
      </li>
    </ul>
    <ul class="topbar__list">
      <li class="topbar__item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <a href="tel:04329222530">04329 222530</a>
      </li>
      <li><span class="topbar__badge">Emergency: <a href="tel:+919487576493">94875 76493</a></span></li>
    </ul>
  </div>
</div>

<!-- ============================ HEADER ============================= -->
<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="index.html" aria-label="Ariyalur Golden Hospital — Home">
      <span class="brand__mark" aria-hidden="true">
        <img src="assets/logo-mark.png" width="375" height="240" alt="" decoding="async">
      </span>
      <span>
        <span class="brand__name">Ariyalur Golden Hospital</span>
        <span class="brand__sub">Multi-Speciality</span>
      </span>
    </a>

    <nav id="primary-nav" class="nav" data-nav aria-label="Primary">
      <a class="nav__link" href="index.html" {{ACTIVE_INDEX}}>Home</a>

      <!-- About — simple dropdown -->
      <div class="nav__item" data-nav-item>
        <a class="nav__link" href="about.html" {{SECTION_ABOUT}}>
          About
          <svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <button class="nav__expand" type="button" data-nav-expand aria-expanded="false" aria-label="Show About menu">
          <svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <ul class="nav__menu">
          <li><a href="about.html" {{ACTIVE_ABOUT}}>About Us</a></li>
          <li><a href="case-studies.html" {{ACTIVE_CASE_STUDIES}}>Case Studies</a></li>
          <li><a href="gallery.html" {{ACTIVE_GALLERY}}>Gallery</a></li>
        </ul>
      </div>

      <a class="nav__link" href="departments.html" {{ACTIVE_DEPARTMENTS}}>Departments</a>
      <a class="nav__link" href="doctors.html" {{ACTIVE_DOCTORS}}>Doctors</a>

      <!-- Services — mega menu -->
      <div class="nav__item nav__item--mega" data-nav-item>
        <a class="nav__link" href="services.html" {{SECTION_SERVICES}}>
          Services
          <svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <button class="nav__expand" type="button" data-nav-expand aria-expanded="false" aria-label="Show Services menu">
          <svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </button>

        <div class="mega">
          <div class="mega__inner">
            <div class="mega__col">
              <p class="mega__title" id="mega-main">Main Services</p>
              <ul class="mega__list" aria-labelledby="mega-main">
                <li>
                  <a href="services.html#orthopaedics">
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17.2 4.8a2.6 2.6 0 0 0-4.3 1.2l-.6 2.1-4.2 4.2-2.1.6a2.6 2.6 0 1 0 3.1 3.1l.6-2.1 4.2-4.2 2.1-.6a2.6 2.6 0 0 0 1.2-4.3z"/></svg></span>
                    <span><span class="mega__label">Orthopaedics</span><span class="mega__desc">Fracture, joint &amp; spine surgery</span></span>
                  </a>
                </li>
                <li>
                  <a href="services.html#general-surgery">
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg></span>
                    <span><span class="mega__label">General Surgery</span><span class="mega__desc">Open &amp; laparoscopic procedures</span></span>
                  </a>
                </li>
                <li>
                  <a href="services.html#laser-surgery">
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v5"/><path d="M12 12.5v9"/><path d="M5.5 5.5l3 3"/><path d="M18.5 5.5l-3 3"/><circle cx="12" cy="10" r="2.5"/><path d="M4 10h3"/><path d="M17 10h3"/></svg></span>
                    <span><span class="mega__label">Laser Surgery</span><span class="mega__desc">Day-care laser procedures</span></span>
                  </a>
                </li>
              </ul>
              <a class="link-arrow mega__more" href="services.html" {{ACTIVE_SERVICES}}>All medical services</a>
            </div>

            <div class="mega__col">
              <p class="mega__title" id="mega-diag">Diagnostics &amp; Imaging</p>
              <ul class="mega__list" aria-labelledby="mega-diag">
                <li>
                  <a href="scans.html" {{ACTIVE_SCANS}}>
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="14.31" y1="8" x2="20.05" y2="17.94"/><line x1="9.69" y1="8" x2="21.17" y2="8"/><line x1="7.38" y1="12" x2="13.12" y2="2.06"/><line x1="9.69" y1="16" x2="3.95" y2="6.06"/><line x1="14.31" y1="16" x2="2.83" y2="16"/><line x1="16.62" y1="12" x2="10.88" y2="21.94"/></svg></span>
                    <span><span class="mega__label">Scans &amp; Imaging</span><span class="mega__desc">MRI 1.5 Tesla, CT, X-ray, ultrasound</span></span>
                  </a>
                </li>
                <li>
                  <a href="diagnostics.html" {{ACTIVE_DIAGNOSTICS}}>
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></span>
                    <span><span class="mega__label">Diagnostic Centre</span><span class="mega__desc">Lab, ECG, ECHO &amp; endoscopy</span></span>
                  </a>
                </li>
                <li>
                  <a href="health-checkup.html" {{ACTIVE_HEALTH_CHECKUP}}>
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 11.5 11 13.5 15 9.5"/></svg></span>
                    <span><span class="mega__label">Health Check-up</span><span class="mega__desc">Master, family &amp; corporate packages</span></span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="mega__col">
              <p class="mega__title" id="mega-hosp">Around the Hospital</p>
              <ul class="mega__list" aria-labelledby="mega-hosp">
                <li>
                  <a href="departments.html" {{ACTIVE_DEPARTMENTS}}>
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>
                    <span><span class="mega__label">Departments</span><span class="mega__desc">Seventeen clinical departments</span></span>
                  </a>
                </li>
                <li>
                  <a href="facilities.html" {{ACTIVE_FACILITIES}}>
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M5 21V6a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v15"/><path d="M12 8v6"/><path d="M9 11h6"/></svg></span>
                    <span><span class="mega__label">Hospital Facilities</span><span class="mega__desc">ICU, theatres, blood bank, pharmacy</span></span>
                  </a>
                </li>
                <li>
                  <a href="services.html#emergency">
                    <span class="mega__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></span>
                    <span><span class="mega__label">Emergency &amp; Trauma</span><span class="mega__desc">24×7 casualty, ICU &amp; ambulance</span></span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="mega__panel">
              <span class="mega__panel-eyebrow">Open 24×7</span>
              <p class="mega__panel-title">Emergency &amp; casualty</p>
              <p class="mega__panel-text">Call ahead so the casualty team is ready before the patient arrives.</p>
              <a class="mega__panel-num" href="tel:+919943827233">99438 27233</a>
              <a class="btn btn--sm btn--white btn--block" href="contact.html#appointment">Book Appointment</a>
            </div>
          </div>
        </div>
      </div>

      <a class="nav__link" href="insurance.html" {{ACTIVE_INSURANCE}}>Insurance</a>
      <a class="nav__link" href="contact.html" {{ACTIVE_CONTACT}}>Contact</a>

      <div class="nav__cta">
        <a class="btn btn--sm btn--block" href="contact.html#appointment">Book Appointment</a>
        <a class="btn btn--sm btn--ghost btn--block" href="tel:+919487576493">Emergency 94875 76493</a>
      </div>
    </nav>

    <div class="header__cta">
      <a class="btn btn--sm" href="contact.html#appointment">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        Book Appointment
      </a>
      <button class="nav-toggle" data-nav-toggle type="button" aria-expanded="false" aria-controls="primary-nav">
        <span class="nav-toggle__bars" aria-hidden="true"><span></span><span></span><span></span></span>
        Menu
      </button>
    </div>
  </div>
</header>
<div class="nav-scrim" data-nav-scrim aria-hidden="true"></div>

<main id="main">
