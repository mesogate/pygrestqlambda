from abc import ABCMeta

class Record(metaclass=ABCMeta):
    """
    Generic record that maps to a row in a database table
    """

    def __init__(self, conn: bool = False) -> None:
        self.conn = conn


    def before_create(self):
        """
        Runs before a new record is created. Useful for mutating a new record before being committed.
        """
        pass


    def before_read(self):
        """
        Before a record is retrieved from the database. Useful for injecting filters or sorting.
        """
        pass


    def before_update(self):
        """
        Before a new record is created. Useful for mutating a record before it is committed.
        """
        pass


    def before_delete(self):
        """
        Before an existing record is deleted. Useful for e.g. updating counters or other aggregate
        fields in other tables.
        """
        pass
