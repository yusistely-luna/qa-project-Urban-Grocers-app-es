# 🛒 Urban Grocers — API Test Automation

**API · Pytest** — TripleTen Bootcamp Project (2026)
> 🎓 Sprint Project

---

## 🎯 Problem

Automated API testing of the `name` parameter when creating a new kit in the Urban Grocers application. The goal was to design and implement equivalence classes and boundary value tests for a single field, validate both successful (`201`) and error (`400`) responses, and confirm that the API's returned data matches what was submitted.

---

## 📊 Results & Impact

| Metric                  | Value                         |
| ------------------------ | ------------------------------ |
| Automated tests          | **9**                          |
| Parameter under test     | `name` (kit creation)          |
| Response codes validated | **201, 400**                   |
| Test framework           | **Pytest**                     |

---

## ⚙️ What I Did

### Test Design

- Applied **equivalence partitioning** to the `name` parameter: valid text, empty string, numeric type, special characters, and strings containing spaces
- Applied **boundary value analysis** on length: 1 character (minimum), 511 characters (maximum valid), and 512 characters (first invalid value over the limit)
- Covered the missing-parameter case, verifying the API's required-fields validation independently of the length/format rules

### Automation (Python + Pytest)

- Built reusable request helpers (`sender_stand_request.py`) to create a user, obtain an auth token, and post a new kit
- Centralized test data and request bodies in `data.py` to keep test cases short and readable
- Implemented shared assertion helpers (`positive_assert`, `negative_assert`, `negative_assert_missing_kit_name`) so every test case checks both the HTTP status code and the exact response body
- 9 test functions in `create_kit_name_kit_test.py`, each isolated to a single equivalence class or boundary value

### Test Cases Summary

| # | Case                                   | Input                        | Expected Result |
| - | --------------------------------------- | ----------------------------- | ---------------- |
| 1 | Minimum valid length                    | 1 character                   | 201 · name echoed back |
| 2 | Maximum valid length                    | 511 characters                | 201 · name echoed back |
| 3 | Empty value                              | `''`                          | 400 · validation message |
| 4 | Exceeds maximum length                   | 512 characters                | 400 · validation message |
| 5 | Special characters                       | `"№%@",`                      | 201 · name echoed back |
| 6 | Contains spaces                          | `' A Aaa '`                   | 201 · name echoed back |
| 7 | Numeric characters (as string)           | `'123'`                       | 201 · name echoed back |
| 8 | Missing `name` parameter                 | key removed from request body | 400 · required-fields message |
| 9 | Invalid type (integer instead of string) | `123`                         | 400 · validation message |

---

## ✅ Learning

Testing a single field thoroughly is more than checking "does it work" — equivalence partitioning and boundary value analysis turn one parameter into a short, deliberate list of cases that each answer a different question about the validation rules. Centralizing request bodies and assertions in helper functions kept the 9 test cases readable and made it obvious, at a glance, which specific input and expected outcome each one covers. Comparing the *type* boundary (integer vs. string) against the *length* boundaries also surfaced a subtlety worth remembering: a field can enforce format and length independently, and each needs its own test.

---

## 🛠️ Skills

Python · Pytest · REST API Testing · Equivalence Partitioning · Boundary Value Analysis · Requests Library · Test Data Management · HTTP Status Code Validation

---

## 🧰 Technologies Used

- Python 3.14
- Pytest 9.1.1
- Requests 2.34.2

---

## 📁 Project Structure

- `configuration.py` — API base URL and endpoints
- `data.py` — Test data and request bodies
- `sender_stand_request.py` — Functions for sending API requests
- `create_kit_name_kit_test.py` — Automated tests for kit creation

---

## ▶️ How to Run the Tests

1. Open the project in PyCharm (or any Python IDE)
2. Install the required packages:
