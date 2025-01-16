
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

