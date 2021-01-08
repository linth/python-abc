# TODO: do connect database and searching data.
from django.db import connection


class IeDB:
    def __init__(self, table: str = ''):
        self.table = table
        self.result = []
        self.num_of_result = len(self.result)

    def multiple_tasks(self):
        # TODO: do several jobs to search database once to
        #  avoid accessing multiple times.
        pass

    def search_by_sql_command(self, sql_command: str = '') -> list:
        """
        search database table by sql command.
        :param sql_command:
        :return:
        """
        try:
            if sql_command == '':
                Exception(f'the sql command is empty.')
            elif self.table is not '':
                cursor = connection[self.table].cursor()
                cursor.execute(sql_command)
                self.result = self.dictfetchall(cursor)
                cursor.close()
            else:
                Exception(f'the database table isn\'t setup.')
        except Exception as e:
            raise e
        return self.result

    @staticmethod
    def dictfetchall(cursor):
        """
        Return all rows from a cursor as a dict.
        :param cursor:
        :return:
        """
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
