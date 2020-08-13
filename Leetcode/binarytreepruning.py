# Definition for a binary tree root.
class Treeroot(object):
	def __init__(self, x):
		self.val = x

		self.left = None
		self.right = None

class Solution(object):

	def pruneTree(self, root):
		if(root == None):
			return None;
		
		else:
			root.left = self.pruneTree(root.left);
			root.right = self.pruneTree(root.right);

			if(root.left == None and root.right == None and root.val == 0):
				return None;
			
		return root;

sol = Solution();

root = Treeroot(1);

one = Treeroot(0);

two = Treeroot(1);

three = Treeroot(0);

four = Treeroot(0);

root.left = one;
root.right = two;

one.left = three;
one.right = four;

x = sol.pruneTree(root);

print(x);