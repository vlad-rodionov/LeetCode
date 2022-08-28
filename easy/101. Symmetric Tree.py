# 1st Solution. BFS
from collections import deque

def is_symmetric(root):

    q = deque([root])

    levels = []

    while q:

        level = []

        for _ in range(len(q)):

            cur = q.popleft()

            level.append(cur.val if cur else None)

            if cur:
                q.append(cur.left)
                q.append(cur.right)

        if len(level) > 1:
            n = len(level)
            first_half, second_half = level[:n // 2], level[n // 2:][::-1]

            if first_half != second_half:
                return False

    return True

# 2nd Solution. Recursive

def is_symmetric_2(root):
    def helper(node1, node2):

        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)

    return helper(root, root)
