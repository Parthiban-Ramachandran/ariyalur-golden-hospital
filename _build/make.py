#!/usr/bin/env python3
"""
Ariyalur Golden Hospital — static page assembler.

Combines _build/header.tpl + _build/pages/<slug>.html + _build/footer.tpl
into plain HTML files at the project root. Run after editing any partial:

    python3 _build/make.py

The generated files are ordinary HTML5 — no runtime dependency on this script.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_build"

DEFAULT_AUTHOR = "Ariyalur Golden Hospital (PVT) Ltd."

# Absolute origin used for canonical links, og:url, og:image and the Hospital
# JSON-LD. Change this one line when the hospital's own domain goes live — the
# same URL is quoted in the text of disclaimer.html §1 and terms.html §1.
BASE_URL = "https://ariyalur-golden-hospital.vercel.app/"

PAGES = {
    "index.html": {
        "active": "INDEX",
        "author": "Ariyalur Golden Hospital",
        "title": "Ariyalur Golden Hospital | Multispecialty Hospital in Ariyalur",
        "desc": "Ariyalur Golden Hospital provides emergency care, specialist consultations, surgery and diagnostic services in Ariyalur, Tamil Nadu. Call 04329 222530.",
    },
    "about.html": {
        "active": "ABOUT",
        "title": "About Ariyalur Golden Hospital | Hospital in Ariyalur",
        "desc": "Learn about Ariyalur Golden Hospital, its patient-care approach, departments and facilities serving Ariyalur and nearby communities.",
    },
    "case-studies.html": {
        "active": "CASE_STUDIES",
        "title": "Overview of Patient Care | Ariyalur Golden Hospital",
        "desc": "General information about how assessment, diagnosis, treatment and follow-up may be coordinated at Ariyalur Golden Hospital.",
    },
    "doctors.html": {
        "active": "DOCTORS",
        "title": "Our Doctors | Consultants — Ariyalur Golden Hospital",
        "desc": "Consultants at Ariyalur Golden Hospital and the specialties they cover. Call reception on 04329 222530 to confirm the current consultation schedule.",
    },
    "departments.html": {
        "active": "DEPARTMENTS",
        "title": "Hospital Departments in Ariyalur | Ariyalur Golden Hospital",
        "desc": "Explore clinical departments at Ariyalur Golden Hospital. Specialist schedules may change; please call reception before travelling.",
    },
    "services.html": {
        "active": "SERVICES",
        "title": "Hospital Services in Ariyalur | Ariyalur Golden Hospital",
        "desc": "Explore selected medical, surgical, emergency and support services at Ariyalur Golden Hospital. Call to confirm current availability.",
    },
    "scans.html": {
        "active": "SCANS",
        "title": "MRI, CT, X-ray and Ultrasound in Ariyalur | Golden Hospital",
        "desc": "On-site MRI, CT, X-ray and ultrasound services at Ariyalur Golden Hospital. Call to confirm availability, preparation and report timelines.",
    },
    "diagnostics.html": {
        "active": "DIAGNOSTICS",
        "title": "Diagnostic Centre in Ariyalur | Lab, ECG and Endoscopy",
        "desc": "Laboratory tests, ECG, echocardiography and selected endoscopic procedures at Ariyalur Golden Hospital. Call to confirm preparation and availability.",
    },
    "facilities.html": {
        "active": "FACILITIES",
        "title": "Hospital Facilities in Ariyalur | Ariyalur Golden Hospital",
        "desc": "Explore selected facilities at Ariyalur Golden Hospital. Availability, hours and access vary by service; call to confirm.",
    },
    "health-checkup.html": {
        "active": "HEALTH_CHECKUP",
        "title": "Health Check-up Packages in Ariyalur | Golden Hospital",
        "desc": "Explore health check-up options at Ariyalur Golden Hospital. Tests should be selected according to individual needs; call 04329 222530 for current inclusions and prices.",
    },
    "insurance.html": {
        "active": "INSURANCE",
        "title": "Insurance Support & Cashless Treatment | Ariyalur Golden Hospital",
        "desc": "Learn about insurance support and cashless treatment at Ariyalur Golden Hospital. Availability is subject to eligibility, pre-authorisation, current empanelment, and insurer or scheme approval.",
    },
    "gallery.html": {
        "active": "GALLERY",
        "title": "Hospital Gallery | Ariyalur Golden Hospital",
        "desc": "View photographs of Ariyalur Golden Hospital, including the hospital exterior, reception, selected patient-care areas and diagnostic facilities.",
    },
    "contact.html": {
        "active": "CONTACT",
        "title": "Contact Ariyalur Golden Hospital | Ariyalur, Tamil Nadu",
        "desc": "Contact Ariyalur Golden Hospital in Ariyalur, Tamil Nadu, for appointments, emergency care, dialysis enquiries and directions.",
    },
    "disclaimer.html": {
        "active": "DISCLAIMER",
        "title": "Medical & Website Disclaimer | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Medical and website disclaimer for Ariyalur Golden Hospital — the site is for general information only, does not create a doctor-patient relationship and is not a substitute for professional medical advice.",
    },
    "privacy.html": {
        "active": "PRIVACY",
        "title": "Privacy Policy | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "How Ariyalur Golden Hospital collects, stores, processes and protects patient personal and health data, in line with the DPDPA 2023 and the IT Act, 2000.",
    },
    "terms.html": {
        "active": "TERMS",
        "title": "Terms & Conditions of Use | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Terms and conditions governing the use of the Ariyalur Golden Hospital website, including intellectual property, appointment requests, patient responsibilities and limitation of liability.",
    },
}

ACTIVE_KEYS = [
    "INDEX", "ABOUT", "CASE_STUDIES", "DEPARTMENTS", "DOCTORS", "SERVICES",
    "SCANS", "DIAGNOSTICS", "FACILITIES", "HEALTH_CHECKUP",
    "INSURANCE", "GALLERY", "CONTACT",
]

# Parent nav links that stay highlighted while any page in their dropdown is
# open. The parent gets aria-current="true" (current item in a set), while the
# page itself keeps aria-current="page" on its dropdown entry.
SECTIONS = {
    "ABOUT": ["ABOUT", "CASE_STUDIES", "GALLERY"],
    "SERVICES": ["SERVICES", "SCANS", "DIAGNOSTICS", "FACILITIES", "HEALTH_CHECKUP"],
}


def build():
    header = (BUILD / "header.tpl").read_text(encoding="utf-8")
    footer = (BUILD / "footer.tpl").read_text(encoding="utf-8")
    written = []

    for slug, meta in PAGES.items():
        body_file = BUILD / "pages" / slug
        if not body_file.exists():
            print(f"  ! skipped {slug} (no body at {body_file.relative_to(ROOT)})")
            continue

        head = header
        head = head.replace("{{TITLE}}", meta["title"])
        head = head.replace("{{DESC}}", meta["desc"])
        # "author" is optional — pages that omit it get the registered name
        head = head.replace("{{AUTHOR}}", meta.get("author", DEFAULT_AUTHOR))
        head = head.replace("{{SLUG}}", slug)
        # absolute canonical — the home page canonicalises to the bare origin
        canonical = BASE_URL if slug == "index.html" else BASE_URL + slug
        head = head.replace("{{CANONICAL}}", canonical)
        head = head.replace("{{BASE}}", BASE_URL)
        for key in ACTIVE_KEYS:
            value = 'aria-current="page"' if key == meta["active"] else ""
            head = head.replace("{{ACTIVE_%s}}" % key, value)
        for section, members in SECTIONS.items():
            value = 'aria-current="true"' if meta["active"] in members else ""
            head = head.replace("{{SECTION_%s}}" % section, value)

        # tidy the empty attribute slots left behind
        head = re.sub(r'\s+(?=>)', '', head)

        page = head + "\n" + body_file.read_text(encoding="utf-8").rstrip() + "\n\n" + footer
        (ROOT / slug).write_text(page, encoding="utf-8")
        written.append(slug)

    print(f"Built {len(written)} pages: {', '.join(written)}")


if __name__ == "__main__":
    build()
