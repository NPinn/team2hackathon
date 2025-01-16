data1 = """Source of History
Patient
Source of referral
Following an emergency admission
History of presenting complaint
1/12 history of dry cough
worsening SOB, now present at rest
No fevers
Attended GP - treated with PO abx for 'chest infection' without resolution in symptoms.
Longstanding right sided chest pain, unchanged recently.
No GI/GU symptoms
No unwell contacts
PMHx
Prediabetes
Depression
Bariatric surgery
Covid Vaccines x2
Medication prior to admission
Nil regular
NKDA
Family and social history
Nil smoking
Nil alcohol
Examination
Well
Slightly short of breath at rest
Reduced AE L mid lower zone, scattered wheeze.
Nil peripheral oedema.
"""

d1 = [
    {'id': '1', 'x': data1, 'y': "Pleuraleffusion"},
    {'id': '2', 'x': data1, 'y': "Pneumonia"},
    {'id': '3', 'x': data1, 'y': "Pnuemothorax"}
]

from embedding.chroma import ChromaDB

db = ChromaDB()

for i in d1:
    db.medical_clerking.add(
        ids=[i['id']],
        documents=[i['x']],
    )
    db.discharge_note.add(
        ids=[i['id']],
        documents=[i['y']],
    )
