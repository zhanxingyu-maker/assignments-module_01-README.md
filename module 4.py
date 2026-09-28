
def find_first(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1



def has_duplicates_slow(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                return True
    return False



def has_duplicates_fast(lst):
    seen = set()

    for item in lst:
        if item in seen:
            return True
        seen.add(item)

    return False



def binary_search(sorted_lst, target):
    low = 0
    high = len(sorted_lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



def sum_pairs(lst):
    pairs = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 0:
                pairs.append((lst[i], lst[j]))

    return pairs


print("find_first tests:")
print(find_first([5, 3, 8, 1, 9], 8))   # 2
print(find_first([5, 3, 8, 1, 9], 7))   # -1
print(find_first([1, 2, 3, 2, 1], 2))   # 1



print("\nhas_duplicates_slow tests:")
print(has_duplicates_slow([1, 2, 3, 4]))  # False
print(has_duplicates_slow([1, 2, 3, 1]))  # True

print("\nhas_duplicates_fast tests:")
print(has_duplicates_fast([1, 2, 3, 4]))  # False
print(has_duplicates_fast([1, 2, 3, 1]))  # True



test = [3, 1, 4, 1, 5, 9]

assert has_duplicates_slow(test) == has_duplicates_fast(test)

print("\nBoth duplicate functions agree!")



print("\nbinary_search tests:")

nums = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(nums, 7))    # 3
print(binary_search(nums, 6))    # -1
print(binary_search(nums, 1))    # 0
print(binary_search(nums, 15))   # 7



print("\nsum_pairs tests:")

print(sum_pairs([-3, 1, 3, -1, 2]))
# Expected: [(-3, 3), (1, -1)]




import time

big_list = list(range(5000))

start = time.time()
has_duplicates_slow(big_list)
slow_time = time.time() - start

print(f"\nSlow (O(n²)): {slow_time:.4f} seconds")


start = time.time()
has_duplicates_fast(big_list)
fast_time = time.time() - start

print(f"Fast (O(n)):  {fast_time:.4f} seconds")


if fast_time > 0:
    speedup = slow_time / fast_time
    print(f"Fast version was approximately {speedup:.2f} times faster.")
else:
    print("Fast version was faster, but the time was too small to calculate the speedup.")


