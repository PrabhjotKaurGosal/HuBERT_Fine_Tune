import pandas as pd
import os

## Change the absolute path in the original Shritpuli dataset be the local path of the machine
Shritpuli_tsv = pd.read_csv("/home/prabhjot/Desktop/HuBERT/train.tsv", sep='\t')
Shritpuli_tsv_without_header = pd.read_csv("/home/prabhjot/Desktop/HuBERT/train.tsv", sep='\t', skiprows=1, header = None)
Shritpuli_tsv_without_header.reset_index(drop=True,inplace=True)
print(Shritpuli_tsv)
print(Shritpuli_tsv_without_header)

old_path = Shritpuli_tsv.columns[0]
new_path = '/home/prabhjot/Desktop/HuBERT/Punjabi'
mapping = {Shritpuli_tsv_without_header.columns[0]: new_path}
Shritpuli_tsv_new = Shritpuli_tsv_without_header.rename(columns=mapping)

Shritpuli_tsv_new.to_csv(os.path.join('/home/prabhjot/Desktop/HuBERT','train_modified.tsv'), sep="\t", index=False)



#for index, row  in Shritpuli_tsv.iterrows():
#  filename = Shritpuli_tsv.iloc[index][0]
#  new_ID = os.path.splitext(filename)[0]



