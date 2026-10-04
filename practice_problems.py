"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    # A set is useful because it only stores unique values.
    # Checking if an item is already in a set is usually O(1), so this works in O(n) time overall.
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added,
and support removing tasks from the front.
"""

class TaskQueue:
    def __init__(self):
        # A list works here because tasks need to stay in the same order they were added.
        # Adding to the end is O(1), while removing from the front is O(n).
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None

        return self.tasks.pop(0)


"""
Problem 3: Unique Value Counter

You receive a stream of integer values.
At any point, you should be able to return the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        # A set is the best fit because duplicate values are automatically ignored.
        # Adding values and checking membership are usually O(1).
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Simple tests for all three problems
if __name__ == "__main__":
    print("Problem 1 Tests")
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))        # False
    print(has_duplicates([]))                     # False

    print("\nProblem 2 Tests")
    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    task_queue.add_task("Meeting")
    print(task_queue.remove_oldest_task())         # Email follow-up
    print(task_queue.remove_oldest_task())         # Code review
    print(task_queue.remove_oldest_task())         # Meeting
    print(task_queue.remove_oldest_task())         # None

    print("\nProblem 3 Tests")
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    tracker.add(30)
    print(tracker.get_unique_count())              # 3
