#include <stdio.h>
#define StackEntry int

typedef struct stacknode
{
    StackEntry entry;
    struct stacknode *next;
} StackNode;

typedef struct stack
{
    StackNode *top;
    int size;
} Stack;

void CreateStack(Stack *ps)
{ // O(1)
    ps->top = NULL;
    ps->size = 0;
};

/*
Pre : The stack exists and is initialized
Post : The argument item has been stored at the top of the stack
*/
void Push(StackEntry e, Stack *ps)
{
    // O(1)
    StackNode *pn = (StackNode *)malloc(sizeof(StackNode));
    pn->entry = e;
    pn->next = ps->top;
    ps->top = pn;
    ps->size++;
};

void Pop(StackEntry *pe, Stack *ps)
{
    // O(1)
    StackNode *ptr_holder;
    *pe = ps->top->entry; // This would be the code for function StackTop
    ptr_holder = ps->top;
    ps->top = ps->top->next;
    free(ptr_holder);
    ps->size--;
};

int StackEmpty(Stack *ps)
{
    // O(1)
    // return !ps->top;
    return ps->top == NULL;
};

int StackFull(Stack *ps)
{ // O(1)
    return 0;
};

/*
Pre : The stack exists
Post : All the elements freed
*/
void ClearStack1(Stack *ps)
{                            // O(n)
    StackNode *pn = ps->top; // holding the next address
    StackNode *qn = ps->top; // holding the previous address
    while (pn)               // pn != NULL
    {
        pn = pn->next;
        free(qn);
        qn = pn;
    };
    ps->top = NULL;
    ps->size = 0;
};

// just another way to implement it
void ClearStack2(Stack *ps)
{                            // O(n)
    StackNode *pn = ps->top; // holding the next address
    while (pn)
    {
        pn = pn->next;
        free(ps->top); // holding the previous address
        ps->top = pn;
    };

    ps->size = 0;
};
// Total Time = N * time of one Loop

void TraverseStack1(Stack *ps, void (*pf)(StackEntry))
{
    // O(n)
    StackNode *ptr_holder = ps->top;

    while (ptr_holder)
    {
        (*pf)(ptr_holder);
        ptr_holder = ptr_holder->next;
    };
};

// Another way
void TraverseStack2(Stack *ps, void (*pf)(StackEntry))
{

    for (StackNode *pn = ps->top; pn; pn = pn->next)
        (*pf)(pn->entry);
}

int StackSize1(Stack *ps)
{ // O(n)
  // if we don't have variable holding the size
    int i;
    StackNode *ptr_holder = ps->top;
    for (i = 0; ptr_holder; ptr_holder = ptr_holder->next)
        i++;

    return i;
}

int StackSize2(Stack *ps)
{ // O(1)
    return ps->size;
}
int main()
{
    return 0;
}
