class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leng = len(numbers)
        star = 1
        lst = leng
        while lst > 0 and star < leng:
            if numbers[star-1] + numbers [lst-1] ==  target :
                return [star, lst]
            elif numbers[star-1] + numbers [lst-1] > target :
                lst -= 1
            elif numbers[star-1] + numbers [lst-1] < target :
                star += 1
        
                


                

        