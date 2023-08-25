#include<stdio.h>
void main()
{
    int age;
    printf("Please Enter the Age: ");
    scanf("%d",&age);
    if(age>=18)
    {
        printf("Your Eligible to Vote");
    }
    else
    {
        printf("Sorry, Your are not eligible Vote");
    }
}
