import os
import pandas as pd
import streamlit as st
from config import DATA_FILES, COLUMN_MAPPINGS


@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(script_dir, 'dataset')
    
    try:
        business_file = os.path.join(dataset_dir, DATA_FILES['business'])
        business_df = pd.read_csv(business_file)
        
        business_df = business_df.rename(columns=COLUMN_MAPPINGS['business'])
        
        marketing_files = {
            channel: os.path.join(dataset_dir, filename)
            for channel, filename in DATA_FILES['marketing'].items()
        }
        
        marketing_dfs = []
        for channel, file_path in marketing_files.items():
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df = df.rename(columns=COLUMN_MAPPINGS['marketing'])
                df['channel'] = channel
                marketing_dfs.append(df)
            else:
                st.warning(f"Marketing data file not found: {file_path}")
        
        if marketing_dfs:
            marketing_df = pd.concat(marketing_dfs, ignore_index=True)
        else:
            st.error("No marketing data files found in dataset folder")
            return None, None
        
        return business_df, marketing_df
        
    except Exception as e:
        st.error(f"Error loading data from dataset folder: {str(e)}")
        st.info(f"Looking for files in: {dataset_dir}")
        return None, None


def prepare_data(business_df, marketing_df):
    business_df['date'] = pd.to_datetime(business_df['date'])
    marketing_df['date'] = pd.to_datetime(marketing_df['date'])
    
    return business_df, marketing_df


def get_data_info(business_df, marketing_df):    
    return {
        'business_records': len(business_df),
        'marketing_records': len(marketing_df),
        'date_range': {
            'start': min(business_df['date'].min(), marketing_df['date'].min()),
            'end': max(business_df['date'].max(), marketing_df['date'].max())
        },
        'channels': sorted(marketing_df['channel'].unique().tolist()),
        'tactics': marketing_df.groupby('channel')['tactic'].nunique().to_dict()
    }
