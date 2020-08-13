# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	d = {};

	def makeTree2(self, postorder, iStart, iFinish):
		if not postorder:
			return None;

		if(iFinish - iStart <= 0):
			return None;

		val = postorder.pop();

		index = self.d[val];
		node = TreeNode(val);
		node.right = self.makeTree2(postorder, index+1, iFinish);
		node.left = self.makeTree2(postorder, iStart, index);
			
		return node;
	

	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""

		if(len(inorder) == 0):
			return None;

		self.inorder = inorder;
		self.postorder = postorder;

		for i in range(len(inorder)):
			self.d[inorder[i]] = i;

		return self.makeTree2(postorder, 0, len(inorder));

	def printTreeInOrder(self, node):
		if(node == None):
			return;
		self.printTreeInOrder(node.left);
		print(node.val,end = " ");

		self.printTreeInOrder(node.right);
		
sol = Solution();

x = sol.buildTree([9,3,15,20,7],[9,15,7,20,3]);

sol.printTreeInOrder(x);		