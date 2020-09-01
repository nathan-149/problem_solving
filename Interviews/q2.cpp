/*
 * For this problem, I implemented a binary tree that holds a letter, a left node, and a right node.
 * For checking for all the possible errors, I split each check into its own function. With this approach, 
 * the code is easier to read, and if any criteria for errors change or need to be added in the future, 
 * we can accomodate for this in the code easily.
 * 
 * 
*/ 

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <assert.h>

using namespace std;


// Binary Tree Implementation
struct Node { 
    char letter; 
    struct Node *left; 
    struct Node *right; 
}; 
  
// createNode() creates a new node
struct Node* createNode(char letter) { 
    // Allocate memory
    Node* node = new Node;
    // Initialize node
    node->letter=letter; 
    node->left = NULL; 
    node->right = NULL; 
    return(node); 
} 

bool insertChild(Node* parent, Node* child) {
    if(parent == NULL || child == NULL) {
        return false;
    }
    if(parent->left == NULL) {
        parent->left = child;
        return true;
    }
    else if(parent->right == NULL) {
        parent->right = child;
        return true;
    }
    return false;
}

/* 
 * pairError returns true if Error E1, or any errors in the input format
 * and returns false otherwise
 */
bool pairError(string input, int i) {
    if(i+4 >= input.size())
        return true;
    if(input[i] != '(')
        return true;
    if(input[i+1] < 'A' || input[i+1] > 'Z')
        return true;
    if(input[i+2] != ',')
        return true;
    if(input[i+3] < 'A' && input[i+3] > 'Z')
        return true;
    if(input[i+4] != ')')
        return true;
    if(i+5 < input.size() && input[i+5] != ' ')
        return true;
    return false;
}

/* 
 * duplicatePairings returns true if Error E2, or any duplicate pairings
 * and returns false otherwise
 */
bool duplicatePairing(Node* parent_node, char child_letter) {
    if (parent_node->left != NULL && 
        parent_node->left->letter == child_letter)
        return true;
    if (parent_node->right != NULL && 
        parent_node->right->letter == child_letter)
        return true;
    return false;
}

/* 
 * nodeHasTwoChildren returns true if a given node has 2/2 children
 * and returns false otherwise 
 */
bool nodeHasTwoChilden(Node* node) {
    if(node->left != NULL && node-> right != NULL)
        return true;
    return false;
}

/* 
 * multipleRoots returns true if Error E4, or the tree has multiple roots
 * and returns false otherwise 
 * 
 * We traverse through the entire tree from the final root node, and then check
 * that we have visited all inputted nodes.
 */
bool multipleRoots(Node* root, unordered_map<char, Node*> umap) {
    if(root == NULL)
        return false;

    // Only need to keep track of val and don't need to keep track of keys,
    // so we can Use unordered set to keep track of nodes we have visited 
    unordered_set<Node*> vis; 
    stack<Node*> st;
    st.push(root);

    // Traverse the binary tree with DFS (preorder)
    while(!st.empty()) {
        Node* curr = st.top();
        st.pop();

        // We should never encounter a cycle, because we deal with that beforehand
        assert(vis.find(curr) == vis.end());
        vis.insert(curr);

        if(curr->left != NULL)
            st.push(curr->left);
        if(curr->right != NULL)
            st.push(curr->right);
    }

    // Check if what we found on the traversal covers the entire map
    unordered_map<char, Node*>:: iterator itr; 
    for (itr = umap.begin(); itr != umap.end(); itr++) { 
        Node* node = itr -> second;

        // If theres a node that we have not found on our traversal,
        // then we have multiple roots
        if(vis.find(node) == vis.end()) 
            return true;
    } 
    return false;
}

/* 
 * containsCycle returns true if Error E5, or the tree contains a cycle
 * and returns false otherwise 
 */
bool containsCycle(Node* root) {
    if(root == NULL)
        return false;

    // Only need to keep track of val and don't need to keep track of keys,
    // so we can use an unordered set which will only keep track of val
    // to keep track of nodes we have visited 
    
    unordered_set<Node*> vis; 
    stack<Node*> st;
    st.push(root);

    // Traverse the binary tree with DFS (preorder)
    while(!st.empty()) {
        Node* curr = st.top();
        st.pop();

        // If we've already visited node, then we found cycle
        if(vis.find(curr) != vis.end()) 
            return true;
        // If not, then mark curr as visited and continue
        else 
            vis.insert(curr);

        if(curr->left != NULL)
            st.push(curr->left);
        if(curr->right != NULL)
            st.push(curr->right);
    }
    return false;
}

/* 
 * printSExpression prints out the Print out Lexicographically Smallest S-Expression 
 * of the final tree, starting from the root node
 */
void printSExpression(Node* root) {
    if(root == NULL)
        return;

    cout << "(";
    cout << root->letter;

    if(root->left != NULL && root->right != NULL){
        if(root->left->letter < root->right->letter) {
            printSExpression(root->left);
            printSExpression(root->right);
        }
        else {
            printSExpression(root->right);
            printSExpression(root->left);
        }  
    }
    else {
        printSExpression(root->left);
        printSExpression(root->right);
    }
    cout << ")";

}
int main() {
    string input;
    string error;
    unordered_map<char, Node*> umap; 
    char parent_letter, child_letter;
    Node* parent_node;
    Node* child_node;
    Node* curr_root = NULL;
    getline(cin >> ws ,input);
    getline(cin >> ws ,error);

    // Check if input is more than one line (Error E1)
    if(error.size() > 0) {
        cout << error;
        cout << "E1";
        return 0;
    }

    // Traverse through input in blocks of each Parent-Child pair
    for(int i = 0; i < input.size(); i+=6) {
        // Check if input is in required Input Format (Error E1)
        if(pairError(input, i)) {
            cout << "E1";
            return 0;
        }

        parent_letter = input[i+1];
        child_letter = input[i+3];

        // Parent node not already made
        if(umap.find(parent_letter) == umap.end()) {
            parent_node = createNode(parent_letter);
            // Add parent node to umap
            pair<char,Node*> parent_pair (parent_letter, parent_node);
            umap.insert(parent_pair);
        }
        // Parent node already made
        else
            parent_node = umap[parent_letter];
        
        // Set current root
        if(curr_root == NULL || curr_root->letter == child_letter)
            curr_root = parent_node;

        // Check for duplicate pairing (Error E2)
        if(duplicatePairing(parent_node, child_letter)) {
            cout << "E2";
            return 0;
        }
        // Check for more than two children (Error E3)
        else if(nodeHasTwoChilden(parent_node)) {
            cout << "E3";
            return 0;
        }

        // Child node not already made
        if(umap.find(child_letter) == umap.end()) {
            child_node = createNode(child_letter);
            // Add child node to umap
            pair<char,Node*> child_pair (child_letter, child_node);
            umap.insert(child_pair);
        }
        // Child node already made
        else
            child_node = umap[child_letter];

        insertChild(parent_node, child_node);
        
        // Note: May want to check if a node has mulitple parents as well, but not required

        // Check for cycle in current binary tree (Error E5)
        if(containsCycle(parent_node)) {
            cout << "E5";
            return 0;
        }
    }

    // Check for cycle in current binary tree (Error E5)
        if(containsCycle(curr_root)) {
            cout << "E5";
            return 0;
        }
    // Check for multiple roots in final tree (Error E4)
    // We want to do this after the final tree is built, since the pairs come in any order.
    if(multipleRoots(curr_root, umap)){
        cout << "E4";
        return 0;
    }

    // Print out Lexicographically Smallest S-Expression of final tree
    printSExpression(curr_root);

    return 0;
}