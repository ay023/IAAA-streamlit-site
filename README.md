# IAAA Streamlit Site

Public showcase website for **IAAA**, a student technical team focused on artificial intelligence, automation, simulation, software systems, and innovative academic projects.

## Features

- Professional public homepage for the IAAA team
- Hero section with logo support and clean fallback
- About, mission, vision, and focus areas
- Team member cards loaded from JSON
- Project cards loaded from JSON
- Achievements and activities timeline loaded from JSON
- Gallery section that reads images from `assets/gallery/`
- Editable links and contact sections
- Graceful handling for missing files, empty data, incomplete objects, and missing images
- Responsive Streamlit layout with custom CSS

## Design System

The visual identity follows a warm, practical academic showcase theme for IAAA Academic Innovation: beige backgrounds, charcoal headings, muted gray text, soft borders, rounded cards, and a calm organized layout.

The website uses a minimal university/team presentation style inspired by warm neutral interiors, with generous spacing, simple cards, readable academic sections, and minimal visual noise. Visual updates are controlled mainly from the custom CSS inside `app.py`, while team, project, and achievement content remains editable through JSON files.

## Project Structure

```text
IAAA-streamlit-site/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── logo.png
│   ├── team/
│   ├── projects/
│   └── gallery/
└── data/
    ├── team.json
    ├── projects.json
    └── achievements.json
```

## How To Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit in your browser.

## How To Update Team Members

Edit `data/team.json`.

Each member should follow this format:

```json
{
  "name": "Member Name",
  "role": "AI Developer",
  "description": "Works on AI models and data processing.",
  "image": "assets/team/member1.png",
  "github": "",
  "linkedin": ""
}
```

Leave `github`, `linkedin`, or `image` empty if unavailable. The app will show clean placeholders instead of errors.

## How To Update Projects

Edit `data/projects.json`.

Each project should follow this format:

```json
{
  "title": "SmartSignal-AI",
  "description": "An intelligent traffic signal system using AI, simulation, and live dashboards.",
  "technologies": ["Python", "SUMO", "Streamlit", "AI"],
  "status": "In Progress",
  "image": "assets/projects/smartsignal.png",
  "github": "",
  "demo": "",
  "report": ""
}
```

Supported status values can be `Completed`, `In Progress`, or `Planned`.

## How To Update Achievements

Edit `data/achievements.json`.

Each achievement should follow this format:

```json
{
  "title": "Project Milestone",
  "description": "Completed initial prototype and dashboard integration.",
  "date": "2026",
  "type": "Milestone"
}
```

Use the `type` field for categories such as competition, milestone, event, certificate, university activity, or team achievement.

## How To Update Images

- Team photos go in `assets/team/`
- Project images and screenshots go in `assets/projects/`
- Gallery images go in `assets/gallery/`
- The team logo should be saved as `assets/logo.png`

After adding images, update the matching JSON path, for example:

```json
"image": "assets/team/member1.png"
```

Gallery images are detected automatically from `assets/gallery/`.

## How To Update Important Links

Open `app.py` and update the `IMPORTANT_LINKS` dictionary near the top of the file.

You can add links for:

- GitHub repositories
- Project reports
- Presentations
- Google Drive folders
- Demo links
- Research and documentation

YouTube links can be updated in the `YOUTUBE_LINKS` list in `app.py`.

## How To Update Contact Information

Open `app.py` and update the `CONTACT_INFO` dictionary near the top of the file.

You can set:

- Team email
- GitHub profile or organization
- LinkedIn or social profile
- Contact person

## Deploy On Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Sign in with GitHub.
4. Click **Create app**.
5. Select the repository, branch, and `app.py` as the main file.
6. Confirm that `requirements.txt` is in the root of the repository.
7. Deploy the app.

## Live Demo

Final live demo link: _Coming soon_
