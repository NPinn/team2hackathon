from embedding.chroma import ChromaDB

def add_docs_to_db(doctxt,id):
    """_summary_

    Args:
        doctxt (_type_): _description_
        id (_type_): _description_

    Raises:
        FileNotFoundError: _description_
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
    """
    db = ChromaDB()
    dev = db.medical_clerking
    dev.add(documents=doctxt, ids= id)
    print("documents added to database successfully")
    return




# model architecture
## data loader (will load the input data)
## data processor (will clean the loaded data)
## embeddings generator (will then create an embedding)
### feature suggestion (let the user select other llm)
## nearest distance calculator
### feature suggestion (the user can select top 3 vs 5 vs 10)
## serve the nearest distances

import pandas as pd
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModel

## data loader (will load the input data)
def dataloader(path):
    """
    load csv file
    """
    
    try:
        path = Path(path)
        
        if path.is_dir():
            csv_files = list(path.glob("*.csv"))
            if not csv_files:
                raise FileNotFoundError(f"No csv files found in directory: {path}")
            print(f" Found {len(csv_files)} CSV Files(s) in this directory")
            data = pd.read_csv(csv_files[0])
            print(f"Successfully loaded: {csv_files[0].name}")
            
        elif path.suffix == ".csv":
            if not path.exists():
                raise FileNotFoundError()
            print(f"File found at {path}")
            data = pd.read_csv(path)
    except Exception as e:
        print(f"Error found {e}")
        


## data processor (will clean the loaded data)

data = {
    'x': ["Doctor, I have a shortness of breath and chest pain and also have temperatures", "My leg hurts", "I am feeling dizzy"],
    'y': ["pneumonia", "dvt", "vertigo"]
}
df = pd.DataFrame(data)

tokenizer = AutoTokenizer.from_pretrained("Charangan/MedBERT")
model = AutoModel.from_pretrained("Charangan/MedBERT")

def text_to_embedding(text):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    # Get the embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    # The embeddings are in the last hidden state
    embeddings = outputs.last_hidden_state
    # You can use the mean of the embeddings as the representation
    mean_embeddings = embeddings.mean(dim=1)
    return mean_embeddings

# Apply the function to the 'x' column
df['x_embeddings'] = df['x'].apply(lambda x: text_to_embedding(x).squeeze().numpy())