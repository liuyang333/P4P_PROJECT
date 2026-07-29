# P4P Conference 2026 — Schedule Viewer

A single-file static website that displays the P4P Conference 2026 presentation schedule with search, filtering, and a full timetable grid. All data is embedded in `index.html`, so it works by double-clicking the file locally or hosted anywhere.

## Features
- **Search & Browse** — live search across title, student, supervisor / co-supervisor, assessor, and room, with matching text highlighted. Restrict to a single field, and filter by stream, room, or session.
- **Timetable Grid** — the full day as time × stream (6 streams), with chairs, breaks, and postgraduate-opportunity sessions.
- 125 talks, 9 info sessions, 5 breaks — colour-coded by stream.

## Deploy to GitHub Pages
1. Create a new GitHub repository (e.g. `p4p-2026`).
2. Upload `index.html` (keep that name).
3. Repo **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**.
5. Select branch `main`, folder `/ (root)`, then **Save**.
6. After ~1 minute the site is live at `https://<username>.github.io/<repo>/`.

`data.json` and `build.py` are included only for reference/regeneration — you do NOT need to upload them; `index.html` is fully self-contained.

## Adding the University of Auckland logo
The header has a logo slot. To show the official logo:
1. Download the official University of Auckland logo from the university's brand/identity portal (staff & students can access it). A **horizontal / reversed (white)** PNG or SVG works best on the blue header.
2. Save it as `logo.png` in the same folder as `index.html` (repo root), then upload it to GitHub.
3. That's it — the header will display it automatically.

If `logo.png` is missing, the header falls back to a clean "The University of Auckland" text mark, so the page never breaks. (The official logo is a trademarked asset, so it isn't bundled here — use your own copy from the brand portal.)
