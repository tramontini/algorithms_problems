# Solução brute force que tem uma melhora no espaço
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]

# Solução pega no fórum, 90% mais rápida do que as outras enviadas.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, item in enumerate(nums):
            # Vê se já existe aquele valor, caso não exista salva no dict
            candidate = nums_dict.get(item)
            if candidate is not None:
                return [candidate, index]
            else:
                nums_dict[target - item] = index
