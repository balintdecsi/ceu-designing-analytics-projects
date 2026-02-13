# Gemini CLI Project Context

## Overview
This file serves as a persistent context and guide for Gemini CLI agents working on this project. It captures key project details, recurring issues, and established best practices to ensure consistency and prevent repeated errors.

## Project Structure
- **Reports:** LaTeX reports are located in `reports/<week_number>/`.
- **Prompts:** Weekly assignment prompts are in `weekly_writeups/prompts.md`.

## Lessons Learned & Best Practices

### Report Writing
- When translating markdown files to pdfs, use `pandoc [FILENAME].md -o [FILENAME].pdf --pdf-engine=pdflatex`.
- When writing code that generates LaTeX (e.g., Python scripts producing tables), ensure the script handles character escaping automatically. Use `pdflatex`.
- Add the following declaration at the end:
```
---

**AI Declaration:** I've used AI for this task according to our MS program's [AI policy](https://gabors-data-analysis.com/aipolicy/). This document's structural skeleton (headings etc.) and typesetting were assisted by the Gemini CLI tool, using Gemini 3. The prompt used was: "Make a skeleton for the report based on Week 3 task in the task description. Stick to the outline of the task markdown file."
```

### LaTeX Generation
- **Critical:** When generating or editing LaTeX files (`.tex`), YOU MUST ESCAPE SPECIAL CHARACTERS.
  - `&` becomes `\&`
  - `%` becomes `\%`
  - `_` becomes `\_` (unless inside `\texttt{}`)
  - `$` becomes `\$`
  - `#` becomes `\#`
- **Math Mode:** Be careful with symbols like `>` or `<`. In text mode, they might need to be wrapped in math mode (e.g., `$<$`, `$>$`) or use specific text commands like `\textgreater`.
- **Tool Usage:** When fixing small errors in a file (like a single unescaped character), prefer using the `replace` tool rather than overwriting the entire file with `write_file`. This reduces the risk of accidentally stripping valid escapes or introducing new formatting issues.

### Compilation
- When compiling latex, do it with `pdflatex -interaction=nonstopmode report.tex` to catch errors early.
- If compilation fails, inspect the log output for "Misplaced alignment tab character" (indicates unescaped `&`) or similar errors.