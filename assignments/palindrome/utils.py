def is_palindrome(sequence):
    """function returning if a sequence is a palindrome"""

    seq = (
        sequence.replace(" ", "")
        .replace(".", "")
        .replace(",", "")
        .replace(";", "")
        .replace("<", "")
        .replace(">", "")
        .strip()
    )

    left_seq = (
        seq[: (len(seq) // 2)] if (len(seq) % 2 == 0) else seq[: ((len(seq) - 1) // 2)]
    )
    right_seq = (
        seq[(len(seq) // 2) :] if (len(seq) % 2 == 0) else seq[((len(seq) + 1) // 2) :]
    )

    for (left_to_right, right_to_left) in zip(left_seq, right_seq[::-1]):
        if left_to_right != right_to_left:
            return False

    return True
