import re
def solution(my_string):
    num_str = re.findall('[0-9]+', my_string)
    nums = [int(i) for i in num_str]
    answer = sum(nums)
    return answer