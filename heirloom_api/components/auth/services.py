from werkzeug.security import generate_password_hash

class AuthDb:
    '''
    Handle Auth DB requests
    '''
    def __init__(self, database):
        self.database = database

    def get_user_by_username(self, username):
        '''
        calls auth db to get user by username
        '''
        return self.database.execute(
                    'SELECT id FROM user WHERE username = ?', (username,)
                )

    def add_user(self, username, password):
        '''
        creates username and a password record
        '''
        self.database.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
        self.database.commit()
        return {'success': True}

    def login(self, username):
        '''
        Login
        '''
        return self.database.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
