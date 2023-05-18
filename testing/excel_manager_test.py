    # Tests that the function handles an empty Excel file correctly. 
from excel_manager import excel_update
import pandas as pd
import os

def test_excel_update_empty_file(self, mocker):
    # Setup
    numbers = {'1', '2', '3'}
    statements = {'NULL'}
    save_on_file = mocker.Mock()
    inbox_path = 'inbox'
    outbox_path = 'outbox'
    filename = 'empty.xlsx'
    sheet_name = 'Sheet1'
    table_name = 'test_table'
    exec_mode = 'auto'

    # Create empty Excel file
    df = pd.DataFrame()
    df.to_excel(os.path.join(outbox_path, filename), sheet_name=sheet_name, index=False)

    # Call function
    excel_update(numbers, statements, save_on_file, inbox_path, outbox_path, filename, sheet_name, table_name, exec_mode)

    # Assert
    save_on_file.assert_not_called()