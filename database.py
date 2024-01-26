import pandas as pd
import os, os.path
from PIL import Image, ImageOps
import pickle

def create_dataframe():
    # path joining version for other paths
    DIR = '/home/bubba/Proyecto_Final/Fotos'
    print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

    ages = []
    genders = []
    images = []
    etnia = []

    for i in os.listdir(DIR):
        split = i.split('_')
        
        if len(split) >= 3 and split[0].isdigit() and split[1].isdigit() and split[2].isdigit():
            ages.append(int(split[0]))
            genders.append(int(split[1]))
            image_path = os.path.join(DIR, i)
            images.append(Image.open(image_path))
            etnia.append(int(split[2]))
        else:
            print(f"Skipping file {i} due to unexpected format.")

    # Convert the lists into Pandas Series
    ages_series = pd.Series(ages, name='Ages')
    genders_series = pd.Series(genders, name='Genders')
    images_series = pd.Series(images, name='Images')
    etnia_series = pd.Series(etnia, name='Etnia')

    # Create a DataFrame from the Series
    df = pd.concat([ages_series, genders_series, etnia_series, images_series], axis=1)
    return df

df = create_dataframe()

# Save the DataFrame using pickle
with open('my_dataframe.pkl', 'wb') as file:
    pickle.dump(df, file)
    