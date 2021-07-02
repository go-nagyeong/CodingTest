def solution(nums):
    set_ = set(nums)
    if len(set_) < len(nums)/2:
        return len(set_)
    else:
        return len(nums)/2