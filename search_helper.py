def search_notes(notes, query):
    """Return notes containing the search query."""
    query = query.strip().lower()

    if not query:
        return notes

    return [
        note for note in notes
        if query in note.lower()
    ]
