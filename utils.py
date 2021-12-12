from database import MariaDB


def fill_in_the_field(field_element, value):
    field_element.click()
    field_element.clear()
    field_element.send_keys(value)


def db_add_admin_user(user='username', password='admin_password', email='some@email.com', user_id=9999):
    sql = f"INSERT INTO oc_user VALUES ({user_id}, 1, '{user}', MD5('{password}'), '', 'FirstName', 'LastName', " \
          f"'{email}', '', '', '0.0.0.0', 1 , CURDATE());"
    with MariaDB() as db:
        db.execute(sql)
