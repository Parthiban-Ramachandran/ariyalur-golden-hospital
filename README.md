# Ariyalur Golden Hospital (PVT) Ltd. — Website

A static, hand-built marketing site: semantic HTML5, one CSS3 stylesheet, no frameworks,
and ~30 lines of JavaScript used only for the mobile navigation drawer.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About Us |
| `doctors.html` | Doctors (grouped by department) |
| `departments.html` | Departments (15 detail blocks) |
| `services.html` | Medical Services |
| `scans.html` | Scans & Imaging (MRI, CT, X-ray, ultrasound) |
| `diagnostics.html` | Diagnostic Centre (cardiac tests, laboratory, endoscopy) |
| `facilities.html` | Facilities |
| `schedule.html` | Consultation Schedule |
| `health-checkup.html` | Health Check-up Packages |
| `insurance.html` | Insurance & Cashless Treatment |
| `gallery.html` | Gallery |
| `contact.html` | Contact |

Open `index.html` in a browser — no build step or server is required to view the site.

## Project structure

```
.
├── *.html                  ← the 13 finished pages (generated — see below)
├── site.webmanifest
├── assets/
│   ├── css/style.css       ← the entire design system
│   ├── js/menu.js          ← mobile drawer toggle only
│   ├── img/                ← optimised photographs (jpg + webp, 2 widths)
│   ├── web/                ← favicons and app icons
│   ├── logo.png, logo-mark.png
│   └── hospitalimage.png   ← original full-resolution source photo
└── _build/                 ← authoring sources, not deployed
    ├── header.tpl          ← shared <head>, top bar, header and nav
    ├── footer.tpl          ← shared footer
    ├── pages/*.html        ← the unique <main> content of each page
    └── make.py             ← assembles the pages
```

### Editing

The header and footer are identical on all 13 pages, so they live in one place.

- To change the nav, logo, meta tags or footer → edit `_build/header.tpl` / `_build/footer.tpl`
- To change a page's content → edit `_build/pages/<page>.html` (body content only)
- To change titles, meta descriptions or keywords → edit the `PAGES` dict in `_build/make.py`

Then regenerate the root HTML files:

```bash
python3 _build/make.py
```

The output is ordinary static HTML with no runtime dependency on the build script. If you
prefer to abandon the templating and hand-edit the 13 root files directly, you can — just
delete `_build/` and remember that header/footer changes then have to be made 13 times.

## Design system (`assets/css/style.css`)

The stylesheet is ordered in numbered sections: reset, tokens, typography, layout, buttons,
header/nav, hero, sections, cards, banners, tables, forms, footer, utilities, motion,
responsive.

Colours are derived from the hospital logo and exposed as custom properties:

- `--blue-600: #0F4CB3` — the logo blue, the primary brand colour
- `--green-500: #7AC61A` — the logo green, used as the accent
- `--navy-*` — deeper blues used as the second stop in gradients
- `--danger` — reserved for emergency messaging only

Reusable components: `.btn`, `.card`, `.doctor-list` / `.doctor-row`, `.dept-card`, `.dept-detail`,
`.facility-card`, `.insurance-card`, `.testimonial`, `.package`, `.cta-banner`,
`.emergency-banner`, `.info-box`, `.notice-strip`, `.schedule-table`, `.form-card`,
`.media`, `.gallery-item`.

Breakpoints: 1380px (tighten nav), 1199px (switch to the mobile drawer), 780px (single
column), 480px (small phones).

## Accessibility

- Skip link, landmark elements, one `<h1>` per page, breadcrumbs on inner pages
- `aria-current="page"` on the active nav item, `aria-expanded` on the menu button
- Visible `:focus-visible` rings; the drawer closes on `Escape`
- Every image has descriptive alt text; decorative SVGs are `aria-hidden`
- Full `prefers-reduced-motion` support

## Before going live

1. **Content still to be supplied** — the "to be updated" / "Not Available" placeholder
   badges have been removed from every page, so the site no longer advertises its own gaps.
   The underlying details are still missing and should be filled in when the hospital
   confirms them: consultant names and years of experience, the email address, accreditation
   status, the founding and expansion years on `about.html`, the Chairman's message and
   signature, health check-up package prices, and the blank (`—`) cells in the consultation
   table on `schedule.html`. Two General Medicine entries (Dr. Devarajan, Dr. Karthikeyan)
   currently carry a name and nothing else on both `doctors.html` and `schedule.html`.
2. **Appointment forms** — the site no longer contains any `<form>`. Both the `contact.html`
   appointment form and the "Quick Appointment" hero form on `index.html` have been removed;
   each place now shows the reception and token-booking numbers instead. The forms section of
   `style.css` (`.form-card`, `.form-grid`, `.field`, `.glass-form`) is kept so a form can be
   reinstated later — if you do, point its `action` at a mail handler or CRM endpoint and add
   server-side validation.
3. **Google Map** — replace the `.map-placeholder` block in `contact.html` with the real
   embed once the full address is confirmed.
4. **Gallery** — only the exterior photograph is real; the other tiles are placeholders.
   Copy the `<picture>` markup from the first tile for each new photograph.
5. **Social links** — the footer icons point at `#`.
6. **Testimonials** — the three on the home page are clearly labelled samples; replace them
   with real feedback published with patient consent.
7. **Absolute URLs** — set `og:image` and the canonical links to the live domain.
