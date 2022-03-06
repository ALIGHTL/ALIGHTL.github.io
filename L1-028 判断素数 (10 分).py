#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int sushu(int n)
{
    int i;
    if (n == 1)
    {
        return 0;
    }
    for (i = 2; i <= sqrt(n); i++)
    {
        if (n%i == 0)
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    int a, b, c;
    scanf("%d", &a);
    for (b = 0; b < a; b++)
    {
        scanf("%d", &c);
        if (sushu(c))
            printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}
