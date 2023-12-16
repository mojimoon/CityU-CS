# Balanced BST

Based on [Programiz](https://www.programiz.com/dsa/avl-tree).

# AVL Tree

## Definition

AVL tree is a self-balancing binary search tree.

**Balancing factor** = Height(left subtree) - Height(right subtree)

In AVL tree, the balancing factor of every node is either -1, 0 or 1.

## Insertion

First, insert the node as you would in a normal binary search tree.

Then, for every node on the path from the inserted node to the root, check if the node is balanced. If not, perform the necessary rotations to balance the tree.

## Rotations

### Left Rotation

![](https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_leftrotate-1.png)

Left rotation happens when the balancing factor of a node is -2.

In the above example, if we insert a child to $\beta$ or $\gamma$, the BF of $x$ becomes -2. This is, insert into RC of RC of $x$.

Solution: let $y$, RC of $x$, be the new root of the subtree.

- $x$ becomes LC of $y$
- $\alpha$ and $\gamma$ is unchanged
- $\beta$ becomes RC of $x$

![](https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_leftrotate-4.png)

### Right Rotation

![](https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_rightrotate-1.png)

Right rotation happens when the balancing factor of a node is 2, or inserting into LC of LC.

![](https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_rightrotate-4.png)

### Left-Right Rotation

![](https://www.programiz.com/sites/tutorial2program/files/avl-tree-leftright-rotate-1.png)

Left-right rotation happens when the balancing factor of a node is 2.

In the above example, $\alpha$ and $\delta$ have a height of $h$, while $\beta$ and $\gamma$ have a height of $h-1$. 

Initial balancing factor of $x$ is 0, $z$ is 1.

In the above example, if we insert a child to $\beta$ or $\gamma$, the BF of $z$ becomes 2. This is, insert into RC of LC of $z$.

Step 1: Perform left rotation on $x$, LC of $z$.

- $\beta$ becomes RC of $x$
- $x$ becomes LC of $y$
- $y$ becomes LC of $z$

Step 2: Perform right rotation on $z$.

- $y$ becomes the new root of the subtree
- $z$ becomes RC of $y$
- RC of $y$, $\gamma$, becomes LC of $z$

![](https://www.programiz.com/sites/tutorial2program/files/avl-tree-leftright-rotate-2.png)

### Right-Left Rotation

![](https://www.programiz.com/sites/tutorial2program/files/avl-tree-rightleft-rotate-1.png)

Right-left rotation happens when the balancing factor of a node is -2, or inserting into LC of RC.

![](https://www.programiz.com/sites/tutorial2program/files/avl-tree-rightleft-rotate-2.png)

## Implementation

```cpp
struct Node {
    Node(int x): val(x), h(1), lc(nullptr), rc(nullptr) {}
    int val, h;
    Node *lc, *rc;
};

int h(Node *x) { return x ? x->h : 0; }

void update(Node*& x) {
    x->h = max(h(x->lc), h(x->rc)) + 1;
}

// AVL tree
void insert(Node*& root, int x) {
    if (!root) { root = new Node(x); return; }
    else if (x < root->val) {
        insert(root->lc, x);
        if (h(root->lc) - h(root->rc) == 2) {
            if (x < root->lc->val) rotateL(root); // LL insertion, Right rotation
            else double_rotateL(root); // LR insertion, Left-Right rotation
        }
    } else if (x > root->val) {
        insert(root->rc, x);
        if (h(root->rc) - h(root->lc) == 2) {
            if (x > root->rc->val) rotateR(root); // RR insertion, Left rotation
            else double_rotateR(root); // RL insertion, Right-Left rotation
        }
    }
}

void rotateL(Node*& root) {
    Node* newroot = root->lc;
    root->lc = newroot->rc;
    newroot->rc = root;
    update(root); // "root" is now the right child of "newroot", so update "root" first
    update(newroot);
    root = newroot;
}

void rotateR(Node*& root) {
    Node* newroot = root->rc;
    root->rc = newroot->lc;
    newroot->lc = root;
    update(root);
    update(newroot);
    root = newroot;
}

void double_rotateL(Node*& root) {
    rotateR(root->lc);
    rotateL(root);
}

void double_rotateR(Node*& root) {
    rotateL(root->rc);
    rotateR(root);
}
```

## Summary

- `rotateL()` on LL insertion: swap root and LC
- `rotateR()` on RR insertion: swap root and RC
- `double_rotateL()` on LR insertion: `rotateR()` on LC, then `rotateL()` on root
- `double_rotateR()` on RL insertion: `rotateL()` on RC, then `rotateR()` on root

# Splay Tree

## Definition

Splay tree is a self-adjusting binary search tree.

The idea is to bring the most recently accessed item to the root of the tree, so that the next access to the same item will be faster.

Whenever insert, search or delete is performed on a node, it is brought to the root of the tree.

## Rotation

- Access left child of root: `zig()` (AVL `rotateL()`)
- Access right child of root: `zag()` (AVL `rotateR()`)
- Access RR grandchild of root: `zigzig()` (1. `zig()` on root, 2. `zig()` on root)
- Access LL grandchild of root: `zagzag()` (1. `zag()` on root, 2. `zag()` on root)
- Access RL grandchild of root: `zigzag()` (1. `zig()` on RC, 2. `zag()` on root)
- Access LR grandchild of root: `zagzig()` (1. `zag()` on LC, 2. `zig()` on root)

## Split & Join

`split(root, k, &L, &R)`: split the tree into two trees, one with keys $\leq k$, the other with keys $> k$

Implementation: splay `k` to the root, then remove the right child of the root and store it in `R`.

`join(root, L, R)`: join two trees `L` and `R` into one tree

## Insertion & Deletion

Insert:

1. Splay `x` to the root. If `x` does not exist, the new root is largest node $\leq x$
2. Split the tree into two trees, one with keys $\leq x$, the other with keys $> x$
3. Create a new node with key `x`, and set its left child to the left tree, and right child to the right tree

Delete:

1. Splay `x` to the root
2. Split the tree into two trees, one with keys $\leq x$, the other with keys $> x$. Delete the root of the left tree
3. Splay the maximum node of the left tree to the root
4. Join the two trees, the new root is the root of the left tree

