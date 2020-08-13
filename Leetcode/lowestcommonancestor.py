#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    done = False;
    found = False;
    ansDepth = 0;
    ansNode = TreeNode(0);

    def DFS(self, node, p, q, depth, parent):
        if(self.done):
            return;  

        #print("curr:", node.val);
        #print("depth:", depth);

        #print(self.found);
        #print("ansdepth:", self.ansDepth);

        if(self.found and self.ansDepth >= depth):
            print("changed");
            self.ansNode = parent;
            self.ansDepth = depth;
        #Case 2:
        if(node.val == p.val and node.val == q.val):
            self.done = True;
            self.ansDepth = depth;
            self.ansNode = node;

        if(node.val == p.val or node.val == q.val):
            if(self.found):
                self.done = True;
                print("done");
                return;
            self.found = True;
            self.ansDepth = depth
            self.ansNode = node;

            #print("found");
            #print("ansDepth:", self.ansDepth);            
        if(node.left and not self.done):
            self.DFS(node.left, p, q, depth + 1, node);
        if(node.right and not self.done):
            self.DFS(node.right, p, q, depth + 1, node);
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


        self.DFS(root, p, q, 0, None);
        return self.ansNode;
        
sol = Solution();
root = TreeNode(3);
left = TreeNode(5);
right = TreeNode(1);

root.left = left;
root.right = right;

left = TreeNode(6);
right = TreeNode(2);

root.left.left = left;
root.left.right = right;

#[3,5,1,6,2,0,8, None, None,7,4];

p = TreeNode(5);
q = TreeNode(3);
print(sol.lowestCommonAncestor(root,p,q));