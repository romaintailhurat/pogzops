from pathlib import Path

def generate_duplicate_report(dups):
    """ WIP dups is an object containing arrays of duplicate object ids."""
    double_line_break = "\n\n"
    doc = f"# Duplicates {double_line_break}"
    for key in dups:
        doc += f"## {key} {double_line_break}"
        if len(dups[key]) > 0:
            line = ", ".join(dups[key])
            doc += f"{line} {double_line_break}"
        else:
            doc += f"> nothing {double_line_break}"

    return doc

def save_report(md_doc: str, path: Path):
    path_to_md = path / "report.md"
    print(f"Report will be written to {path_to_md}")
    with path_to_md.open("w", encoding="UTF-8") as md_file:
        md_file.write(md_doc)