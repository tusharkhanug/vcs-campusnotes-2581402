def load_notes(lines):
    """Load non-empty notes from a list of lines."""
    return [
        line.strip()
        for line in lines
        if line.strip()
    ]
