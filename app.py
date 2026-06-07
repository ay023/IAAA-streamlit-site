from pathlib import Path
import json
import base64
import html

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
    """Display an image only when the file is available."""
    if not image_path:
        return

    path = Path(image_path)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        if path.exists() and path.is_file():
            Image.open(path)
            st.image(str(path), caption=caption, use_container_width=use_container_width)
    except Exception:
        return


def apply_css():
    st.markdown(
        """
        <style>
            :root {
                --background: #d8d0c3;
                --secondary-background: #ebe6dd;
                --section-background: #ebe6dd;
                --card-background: #f4f1eb;
                --text-primary: #111718;
                --text-heading-soft: #1f2526;
                --text-body: #2f3433;
                --text-secondary: #4a4f4d;
                --text-muted: #6b6f6a;
                --border: #c8bfb2;
                --primary: #111718;
                --primary-hover: #111718;
                --accent-soft: #e4ddd2;
                --shadow: rgba(31, 37, 38, 0.12);
                --font-body: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .stApp {
                background: var(--background);
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
            h4,
            .stMarkdown h1,
            .stMarkdown h2,
            .stMarkdown h3,
            .stMarkdown h4 {
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

            .stMarkdown h1 a,
            .stMarkdown h2 a,
            .stMarkdown h3 a,
            [data-testid="stMarkdownContainer"] h1 a,
            [data-testid="stMarkdownContainer"] h2 a,
            [data-testid="stMarkdownContainer"] h3 a,
            a.anchor-link,
            a.headerlink,
            a[title="Permalink"] {
                display: none !important;
            }

            a {
                color: var(--primary);
                text-decoration: none;
            }

            a:hover {
                color: var(--primary-hover);
                text-decoration: none;
            }

            [data-testid="stCaptionContainer"] {
                color: var(--text-muted);
            }

            hr {
                border-color: var(--border);
                opacity: 1;
            }

            .section-kicker {
                display: block;
                color: var(--text-heading-soft);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08rem;
                text-transform: uppercase;
                margin-top: 48px;
                margin-bottom: 16px;
            }

            .hero .section-kicker {
                margin-top: 0;
            }

            .hero {
                position: relative;
                overflow: hidden;
                background: var(--secondary-background);
                color: var(--text-primary);
                border-radius: 16px;
                padding: clamp(32px, 5vw, 64px);
                margin-bottom: 40px;
                border: 1px solid var(--border);
                box-shadow: 0 16px 40px var(--shadow);
            }

            .hero-grid {
                display: grid;
                grid-template-columns: minmax(0, 1fr);
                gap: 0;
                align-items: center;
            }

            .hero h1 {
                color: var(--text-primary);
                font-size: clamp(3.2rem, 8vw, 6.4rem);
                line-height: 1;
                margin-bottom: 12px;
                font-weight: 900;
            }

            .hero-slogan {
                color: var(--text-heading-soft);
                font-size: clamp(1.12rem, 2vw, 1.45rem);
                font-weight: 700;
                margin-bottom: 16px;
            }

            .hero-description {
                color: var(--text-body);
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
                border: 1px solid var(--border);
                background: rgba(244, 241, 235, 0.72);
                border-radius: 8px;
                padding: 14px;
            }

            .stat strong {
                display: block;
                color: var(--text-heading-soft);
                font-size: 1rem;
                letter-spacing: 0;
                margin-bottom: 4px;
            }

            .stat span {
                color: var(--text-muted);
                font-size: 0.88rem;
            }

            .card {
                background: var(--card-background);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 24px;
                min-height: 100%;
                box-shadow: 0 10px 30px var(--shadow);
                transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
            }

            .card:hover {
                border-color: #b8ad9e;
                box-shadow: 0 14px 34px rgba(31, 37, 38, 0.14);
                transform: translateY(-2px);
            }

            .card h3 {
                color: var(--text-heading-soft);
                margin-top: 0;
                margin-bottom: 8px;
                font-size: 1.15rem;
            }

            .muted {
                color: var(--text-secondary);
                line-height: 1.65;
            }

            .team-role {
                color: var(--text-heading-soft);
                font-weight: 700;
                font-size: 1rem;
                line-height: 1.4;
                margin: 0 0 18px;
            }

            .team-card h3 {
                color: var(--text-primary);
                font-size: 1.375rem;
                line-height: 1.25;
                margin-top: 0;
                margin-bottom: 14px;
            }

            .team-card {
                text-align: center;
                min-height: 460px;
                height: 460px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                padding: 28px 24px;
            }

            .team-card .muted {
                color: var(--text-secondary);
                max-width: 28rem;
                margin-top: 0;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
                font-size: 0.95rem;
                line-height: 1.6;
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
                border: 1px solid #d2c8ba;
                background: var(--accent-soft);
                color: var(--text-heading-soft);
                font-size: 0.78rem;
                font-weight: 700;
                padding: 6px 10px;
                line-height: 1;
            }

            .status {
                background: #ebe6dd;
                border-color: var(--border);
                color: var(--text-heading-soft);
            }

            .avatar-placeholder {
                width: 125px;
                height: 125px;
                border-radius: 50%;
                border: 1px solid var(--border);
                background: var(--secondary-background);
                color: var(--text-heading-soft);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.9rem;
                font-weight: 900;
                letter-spacing: 0;
                margin: 0 auto 22px;
            }

            .member-photo {
                width: 125px;
                height: 125px;
                border-radius: 50%;
                object-fit: cover;
                display: block;
                margin: 0 auto 22px;
                border: 1px solid var(--border);
                background: var(--secondary-background);
            }

            .project-image {
                width: 100%;
                max-height: 230px;
                object-fit: cover;
                display: block;
                margin-bottom: 18px;
                border-radius: 16px;
                border: 1px solid var(--border);
                background: var(--secondary-background);
            }

            .project-card {
                height: 100%;
            }

            [data-testid="stImage"] img {
                border-radius: 16px;
                border: 1px solid var(--border);
                background: var(--secondary-background);
            }

            .timeline-item {
                border-left: 4px solid var(--primary);
                border-radius: 0 16px 16px 0;
                background: var(--card-background);
                border-top: 1px solid var(--border);
                border-right: 1px solid var(--border);
                border-bottom: 1px solid var(--border);
                padding: 18px 20px;
                margin-bottom: 14px;
                box-shadow: 0 10px 28px var(--shadow);
            }

            .timeline-meta {
                color: var(--text-heading-soft);
                font-size: 0.82rem;
                font-weight: 800;
                text-transform: uppercase;
            }

            .timeline-item h3 {
                color: var(--text-heading-soft);
                margin: 8px 0 4px;
            }

            .link-list a {
                display: inline-flex;
                width: fit-content;
                margin: 4px 0;
                border: 1px solid var(--border);
                border-radius: 8px;
                padding: 8px 12px;
                color: var(--text-heading-soft);
                font-weight: 700;
                text-decoration: none;
                background: var(--card-background);
            }

            .link-list a:hover {
                border-color: var(--primary);
                color: var(--primary-hover);
            }

            [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stMarkdownContainer"] {
                color: var(--text-body);
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
                border: 1px solid var(--primary);
                background: var(--primary);
                color: var(--card-background);
                font-weight: 800;
            }

            .stButton > button:hover,
            .stDownloadButton > button:hover {
                border-color: var(--primary-hover);
                background: var(--primary-hover);
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

                .hero-grid {
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


def member_initials(name):
    words = [part for part in clean_text(name, "Team Member").split() if part]
    if not words:
        return "TM"
    return "".join(word[0].upper() for word in words[:2])


def image_data_uri(image_file):
    if not image_file or not image_file.exists() or not image_file.is_file():
        return ""

    suffix = image_file.suffix.lower()
    media_type = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }.get(suffix)
    if not media_type:
        return ""

    try:
        image_data = base64.b64encode(image_file.read_bytes()).decode("utf-8")
    except OSError:
        return ""
    return f"data:{media_type};base64,{image_data}"


def member_avatar_html(image_file, name):
    safe_name = html.escape(clean_text(name, "Team Member"))
    image_src = image_data_uri(image_file)
    if image_src:
        return f'<img class="member-photo" src="{image_src}" alt="{safe_name}">'
    return f'<div class="avatar-placeholder">{member_initials(name)}</div>'


def project_image_html(image_path, title):
    path = str(image_path or "").strip()
    if not path:
        return ""
    image_file = BASE_DIR / path if not Path(path).is_absolute() else None
    image_src = image_data_uri(image_file)
    if not image_src:
        return ""
    safe_title = html.escape(clean_text(title, "Project image"))
    return f'<img class="project-image" src="{image_src}" alt="{safe_title}">'


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
    st.markdown(
        """
        <section class="hero">
            <div class="hero-grid">
                <div>
                    <div class="section-kicker">IAAA Academic Innovation</div>
                    <h1>IAAA</h1>
                    <div class="hero-slogan">Engineering intelligent academic systems for real-world impact.</div>
                    <p class="hero-description">IAAA is a student technical team focused on artificial intelligence,
                    automation, simulation, software systems, and innovative academic projects.</p>
                    <div class="stat-row">
                        <div class="stat"><strong>AI</strong><span>Models and automation</span></div>
                        <div class="stat"><strong>Simulation</strong><span>Scenarios and systems</span></div>
                        <div class="stat"><strong>Software Systems</strong><span>Tools and dashboards</span></div>
                        <div class="stat"><strong>Academic Innovation</strong><span>Research-minded projects</span></div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


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
            member_name = clean_text(member.get("name"), "Team Member")
            member_role = clean_text(member.get("role"), "Technical Member")
            member_description = clean_text(member.get("description"), "Profile details coming soon.")
            image_path = str(member.get("image", "") or "").strip()
            image_file = BASE_DIR / image_path if image_path and not Path(image_path).is_absolute() else None
            st.markdown(
                f"""
                <div class="card team-card">
                    {member_avatar_html(image_file, member_name)}
                    <h3>{html.escape(member_name)}</h3>
                    <p class="team-role">{html.escape(member_role)}</p>
                    <p class="muted">{html.escape(member_description)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


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
                title = str(project.get("title") or "").strip()
                description = str(project.get("description") or "").strip()
                status = str(project.get("status") or "").strip()
                technologies = project.get("technologies") or ["Technology details coming soon"]
                if not isinstance(technologies, list):
                    technologies = [str(technologies)]
                technologies = [str(tech).strip() for tech in technologies if str(tech).strip()]

                if not any([title, description, status, technologies]):
                    continue

                title = title or "Project Title"
                description = description or "Project details will be shared as the work develops."
                status = status or "Planned"
                badges = f'<span class="badge status">{html.escape(status)}</span>' + "".join(
                    f'<span class="badge">{html.escape(tech)}</span>' for tech in technologies
                )
                project_card_html = (
                    '<div class="card project-card">'
                    f'{project_image_html(project.get("image"), title)}'
                    f'<h3>{html.escape(title)}</h3>'
                    f'<p class="muted">{html.escape(description)}</p>'
                    f'<div class="badge-row">{badges}</div>'
                    '</div>'
                )
                st.markdown(project_card_html, unsafe_allow_html=True)


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
        title = str(item.get("title") or "").strip()
        description = str(item.get("description") or "").strip()
        date = str(item.get("date") or "").strip()
        achievement_type = str(item.get("type") or "").strip()
        if not any([title, description, date, achievement_type]):
            continue
        st.markdown(
            f"""
            <div class="timeline-item">
                <div class="timeline-meta">{html.escape(achievement_type or "Achievement")} | {html.escape(date or "Date TBA")}</div>
                <h3>{html.escape(title or "Achievement Title")}</h3>
                <p class="muted">{html.escape(description or "Achievement details coming soon.")}</p>
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
            '<p class="muted">Gallery media will appear here when team photos, screenshots, or demo visuals are available.</p>',
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
        visible_links = [
            link
            for link in links
            if isinstance(link, dict) and str(link.get("url") or "").strip()
        ]
        if not visible_links:
            continue
        with cols[index % 2]:
            links_html = "".join(
                f'<p><a href="{html.escape(str(link.get("url", "")).strip())}">{html.escape(clean_text(link.get("label"), "Link"))}</a></p>'
                for link in visible_links
            )
            st.markdown(
                f"""
                <div class="card link-list">
                    <h3>{html.escape(category)}</h3>
                    {links_html}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_contact():
    render_section_header(
        "Contact",
        "Contact IAAA",
        "For academic collaboration, project discussion, or university activities, the team can be reached through the contact details below.",
    )

    contact_rows = []
    email = str(CONTACT_INFO.get("email") or "").strip()
    contact_person = str(CONTACT_INFO.get("contact_person") or "").strip()

    if email:
        contact_rows.append(f"<p class=\"muted\"><strong>Email:</strong> {email}</p>")
    if contact_person:
        contact_rows.append(f"<p class=\"muted\"><strong>Contact person:</strong> {contact_person}</p>")

    if contact_rows:
        st.markdown(
            f"""
            <div class="card">
                <h3>Team Contact</h3>
                {''.join(contact_rows)}
            </div>
            """,
            unsafe_allow_html=True,
        )


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
