import pandas as pd
import os
import configparser

conf = configparser.ConfigParser()
conf.read("../conf/config.ini")

def process_data():
    input_path = conf ["datapaths"]["input_path"]
    
    #read input file
    file_list = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    df_files = [pd.read_csv(os.path.join(input_path, f)).assign(input=f) for f in file_list]
    df = pd.concat(df_files, ignore_index=True)
    df.rename(columns = {'input':'Environment'}, inplace = True)
    df['Environment']=df.Environment.str.replace(r'(.csv)', '')
    df_output=df[['Source IP','Environment']].drop_duplicates().sort_values(by=['Source IP'])
    df_output.to_csv(conf ["datapaths"]["output_path"]+"combine.csv", index=False)
    
if __name__ == '__main__':
    process_data()
