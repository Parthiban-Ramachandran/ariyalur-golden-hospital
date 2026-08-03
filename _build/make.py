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

PAGES = {
    "index.html": {
        "active": "INDEX",
        "author": "Ariyalur Golden Hospital",
        "title": "Ariyalur Golden Hospital | Multi-Speciality Hospital in Ariyalur",
        "desc": "Ariyalur Golden Hospital — multi-speciality hospital with 24×7 emergency care, ICU, blood bank, dialysis, MRI 1.5 Tesla, CT scan, modern operation theatres and expert consultants. Call 04329 222530.",
        "keywords": "multi speciality hospital Ariyalur, 24x7 emergency hospital, cardiology, neurosurgery, urology, dialysis centre, medical oncology, MRI 1.5 Tesla, CT scan, blood bank, ICU, maternity hospital, cashless hospital",
    },
    "about.html": {
        "active": "ABOUT",
        "title": "About Us | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Learn about Ariyalur Golden Hospital — our mission, vision, core values and the multi-speciality services we provide to Ariyalur and the surrounding districts.",
        "keywords": "about Ariyalur Golden Hospital, hospital mission vision, multi speciality hospital Ariyalur, hospital history, why choose us",
    },
    "case-studies.html": {
        "active": "CASE_STUDIES",
        "title": "Case Studies | Treatment Pathways — Ariyalur Golden Hospital",
        "desc": "Illustrative case studies showing how emergency care, imaging, theatre, intensive care and rehabilitation work together at Ariyalur Golden Hospital — trauma, joint replacement, kidney stone, dialysis, emergency caesarean and poisoning.",
        "keywords": "hospital case studies Ariyalur, trauma care case study, joint replacement, kidney stone surgery, dialysis, emergency caesarean, poisoning treatment, treatment pathway, patient care journey",
    },
    "doctors.html": {
        "active": "DOCTORS",
        "title": "Our Doctors | Specialist Consultants — Ariyalur Golden Hospital",
        "desc": "Meet the specialist consultants at Ariyalur Golden Hospital across cardiology, neurosurgery, urology, nephrology, oncology, pulmonology, radiology, paediatrics, obstetrics & gynaecology, general medicine, psychiatry, vascular surgery and physiotherapy.",
        "keywords": "doctors Ariyalur Golden Hospital, cardiologist Ariyalur, neurosurgeon, urologist, nephrologist, oncologist, pulmonologist, paediatrician, gynaecologist, psychiatrist, vascular surgeon, physiotherapist, consultant doctors",
    },
    "departments.html": {
        "active": "DEPARTMENTS",
        "title": "Departments | Centres of Excellence — Ariyalur Golden Hospital",
        "desc": "Explore the seventeen clinical departments at Ariyalur Golden Hospital — cardiology, neurology, orthopaedics, general surgery, urology, nephrology, oncology, pulmonology, paediatrics, obstetrics & gynaecology, psychiatry, vascular surgery and more.",
        "keywords": "hospital departments Ariyalur, cardiology department, neurology, orthopaedics, general surgery, urology, nephrology, medical oncology, pulmonology, radiology, paediatrics, obstetrics gynaecology, psychiatry, vascular surgery, anaesthesiology, physiotherapy",
    },
    "services.html": {
        "active": "SERVICES",
        "title": "Medical Services | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Main services — orthopaedics, general surgery and laser surgery — alongside emergency and trauma care, ICU, joint replacement, arthroscopy, spine surgery, laparoscopic surgery, kidney stone and prostate surgery, dialysis, oncology, poison treatment and maternity care.",
        "keywords": "medical services Ariyalur, orthopaedics Ariyalur, general surgery, laser surgery Ariyalur, piles laser treatment, varicose veins, emergency care, trauma care, ICU, joint replacement, arthroscopy, spine surgery, laparoscopic surgery, kidney stone surgery, prostate surgery, dialysis, poison treatment, maternity care",
    },
    "scans.html": {
        "active": "SCANS",
        "title": "Scans & Imaging | MRI 1.5 Tesla, CT Scan, X-Ray — Ariyalur Golden Hospital",
        "desc": "In-house scans at Ariyalur Golden Hospital — MRI 1.5 Tesla, CT scan, digital X-ray, ultrasound and consultant radiology reporting, with emergency imaging available 24×7.",
        "keywords": "MRI scan Ariyalur, MRI 1.5 Tesla, CT scan Ariyalur, digital X-ray, ultrasound scan, radiology reporting, scan centre Ariyalur, emergency CT scan",
    },
    "diagnostics.html": {
        "active": "DIAGNOSTICS",
        "title": "Diagnostic Centre | Laboratory, ECG, ECHO, Endoscopy — Ariyalur Golden Hospital",
        "desc": "In-house diagnostics at Ariyalur Golden Hospital — ECG, ECHO, a full laboratory and a complete endoscopy suite covering endoscopy, colonoscopy, colposcopy, hysteroscopy and laparoscopy. Scans are listed separately.",
        "keywords": "diagnostic centre Ariyalur, laboratory Ariyalur, ECG, ECHO, blood test, endoscopy, colonoscopy, colposcopy, hysteroscopy, laparoscopy",
    },
    "facilities.html": {
        "active": "FACILITIES",
        "title": "Hospital Facilities | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Ambulance, ICU, blood bank, dialysis unit, three operation theatres with C-Arm, MRI, CT scan, pharmacy, laboratory, physiotherapy and a 24-hour emergency ward.",
        "keywords": "hospital facilities Ariyalur, ambulance service, ICU, blood bank, dialysis unit, operation theatre, C-Arm, MRI, CT scan, pharmacy, laboratory, physiotherapy, emergency ward",
    },
    "health-checkup.html": {
        "active": "HEALTH_CHECKUP",
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
        "desc": "Contact Ariyalur Golden Hospital — reception 04329 222530, emergency 99438 27233, dialysis 84899 26941, token booking 94875 76493. Appointment request form and location.",
        "keywords": "contact Ariyalur Golden Hospital, hospital phone number Ariyalur, emergency number, dialysis contact, appointment booking, hospital address",
    },
    "disclaimer.html": {
        "active": "DISCLAIMER",
        "title": "Medical & Website Disclaimer | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Medical and website disclaimer for Ariyalur Golden Hospital — the site is for general information only, does not create a doctor-patient relationship and is not a substitute for professional medical advice.",
        "keywords": "medical disclaimer, website disclaimer, Ariyalur Golden Hospital, no doctor patient relationship, not medical advice, emergency notice",
    },
    "privacy.html": {
        "active": "PRIVACY",
        "title": "Privacy Policy | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "How Ariyalur Golden Hospital collects, stores, processes and protects patient personal and health data, in line with the DPDPA 2023 and the IT Act, 2000.",
        "keywords": "privacy policy, patient data protection, DPDPA 2023, IT Act 2000, health data privacy, cookies policy, grievance officer, Ariyalur Golden Hospital",
    },
    "terms.html": {
        "active": "TERMS",
        "title": "Terms & Conditions of Use | Ariyalur Golden Hospital (PVT) Ltd.",
        "desc": "Terms and conditions governing the use of the Ariyalur Golden Hospital website, including intellectual property, online appointment requests, patient responsibilities and limitation of liability.",
        "keywords": "terms and conditions, terms of use, website terms, appointment request terms, limitation of liability, governing law, Ariyalur Golden Hospital",
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
        head = head.replace("{{KEYWORDS}}", meta["keywords"])
        # "author" is optional — pages that omit it get the registered name
        head = head.replace("{{AUTHOR}}", meta.get("author", DEFAULT_AUTHOR))
        head = head.replace("{{SLUG}}", slug)
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
