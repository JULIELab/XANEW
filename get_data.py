from git import Repo
from pathlib import Path
import pandas as pd


def get_xanew(split='train',
              root=Path.home() / 'data/X-ANEW',
              url='https://github.com/JULIELab/X-ANEW.git'):
    assert split in ['train', 'dev', 'test'], 'split must be "train", "dev", or "test".'

    if not root.is_dir():
        root.mkdir()
        print('Downloading the dataset from github...')
        Repo.clone_from(url, str(root))

    csv = str(root / 'Ratings_Warriner_et_al.csv')
    df = pd.read_csv(csv, index_col=0)
    df = df[['Word', 'V.Mean.Sum', 'A.Mean.Sum', 'D.Mean.Sum']]
    df.columns = ['word', 'valence', 'arousal', 'dominance']
    df.set_index('word', inplace=True)

    with open(str(root / '{}.txt'.format(split)), 'r') as f:
        words = f.read().split('\n')

    return df.loc[words]


get_xanew('train')