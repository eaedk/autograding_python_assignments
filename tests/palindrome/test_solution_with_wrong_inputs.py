from assignments.palindrome.utils import is_palindrome


def test_solution():  # _with_valid_inputs
    valid_sequences = [
        "mom go to the market",
        "bonjour",
    ]
    expected_outputs = [True, True]
    outputs = []

    for seq in valid_sequences:
        outputs.append(is_palindrome(sequence=seq))

    assert expected_outputs == outputs
