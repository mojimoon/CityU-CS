# CS3334 Midterm Review

## Abstract Data Types

Abstract data types define the **values** and **operations** of a data structure.

It does not define the **implementation** of the data structure.

Value definition has 2 parts:
- Definition: what is stored in the data structure.
- (Optional) Condition: what limitations are placed on the data structure.

Operation definition has 3 parts:
- Header: method signature. This includes the name, parameters, and return type.
- (Optional) Precondition: what must be true before the operation is called.
- Postcondition: what will be realized after the operation is called.

Example: Set

- Value: A set of elements.
    - Condition: Elements are unique.
- Operations:
    - `void add(E e)`
        - Postcondition: `e` will be added to the set.
    - `void remove(E e)`
        - Precondition: `e` is in the set.
        - Postcondition: `e` will be removed from the set.
    - `int size()`
        - Postcondition: The number of elements in the set will be returned.
    - `boolean has(E e)`
        - Postcondition: `true` will be returned if `e` is in the set, `false` otherwise.
    
## List

List is a sequence of elements.

Structure of list is organized by **index**, the relative position of an element in the list.

### Singly Linked List

Each data is stored in a **node**. The node contains the data and a reference to the next node.

See Midterm.cpp for implementation.

## Stack

Stack is a data structure that follows the **Last In First Out** (LIFO) principle.

### Applications

#### Postfix Expression Evaluation

1. Maintain a stack of operands.
2. If the next symbol is an operand, push it onto the stack.
3. If the next symbol is an operator, pop the top two operands from the stack, perform the operation, and push the result onto the stack.
4. When the expression is exhausted, the result is the top of the stack.

Do note that operand 1 is pushed prior to operand 2, so operand 2 will be popped first.

```cpp
    operand2 = s.pop();
    operand1 = s.pop();
    result = compute(op, operand1, operand2);
    s.push(result);
```

#### Convert Infix to Postfix

| Operator | Precedence |
|----------|------------|
| `(`      | 0          |
| `+` `-`  | 1          |
| `*` `/`  | 2          |

The smaller the precedence, the higher the priority.

1. Maintain a stack of operators.
2. If the next symbol is an operand, output it.
3. If the next symbol is `)`:
    1. Pop the top operator from the stack.
    2. Output the operator.
    3. Repeat until the top operator is `(`.
4. If the next symbol is `*` or `/`:
    1. Pop the top operator from the stack.
    2. Output the operator.
    3. Repeat until the top operator is `(` or `+` or `-`.
    4. Push the operator onto the stack.
5. If the next symbol is `+` or `-`:
    1. Pop the top operator from the stack.
    2. Output the operator.
    3. Repeat until the top operator is `(`.
    4. Push the operator onto the stack.
6. If the next symbol is `(`:
    1. Push the operator onto the stack.
7. When the expression is exhausted, pop and output all operators from the stack.

```cpp
char* infixToPostfix(char* infix) {
    Stack<char> s;
    char* postfix = new char[strlen(infix) + 1];
    int i = 0;
    while (*infix != '\0') {
        if (isdigit(*infix)) {
            postfix[i++] = *infix;
        } else if (*infix == ')') {
            while (s.top() != '(') {
                postfix[i++] = s.pop();
            }
            s.pop();
        } else if (*infix == '*' || *infix == '/') {
            while (s.top() != '(' && s.top() != '+' && s.top() != '-') {
                postfix[i++] = s.pop();
            }
            s.push(*infix);
        } else if (*infix == '+' || *infix == '-') {
            while (s.top() != '(') {
                postfix[i++] = s.pop();
            }
            s.push(*infix);
        } else if (*infix == '(') {
            s.push(*infix);
        }
        infix++;
    }
    while (!s.isEmpty()) {
        postfix[i++] = s.pop();
    }
    postfix[i] = '\0';
    return postfix;
}
```

#### Boundary of Lines Looking from Above

Given several lines, identify which parts of the lines can been seen if you look from the above.

1. Maintain a stack of lines. Push `l[1]`, `l[2]` onto the stack.
2. for `i` from `3` to `n`:
    1. Pop the top line from the stack and store as `A`.
    2. Pop the top line from the stack and store as `B`.
    3. While the intersects of `A` and `B` is under `l[i]`:
        1. `A = B`
        2. Pop the top line from the stack and store as `B`
    4. Push `B` onto the stack.
    5. Push `A` onto the stack.
    6. Push `l[i]` onto the stack.

Example:

![](https://raw.githubusercontent.com/jerrykhh/cityu/main/cs3334/midterm/q6_ans.png)

1. Push `l[1]`, `l[2]` onto the stack. The stack is: `bottom -> l[1] -> l[2] -> top`
2. Processing `l[3]`
    1. `A=l[2]`, `B=l[1]`, intersects under `l[3]`.
    2. `A=l[1]`, `B=null`
    3. Push `A=l[1]`, `l[3]` onto the stack.
    4. The stack is: `bottom -> l[1] -> l[3] -> top`
3. Processing `l[4]`
    1. `A=l[3]`, `B=l[1]`, intersects above `l[4]`.
    2. Push `B=l[1]`, `A=l[3]`, `l[4]` onto the stack.
    3. The stack is: `bottom -> l[1] -> l[3] -> l[4] -> top`
4. Processing `l[5]`
    1. `A=l[4]`, `B=l[3]` intersects under `l[5]`.
    2. `A=l[3]`, `B=l[1]` intersects under `l[5]`.
    3. `A=l[1]`, `B=null`.
    4. Push `A=l[1]`, `l[5]` onto the stack.
    5. The stack is: `bottom -> l[1] -> l[5] -> top`
5. Therefore, part of `l[1]` and `l[5]` can be seen from the above.

#### Find Duplicate Parentheses

1. Maintain a stack of characters.
2. If a character is not `)`, push it onto the stack.
3. If a character is `)`, pop all characters from the stack until `(` is found.
    1. If the top of the stack is `(`, then there is a duplicate parentheses.
    2. If the top of the stack is not `(`, then there is no duplicate parentheses.

This is because all duplicate paretheses follow this pattern: `((...))`. If there are any character between the parentheses, then it is not a duplicate parentheses.

Therefore, the inner `)` will pop all characters until the inner `(` is found. For the outer `)`, it will find no character between, and the top is outer `(`.

#### Find Smallest Number by Removing K Digits

Given a non-negative integer `num` represented as a string, remove `k` digits from the number so that the new number is the smallest possible.

```cpp
string removeKDigits(string num, int k) {
    if (num.length() == k) {
        return "0";
    }
    Stack<char> s;
    for (int i = 0; i < num.length(); i++) {
        while (!s.isEmpty() && s.top() > num[i] && k > 0) {
            s.pop();
            k--;
        }
        s.push(num[i]);
    }
    while (k > 0) {
        s.pop();
        k--;
    }
    string result = "";
    while (!s.isEmpty()) {
        result = s.pop() + result;
    }
    return result;
}
```

1. Maintain a stack of digits.
2. Process the given number from high to low.
3. If there are still quota to remove digits, and the top of the stack is larger than the current digit, pop the top of the stack. (e.g. given n=8997, k=1, at i=3, stack=899, top=9, num[i]=7, pop 9 and keep 7 will result in a smaller number)
4. Push the current digit onto the stack.
5. After processing the number, if there are still quota to remove digits, pop the top of the stack. (This is better than popping at the start)
6. Pop all digits from the stack. They are stored from low to high. So reverse the order and return.

## Complexity Analysis

### Notation

Big-O notation describes the upper bound of the complexity.

$f(n)=O(g(n))$ means $f(n)$ grows no faster than $g(n)$.

Mathematically, $\exists c>0, \exists n_0>0, \forall n \geq n_0, 0\leq f(n)\leq cg(n)$.

Big-Omega notation describes the lower bound of the complexity.

$f(n)=\Omega(g(n))$ means $f(n)$ grows no slower than $g(n)$.

Mathematically, $\exists c>0, \exists n_0>0, \forall n \geq n_0, 0\leq cg(n)\leq f(n)$.

Big-Theta notation describes the tight bound of the complexity.

$f(n)=\Theta(g(n))$ means $f(n)$ grows at the same rate as $g(n)$.

Mathematically, $\exists c_1>0, \exists c_2>0, \exists n_0>0, \forall n \geq n_0, 0\leq c_1g(n)\leq f(n)\leq c_2g(n)$.

$f(n)=\Theta(g(n)) \iff f(n)=O(g(n)) \land f(n)=\Omega(g(n))$.

Little-O notation describes the strict upper bound of the complexity. It can be as loose as possible.

$f(n)=o(g(n))$ means $f(n)$ grows strictly slower than $g(n)$.

Mathematically, $\forall c>0, \exists n_0>0, \forall n \geq n_0, 0\leq f(n)< cg(n)$.

Usually, average case complexity is the same as worst case complexity. Big-O notation is used to describe the complexity.

Example:

```cpp
void function(int n){
    int x = 200;
    int y = 100;
    for(int i =0; i<n; i++){
        if(x>50)x--;
        else{
            for(j=0;j<n;j++) y++;
            x++;
        }
    }
}
```

Running time:

$T(n)=n$ for $n < 150$

$T(n)=n+\left(\frac{(n-150)}{2}+1\right)\times n$ for $n \geq 150$

Asymptotic complexity:

$O(n)$ for $n < 150$

$O(n^2)$ for $n \geq 150$

### Recurrence Relation

Master Theorem: If $T(n)=aT\left(\frac{n}{b}\right)+f(n)$, where $a\geq 1, b>1, f(n)>0, T(1)=1$, then:

1. If $aT\left(\frac{n}{b}\right)$ dominates $f(n)$, then $T(n)=\Theta\left(n^{\log_ba}\right)$.
2. If $f(n)$ dominates $aT\left(\frac{n}{b}\right)$, then $T(n)=\Theta\left(f(n)\right)$.
3. If $f(n)$ and $aT\left(\frac{n}{b}\right)$ are of the same order, (this is out of scope of this course)

Explanation for rule 1:

It takse $\log_bn$ levels to reach $T(1)$. Each level multiplies running time by $a$.

Therefore, total time is $T(n)=a^{\log_bn}$

$\log T(n)=\log_bn\log a=\frac{\log n}{\log b}\log a=\log n\frac{\log a}{\log b}=\log n\log_ba$

$T(n)=\Theta\left(n^{\log_ba}\right)$

Example: 

1. $T(n)=T(n-1)+C$, recursion dominates, $T(n)=\Theta(n)$.
2. $T(n)=T(n-1)+n$, recursion and $n$ are of the same order, we can directly compute $T(n)=\Theta(n^2)$.
3. $T(n)=2T\left(\frac{n}{2}\right)+n$, recursion dominates, $T(n)=\Theta(n\log n)$.
4. $T(n)=T\left(\frac{n}{2}\right)+n$, recursion and $n$ are of the same order, we can directly compute $T(n)=\Theta(n)$.

Exercises:

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i * i; j++) {
        if (j % i == 0) {
            for (int k = 0; k < j; k++) {
                // O(1)
            }
        }
    }
}
```

- Outer loop: $n$
- Middle loop: $i^2=O(n^2)$
- If `j % i == 0` ($O(n)$ cases), inner loop: $j=O(n^2)$, total time: $O(n \cdot n \cdot n^2)=O(n^4)$
- If `j % i != 0` ($O(n^2-n)$ cases), inner loop: $j=O(n)$, total time: $O(n \cdot n \cdot n)=O(n^3)$
- Total time: $O(n^4)$

## Hashing

### Collision Resolution

Linear probing: If the slot is occupied, try $f(x)+1$, $f(x)+2$, $f(x)+3$, etc.

Quadratic probing: If the slot is occupied, try $f(x)+1^2$, $f(x)+2^2$, $f(x)+3^2$, etc. If $N$ is prime and **load factor** is less than 0.5, then all slots will be visited.

Second hashing: If the slot is occupied, try $f(x)+h(x)$, $f(x)+2h(x)$, $f(x)+3h(x)$, etc. $h(x)$ CAN NOT BE 0.

Chaining: If the slot is occupied, store the data in a linked list.

**Rehashing**: If the load factor is greater than 0.5, rehash the table by expanding the table size to the next prime number larger than $2N$.

## Tree

### Terminology

- **Tree**: A set of nodes that:
    - Has a root node.
    - If, removing the root node, the remaining nodes form a set of disjoint subtrees.
- **Degree**: The number of children of a node.
- **Leaf**: A node with degree 0.
- **Internal node**: A node with degree greater than 0.
- **Parent**: If tree with root $v$ is the subtree of tree with root $w$, then $w$ is the parent of $v$, and $v$ is the child of $w$.
- **Sibling**: Nodes with the same parent.
- **Path**: A sequence of nodes such that any two consecutive nodes are parent and child.
- **Distance**: Distance between two nodes is the number of edges in the path between them.
- **Depth**: Distance between the root and the node.
- **Height**: The maximum depth of any leaf in the tree.
- **Ancestor**: A node $v$ is an ancestor of node $w$ if $v$ is on the path from the root to $w$, and $w$ is a descendant of $v$.  ($v$ is the ancestor of itself)

### Binary Tree

**Binary tree**: A set of nodes that:
- Either empty, or
- Has a root node, and two disjoint binary trees (left and right subtrees).

**Full binary tree**: A binary tree where all leaves are at the same depth. It has $2^h-1$ nodes, where $h$ is the height.

Equivalent definition: A binary tree where all internal nodes have degree 2, and all leaves are at level $h$.

**Complete binary tree**: A binary tree where all leaves are at the same depth, except the last level. The last level is filled from left to right. It has $[2^{h-1}, 2^h-1]$ nodes, where $h$ is the height.

Equivalent definition: A binary tree where all internal nodes have degree 2, and all leaves are at level $h$ or $h-1$.

### Binary Search Tree

Binary search tree is a binary tree such that:
- The value of the left child is less than the value of the parent.
- The value of the right child is greater than the value of the parent.

**Inorder traversal**: Traverse the left subtree, visit the root, traverse the right subtree.

Inorder traversal of a binary search tree will visit the nodes in ascending order.

Worst case analysis: If the tree is a linked list, then the time complexity is $O(n)$.

### Binary Tree Traversal

**Preorder traversal**: Visit the root, traverse the left subtree, traverse the right subtree.

Recursive implementation is trivial.

Iterative implementation:

1. Maintain a stack of nodes, that will store the nodes not yet visited.
2. Push the root onto the stack.
3. While the stack is not empty:
    1. Pop the top of the stack and store as `node`.
    2. Visit `node`.
    3. Push the right child of `node` onto the stack, so it will be visited later.
    4. Push the left child of `node` onto the stack.

Inorder Iterative implementation:

1. Maintain a stack of nodes, that will store the nodes reached, but itself and right subtree are not yet visited.
2. Push the root onto the stack. Use `cur` to track the current node.
3. While the stack is not empty:
    1. Push `cur` onto the stack, and move `cur` to its left child.
    2. Repeat step 1 until `cur` is `null`. Therefore, the top of the stack is the leftmost node.
    3. Pop the top of the stack and store as `cur`. Visit `cur`, and move `cur` to its right child.

## Heap

Heap is a complete binary tree such that:
- The value of the parent is greater than the value of the children, if the heap is a **max heap**; or
- The value of the parent is less than the value of the children, if the heap is a **min heap**.

Take min heap as an example.

To insert a value:

1. Insert the value at the end of the heap.
2. Keep swapping the value with its parent until the parent is smaller than the value.

To delete the minimum value (root):

1. Replace the root with the last value of the heap.
2. Keep swapping the value with its smaller child until the value is smaller than both children.

## Miscellaneous

### Linked List

- Advantages:
    - Efficient use of memory
    - Easy manipulation
    - Extensible
- Disadvantages:
    - Extra memory for pointers
    - O(n) random access

### Array Implementation of Binary Tree

- Advantages:
    - Simple
    - Best for full binary tree or complete binary tree
- Disadvantages:
    - Wasteful for sparse binary tree
    - Maximum size must be known in advance
    - Inadequate for insertion and deletion
