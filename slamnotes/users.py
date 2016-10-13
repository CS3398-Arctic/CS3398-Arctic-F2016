"""
Module to handle users.
"""

import database_search
import database_store
from django.contrib.auth.hashers import check_password, make_password

class user:
    """Object to hold a user's information."""
    pass

def load_user (id = None, username = None):
    """Load a user by id or username, returns a user object or None.
    id or username must be passed, but not both.
    
    Keyword arguments:
    id -- the id of the user to load (default None)
    username -- the username of the user to load (default None)
    """
    
    if id is None and username is None:
        raise ValueError("Neither an id, nor a username were specified. "
                         "Please pass one.")
    elif id is not None and username is not None:
        raise ValueError("Both an id, and a username were specified. "
                         "Please pass only one.")
    
    if not user_exists(id= id, username= username):
        # The user does not exist, return None.
        return None
    
    if id is not None:
        if type(id) is not int:
            raise TypeError("expected integer")
        user_data = database_search.find_user_by_id(id)
    else:
        if type(username) is not str:
            raise TypeError("expected string")
        user_data = database_search.find_user_by_username(username)
    
    the_user = user()
    
    # Populate user object with data.
    if id is not None:
        the_user.id = id
        the_user.username = user_data['username']
    else:
        the_user.id = user_data['user_ID']
        the_user.username = username
    
    the_user.password = user_data['password']
    the_user.email = user_data['user_email']
    the_user.school = user_data['user_school']
    the_user.major = user_data['user_major']
    the_user.date_entered = user_data['date_entered']
    
    return the_user

def user_exists (id = None, username = None):
    """Check if a user exists by id or username, returns True or False.
    id or username must be passed, but not both.
    
    Keyword arguments:
    id -- the id of the user to check for (default None)
    username -- the username of the user to check for (default None)
    """
    
    if id is None and username is None:
        raise ValueError("Neither an id, nor a username were specified. "
                         "Please pass one.")
    elif id is not None and username is not None:
        raise ValueError("Both an id, and a username were specified. "
                         "Please pass only one.")
    
    try:
        if id is not None:
            if type(id) is not int:
                raise TypeError("expected integer")
            database_search.find_user_by_id(id)
        else:
            if type(username) is not str:
                raise TypeError("expected string")
            database_search.find_user_by_username(username)
    except (KeyError, IndexError):
        # The user does not exist, return False.
        return False
    
    # The user exists, return True.
    return True

def valid_credentials (username, password):
    """Check if given username/password combination is valid,
    returns True or False.
    
    Keyword arguments:
    username -- the username to validate
    password -- the password to validate
    """
    
    # Sanity check: are username and password str?
    if type(username) is not str:
        raise TypeError("expected string")
    if type(password) is not str:
        raise TypeError("expected string")
    
    # Sanity check: are username or password empty?
    if not username or not password:
        return False
    
    the_user = load_user(username= username)
    
    if the_user is None:
        # The user does not exist, return False.
        return False
    
    if check_password(password, the_user.password):
        # The password matches, return True.
        return True
    else:
        # The password does not match, return False.
        return False
