import sys
sys.path.append("..")
from helpers.users import *


def test_users():
    get_user_by_id("1")
    create_user("svetogor", "svetogor@gmail.com", 32)
    update_user_by_id("1", "svyatogor")
    delete_user_by_id("2")
    get_users()