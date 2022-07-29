from assignments.palindrome.utils import is_palindrome


def test_solution_with_wrong_inputs():  #
    valid_sequences = [
        "mom go to the market",
        "bonjour",
    ]
    expected_outputs = [False, False]
    outputs = []

    for seq in valid_sequences:
        outputs.append(is_palindrome(sequence=seq))

    assert expected_outputs == outputs
