# Automation Agents Workspace

This repository is a central hub for various automation scripts and agents designed to improve productivity and automate repetitive tasks.

## Table of Contents

- [Project Structure](#project-structure)
- [List of Active Agents](#list-of-active-agents)
- [How to Add a New Agent](#how-to-add-a-new-agent)
- [Development Guidelines](#development-guidelines)

---

## Project Structure

To maintain consistency, each script or agent must follow this structure:

```
Scripts/
├── AGENTS.md          # Root documentation (this file)
└── [agent-name]/      # Specific folder for the agent
    ├── agents.md      # Detailed documentation for the agent
    └── [script-files] # Implementation files (e.g., .py, .js, .sh)
```

## List of Active Agents

| Agent Name                | Description                                         | Folder                        | Status         |
| :------------------------ | :-------------------------------------------------- | :---------------------------- | :------------- |
| Automated Email           | Sends emails to multiple recipients via Python      | `automated_email/`            | ✅ Active      |
| Battery Notification      | Windows battery low/full alerts                     | `Battery_notification/`       | ✅ Active      |
| File Organizer            | Categorizes files into folders by extension         | `file-organizer/`             | ✅ Active      |
| Image Compressor          | Compresses images while maintaining quality         | `Image_Compressor/`           | ✅ Active      |
| Images to PDF             | Converts ordered images into a PDF document         | `images2pdf/`                 | ✅ Active      |
| Movie Sync                | Syncs missing movies from competitors to DB         | `movie-sync/`                 | 🚧 In Progress |
| Random Password Gen       | Generates secure, random passwords                  | `Random_Password_Generator/`  | ✅ Active      |
| Remove Duplicate Files    | Finds and removes duplicate files                   | `Remove-Duplicate-Files/`     | ✅ Active      |
| Subtitle Downloader       | Automatically downloads subtitles for movies         | `Subtitle-downloader/`        | ✅ Active      |
| Take Screenshot           | Captures screenshots using OpenCV                   | `Take_screenshot/`            | ✅ Active      |
| Task Scheduler            | CLI task management with due dates                  | `Task-Scheduler/`             | ✅ Active      |
| To Do Bot                 | Telegram bot for task management                    | `To Do Bot/`                  | ✅ Active      |
| URL Shortener             | Shortens long URLs using web scraping               | `url_shortener/`              | ✅ Active      |
| Website Blocker           | Blocks distracting sites during work hours          | `Website-Blocker/`            | ✅ Active      |
| Website URL Detector      | Detects and logs all URLs on a website              | `Website_Url_Detector/`       | ✅ Active      |
| Wifi Password             | Views saved Wi-Fi passwords                         | `Wifi-Password/`              | ✅ Active      |
| Wikipedia Search          | Searches Wikipedia and returns info                 | `Wikipedia-Search/`           | ✅ Active      |
| X Scrapper                | Scrapes tweets from specified X handle              | `X_Scrapper/`                 | ✅ Active      |
| Youtube Downloader        | Downloads YouTube videos using pytube               | `Youtube_Video_Downloader/`   | ✅ Active      |
| YTS Torrents              | Downloads movie torrents via Yify API               | `yts_torrents/`               | ✅ Active      |
| Zip Password Cracker      | Dictionary attack on ZIP file passwords             | `zip_password_cracker/`       | ✅ Active      |
| _Next Agent_              | _Awaiting your next request_                        | `tbd/`                        | 🚧 Planned     |

## How to Add a New Agent

1. **Create a Folder**: Create a subfolder with a kebab-case name (e.g., `web-scraper`).
2. **Document Your Agent**: Create an `agents.md` file inside that folder. It should include:
   - **Goal**: What does this agent do?
   - **Pre-requisites**: What needs to be installed (Python, Node, API keys)?
   - **Usage**: How do I run it?
   - **Maintenance**: Any specific logs or cleanup needed?
3. **Register/Update**: Add the new agent to the table in the "List of Active Agents" section in this root `AGENTS.md`.

## Development Guidelines

- **Standard Language**: Unless specified, prefer Python for data processing and Node.js for web-related automations.
- **Environment**: Use virtual environments (`venv`) or `package.json` to manage dependencies.
- **Documentation**: Keep documentation up to date as the script evolves.

---
