import os
import pandas as pd
import numpy as np
import requests
import gzip
import io
import sqlite3
import logging


class Pipeline:

    # Unzip dataset from URL
    # Downloads a gzipped CSV file from the specified URL, decompresses it,
    # and returns a Pandas DataFrame.

    # Parameters:
    # url (str): The URL of the gzipped CSV file.

    # Returns:
    # pd.DataFrame: The content of the CSV file as a Pandas DataFrame.

    def read_gzipped_csv_from_url(self, url):
        # Step 1: Download the gzipped file
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses

        # Step 2: Decompress the gzipped file
        compressed_file = io.BytesIO(response.content)
        with gzip.GzipFile(fileobj=compressed_file, mode='rb') as f:
            # Step 3: Read the decompressed content using pandas
            df = pd.read_csv(f)

        return df

    ### DATA TRANSFORMATION ###

    # DROP some unimportant Columns
    def drop_columns(self, df, columns_to_drop):
        """
        Drops specified columns from the DataFrame.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns_to_drop (list): List of columns to drop from the DataFrame.

        Returns:
        pd.DataFrame: The DataFrame with specified columns dropped.
        """
        df = df.drop(columns=columns_to_drop, errors='ignore')
        return df

    # Covert a YEAR column to DATETIME type
    def convert_to_datetime(self, df, column_name):
        """
        Converts a specified column to datetime values.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to convert to datetime.

        Returns:
        pd.DataFrame: The DataFrame with the specified column converted to datetime.
        """

        if "TIME_PERIOD" in df.columns:
            df[column_name] = df[column_name].astype(str)
            df[column_name] = pd.to_datetime(df[column_name], format='%Y')

        return df

    # Rename title of column for better readability
    def rename_columns(self, df, columns_mapping):
        """
        Renames columns in the DataFrame based on the provided mapping.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns_mapping (dict): A dictionary mapping old column names to new column names.

        Returns:
        pd.DataFrame: The DataFrame with renamed columns.
        """
        df = df.rename(columns=columns_mapping)
        return df
    ###########################

    # SAVE Data Frame to SQLITE in DATA folder
    def save_to_sqlite(self, df, db_name, table_name):
        """
        Saves the DataFrame to a SQLite database.

        Parameters:
        df (pd.DataFrame): The DataFrame to save.
        db_name (str): The name of the SQLite database file.
        table_name (str): The name of the table to create or replace in the database.

        Returns:
        None
        """
        # Ensure the "data" directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

            # Construct the full path to the database file
        db_path = os.path.join('data', db_name)

        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        # Save DataFrame to SQLite database
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        # Close the connection
        conn.close()

    def run_pipeline(self):
        # DATASET_1 : Final energy consumption in transport by type of fuel
        # Read Information from Link and unzip
        try:
            url_Dataset_1 = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00126/?format=SDMX-CSV&compressed=true'
            df_Dataset_1 = self.read_gzipped_csv_from_url(url_Dataset_1)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Something Wrong happen during getting the Dataset_1")
            return

        print("#1 DATASET 1: Read and Unzipped Data from URL.")

        # Drop columns
        try:
            columns_to_drop_Dataset_1 = ['DATAFLOW', 'OBS_FLAG']
            df_Dataset_1 = self.drop_columns(
                df_Dataset_1, columns_to_drop_Dataset_1)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Something Wrong happen during Drop columns on the Dataset_1")
            return

        # Convert TIME_PERIOD to datetime
        try:
            df_Dataset_1 = self.convert_to_datetime(
                df_Dataset_1, 'TIME_PERIOD')
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Convert TIME_PERIOD to datetime on the Dataset_1")
            return

        # Rename columns
        columns_mapping_Dataset_1 = {
            'LAST UPDATE': 'last_updated_timestamp',
            'freq': 'data_collection_frequency',
            'nrg_bal': 'energy_balance_category',
            'siec': 'specific_energy_product',
            'unit': 'unit_of_measurement',
            'geo': 'geographic_area',
            'TIME_PERIOD': 'time_period',
            'OBS_VALUE': 'energy_consumption_value',
        }
        try:
            df_Dataset_1 = self.rename_columns(
                df_Dataset_1, columns_mapping_Dataset_1)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Something Wrong happen during Rename columns on the Dataset_1")
            return

        print("#2 DATASET 1: Transformed and Cleaned Data")
        # Save to SQLite database
        try:
            self.save_to_sqlite(
                df_Dataset_1, 'energy_consumption.db', 'FECT_Total')
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Save to SQLite database on the Dataset_1")
            return

        print("#3 DATASET 1: Transfered Data to FECT_Total table in SQLLite.")

        print("\n")
        print("******************************************************")
        print("\n")

        # DATASET_2 : Final energy consumption in road transport by type of fuel
        # Read Information from Link and unzip
        try:
            url_Dataset_2 = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00127/?format=SDMX-CSV&compressed=true'
            df_Dataset_2 = self.read_gzipped_csv_from_url(url_Dataset_2)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Read Information from Link and unzip on the Dataset_2")
            return

        print("#4 DATASET 2: Read and Unzipped Data from URL.")

        # Drop columns
        try:
            columns_to_drop_Dataset_2 = ['DATAFLOW', 'OBS_FLAG']
            df_Dataset_2 = self.drop_columns(
                df_Dataset_2, columns_to_drop_Dataset_2)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Something Wrong happen during Drop columns on the Dataset_2")
            return

        # Convert TIME_PERIOD to datetime
        try:
            df_Dataset_2 = self.convert_to_datetime(
                df_Dataset_2, 'TIME_PERIOD')
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Convert TIME_PERIOD to datetime on the Dataset_2")
            return

        # Rename columns
        columns_mapping_Dataset_2 = {
            'LAST UPDATE': 'last_updated_timestamp',
            'freq': 'data_collection_frequency',
            'nrg_bal': 'energy_balance_category',
            'siec': 'specific_energy_product',
            'unit': 'unit_of_measurement',
            'geo': 'geographic_area',
            'TIME_PERIOD': 'time_period',
            'OBS_VALUE': 'energy_consumption_value',
        }
        try:
            df_Dataset_2 = self.rename_columns(
                df_Dataset_2, columns_mapping_Dataset_2)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Rename columns on the Dataset_2")
            return

        print("#5 DATASET 2: Transformed and Cleaned Data")
        # Save to SQLite database
        try:
            self.save_to_sqlite(
                df_Dataset_2, 'energy_consumption.db', 'FECT_Road')
        except Exception as e:
            logging.error(f"Error: {e}")
            print(
                f"Something Wrong happen during Save to SQLite database on the Dataset_2")
            return

        print("#6 DATASET 2: Transfered Data to FECT_Total table in SQLLite.")


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run_pipeline()
