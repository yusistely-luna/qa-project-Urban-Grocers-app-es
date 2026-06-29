import sender_stand_request
import data

# Update the request body with a new kit name
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

# Get new user token
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()['authToken']

# Verifies that a kit is created successfully (HTTP 201) and the response name matches the request.
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        get_new_user_token()
    )
    assert response.status_code == 201
    assert response.json()['name'] == kit_body['name']

# Verifies that an invalid request returns HTTP 400
# and the expected error message.
def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        get_new_user_token()
    )
    assert response.status_code == 400
    assert response.json()['message'] == 'El nombre debe contener sólo letras latino, ' \
                                         'un espacio y un guión. De 2 a 15 caracteres'

# Verifies that an invalid request returns HTTP 400
# and the expected error message when kit name is missing.
def negative_assert_missing_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        get_new_user_token()
    )
    assert response.status_code == 400
    assert response.json()['message'] == 'No se han aprobado todos los parámetros requeridos'

# Test case 1: One-character name.
# Expected result: HTTP 201 and the response name matches the request.
def test_create_kit_1_letter_in_name_get_success_response():
    new_kit_body = get_kit_body('a')
    positive_assert(new_kit_body)

# Test case 2: Maximum allowed name length (511 characters).
# Expected result: HTTP 201 and the response name matches the request.
def test_create_kit_511_letter_in_name_get_success_response():
    new_kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    positive_assert(new_kit_body)

# Test case 3: Empty name value.
# Expected result: HTTP 400.
def test_create_kit_empty_name_get_error_response():
    new_kit_body = get_kit_body('')
    negative_assert(new_kit_body)

# Test case 4: Name length exceeds the limit (512 characters).
# Expected result: HTTP 400.
def test_create_kit_512_letter_in_name_get_error_response():
    new_kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    negative_assert(new_kit_body)

# Test case 5: Name contains special characters.
# Expected result: HTTP 201 and the response name matches the request.
def test_create_kit_special_characters_name_get_success_response():
    new_kit_body = get_kit_body('"№%@",')
    positive_assert(new_kit_body)

# Test case 6: Name contains spaces.
# Expected result: HTTP 201 and the response name matches the request.
def test_create_kit_contain_spaces_name_get_success_response():
    new_kit_body = get_kit_body(' A Aaa ')
    positive_assert(new_kit_body)

# Test case 7: Name contains numeric characters.
# Expected result: HTTP 201 and the response name matches the request.
def test_create_kit_numeric_characters_name_get_success_response():
    new_kit_body = get_kit_body('123')
    positive_assert(new_kit_body)

# Test case 8: Missing "name" parameter.
# Expected result: HTTP 400.
def test_create_kit_missing_name_get_error_response():
    new_kit_body = data.kit_body.copy()
    new_kit_body.pop('name')

    negative_assert_missing_kit_name(new_kit_body)

# Test case 9: "name" parameter has an invalid type (integer).
# Expected result: HTTP 400.
def test_create_kit_number_name_get_error_response():
    new_kit_body = get_kit_body(123)
    negative_assert(new_kit_body)