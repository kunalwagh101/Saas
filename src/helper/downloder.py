import requests
import os
from pathlib import Path


def extractor(url:str ,outpath:Path):
    if not isinstance(outpath, Path):
        raise ValueError(f"{outpath} must be a valid pathlib.Path object")
    
    try :
        link = requests.get(url) 
        link.raise_for_status()
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_bytes(link.content)
        return True


    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False


        