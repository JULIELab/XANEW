# X-ANEW: The Extended Affective Norms for English Words

This repository serves as a secondary distribution of the emotional word ratings provided by:

*Warriner, A.B., Kuperman, V., & Brysbaert, M. (2013). Norms of valence, arousal, and dominance for 13,915 English 
lemmas. Behavior Research Methods, 45, 1191-1207.* 

Originally, the dataset has been released on this [website](http://crr.ugent.be/archives/1003) under a  
[Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License](https://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US).
Additionally, we provide a fix train-dev-test split to increase reproducibility in machine learning experiments.

An easy way to access the data is by using this code snippet which clones this repository from GitHub and 
returns a Pandas DataFrame:

```
from git import Repo
from pathlib import Path
import pandas as pd

def get_xanew(split='train', 
              root=Path.home()/'data/X-ANEW',
              url = 'https://github.com/JULIELab/X-ANEW.git'):
    
    assert split in ['train', 'dev', 'test'], 'split must be "train", "dev", or "test".'
   
    if not root.is_dir():
        root.mkdir()
        print('Downloading the dataset from github...')
        Repo.clone_from(url, str(root))
        
    csv = str(root / 'Ratings_Warriner_et_al.csv')
    df = pd.read_csv(csv, index_col=0)
    df=df[['Word','V.Mean.Sum', 'A.Mean.Sum', 'D.Mean.Sum']]
    df.columns=['word', 'valence', 'arousal', 'dominance']
    df.set_index('word',inplace=True)
    
    with open(str(root / '{}.txt'.format(split)), 'r') as f:
        words = f.read().split('\n')
       
    return df.loc[words]


# downloads the dataset if necessary and returns a pandas DataFrame
get_xanew('train')

```

Requirements:
* Python 3
* [GitPython](https://gitpython.readthedocs.io/en/stable/tutorial.html)
* [Pandas](https://pandas.pydata.org/) 