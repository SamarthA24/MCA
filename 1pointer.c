#include<stdio.h>
int main()
{
    int a = 5, *x;
    char b = 'z', *y;
    x = &a;
    printf("x=%d\n",x);
    printf("x+3=%d\n",x+3);
    printf("x-2=%d\n",x-2);
    y = &b;
    printf("y=%d\n",y);
    printf("y+3=%d\n",y+3);
    printf("y-2=%d\n",y-2);
    return 0;
}
