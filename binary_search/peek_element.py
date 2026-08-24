# def find_peek(nums):
#     l=0
#     r=len(nums)-1
#     while l<=r:
#         mid = (l+r)//2
#         if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
#             return mid
#         else:
#             if nums[mid]<nums[mid+1]:
#                 l=mid
#             else:
#                 r=mid-1
# print(find_peek([1,2,1,3,5,6,4]))
def find_peak(nums):
    l=0
    r=len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid]<nums[mid+1]:
            l = mid+1
        else:
            r=mid
    return r
            