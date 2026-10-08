# Education plugins for ChatGPT and Codex

Skill-based plugins, published by `jonathan-exercising-tech`. No MCP service or account credentials are required by these packages.

| Plugin | Version | Contents |
|---|---|---|
| [LaTeX Theory Handouts](plugins/latex-theory-handouts) | 3.0.0 | Uploaded editorial v3 theory skill, fonts, master, QA |
| [LaTeX Worksheets](plugins/latex-worksheets) | 3.0.0 | Skill packaged from uploaded worksheet v3 project |

## Install

Add this repository as a marketplace in a supported ChatGPT/Codex desktop client, or run:

```sh
codex plugin marketplace add jonathan-exercising-tech/chatgpt-plugins
```

Choose **Education Plugins** in the Plugins Directory and install the desired package. Start a new chat and invoke it from the plugin picker.

For a managed ChatGPT workspace, an administrator can import this GitHub repository from Admin > Plugins. Select the repository root, which contains `.agents/plugins/marketplace.json`. Availability depends on the client and workspace policy. GitHub publication alone does not install plugins on every device or submit them to OpenAI's universal public directory.

Official references: [packaging](https://developers.openai.com/plugins/build/plugins), [workspace import](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Requirements

LaTeX packages need XeLaTeX, standard TeX packages used by the masters, Latin Modern Math, and Poppler. Font files and their upstream license notices are included. HTML scripts require Python 3; image preprocessing may require Pillow. Illustration workflows need an available image-generation tool. No hosted service is deployed by installing these skills.

## Private signatures

LaTeX templates default to no signature. Configure an optional `signature.local.tex` beside your working document; see each LaTeX skill's `references/signatures.md`. The private file is ignored by Git. Do not distribute it or signed PDFs unintentionally.

## Source provenance

The LaTeX sources come from the two v3 ZIP attachments supplied for this release, not older locally installed LaTeX skills. The worksheet ZIP was a project, so its skill instructions and UI metadata were added while retaining the supplied template and fonts.

## Rights

Bundled third-party font license notices remain in their font directories. No new blanket license is granted for the original templates, skill text, or reference artwork by this release; their existing rights remain unchanged.
