import os
import re

file_path = "paragon/_overrides.scss"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    r"\$primary-light": "var(--pgn-color-primary-light)",
    r"\$primary": "var(--pgn-color-primary-base)",
    r"\$light-dark": "var(--pgn-color-text-footer)",
    r"\$text-color-primary": "var(--pgn-color-text-primary)",
    r"\$text-color-light": "var(--pgn-color-text-light)",
    r"\$text-color": "var(--pgn-color-text-base)",
    # Media queries that were inside overrides
    r"@include media-breakpoint-up\(sm\)": "@media (min-width: 576px)",
    r"@include media-breakpoint-down\(sm\)": "@media (max-width: 575.98px)",
    r"@include media-breakpoint-up\(md\)": "@media (min-width: 768px)",
    r"@include media-breakpoint-down\(md\)": "@media (max-width: 767.98px)",
    r"@include media-breakpoint-up\(lg\)": "@media (min-width: 992px)",
    r"@include media-breakpoint-down\(lg\)": "@media (max-width: 991.98px)",
    r"@include media-breakpoint-up\(xl\)": "@media (min-width: 1200px)",
    r"@include media-breakpoint-down\(xl\)": "@media (max-width: 1199.98px)",
}

for pattern, repl in replacements.items():
    content = re.sub(pattern, repl, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated {file_path}")
