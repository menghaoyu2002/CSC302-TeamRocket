from sqlitehelper import SQLiteHelper

if __name__ == "__main__":
    db_helper = SQLiteHelper()
    db_helper.get_all_data()
    db_helper.close_connection()