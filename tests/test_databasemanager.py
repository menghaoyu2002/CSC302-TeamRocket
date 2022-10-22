from pathlib import Path
from app.databasemanager import DatabaseManager

class TestDatabaseManager:
    dbm = DatabaseManager()

    def test_import(self):
        path = Path(__file__).parent / '../app/datasets/prevalence-of-undernourishment.csv'
        assert(self.dbm.import_dataset(path)) == True


    def test_failed_import(self):
        path = 'somepath'
        assert(self.dbm.import_dataset(path)) == False
    

    def test_get_prevalence_one(self):
        assert(self.dbm.get_prevalence('Afghanistan', 2004)) == 38.0
    

