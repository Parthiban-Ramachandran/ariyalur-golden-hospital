<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="keywords" content="{{KEYWORDS}}">
<meta name="author" content="Ariyalur Golden Hospital (PVT) Ltd.">
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
      <li><span class="topbar__badge">Emergency: <a href="tel:+919943827233">99438 27233</a></span></li>
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
        <span class="brand__sub">Multi-Speciality · PVT Ltd</span>
      </span>
    </a>

    <nav id="primary-nav" class="nav" data-nav aria-label="Primary">
      <a class="nav__link" href="index.html" {{ACTIVE_INDEX}}>Home</a>
      <a class="nav__link" href="about.html" {{ACTIVE_ABOUT}}>About</a>
      <a class="nav__link" href="departments.html" {{ACTIVE_DEPARTMENTS}}>Departments</a>
      <a class="nav__link" href="doctors.html" {{ACTIVE_DOCTORS}}>Doctors</a>
      <div class="nav__item">
        <a class="nav__link" href="services.html" {{ACTIVE_SERVICES}}>
          Services
          <svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <ul class="nav__menu">
          <li><a href="services.html">Medical Services</a></li>
          <li><a href="diagnostics.html">Diagnostic Centre</a></li>
          <li><a href="facilities.html">Hospital Facilities</a></li>
          <li><a href="health-checkup.html">Health Check-up Packages</a></li>
        </ul>
      </div>
      <a class="nav__link" href="schedule.html" {{ACTIVE_SCHEDULE}}>Schedule</a>
      <a class="nav__link" href="insurance.html" {{ACTIVE_INSURANCE}}>Insurance</a>
      <a class="nav__link" href="gallery.html" {{ACTIVE_GALLERY}}>Gallery</a>
      <a class="nav__link" href="contact.html" {{ACTIVE_CONTACT}}>Contact</a>
      <div class="nav__cta">
        <a class="btn btn--sm btn--block" href="contact.html#appointment">Book Appointment</a>
        <a class="btn btn--sm btn--ghost btn--block" href="tel:+919943827233">Emergency 99438 27233</a>
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
