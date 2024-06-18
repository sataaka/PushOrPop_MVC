#ifndef STACK_H
#define STACK_H

#define STACK_MAX 5

// スタックを表す構造体
typedef struct {
    int stack[STACK_MAX];
    int sp; // スタックポインタ
} Stack;

// スタック操作の関数のプロトタイプ宣言
void push(Stack *stack, int data);
int pop(Stack *stack);

#endif /* STACK_H */
