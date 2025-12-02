def check_notes(notes):
    if isinstance(notes, str):
       return '#TODO' in notes
    raise TypeError("Only strings allowed!")