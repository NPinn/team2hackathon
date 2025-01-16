from embedding.chroma import ChromaDB


def summarize_discharge_notes(discharge_notes: list) -> str:
    summary = ""
    for note in discharge_notes:
        summary += note + "\n"
    return summary


def generate_discharge_note_from_medical_clerking(medical_clearking: str, db: ChromaDB) -> str:
    discharge_notes = db.discharge_note.query(
        query_texts=medical_clearking, n_results=5
    )
    summary = summarize_discharge_notes(discharge_notes)
    return summary
