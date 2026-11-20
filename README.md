<div align="center">
  <h1>☘️ OpenNotesHub</h1>
  <p><b>A Curated Digital Garden for AI Engineering, Course Notes & Technical Knowledge</b></p>
  <p><i>Maintained by <a href="https://nthaihoc.github.io/about-me"><b>Nguyễn Thái Học</b></a> - AI Engineer</i></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22C55E?style=flat-square&labelColor=1F2937&logo=opensourceinitiative&logoColor=white" alt="License"></a>
    <a href="https://github.com/nthaihoc/open-notes-hub/actions"><img src="https://img.shields.io/github/actions/workflow/status/nthaihoc/open-notes-hub/ci.yml?style=flat-square&label=build&labelColor=1F2937&logo=githubactions&logoColor=white" alt="Build"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&labelColor=1F2937&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://squidfunk.github.io/mkdocs-material/"><img src="https://img.shields.io/badge/mkdocs--material-9.x-526CFE?style=flat-square&labelColor=1F2937&logo=materialformkdocs&logoColor=white" alt="MkDocs Material"></a>
    <a href="https://github.com/nthaihoc/open-notes-hub/stargazers"><img src="https://img.shields.io/github/stars/nthaihoc/open-notes-hub?style=flat-square&labelColor=1F2937&color=FBBF24&logo=github&logoColor=white" alt="Stars"></a>
  </p>

  <p>
    <a href="https://nthaihoc.github.io/open-notes-hub/"><img src="https://img.shields.io/badge/Live_Website-2563EB?style=flat-square&logo=google-chrome&logoColor=white" alt="Live Website"></a>
    <a href="https://nthaihoc.github.io/about-me"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=flat-square&logo=aboutdotme&logoColor=white" alt="Portfolio"></a>
    <a href="https://scholar.google.com/citations?user=SvS3rssAAAAJ&hl=vi"><img src="https://img.shields.io/badge/Scholar-34A853?style=flat-square&logo=google-scholar&logoColor=white" alt="Google Scholar"></a>
    <a href="mailto:thaihoc.ictu@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  </p>
</div>

## 📖 Overview

**OpenNotesHub** is an open-source digital garden where I systematize and document my continuous learning journey in Artificial Intelligence (AI). It serves as a centralized repository for structured lecture notes, mathematical foundations, and practical software engineering references.

Designed with clarity and accessibility in mind, this knowledge base supports both personal long-term reference and the broader AI community - particularly students and practitioners exploring **Machine Learning**, **Computer Vision**, **Large Language Models**, and **Backend Engineering**.

## 📂 Repository Structure

The repository keeps CI/CD automation and site configuration at the root, while all documentation content lives under `docs/`:

```text
open-notes-hub/
├── .github/workflows/       # CI/CD pipelines
├── docs/
│   ├── courses/             # Structured course notes
│   │   ├── applied-ml/      # Applied Machine Learning
│   │   ├── computer-vision/ # Computer Vision
│   │   └── llms/            # Large Language Models
│   └── knowledge-base/      # Practical engineering references
│       └── fastapi/         # FastAPI guides
├── mkdocs.yml
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Local Development & Installation

This site is built with **[MkDocs](https://www.mkdocs.org/)** and the **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** theme. To preview or edit the documentation locally, ensure you have **Python 3.10+** installed and follow these steps:

**Step 1: Clone the repository**
```bash
git clone https://github.com/nthaihoc/open-notes-hub.git
cd open-notes-hub
```

**Step 2: Create a virtual environment and install dependencies**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Step 3: Start the local development server**
```bash
mkdocs serve
```

Once the server is running, open your browser and visit `http://127.0.0.1:8000/` to preview the live site with hot-reload enabled.

## 🤝 Contributing

Contributions from the community are warmly welcomed! Whether you are fixing a typo, clarifying a mathematical derivation, adding code examples, or expanding an existing topic, every improvement helps make this resource better.

### How to Contribute
1. **Fork** the repository to your own GitHub account.
2. **Clone** your fork locally and create a dedicated branch for your changes:
   ```bash
   git checkout -b docs/your-topic-name
   ```
3. **Make your edits** inside the `docs/` directory and verify how they render locally using `mkdocs serve`.
4. **Commit** your changes with a clear, descriptive message (following [Conventional Commits](https://www.conventionalcommits.org/) is encouraged, e.g., `docs(cv): fix typo in convolution formula`).
5. **Push** your branch to your fork and open a **Pull Request** against the `main` branch.

### Reporting Issues & Suggestions
Found a broken link, rendering bug, or have a request for a new lecture topic? Please open a [GitHub Issue](https://github.com/nthaihoc/open-notes-hub/issues) with a brief description so we can discuss it.

## 👏 Acknowledgments

This project is made possible thanks to the incredible open-source tools and maintainers in the Python and documentation ecosystem:

- **[MkDocs](https://www.mkdocs.org/)** — Fast, simple static site generator geared towards building project documentation.
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — Modern, responsive, and feature-rich documentation framework by [@squidfunk](https://github.com/squidfunk).
- **[mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/)** — Seamless multi-language documentation plugin by [@ultrabug](https://github.com/ultrabug).
- **Open-Source Contributors** — Everyone who takes the time to read, share feedback, and submit pull requests.

## ⚖️ License

This repository is licensed under the **[MIT License](LICENSE)**. You are free to use, copy, modify, and distribute the content and source code for personal or educational purposes, provided that proper attribution is given to the original author.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/nthaihoc"><b>Nguyễn Thái Học</b></a> — AI Engineer</sub>
</div>