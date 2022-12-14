from assignments.palindrome.utils import is_palindrome


def test_solution_with_valid_inputs():  #
    valid_sequences = [
        "kayak",
        "laval",
    ]
    expected_outputs = [True, True]
    outputs = []

    for seq in valid_sequences:
        outputs.append(is_palindrome(sequence=seq))

    assert expected_outputs == outputs
