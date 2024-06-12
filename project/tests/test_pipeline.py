import pytest
import pandas as pd
import sqlite3
import os
from pipeline import Pipeline  # Adjust this import based on your project structure

# Utility function to load a DataFrame from SQLite
def load_dataframe(db_path, table_name):
    cnx = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx)
    cnx.close()
    return df

# Fixture to run the pipeline and create the database
@pytest.fixture(scope="session", autouse=True)
def setup_pipeline():
    pipeline = Pipeline()
    pipeline.run_pipeline()

# Fixture for the 'FECT_Total' table
@pytest.fixture
def fect_total_df():
    db_path = 'data/energy_consumption.db'
    table_name = 'FECT_Total'
    return load_dataframe(db_path, table_name)

# Fixture for the 'FECT_Road' table
@pytest.fixture
def fect_road_df():
    db_path = 'data/energy_consumption.db'
    table_name = 'FECT_Road'
    return load_dataframe(db_path, table_name)

# Test case to check if the database file exists
def test_database_file_exists():
    db_path = 'data/energy_consumption.db'
    assert os.path.exists(db_path), "The SQLite database file does not exist"

# Test case to check if the 'FECT_Total' table exists
def test_fect_total_table_exists():
    db_path = 'data/energy_consumption.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FECT_Total';")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "The FECT_Total table does not exist"

# Test case to check if the 'FECT_Road' table exists
def test_fect_road_table_exists():
    db_path = 'data/energy_consumption.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FECT_Road';")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "The FECT_Road table does not exist"

# Test cases for the 'FECT_Total' table
def test_fect_total_size(fect_total_df):
    assert len(fect_total_df) == 6734, "Expected 6734 rows in the FECT_Total table"

def test_fect_total_schema(fect_total_df):
    expected_columns = [
        'last_updated_timestamp', 'data_collection_frequency', 'energy_balance_category',
        'specific_energy_product', 'unit_of_measurement', 'geographic_area',
        'time_period', 'energy_consumption_value'
    ]
    assert list(fect_total_df.columns) == expected_columns, "FECT_Total table schema does not match the expected schema"

# Test cases for the 'FECT_Road' table
def test_fect_road_size(fect_road_df):
    assert len(fect_road_df) == 5772, "Expected 5772 rows in the FECT_Road table"

def test_fect_road_schema(fect_road_df):
    expected_columns = [
        'last_updated_timestamp', 'data_collection_frequency', 'energy_balance_category',
        'specific_energy_product', 'unit_of_measurement', 'geographic_area',
        'time_period', 'energy_consumption_value'
    ]
    assert list(fect_road_df.columns) == expected_columns, "FECT_Road table schema does not match the expected schema"


#Test Functions in pipeline.py
def test_drop_columns():
    pipeline = Pipeline()
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df = pipeline.drop_columns(df, ['B'])
    assert 'B' not in df.columns, "Column 'B' was not dropped from DataFrame"

def test_convert_to_datetime():
    pipeline = Pipeline()
    df = pd.DataFrame({'TIME_PERIOD': ['2000', '2001', '2002']})
    df = pipeline.convert_to_datetime(df, 'TIME_PERIOD')
    assert pd.api.types.is_datetime64_any_dtype(df['TIME_PERIOD']), "Column 'TIME_PERIOD' was not converted to datetime"

def test_rename_columns():
    pipeline = Pipeline()
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df = pipeline.rename_columns(df, {'A': 'alpha', 'B': 'beta'})
    assert 'alpha' in df.columns and 'beta' in df.columns, "Columns were not renamed correctly"

# Integration Test for the Entire Pipeline
def test_run_pipeline_integration():
    pipeline = Pipeline()
    pipeline.run_pipeline()
    
    db_path = 'data/energy_consumption.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM FECT_Total;")
    fect_total_count = cursor.fetchone()[0]
    assert fect_total_count == 6734, "FECT_Total table row count does not match expected count"
    
    cursor.execute("SELECT COUNT(*) FROM FECT_Road;")
    fect_road_count = cursor.fetchone()[0]
    assert fect_road_count == 5772, "FECT_Road table row count does not match expected count"
    
    conn.close()
