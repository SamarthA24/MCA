#include<stdio.h>
void main()
{
    int rows;
    int num = 0;
    printf("Enter the number of rows: ");
    scanf("%d",&rows);
    for(int i = 1; i <= rows; i++)
    {
        for(int j = 1; j <= rows - i; j++)
        {
            printf("  ");
        }
        for( int k = 1; k <= i; k++)
        {
            printf("%-5d",num);
            num +=5;
        }
        printf("\n");
    }
}
