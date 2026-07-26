#FIND PAIRS WITH GIVEN SUM FOR A DOUBLY LINKED LIST

def findPairs(head, target):

    # Empty list
    if head is None:
        return []

    pairs = []

    left = head                  # Left pointer starts from head
    right = head

    # Move right to the last node
    while right.next:
        right = right.next

    # Traverse until pointers meet
    while left != right and left.prev != right:

        current_sum = left.data + right.data

        # Pair found
        if current_sum == target:

            pairs.append((left.data, right.data))

            left = left.next      # Move left forward
            right = right.prev    # Move right backward

        # Sum is too small
        elif current_sum < target:

            left = left.next      # Increase the sum

        # Sum is too large
        else:

            right = right.prev    # Decrease the sum

    return pairs