from typing import List

class LinkedList:
    def __init__(self, name, end):
        self.next = None
        self.name = name
        self.end = end



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = {}
        for fold in folder:
            temps = fold.split('/')
            temps.remove(temps[0])
            start = temps[0]
            result[start] = LinkedList(temps[0], False)
            temps.remove(temps[0])
            save = result[start]
            for index in range(0, len(temps)):
                if index == len(temps)-1 and save.next is None:
                    save.next = LinkedList(temps[index], True)
                elif index == len(temps) - 1 and save.next is not None:
                    save.next.end = True
                elif save.next is None:
                    save.next = LinkedList(temps[index], False)
                save = save.next
        for re in result.values():
            pass
        return []


sl = Solution()
A = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
print(sl.removeSubfolders(A))


