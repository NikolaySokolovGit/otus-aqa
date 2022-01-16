import allure


@allure.step('Filling field {field_element} with value {value}')
def fill_in_the_field(field_element, value):
    field_element.click()
    field_element.clear()
    field_element.send_keys(value)
