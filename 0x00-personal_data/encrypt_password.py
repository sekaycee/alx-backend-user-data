#!/usr/bin/env python3
""" password encrypting module. """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password using a random salt. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

