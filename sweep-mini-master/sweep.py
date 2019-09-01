def all_same(l: list) -> bool:
    if len(l) == 0:
        return True
    for item in l:
        if item != l[0]:
            return False
    return True

def dedup(l: list) -> list:
    if len(l) == 0:
        return []
    alist = []
    for item in l:
        if item not in alist:
            alist.append(item)
    return alist

def max_run(l: list) -> int:
    if len(l) == 0:
        return 0
    current_run = []
    longest_run = 0
    current_value = l[0]
    for item in l:
        if item == current_value:
            current_run.append(item)
            if len(current_run) > longest_run:
                longest_run = len(current_run)
        else:
            current_value = item
            current_run = []
            current_run.append(item)
    return longest_run








