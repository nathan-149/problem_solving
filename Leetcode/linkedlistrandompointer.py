# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head == None:
        	return None;

        traverse = head;

        copy = Node(head.val, head.next, head.random);
        #our answer is the head of our deep copy
        ans = copy;

        d = {};
        d[head] = copy;

        while traverse != None:

        	#next
        	if traverse.next == None:
        		copy.next = None;

        	elif traverse.next not in d:
        		newNext = Node(traverse.next.val, traverse.next.next, traverse.next.random);
        		copy.next = newNext;
        		d[traverse.next] = newNext;

        	else:
        		copy.next = d[traverse.next];

        	#random
        	if traverse.random == None:
        		copy.random = None;

        	elif traverse.random not in d:
        		newRand = Node(traverse.random.val, traverse.random.next, traverse.random.random);
        		copy.random = newRand;
        		d[traverse.random] = newRand;

        	else:
        		copy.random = d[traverse.random];



        	traverse = traverse.next;
        	copy = copy.next;

        return ans;


sol = Solution();

a = Node(1, None, None);
b = Node(2, None, None);
a.next = b;
a.random = b;
b.random = b;

ans = sol.copyRandomList(a);

while ans != None:
	print(ans.random.val);
	ans = ans.next;




