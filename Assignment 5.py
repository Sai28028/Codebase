import re

def is_valid_string(input_str, allowed_chars):
    """
    Checks if input_str contains ONLY characters present in allowed_chars.
    """
    # Using set membership for efficient checking
    return set(input_str).issubset(set(allowed_chars))


def is_valid_string_regex(input_str, pattern_chars):
    """
    Alternative approach using Regular Expressions.
    Checks if input_str consists only of characters defined in pattern_chars.
    """
    pattern = f"^[{re.escape(pattern_chars)}]+$"
    return bool(re.match(pattern, input_str))


if __name__ == "__main__":
    # Define the allowed set of characters (e.g., alphanumeric only)
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Test cases
    test_cases = [
        "Python312",
        "Hello World!",   # Contains spaces and '!'
        "Assignment2026",
        "user_name#1"     # Contains '_' and '#'
    ]

    print(f"Allowed Set: '{allowed}'\n")

    print("--- Test Results ---")
    for test in test_cases:
        result = is_valid_string(test, allowed)
        print(f"Input: '{test:15}' -> Valid: {result}"
