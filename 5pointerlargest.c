#include <stdio.h>

int main() {
    int num1, num2;
    int *ptr1, *ptr2;
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    ptr1 = &num1;
    ptr2 = &num2;
    if (*ptr1 > *ptr2) {
        printf("The maximum number is: %d\n", *ptr1);
    } else {
        printf("The maximum number is: %d\n", *ptr2);
    }
    return 0;
}
