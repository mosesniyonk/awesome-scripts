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

| Agent Name     | Description                                 | Folder            | Status     |
| :------------- | :------------------------------------------ | :---------------- | :--------- |
| File Organizer | Categorizes files into folders by extension | `file-organizer/` | ✅ Active  |
| _Next Agent_   | _Awaiting your next request_                | `tbd/`            | 🚧 Planned |

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
