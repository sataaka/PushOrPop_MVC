#include "entity/stack.h"
#include <stdio.h>

int main(void) {
    Stack stack = { .sp = 0 }; // スタックの初期化

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    int a = pop(&stack);
    printf("a = %d\n", a);

    a = pop(&stack);
    printf("a = %d\n", a);

    push(&stack, 40);
    push(&stack, 50);

    a = pop(&stack);
    printf("a = %d\n", a);

    // スタックの内容を表示
    for (int i = 0; i < stack.sp; i++) {
        printf("Stack[%d] = %d\n", i, stack.stack[i]);
    }

    return 0;
}
