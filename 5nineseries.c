#include<stdio.h>
void main()
{
    int n, term, sum =0;
    printf("Enter the number of terms: ");
    scanf("%d",&n);
    term = 9;
    for(int i = 1; i <= n; i++)
    {
        printf("%d ",term);
        sum +=term;
        term = term * 10 + 9;
    }
    printf("\nThe sum of series is: %d",sum);
}
