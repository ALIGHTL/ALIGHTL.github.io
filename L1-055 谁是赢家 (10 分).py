#include<stdio.h>
int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    int c,d,e;
    scanf("%d %d %d",&c,&d,&e);
    if (a>b)
    {
        if (c+d+e<3)
        {
            printf("The winner is a: %d + %d\n",a,3-(c+d+e));
        }
        else
        {
            printf("The winner is b: %d + 3\n",b);
        }
    }
    else if (a<b)
    {
        if (c+d+e>0)
        {
            printf("The winner is b: %d + %d\n",b,c+d+e);
        }
        else
        {
            printf("The winner is a: %d + 3\n",a);
        }
    }
    return 0;
}
