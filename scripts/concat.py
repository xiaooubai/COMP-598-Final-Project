import pandas as pd
import os.path as osp

"""
Script for merging the entire data
"""

def main():

    list_df = []

    C_data = pd.read_csv(osp.join('..' , 'data' , 'Cristian_annotation' , '20201124_conservative_annotated.tsv'), delimiter='\t')
    C_data2 = pd.read_csv(osp.join('..' , 'data' , 'Cristian_annotation' , '20201124_politics_annotated.tsv'), delimiter='\t')

    list_df.append(C_data)
    list_df.append(C_data2)

    K_data = pd.read_csv(osp.join('..' , 'data' , 'Kagan_annotation' , '20201125_conservative_filtered_annotated.tsv.txt') , delimiter='\t')
    K_data2 = pd.read_csv(osp.join('..' , 'data' , 'Kagan_annotation' , '20201125_politics_filtered_annotated.tsv.txt') , delimiter='\t')

    list_df.append(K_data)
    list_df.append(K_data2)

    O_data = pd.read_csv(osp.join('..' , 'data' , 'Owen_annotation' , '20201123_conservative_filtered_annotated.tsv.txt'), delimiter='\t')
    O_data2 =pd.read_csv(osp.join('..' , 'data' , 'Owen_annotation' , '20201123_politics_filtered_annotated.tsv.txt'), delimiter='\t')

    list_df.append(O_data)
    list_df.append(O_data2)

    df = pd.concat(list_df)

    df_shuffled = df.sample(frac=1).reset_index(drop=True)
    del df_shuffled['Unnamed: 3']
    print(df_shuffled)

    df.to_csv(osp.join('..' , 'data' , 'Final_data' , 'final_data.csv') , sep=',' , index=False)






if __name__ == '__main__':
    main()