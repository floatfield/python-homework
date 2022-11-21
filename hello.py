from typing import Tuple

def find_local_time(n: int) -> Tuple[int, int]:
    hours = (n // 60) % 24
    minutes = n % 60
    return (hours, minutes)

n = int(input())

print(find_local_time(n))