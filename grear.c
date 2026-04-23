#include <stdio.h>
void main()
{
    int a;
    int b;
    int c;
    int d;
    printf("enter the numbers NIGGA");
    scanf("%d%d%d%d", &a, &b, &c, &d);
    if (a > b)
    {
        if (a > c)
        {
            if (a > d)
            {
                printf("a is greater");
            }
        }
    }
    else if (b > c)
    {
        if (b > d)
        {
            printf("b is greeater");
        }
    }
    else if (c > d)
    {
        printf(" c is greatest");
    }
    else
    {
        printf("d is greatest");
    }
}
