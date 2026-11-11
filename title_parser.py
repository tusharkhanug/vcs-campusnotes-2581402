def parse_title(text):
    """Extract and normalize a note title."""
    title = text.strip().splitlines()[0].strip() if text.strip() else ""

    if not title:
        return "Untitled"

    return title
