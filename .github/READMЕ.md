<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview".-->

# GitHub configuration (`.github/`)

The `.github/` folder holds files that support how a repository works on GitHub. For setup, activity directions, and course help, start with the [course README](../README.md).

> **About this filename.** The final letter in `READMЕ` is a Cyrillic `Е` (U+0415), which looks like the Latin `E`. This spelling keeps the root `README.md` visible on the repository home page. GitHub would otherwise give a standard `.github/README.md` priority. [GitHub README documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## What’s in this course repository

| File or folder | What it does |
| --- | --- |
| [`workflows/`](workflows/) and [`ci/`](ci/README.md) | Define automated checks for repository configuration, documentation links, and command examples. |
| [`CODEOWNERS`](CODEOWNERS) | Identifies the teams responsible for reviewing changes to repository files. |
| [`CHANGELOG.md`](CHANGELOG.md) | Records notable changes to the course repository. |
| [`copilot-instructions.md`](copilot-instructions.md), `agents/`, `instructions/`, and [`skills/`](skills/) | Guide Copilot and the Course Mentor in helping you understand and debug your work while keeping assessed work yours. |

## Shared GC-STEM guidance

A `.github/` folder can also contain templates for issues, pull requests, and discussions. GC-STEM maintains shared templates and community guidance, including its code of conduct, accessibility guidance, and support information, in the [GC-STEM `.github` repository](https://github.com/GC-STEM/.github).

GitHub can use these defaults for repositories owned by GC-STEM when a repository has no corresponding file of its own. If your course copy is under your personal account, use the links above to find the shared guidance. For help with coursework or setup, see [Help and Support](../README.md#help-and-support).
