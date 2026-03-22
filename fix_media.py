import os
import glob
import re

directory = "paragon"
scss_files = glob.glob(f"{directory}/**/*.scss", recursive=True)

replacements = {
    r"@media \(--pgn-size-breakpoint-min-width-sm\)": "@media (min-width: 576px)",
    r"@media \(--pgn-size-breakpoint-max-width-sm\)": "@media (max-width: 575.98px)",
    r"@media \(--pgn-size-breakpoint-min-width-md\)": "@media (min-width: 768px)",
    r"@media \(--pgn-size-breakpoint-max-width-md\)": "@media (max-width: 767.98px)",
    r"@media \(--pgn-size-breakpoint-min-width-lg\)": "@media (min-width: 992px)",
    r"@media \(--pgn-size-breakpoint-max-width-lg\)": "@media (max-width: 991.98px)",
    r"@media \(--pgn-size-breakpoint-min-width-xl\)": "@media (min-width: 1200px)",
    r"@media \(--pgn-size-breakpoint-max-width-xl\)": "@media (max-width: 1199.98px)",
}

for file_path in scss_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for pattern, repl in replacements.items():
        new_content = re.sub(pattern, repl, new_content)
        
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
