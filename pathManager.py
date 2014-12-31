__author__ = 'bernardo'
import os.path
import config
import fileExtensions

def in_directory(file, directory):
    directory = os.path.join(os.path.realpath(directory), '')
    file = os.path.realpath(file)
    return os.path.commonprefix([file, directory]) == directory


def is_directory(file, directory):
    directory = os.path.join(os.path.realpath(directory), '')
    file = os.path.realpath(file)
    return os.path.dirname(file) + '/' == directory


def verify_in_directory(file):
    if len(config.__ALLOWED_DIRS_AND_SUB__) < 1:
        return False
    for koopa in config.__ALLOWED_DIRS_AND_SUB__:
        if in_directory(file, koopa) == False:
            return False

    return True


def verify_is_directory(file):
    if len(config.__ALLOWED_DIRS__) < 1:
        return False
    for koopa in config.__ALLOWED_DIRS__:
        if is_directory(file, koopa) == False:
            return False

    return True


def verify_all(file):
    if verify_in_directory(file) and fileExtensions.check_allowed(file) and fileExtensions.check_denied(file) == True:
        return True
    if verify_is_directory(file) and fileExtensions.check_allowed(file) and fileExtensions.check_denied(file) == True:
        return True
    return False