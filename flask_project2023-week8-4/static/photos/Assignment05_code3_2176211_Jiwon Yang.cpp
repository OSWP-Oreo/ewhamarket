#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode *left, *right, *parent;
} TreeNode;

/*           G
        C         F
      A   B     D   E         */

TreeNode n1 = {'A', NULL, NULL, NULL};
TreeNode n2 = {'B', NULL, NULL, NULL};
TreeNode n3 = {'C', &n1, &n2, NULL};
TreeNode n4 = {'D', NULL, NULL, NULL};
TreeNode n5 = {'E', NULL, NULL, NULL};
TreeNode n6 = {'F', &n4, &n5, NULL};
TreeNode n7 = {'G', &n3, &n6, NULL};
TreeNode *exp = &n7;

// find node p's predecessor
//1. if node p has left subtree, find rightmost node.
//2. if node p does not have left subtree,   ->   find parent.
TreeNode *tree_predecessor(TreeNode *p){

    if (p->left != NULL){
        //left subtree의 가장 오른쪽 노드 찾기.
        TreeNode *temp = p->left;
        while (temp ->right != NULL){
            temp = temp->right;
        }
        return temp;
    }

    else {
    // 내가 오른쪽 자식인 엄마 찾기. 
    // 즉, 엄마가 널이기 전 & 모녀가 왼쪽인 한 계속 돎
        TreeNode *temp = p->parent;
        while (temp != NULL && temp->left == p){
            p = temp;
            temp = temp->parent;
        }
        return temp;
    }
}



int main(){

    TreeNode *q = exp;
    n1.parent = &n3;
    n2.parent = &n3;
    n3.parent = &n7;
    n4.parent = &n6;
    n5.parent = &n6;
    n6.parent = &n7;
    n7.parent = NULL;

   //go to the rightmost node
    while (q->right) q = q->right;


   //print in reverse order 
   do {
    printf("%c\n", q->data);
    q = tree_predecessor(q);
   } while (q); 
    
    return 0;
}