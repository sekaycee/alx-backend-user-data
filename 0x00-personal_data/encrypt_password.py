#!/usr/bin/env python3
''' password encrypting module. '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' hash a password using a random salt. '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' check if a password hash was formed from the given password. '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
