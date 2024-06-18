#include "entity/stack.h"
#include <stdio.h>

void push(Stack *stack, int data) {
    if (stack->sp < STACK_MAX) {
        stack->stack[stack->sp++] = data;
    } else {
        printf("スタック領域に空きがない\n");
    }
}

int pop(Stack *stack) {
    if (stack->sp > 0) {
        return stack->stack[--stack->sp];
    } else {
        printf("スタックが空である\n");
        return -999; // エラー値を返す
    }
}
