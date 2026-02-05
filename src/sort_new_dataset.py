import os
import shutil
import requests
from urllib.parse import urlparse
import pandas as pd

# --- 1. CONFIGURATION ---
# Please verify these values

# The path to your NEW CSV file from Hugging Face.
CSV_FILE_PATH = 'movies_dataset_new.csv'

# The folder where we will temporarily download all new posters.
DOWNLOAD_FOLDER = 'new_posters_downloaded'

# The folder where the NEW sorted genre folders will be created.
OUTPUT_SORTED_FOLDER = 'sorted_by_genre_new'

# The name of the column in your CSV that contains the genre(s).
GENRE_COLUMN = 'Genre'

# The name of the column that contains the full URL to the poster.
POSTER_URL_COLUMN = 'Poster_Url'

# --- END OF CONFIGURATION ---

# --- 2. SCRIPT LOGIC ---

def download_and_sort_posters():
    """
    Downloads posters from URLs in a CSV and sorts them into genre folders.
    """
    print("Starting the download and sorting process...")
    
    # Create necessary directories
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_SORTED_FOLDER, exist_ok=True)
    
    # Read the dataset
    df = pd.read_csv(CSV_FILE_PATH)
    
    for index, row in df.iterrows():
        try:
            url = row[POSTER_URL_COLUMN]
            genres = row[GENRE_COLUMN]
            
            if pd.isna(url) or pd.isna(genres):
                continue
                
            # Download image
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Parse filename from URL or use index
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path) or f"poster_{index}.jpg"
                
                # Handle multiple genres (split by '|')
                genre_list = [g.strip() for g in str(genres).split('|')]
                
                for genre in genre_list:
                    genre_folder = os.path.join(OUTPUT_SORTED_FOLDER, genre)
                    os.makedirs(genre_folder, exist_ok=True)
                    
                    filepath = os.path.join(genre_folder, filename)
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                        
                if index % 100 == 0:
                    print(f"Processed {index} images...")
                    
        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue
    
    print("Download and sorting complete!")

if __name__ == "__main__":
    download_and_sort_posters()