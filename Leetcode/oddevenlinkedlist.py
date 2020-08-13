# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		#empty case
		if(head == None or head.next == None):
			return head;

		evenHead = head.next;
		evenCurr = evenHead;
		oddCurr = head;

		while(oddCurr.next != None and evenCurr.next != None):
			oddCurr.next = oddCurr.next.next;
			oddCurr = oddCurr.next;
			evenCurr.next = oddCurr.next;
			evenCurr = evenCurr.next;

		#end
		oddCurr.next = evenHead;
		return head;

sol = Solution();

head = ListNode(1);
two = ListNode(2);
#three = ListNode(3);
#four = ListNode(4);

head.next = two;
#two.next = three;
#three.next = four;

x = sol.oddEvenList(head);

while(x != None):
	print(x.val);
	x = x.next;

		

