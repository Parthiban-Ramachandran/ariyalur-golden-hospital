# Ariyalur Golden Hospital (PVT) Ltd. — Website

A static, hand-built marketing site: semantic HTML5, one CSS3 stylesheet, no frameworks,
and ~30 lines of JavaScript used only for the mobile navigation drawer.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About Us |
| `patient-care-outcomes.html` | Overview of Patient Care Outcomes (nav label: "Patient Care Outcomes") |
| `doctors.html` | Doctors (grouped by department) |
| `departments.html` | Departments (15 detail blocks) |
| `services.html` | Medical Services |
| `scans.html` | Scans & Imaging (MRI, CT, X-ray, ultrasound) |
| `diagnostics.html` | Diagnostic Centre (cardiac tests, laboratory, endoscopy) |
| `facilities.html` | Facilities |
| `health-checkup.html` | Health Check-up Packages |
| `insurance.html` | Insurance & Cashless Treatment |
| `gallery.html` | Gallery |
| `careers.html` | Careers (linked from the About dropdown and the footer Quick Links) |
| `contact.html` | Contact |
| `disclaimer.html` | Medical & Website Disclaimer |
| `privacy.html` | Privacy Policy |
| `terms.html` | Terms & Conditions of Use |

The last three are the legal pages linked from the footer's Legal navigation. They carry no
nav highlight — `active` in `make.py` is set to a key that is not in `ACTIVE_KEYS`, so no
header item is marked current.

Open `index.html` in a browser — no build step or server is required to view the site.

## Project structure

```
.
├── *.html                  ← the 17 finished pages
├── site.webmanifest
└── assets/
    ├── css/style.css       ← the entire design system
    ├── js/menu.js          ← mobile drawer toggle only
    ├── js/lightbox.js      ← gallery lightbox
    ├── img/                ← optimised photographs (jpg + webp, 2 widths)
    ├── web/                ← favicons and app icons
    ├── logo.png, logo-mark.png
    └── hospitalimage.png   ← original full-resolution source photo
```

`_lbtest.html` is a lightbox scratch file, not a published page — it is deliberately left
out of the nav and the page table above.

### Editing

The site is now hand-edited. Earlier versions were assembled by a `_build/` templating
script (`header.tpl`, `footer.tpl`, `pages/*.html`, `make.py`); that directory has since
been removed and was never committed, so **there is no build step** — edit the root `.html`
files directly and open them in a browser.

The consequence is that the top bar, header/nav and footer are duplicated in all 17 files.
A change to any of them has to be repeated in every page, and the pages will drift apart if
it is not. When adding a nav item or a new page, the reliable approach is to copy an
existing page's scaffolding and apply the shared-markup edit to every file in one scripted
pass, then check that each page still has exactly the links you expect.

Per-page `<title>`, meta description, `og:*` tags and the canonical link live in each
file's own `<head>`.

## Design system (`assets/css/style.css`)

The stylesheet is ordered in numbered sections: reset, tokens, typography, layout, buttons,
header/nav, hero, sections, cards, banners, tables, forms, footer, legal/long-form,
utilities, motion, responsive.

Colours are derived from the hospital logo and exposed as custom properties:

- `--blue-600: #0F4CB3` — the logo blue, the primary brand colour
- `--green-500: #7AC61A` — the logo green, used as the accent
- `--navy-*` — deeper blues used as the second stop in gradients
- `--danger` — reserved for emergency messaging only

Reusable components: `.btn`, `.card`, `.doctor-list` / `.doctor-row`, `.dept-card`, `.dept-detail`,
`.facility-card`, `.insurance-card`, `.testimonial`, `.package`, `.cta-banner`,
`.case-list` / `.case-card` / `.case-steps` (the case-study timeline),
`.emergency-banner`, `.info-box`, `.notice-strip`, `.schedule-table`, `.form-card`,
`.media`, `.gallery-item`, `.legal-meta` / `.legal-toc` / `.legal-block` / `.legal-list`.

Breakpoints: 1380px (tighten nav), 1199px (switch to the mobile drawer), 780px (single
column), 480px (small phones).

## Accessibility

- Skip link, landmark elements, one `<h1>` per page
- `aria-current="page"` on the active nav item, `aria-expanded` on the menu button
- Visible `:focus-visible` rings; the drawer closes on `Escape`
- Every image has descriptive alt text; decorative SVGs are `aria-hidden`
- Full `prefers-reduced-motion` support

## Before going live

1. **Content still to be supplied** — the "to be updated" / "Not Available" placeholder
   badges have been removed from every page, so the site no longer advertises its own gaps.
   The underlying details are still missing and should be filled in when the hospital
   confirms them: years of experience for most consultants, the email address, accreditation
   status, the founding and expansion years on `about.html`, the Chairman's message and
   signature, health check-up package prices, and Dr. Santhip's consultation time and the
   dialysis slot timing. The full consultant roster (names, qualifications, visiting days and
   timings) was supplied by the hospital and is reflected on `doctors.html` and
   `departments.html` — the two pages are the only places doctor data lives, so they must be
   kept in step whenever a consultant changes.
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
6. **Testimonials** — the sample testimonials have been removed from the home page. Publish
   patient feedback only once it is genuine and published with written patient consent.
7. **Patient care examples** — the six examples on `patient-care-outcomes.html` are fictional,
   simplified examples in three stages (Assessment / Possible care / Follow-up), not accounts
   of identifiable patients. One `.notice-strip` under the intro states this, and each
   example carries a one-line clinician-decides reminder. If the hospital wants to publish
   real cases, replace the text but keep the notices honest: written patient consent is
   required, no identifying detail may be used, and nothing should be phrased as a guarantee
   of outcome. The filename is still `patient-care-outcomes.html`; the review asked for a
   `/patient-care/` URL, which needs a rename plus redirects.
8. **Absolute URLs** — set `og:image` and the canonical links to the live domain. The legal
   pages also quote the current Vercel URL in their text (`disclaimer.html` §1,
   `terms.html` §1) — update both when the hospital's own domain goes live.
9. **Legal contact email** — `privacy.html` and `terms.html` use the placeholder
   `privacy@ariyalurgoldenhospital.com` for the Grievance Officer. Replace it with the
   hospital's primary monitored mailbox (it is the only email address on the site) before
   publishing, since the Privacy Policy commits to answering requests sent there.
10. **Legal review** — the disclaimer, privacy policy and terms were drafted from the
   hospital's supplied text against the DPDPA 2023 and IT Act, 2000. Have them checked by
   the hospital's legal advisor before going live, and keep the "Effective / Last updated —
   July 2026" lines on `privacy.html` and `terms.html` current when the text changes.
11. **Careers page** — the six role groups on `careers.html` (Nursing, Allied Health &
   Diagnostics, Doctors, Pharmacy, Administration & Front Office, Support Services) are
   *indicative categories the hospital recruits for, not confirmed live vacancies*. A
   `.notice-strip` under the hero says so explicitly, and the section intro repeats it.
   Have the hospital confirm the role list, the qualifications quoted for each group and
   the statement that freshers are considered, and replace the categories with real posts
   (with a date) if and when specific vacancies are advertised. If the notice is removed,
   the page starts reading as a list of open jobs — keep the two honest, or take the page
   down between recruitment rounds.

   Applications are handled by phone and in person: reception on 04329 222530 plus walk-in
   CV submission, matching the site's no-forms decision (item 2). There is deliberately no
   careers email address, because the hospital has not supplied one — add one to the
   "Recruitment enquiries" tiles once it exists. The page also carries a no-recruitment-fee
   warning, an equal-opportunity statement and a line pointing applicants at the Privacy
   Policy for how their CV is handled; keep all three if the page is edited.
