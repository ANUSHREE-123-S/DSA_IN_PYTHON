class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail (to avoid edge cases)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Helper functions ---
    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add_to_front(self, node: Node) -> None:
        """Always add new node right after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: Node) -> None:
        """Move existing node to front (MRU)."""
        self._remove(node)
        self._add_to_front(node)

    def _evict_from_tail(self) -> None:
        """Remove the least recently used node (before tail)."""
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]

    # --- Main API ---
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                self._evict_from_tail()
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_to_front(newNode)