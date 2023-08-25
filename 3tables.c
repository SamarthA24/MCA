#include<stdio.h>
void main()
{
    int n,n1;
    printf("enter number for the tables: ");
    scanf("%d %d",&n,&n1);
    for(int i = 1; i<=n1;i = i + 1)
    {
        printf("%d x %d = %d\n",n,i,(i*n));
    }
}
