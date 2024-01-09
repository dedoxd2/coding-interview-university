#include <stdio.h>
#define MAXSTACK 100
#define StackEntry int // Those Should be defined in the user level but i did that just to clear the Errors
typedef struct stack
{
    int top;
    StackEntry entry[MAXSTACK];

} Stack;

void CreateStack(Stack *ps)
{
    // initializing the stack
    // O(1)
    ps->top = 0; //  *ps.top=0;
};

/*
Pre: The stack in initialized and not full
Post: The element e has been stored at the top of the stack ; and e does not change
*/
void push(StackEntry e, Stack *ps)
{
    ps->entry[ps->top] = e;
    ps->top++;
    // or you can just : ps->entry [ ps -> top++] =e;
};

int StackFull(Stack *ps)
{

    if (ps->top == MAXSTACK)
        return 1;
    else
        return 0;
    // another way to do it
    // return  ps->top ==MAXSTACK;
};

/*
Pre : The stack is initialized and not Empty
Post : The last element entered is returned
*/
void Pop(StackEntry *pe, Stack *ps)
{
    ps->top--;
    *pe = ps->entry[ps->top];
    // Another way to di it
    // *pe = ps->entry[--ps->top];
};

int StackEmpt(Stack *ps)
{
    if (ps->top == 0)
        return 1;
    else
        return 0;
    // or just
    // return ps->top ==0;
    // return !ps->top;
};

// Same preconditions of Pop.
void StackTop(StackEntry *pe, Stack *ps)
{
    *pe = ps->entry[ps->top - 1];
};

/*
Pre : Stack is initialized.
Post : retruns size of stack
*/
int StackSize(Stack *ps)
{
    return ps->top;
};

/*
Pre : Stack is initialized.
Post : destroy all elements; stack looks initialized.
*/
void ClearStack(Stack *ps)
{
    ps->top = 0;
};

void Display(StackEntry e)
{
    // Logic from User Level
    printf("e is: %d\n", e);
};

// Pre : The stack is initialized
void TraverseStack(Stack *ps, void (*pf)(StackEntry))
{
    for (int i = ps->top; i > 0; i--)
        (*pf)(ps->entry[i - 1]);
};
int main()
{

    Stack s;
    StackEntry e;
    CreateStack(&s);
    return 0;
}
