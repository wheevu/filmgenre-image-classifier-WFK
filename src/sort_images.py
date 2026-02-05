import pandas as pd
import os
import shutil

# --- 1. CONFIGURATION ---
# This is now configured for your setup.

# The path to your CSV file.
CSV_FILE_PATH = 'MovieGenre.csv'

# The folder where all your poster images are stored.
SOURCE_IMAGES_FOLDER = 'all_posters'

# The folder where the sorted genre folders will be created.
OUTPUT_SORTED_FOLDER = 'sorted_by_genre'

# The name of the column with the poster's ID (e.g., 114709).
POSTER_ID_COLUMN = 'imdbId'

# The name of the column with the genre(s).
GENRE_COLUMN = 'Genre'

# --- END OF CONFIGURATION ---

# --- 2. SCRIPT LOGIC ---

def sort_posters_by_genre():
    """
    Reads a CSV, finds corresponding images, and copies them into
    folders named after their genres, splitting by the '|' character.
    """
    print("Starting the sorting process...")
    os.makedirs(OUTPUT_SORTED_FOLDER, exist_ok=True)
    print(f"Output will be saved in '{OUTPUT_SORTED_FOLDER}'")
    
    try:
        # --- THIS IS THE KEY FIX ---
        # Added encoding='latin1' to handle the character format of your CSV.
        df = pd.read_csv(CSV_FILE_PATH, encoding='latin1')
        
        for index, row in df.iterrows():
            try:
                poster_id = str(row[POSTER_ID_COLUMN])
                genres = row[GENRE_COLUMN]
                
                if pd.isna(genres):
                    continue
                
                source_path = os.path.join(SOURCE_IMAGES_FOLDER, f"{poster_id}.jpg")
                
                if not os.path.exists(source_path):
                    continue
                
                # Handle multiple genres (e.g., "Action|Adventure")
                genre_list = [g.strip() for g in str(genres).split('|')]
                
                for genre in genre_list:
                    genre_folder = os.path.join(OUTPUT_SORTED_FOLDER, genre)
                    os.makedirs(genre_folder, exist_ok=True)
                    
                    dest_path = os.path.join(genre_folder, f"{poster_id}.jpg")
                    shutil.copy2(source_path, dest_path)
                
                if index % 100 == 0:
                    print(f"Processed {index} posters...")
                    
            except Exception as e:
                print(f"Error processing row {index}: {e}")
                continue
                
        print("Sorting complete!")
        
    except Exception as e:
        print(f"Error reading CSV: {e}")

if __name__ == "__main__":
    sort_posters_by_genre()