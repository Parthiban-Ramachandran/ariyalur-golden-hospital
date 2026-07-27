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

PAGES = {
    "index.html": {
        "active": "INDEX",
        "title": "Ariyalur Golden Hospital (PVT) Ltd. | Multi-Speciality Hospital in Ariyalur",
        "desc": "Ariyalur Golden Hospital (PVT) Ltd. — multi-speciality hospital with 24×7 emergency care, ICU, blood bank, dialysis, MRI 1.5 Tesla, CT scan, modern operation theatres and expert consultants. Call 04329 222530.",
        "keywords": "multi speciality hospital Ariyalur, 24x7 emergency hospital, cardiology, neurosurgery, urology, dialysis centre, medical oncology, MRI 1.5 Tesla, CT scan, blood bank, ICU, maternity hospital, cashless hospital",
    },
    "about.html": {
        "active": "ABOUT",
        "title": "About Us | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Learn about Ariyalur Golden Hospital — our mission, vision, core values and the multi-speciality services we provide to Ariyalur and the surrounding districts.",
        "keywords": "about Ariyalur Golden Hospital, hospital mission vision, multi speciality hospital Ariyalur, hospital history, why choose us",
    },
    "doctors.html": {
        "active": "DOCTORS",
        "title": "Our Doctors | Specialist Consultants — Ariyalur Golden Hospital",
        "desc": "Meet the specialist consultants at Ariyalur Golden Hospital across cardiology, neurosurgery, urology, nephrology, oncology, pulmonology, radiology, general medicine and physiotherapy.",
        "keywords": "doctors Ariyalur Golden Hospital, cardiologist Ariyalur, neurosurgeon, urologist, nephrologist, oncologist, pulmonologist, physiotherapist, consultant doctors",
    },
    "departments.html": {
        "active": "DEPARTMENTS",
        "title": "Departments | Centres of Excellence — Ariyalur Golden Hospital",
        "desc": "Explore the clinical departments at Ariyalur Golden Hospital — cardiology, neurology, orthopaedics, general surgery, urology, nephrology, oncology, pulmonology and more.",
        "keywords": "hospital departments Ariyalur, cardiology department, neurology, orthopaedics, general surgery, urology, nephrology, medical oncology, pulmonology, radiology, physiotherapy",
    },
    "services.html": {
        "active": "SERVICES",
        "title": "Medical Services | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Emergency and trauma care, ICU, joint replacement, arthroscopy, spine surgery, laparoscopic surgery, kidney stone and prostate surgery, dialysis, oncology, poison treatment and maternity care.",
        "keywords": "medical services Ariyalur, emergency care, trauma care, ICU, joint replacement, arthroscopy, spine surgery, laparoscopic surgery, kidney stone surgery, prostate surgery, dialysis, poison treatment, maternity care",
    },
    "diagnostics.html": {
        "active": "SERVICES",
        "title": "Diagnostic Centre | MRI, CT Scan, Laboratory — Ariyalur Golden Hospital",
        "desc": "In-house diagnostics at Ariyalur Golden Hospital — MRI 1.5 Tesla, CT scan, digital X-ray, ECG, ECHO, ultrasound-guided radiology, laboratory, endoscopy, colonoscopy, colposcopy, hysteroscopy and laparoscopy.",
        "keywords": "diagnostic centre Ariyalur, MRI 1.5 Tesla, CT scan, digital X-ray, ECG, ECHO, laboratory, endoscopy, colonoscopy, colposcopy, hysteroscopy, laparoscopy",
    },
    "facilities.html": {
        "active": "SERVICES",
        "title": "Hospital Facilities | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Ambulance, ICU, blood bank, dialysis unit, three operation theatres with C-Arm, MRI, CT scan, pharmacy, laboratory, physiotherapy and a 24-hour emergency ward.",
        "keywords": "hospital facilities Ariyalur, ambulance service, ICU, blood bank, dialysis unit, operation theatre, C-Arm, MRI, CT scan, pharmacy, laboratory, physiotherapy, emergency ward",
    },
    "schedule.html": {
        "active": "SCHEDULE",
        "title": "Consultation Schedule | Doctor Visiting Days — Ariyalur Golden Hospital",
        "desc": "Consultant visiting days and consultation timings at Ariyalur Golden Hospital, listed department-wise with appointment type.",
        "keywords": "doctor visiting schedule Ariyalur, consultation timing, OP timing, specialist visiting days, appointment booking",
    },
    "health-checkup.html": {
        "active": "SERVICES",
        "title": "Health Check-up Packages | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Master health check-up, preventive screening, family and corporate health packages at Ariyalur Golden Hospital.",
        "keywords": "master health checkup Ariyalur, preventive health package, corporate health checkup, family health package, annual health screening",
    },
    "insurance.html": {
        "active": "INSURANCE",
        "title": "Insurance & Cashless Treatment | Ariyalur Golden Hospital",
        "desc": "Cashless treatment under government employee insurance, the Chief Minister's Comprehensive Health Insurance Scheme, government dialysis cover, Star Health, Medi Assist, MD India, VIDAL and other TPAs.",
        "keywords": "cashless hospital Ariyalur, CM comprehensive health insurance scheme, government employee insurance, dialysis scheme, Star Health, Medi Assist, MD India, VIDAL, TPA hospital",
    },
    "gallery.html": {
        "active": "GALLERY",
        "title": "Gallery | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Photo gallery of Ariyalur Golden Hospital — building, reception, ICU, operation theatres, laboratory, MRI and CT suites, doctors and ambulance service.",
        "keywords": "Ariyalur Golden Hospital gallery, hospital photos, ICU, operation theatre, MRI, CT scan, laboratory, ambulance",
    },
    "contact.html": {
        "active": "CONTACT",
        "title": "Contact Us | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Contact Ariyalur Golden Hospital — reception 04329 222530, emergency 99438 27233, dialysis 84899 26941, token booking 84899 26947. Appointment request form and location.",
        "keywords": "contact Ariyalur Golden Hospital, hospital phone number Ariyalur, emergency number, dialysis contact, appointment booking, hospital address",
    },
}

ACTIVE_KEYS = [
    "INDEX", "ABOUT", "DEPARTMENTS", "DOCTORS", "SERVICES",
    "SCHEDULE", "INSURANCE", "GALLERY", "CONTACT",
]


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
        head = head.replace("{{KEYWORDS}}", meta["keywords"])
        head = head.replace("{{SLUG}}", slug)
        for key in ACTIVE_KEYS:
            value = 'aria-current="page"' if key == meta["active"] else ""
            head = head.replace("{{ACTIVE_%s}}" % key, value)

        # tidy the empty attribute slots left behind
        head = re.sub(r'\s+(?=>)', '', head)

        page = head + "\n" + body_file.read_text(encoding="utf-8").rstrip() + "\n\n" + footer
        (ROOT / slug).write_text(page, encoding="utf-8")
        written.append(slug)

    print(f"Built {len(written)} pages: {', '.join(written)}")


if __name__ == "__main__":
    build()
