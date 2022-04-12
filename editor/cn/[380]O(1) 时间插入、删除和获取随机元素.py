# leetcode submit region begin(Prohibit modification and deletion)
import random


class RandomizedSet:
    #
    # def __init__(self):
    #     # self.res = set()
    #     self.res = dict()
    #
    # def insert(self, val: int) -> bool:
    #     # if val in self.res:
    #     #     return False
    #     # self.res.add(val)
    #     # return True
    #     try:
    #         z = self.res[val]
    #         return False
    #     except:
    #         self.res.update({val: val})
    #         return True
    #
    # def remove(self, val: int) -> bool:
    #     # if val in self.res:
    #     #     self.res.remove(val)
    #     #     return True
    #     # return False
    #     try:
    #         self.res.pop(val)
    #         return True
    #     except:
    #         return False
    #
    # def getRandom(self) -> int:
    #     return random.choice(list(self.res.keys()))
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)


# x = RandomizedSet()
# x.insert()
# print(x)