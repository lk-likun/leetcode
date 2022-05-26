# leetcode submit region begin(Prohibit modification and deletion)
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue)//2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            res = self.queue.pop(0)
            return res
        else:
            return -1

    def popMiddle(self) -> int:
        if self.queue:
            mid = len(self.queue) / 2
            midint = len(self.queue) // 2
            if mid > midint:
                mid = midint
            else:
                mid = midint - 1
            res = self.queue.pop(mid)
            return res
        else:
            return -1

    def popBack(self) -> int:
        if self.queue:
            res = self.queue.pop(-1)
            return res
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# leetcode submit region end(Prohibit modification and deletion)
