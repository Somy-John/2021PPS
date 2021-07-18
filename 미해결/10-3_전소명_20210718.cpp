/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        int rst = -1;
        while(rst!=-2){
            if(root==NULL) break;
            rst = summation(root);
            std::cout<<rst<<',';
            if(targetSum == rst) return true;
            if(root->right == NULL && root->left == NULL) break;
        }
        return false;
        
    }
    int summation(TreeNode* root){
        if (root->left != NULL && root->right != NULL && root->right->val == -1 && root->left->val == -1) return -2;
        else if (root->left != NULL && root->left->val == -1) return -2;
        else if (root->right != NULL && root->right->val == -1) return -2;
        else if(root->left == NULL && root->right == NULL){
            int tmp = root->val;
            root->val= -1;
            return tmp;
        }
        else if (root->left != NULL && root->right == NULL && root->left->val != -1){
            int tmp = root->val;
            root->val= -1;
            return summation(root->left)+tmp;
        }
        else if (root->right != NULL && root->left == NULL && root->right->val != -1){
            int tmp = root->val;
            root->val= -1;
            return summation(root->right)+tmp;
        }
        return root->val;
    }
};