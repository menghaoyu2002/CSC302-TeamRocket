from databasemanager import DatabaseManager

if __name__ == "__main__":
    db_helper = DatabaseManager()
    db_helper.get_all_data()
    db_helper.close_connection()