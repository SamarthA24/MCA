#include<stdio.h>
void main()
{
    int n, i;
    float sum = 0;
    printf("Enter the number of harmonic series: ");
    scanf("%d",&n);
    for(i = 1; i <= n; i++)
    {
        printf("1/%d + ",i);
        sum += 1.0 / i;
    }
    printf("\nSum of harmonic series  upto %d are: %.2f\n",n,sum);
}
