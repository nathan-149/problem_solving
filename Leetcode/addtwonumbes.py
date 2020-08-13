class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        exp = 0
        while(l1 != None):
            #build number in reverse orce
            num1 += l1.val * (10**exp)
            l1 = l1.next
            exp += 1
        exp = 0
        while(l2 != None):
            num2 += l2.val * (10**exp)
            l2 = l2.next
            exp += 1
        print(num1)
        resNum = num1 + num2
        print(resNum);
        res = ListNode(resNum %10)
        resNum //= 10
        temp = res
        while(resNum > 0):
            res.next = ListNode(resNum % 10)
            resNum //= 10
            res = res.next
        return temp