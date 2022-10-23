from pathlib import Path
from sqlite3 import Error
from databasemanager import DatabaseManager

class TestDatabaseManager:
    db_manager = DatabaseManager()

    def test_import(self):
        path = Path(__file__).parent / '../app/datasets/prevalence-of-undernourishment.csv'
        try:
            self.db_manager.import_dataset(path)
        except Error:
            assert False
        except FileNotFoundError:
            assert False
        except IOError:
            assert False
        except ValueError:
            assert False

    def test_update(self):
        path = Path(__file__).parent / '../app/datasets/prevalence-of-undernourishment.csv'
        try:
            self.db_manager.update_dataset(path)
        except FileNotFoundError:
            assert False
        except IOError:
            assert False
        except ValueError:
            assert False

    def test_get_prevalence_one(self):
        assert self.db_manager.get_prevalence('Afghanistan', 2004) == 38.0
