import pandas as pd
import json

mler_df = pd.read_csv('mler.csv')

def get_data():

    mler_list = mler_df.to_dict('records')

    return mler_list

def get_unique_districts():

    u_districts = mler_df['district_code'].unique()

    return u_districts


def read_district_json():
    cfile = open('district_codes.json','r')
    data = json.load(cfile)

    return data

def get_key_by_value(d,value):
    for key,val in d.items():
        if val.lower() == value.lower():
            return key

    return None

def get_matched_rows_by_district_code(d_code):

    print(f'd_code:{d_code}')
    sub_mler_df = mler_df[mler_df['district_code']== int(d_code)]
    
    print(sub_mler_df)
    return sub_mler_df.to_dict('records')



if __name__ =="__main__":
    get_matched_rows_by_district_code(1)