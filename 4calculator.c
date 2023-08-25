#include<stdio.h>
void main()
{
    int num1, num2, ch;
    printf("Enter the First Number: ");
    scanf("%d",&num1);
    printf("Enter the Second Number: ");
    scanf("%d",&num2);
    printf("1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Mod \n6.Exit \nEnter the Option: ");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1:
        printf("The Addition of %d and %d is: %d",num1,num2,num1+num2);
        break;
    case 2:
        printf("The Substraction of %d and %d is: %d",num1,num2,num1-num2);
        break;
    case 3:
        printf("The Mulplication of %d and %d is: %d",num1,num2,num1*num2);
        break;
    case 4:
        if(num2==0){
            printf("For Division the denomenator cannot be Zero");
        }
        else{
             printf("The Division of %d and %d is: %d",num1,num2,num1/num2);
        }
        break;
    case 5:
        printf("The Mod of %d and %d is: %d",num1,num2,num1%num2);
        break;
    case 6:
        break;
    default:
        printf("Invalid Choice");
    }
}
