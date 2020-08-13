# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	inorder = [];
	d = {};

	def recursive(self, preorder, iStart, iFinish):

		if not preorder:
			return None;

		if iFinish - iStart <= 0:
			return None;

		val = preorder.pop(0);

		index = self.d[val];

		node = TreeNode(val);

		node.left = self.recursive(preorder, iStart, index);
		node.right = self.recursive(preorder, index + 1, iFinish);

		return node;

	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""

		if len(preorder) == 0:
			return None;

		for i, val in enumerate(inorder):
			self.d[val] = i;

		return self.recursive(preorder, 0, len(inorder));

	def printTreeInOrder(self, node):
		if(node == None):
			return;
		self.printTreeInOrder(node.left);
		print(node.val,end = " ");
		self.printTreeInOrder(node.right);


sol = Solution();

x = sol.buildTree([3,9,20,15,7],[9,3,15,20,7]);

#print(x.val);
sol.printTreeInOrder(x);
		
			

		