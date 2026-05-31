from pathlib import Path
import json

import streamlit as st
import pandas as pd
from PIL import Image


BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"

TEAM_FILE = DATA_DIR / "team.json"
PROJECTS_FILE = DATA_DIR / "projects.json"
ACHIEVEMENTS_FILE = DATA_DIR / "achievements.json"

# Update these lists when the team has new public videos, repositories, reports,
# presentations, drives, demos, research links, or contact information.
YOUTUBE_LINKS = [
    {
        "title": "IAAA Demo Video",
        "url": "",
        "description": "Add a public YouTube demo, activity recap, or project walkthrough link here.",
    }
]

IMPORTANT_LINKS = {
    "GitHub repositories": [
        {"label": "IAAA GitHub Profile", "url": ""},
        {"label": "SmartSignal-AI Repository", "url": ""},
    ],
    "Project reports": [
        {"label": "SmartSignal-AI Report", "url": ""},
        {"label": "Simulation Dashboard Report", "url": ""},
    ],
    "Presentations": [
        {"label": "Team Presentation", "url": ""},
    ],
    "Google Drive links": [
        {"label": "Shared Project Folder", "url": ""},
    ],
    "Demo links": [
        {"label": "Live Demo Placeholder", "url": ""},
    ],
    "Research and documentation": [
        {"label": "Documentation Folder", "url": ""},
    ],
}

CONTACT_INFO = {
    "email": "alialabid@ieee.org",
    "contact_person": "IAAA Team Coordinator",
}

FOCUS_AREAS = [
    "Artificial Intelligence",
    "Simulation",
    "Software Development",
    "Data Analysis",
    "Smart Systems",
    "Academic Innovation",
]

PLACEHOLDER_PROJECTS = [
    {
        "title": "SmartSignal-AI",
        "description": "An intelligent traffic signal system using AI, simulation, and live dashboards.",
        "technologies": ["Python", "SUMO", "Streamlit", "AI"],
        "status": "In Progress",
        "image": "assets/projects/smartsignal.png",
        "github": "",
        "demo": "",
        "report": "",
    },
    {
        "title": "AI University Assistant",
        "description": "A smart assistant concept for academic support, information retrieval, and student services.",
        "technologies": ["Python", "NLP", "Streamlit"],
        "status": "Planned",
        "image": "",
        "github": "",
        "demo": "",
        "report": "",
    },
    {
        "title": "Digital Heritage Platform",
        "description": "A platform concept for preserving, organizing, and presenting cultural and academic heritage.",
        "technologies": ["Python", "Data Management", "Web"],
        "status": "Planned",
        "image": "",
        "github": "",
        "demo": "",
        "report": "",
    },
    {
        "title": "Simulation Dashboard",
        "description": "Interactive dashboards for modeling, monitoring, and analyzing simulation outputs.",
        "technologies": ["Python", "Streamlit", "Pandas", "Visualization"],
        "status": "In Progress",
        "image": "",
        "github": "",
        "demo": "",
        "report": "",
    },
]

PLACEHOLDER_TEAM = [
    {
        "name": "Member Name",
        "role": "AI Developer",
        "description": "Works on AI models, automation workflows, and data processing for IAAA projects.",
        "image": "assets/team/member1.png",
        "github": "",
        "linkedin": "",
    },
    {
        "name": "Team Member",
        "role": "Software Developer",
        "description": "Builds web tools, dashboards, and software systems for academic innovation.",
        "image": "",
        "github": "",
        "linkedin": "",
    },
    {
        "name": "Team Member",
        "role": "Simulation Engineer",
        "description": "Supports modeling, simulation scenarios, and technical project documentation.",
        "image": "",
        "github": "",
        "linkedin": "",
    },
]

PLACEHOLDER_ACHIEVEMENTS = [
    {
        "title": "Project Milestone",
        "description": "Completed initial prototype and dashboard integration.",
        "date": "2026",
        "type": "Milestone",
    },
    {
        "title": "University Activity",
        "description": "Presented student technical work and academic project ideas.",
        "date": "2026",
        "type": "Activity",
    },
]


def load_json(path, fallback=None):
    """Load a JSON list or dictionary without exposing errors to app visitors."""
    fallback = fallback if fallback is not None else []
    try:
        if not Path(path).exists():
            return fallback
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if data in ("", None, [], {}):
            return fallback
        return data
    except (json.JSONDecodeError, OSError, TypeError):
        return fallback


def safe_image(image_path, caption=None, use_container_width=True):
    """Display an image when available and otherwise render a calm placeholder."""
    if not image_path:
        st.markdown('<div class="image-placeholder">Image coming soon</div>', unsafe_allow_html=True)
        return

    path = Path(image_path)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        if path.exists() and path.is_file():
            Image.open(path)
            st.image(str(path), caption=caption, use_container_width=use_container_width)
        else:
            st.markdown('<div class="image-placeholder">Image coming soon</div>', unsafe_allow_html=True)
    except Exception:
        st.markdown('<div class="image-placeholder">Image coming soon</div>', unsafe_allow_html=True)


def apply_css():
    st.markdown(
        """
        <style>
            :root {
                --background: #101415;
                --surface-lowest: #0b0f10;
                --surface-card: #1d2022;
                --surface-slate: #1e293b;
                --surface-raised: #272a2c;
                --surface-higher: #323537;
                --primary: #adc6ff;
                --primary-strong: #3b82f6;
                --secondary: #4cd7f6;
                --secondary-strong: #06b6d4;
                --text-primary: #f8fafc;
                --text-soft: #e0e3e5;
                --text-secondary: #c2c6d6;
                --border: #334155;
                --border-strong: #424754;
                --border-bright: #8c909f;
                --shadow: rgba(0, 0, 0, 0.34);
                --font-body: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                --font-mono: "JetBrains Mono", "Courier New", monospace;
            }

            .stApp {
                background:
                    radial-gradient(circle at 18% 0%, rgba(59, 130, 246, 0.18), transparent 28rem),
                    radial-gradient(circle at 88% 10%, rgba(76, 215, 246, 0.12), transparent 24rem),
                    linear-gradient(180deg, #101415 0%, #0b0f10 100%);
                color: var(--text-primary);
                font-family: var(--font-body);
            }

            .block-container {
                max-width: 1220px;
                padding-top: 32px;
                padding-bottom: 56px;
            }

            h1, h2, h3, p, li, span, div {
                font-family: var(--font-body);
            }

            h1, h2, h3 {
                letter-spacing: 0;
            }

            h1, h2, h3,
            .stMarkdown h1,
            .stMarkdown h2,
            .stMarkdown h3 {
                color: var(--text-primary);
            }

            h2 {
                font-size: clamp(1.75rem, 2.5vw, 2.3rem);
                margin-top: 40px;
                margin-bottom: 12px;
            }

            h3,
            .stMarkdown h3 {
                font-size: 1.12rem;
            }

            a {
                color: var(--secondary);
                text-decoration: none;
            }

            a:hover {
                color: var(--primary);
                text-decoration: none;
            }

            [data-testid="stCaptionContainer"] {
                color: var(--text-secondary);
            }

            hr {
                border-color: var(--border);
                opacity: 0.75;
            }

            .section-kicker {
                color: var(--secondary);
                font-family: var(--font-mono);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08rem;
                text-transform: uppercase;
                margin-bottom: 8px;
            }

            .hero {
                position: relative;
                overflow: hidden;
                background:
                    radial-gradient(circle at 82% 14%, rgba(76, 215, 246, 0.26), transparent 18rem),
                    radial-gradient(circle at 18% 6%, rgba(59, 130, 246, 0.24), transparent 20rem),
                    linear-gradient(135deg, #0b0f10 0%, #101415 42%, #1e293b 100%);
                color: var(--text-primary);
                border-radius: 16px;
                padding: clamp(32px, 5vw, 64px);
                margin-bottom: 40px;
                border: 1px solid rgba(76, 215, 246, 0.22);
                box-shadow: 0 28px 80px var(--shadow);
            }

            .hero::before {
                content: "";
                position: absolute;
                inset: 0;
                background:
                    linear-gradient(rgba(173, 198, 255, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(173, 198, 255, 0.04) 1px, transparent 1px);
                background-size: 44px 44px;
                mask-image: linear-gradient(135deg, rgba(0, 0, 0, 0.85), transparent 72%);
                pointer-events: none;
            }

            .hero > div {
                position: relative;
                z-index: 1;
            }

            .hero h1 {
                color: var(--text-primary);
                font-size: clamp(3.2rem, 8vw, 6.4rem);
                line-height: 1;
                margin-bottom: 12px;
                font-weight: 900;
            }

            .hero-slogan {
                color: var(--primary);
                font-size: clamp(1.12rem, 2vw, 1.45rem);
                font-weight: 700;
                margin-bottom: 16px;
            }

            .hero-description {
                color: var(--text-soft);
                font-size: 1.02rem;
                line-height: 1.7;
                max-width: 720px;
            }

            .stat-row {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 12px;
                margin-top: 28px;
            }

            .stat {
                border: 1px solid rgba(76, 215, 246, 0.22);
                background: rgba(30, 41, 59, 0.72);
                border-radius: 8px;
                padding: 14px;
                backdrop-filter: blur(12px);
            }

            .stat strong {
                display: block;
                color: var(--secondary);
                font-family: var(--font-mono);
                font-size: 1rem;
                letter-spacing: 0.04rem;
                margin-bottom: 4px;
            }

            .stat span {
                color: var(--text-secondary);
                font-size: 0.88rem;
            }

            .card {
                background: linear-gradient(180deg, rgba(30, 41, 59, 0.92), rgba(29, 32, 34, 0.96));
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 24px;
                min-height: 100%;
                box-shadow: 0 18px 46px rgba(0, 0, 0, 0.18);
                transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
            }

            .card:hover {
                border-color: rgba(76, 215, 246, 0.7);
                box-shadow: 0 22px 54px rgba(6, 182, 212, 0.10);
                transform: translateY(-2px);
            }

            .card h3 {
                color: var(--text-primary);
                margin-top: 0;
                margin-bottom: 8px;
                font-size: 1.15rem;
            }

            .muted {
                color: var(--text-secondary);
                line-height: 1.65;
            }

            .badge-row {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 16px;
                margin-bottom: 4px;
            }

            .badge {
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                border: 1px solid rgba(76, 215, 246, 0.26);
                background: rgba(6, 182, 212, 0.12);
                color: var(--secondary);
                font-family: var(--font-mono);
                font-size: 0.78rem;
                font-weight: 700;
                padding: 6px 10px;
                line-height: 1;
            }

            .status {
                background: rgba(59, 130, 246, 0.16);
                border-color: rgba(173, 198, 255, 0.34);
                color: var(--primary);
            }

            .image-placeholder {
                min-height: 150px;
                border-radius: 16px;
                border: 1px dashed var(--border-bright);
                background:
                    linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(76, 215, 246, 0.08)),
                    var(--surface-lowest);
                color: var(--text-secondary);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: var(--font-mono);
                font-weight: 700;
                margin-bottom: 16px;
                text-align: center;
            }

            .logo-placeholder {
                height: 180px;
                border-radius: 16px;
                border: 1px solid rgba(76, 215, 246, 0.26);
                background: rgba(11, 15, 16, 0.46);
                color: var(--primary);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2.4rem;
                font-weight: 900;
                box-shadow: inset 0 0 40px rgba(76, 215, 246, 0.10);
            }

            [data-testid="stImage"] img {
                border-radius: 16px;
                border: 1px solid rgba(66, 71, 84, 0.8);
                background: var(--surface-lowest);
            }

            .timeline-item {
                border-left: 4px solid var(--secondary);
                border-radius: 0 16px 16px 0;
                background: linear-gradient(90deg, rgba(76, 215, 246, 0.10), rgba(30, 41, 59, 0.62));
                border-top: 1px solid var(--border);
                border-right: 1px solid var(--border);
                border-bottom: 1px solid var(--border);
                padding: 18px 20px;
                margin-bottom: 14px;
                box-shadow: 0 14px 32px rgba(0, 0, 0, 0.14);
            }

            .timeline-meta {
                color: var(--secondary);
                font-family: var(--font-mono);
                font-size: 0.82rem;
                font-weight: 800;
                text-transform: uppercase;
            }

            .timeline-item h3 {
                color: var(--text-primary);
                margin: 8px 0 4px;
            }

            .link-list a {
                display: inline-flex;
                width: fit-content;
                margin: 4px 0;
                border: 1px solid rgba(76, 215, 246, 0.28);
                border-radius: 8px;
                padding: 8px 12px;
                color: var(--text-primary);
                font-weight: 700;
                text-decoration: none;
                background: linear-gradient(135deg, rgba(59, 130, 246, 0.24), rgba(6, 182, 212, 0.18));
            }

            .link-list a:hover {
                border-color: var(--secondary);
                color: #ffffff;
            }

            .primary-action {
                display: inline-flex;
                width: fit-content;
                align-items: center;
                justify-content: center;
                margin-top: 24px;
                border: 1px solid rgba(76, 215, 246, 0.38);
                border-radius: 8px;
                padding: 11px 16px;
                color: #ffffff;
                font-weight: 800;
                text-decoration: none;
                background: linear-gradient(135deg, var(--primary-strong), var(--secondary-strong));
                box-shadow: 0 12px 30px rgba(6, 182, 212, 0.18);
            }

            .primary-action:hover {
                color: #ffffff;
                border-color: var(--primary);
            }

            .empty-note {
                border: 1px dashed var(--border-bright);
                background: rgba(30, 41, 59, 0.58);
                color: var(--text-secondary);
                border-radius: 16px;
                padding: 20px;
            }

            [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stMarkdownContainer"] {
                color: var(--text-soft);
            }

            [data-testid="stMarkdownContainer"] strong {
                color: var(--text-primary);
            }

            div[data-testid="column"] > div:has(> div .card),
            div[data-testid="column"] > div:has(> .card) {
                height: 100%;
            }

            .stButton > button,
            .stDownloadButton > button {
                border-radius: 8px;
                border: 1px solid rgba(76, 215, 246, 0.34);
                background: linear-gradient(135deg, var(--primary-strong), var(--secondary-strong));
                color: #ffffff;
                font-weight: 800;
            }

            .stButton > button:hover,
            .stDownloadButton > button:hover {
                border-color: var(--primary);
            }

            @media (max-width: 760px) {
                .block-container {
                    padding: 20px 16px 40px;
                }

                .hero {
                    padding: 24px;
                }

                .hero h1 {
                    font-size: 3rem;
                }

                .stat-row {
                    grid-template-columns: 1fr;
                }

                .card {
                    padding: 18px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def clean_text(value, fallback="Not available yet"):
    if value is None:
        return fallback
    text = str(value).strip()
    return text if text else fallback


def render_section_header(kicker, title, description=None):
    st.markdown(f'<div class="section-kicker">{kicker}</div>', unsafe_allow_html=True)
    st.markdown(f"## {title}")
    if description:
        st.markdown(f'<p class="muted">{description}</p>', unsafe_allow_html=True)


def render_link(label, url):
    label = clean_text(label, "Link")
    url = str(url or "").strip()
    if url:
        st.markdown(f"[{label}]({url})")
    


def render_hero():
    logo_path = ASSETS_DIR / "logo.png"
    with st.container():
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        h_left, h_right = st.columns([2.2, 0.8], gap="large")
        with h_left:
            st.markdown('<div class="section-kicker">IAAA Academic Innovation</div>', unsafe_allow_html=True)
            st.markdown("# IAAA")
            st.markdown(
                '<div class="hero-slogan">Engineering intelligent academic systems for real-world impact.</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<p class="hero-description">IAAA is a student technical team focused on artificial intelligence, '
                "automation, simulation, software systems, and innovative academic projects.</p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                """
                <div class="stat-row">
                    <div class="stat"><strong>AI</strong><span>Models and automation</span></div>
                    <div class="stat"><strong>Simulation</strong><span>Scenarios and systems</span></div>
                    <div class="stat"><strong>Software Systems</strong><span>Tools and dashboards</span></div>
                    <div class="stat"><strong>Academic Innovation</strong><span>Research-minded projects</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with h_right:
            if logo_path.exists():
                safe_image(logo_path)
            else:
                st.markdown('<div class="logo-placeholder">IAAA</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


def render_about():
    render_section_header(
        "About",
        "About IAAA",
        "A student-led academic team building practical systems from research, engineering, and disciplined collaboration.",
    )
    who, mission, vision = st.columns(3, gap="medium")
    with who:
        st.markdown(
            """
            <div class="card">
                <h3>Who We Are</h3>
                <p class="muted">IAAA brings together students who are interested in turning technical study into
                thoughtful, working academic projects in intelligent systems, automation, simulation, and software.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with mission:
        st.markdown(
            """
            <div class="card">
                <h3>Mission</h3>
                <p class="muted">To develop well-documented prototypes, strengthen technical skill, and create a
                collaborative environment where students learn by building serious, useful systems.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with vision:
        st.markdown(
            """
            <div class="card">
                <h3>Vision</h3>
                <p class="muted">To become a trusted academic innovation team known for clear ideas, reliable
                engineering practice, and projects that reflect both ambition and responsibility.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Main Focus Areas")
    st.markdown(
        '<div class="badge-row">'
        + "".join(f'<span class="badge">{area}</span>' for area in FOCUS_AREAS)
        + "</div>",
        unsafe_allow_html=True,
    )


def render_team():
    members = load_json(TEAM_FILE, PLACEHOLDER_TEAM)
    if not isinstance(members, list) or not members:
        members = PLACEHOLDER_TEAM

    render_section_header(
        "People",
        "Team Members",
        "A multidisciplinary group of students contributing research, design, development, analysis, and project leadership.",
    )

    cols = st.columns(3, gap="medium")
    for index, member in enumerate(members):
        if not isinstance(member, dict):
            member = {}
        with cols[index % 3]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            safe_image(member.get("image"))
            st.markdown(f"### {clean_text(member.get('name'), 'Team Member')}")
            st.markdown(f"**{clean_text(member.get('role'), 'Technical Member')}**")
            st.markdown(f'<p class="muted">{clean_text(member.get("description"), "Profile details coming soon.")}</p>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


def render_projects():
    projects = load_json(PROJECTS_FILE, PLACEHOLDER_PROJECTS)
    if not isinstance(projects, list) or not projects:
        projects = PLACEHOLDER_PROJECTS

    render_section_header(
        "Work",
        "Projects",
        "Applied academic work across artificial intelligence, simulation, dashboards, smart systems, and software platforms.",
    )

    for index in range(0, len(projects), 2):
        row = st.columns(2, gap="medium")
        for col, project in zip(row, projects[index : index + 2]):
            if not isinstance(project, dict):
                project = {}
            with col:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                safe_image(project.get("image"))
                st.markdown(f"### {clean_text(project.get('title'), 'Project Title')}")
                st.markdown(f'<p class="muted">{clean_text(project.get("description"), "Project description coming soon.")}</p>', unsafe_allow_html=True)
                technologies = project.get("technologies") or ["Technology details coming soon"]
                if not isinstance(technologies, list):
                    technologies = [str(technologies)]
                st.markdown(
                    '<div class="badge-row">'
                    + f'<span class="badge status">{clean_text(project.get("status"), "Planned")}</span>'
                    + "".join(f'<span class="badge">{clean_text(tech, "Tech")}</span>' for tech in technologies)
                    + "</div>",
                    unsafe_allow_html=True,
                )
                st.markdown("</div>", unsafe_allow_html=True)


def render_achievements():
    achievements = load_json(ACHIEVEMENTS_FILE, PLACEHOLDER_ACHIEVEMENTS)
    if not isinstance(achievements, list) or not achievements:
        achievements = PLACEHOLDER_ACHIEVEMENTS

    render_section_header(
        "Progress",
        "Achievements and Activities",
        "A record of academic milestones, competitions, events, certificates, university activities, and team progress.",
    )

    for item in achievements:
        if not isinstance(item, dict):
            item = {}
        st.markdown(
            f"""
            <div class="timeline-item">
                <div class="timeline-meta">{clean_text(item.get("type"), "Achievement")} | {clean_text(item.get("date"), "Date TBA")}</div>
                <h3>{clean_text(item.get("title"), "Achievement Title")}</h3>
                <p class="muted">{clean_text(item.get("description"), "Achievement details coming soon.")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_gallery():
    render_section_header(
        "Media",
        "Gallery / Media",
        "Selected project visuals, team activity photos, prototype screenshots, and demonstration media.",
    )

    gallery_dir = ASSETS_DIR / "gallery"
    image_files = []
    if gallery_dir.exists():
        image_files = sorted(
            [
                path
                for path in gallery_dir.iterdir()
                if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
            ]
        )

    if image_files:
        cols = st.columns(3, gap="medium")
        for index, image in enumerate(image_files):
            with cols[index % 3]:
                safe_image(image, caption=image.stem.replace("-", " ").replace("_", " ").title())
    else:
        st.markdown(
            '<div class="empty-note">Gallery images will appear here after files are added to assets/gallery/.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("### Video Links")
    has_video = False
    for video in YOUTUBE_LINKS:
        url = str(video.get("url", "")).strip()
        if url:
            has_video = True
            st.markdown(f"**{clean_text(video.get('title'), 'Video')}**")
            st.markdown(f'<p class="muted">{clean_text(video.get("description"), "")}</p>', unsafe_allow_html=True)
            st.video(url)
    if not has_video:
        st.caption("Video highlights will appear here when they are available.")


def render_links():
    render_section_header(
        "Resources",
        "Links and Documents",
        "Public repositories, reports, presentations, demos, drives, and research resources.",
    )

    cols = st.columns(2, gap="medium")
    for index, (category, links) in enumerate(IMPORTANT_LINKS.items()):
        with cols[index % 2]:
            st.markdown('<div class="card link-list">', unsafe_allow_html=True)
            st.markdown(f"### {category}")
            for link in links:
                render_link(link.get("label", "Link"), link.get("url", ""))
            st.markdown("</div>", unsafe_allow_html=True)


def render_contact():
    render_section_header(
        "Contact",
        "Contact IAAA",
        "For academic collaboration, project discussion, or university activities, the team can be reached through the contact details below.",
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Team Contact")
    st.markdown(f"**Email:** {clean_text(CONTACT_INFO.get('email'), 'Email coming soon')}")
    st.markdown(f"**Contact person:** {clean_text(CONTACT_INFO.get('contact_person'), 'Contact person TBA')}")
    st.markdown("</div>", unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="IAAA | Student Technical Team",
        page_icon=str(ASSETS_DIR / "logo.png") if (ASSETS_DIR / "logo.png").exists() else None,
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    apply_css()

    render_hero()
    render_about()
    render_team()
    render_projects()
    render_achievements()
    render_gallery()
    render_contact()

    st.markdown("---")
    st.caption("IAAA Student Technical Team | Artificial Intelligence, Automation, Simulation, and Academic Innovation")


if __name__ == "__main__":
    main()
