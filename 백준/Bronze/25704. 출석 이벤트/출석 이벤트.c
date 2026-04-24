//포인터 연습
#include <stdio.h>

int main(void)
{
    int n, p;
    scanf("%d", &n);
    scanf("%d", &p);
    
    int stamp[4] = {5, 10, 15, 20};
    int discount[4] = { 500, 10, 2000, 25 };
    char type[4] = { 'w', 'p', 'w', 'p' };

    int min = p;
    for (int i = 0; i < 4; i++)
    {
        if (n >= stamp[i])
        {
            int price;
            int *ptr_price = &price;

            if (type[i] == 'w')
            {
                *ptr_price = p - discount[i];
            }
            else
            {
                *ptr_price = p - (p * discount[i] / 100);
            }
            if (*ptr_price < 0) *ptr_price = 0;
            if (*ptr_price < min) min = *ptr_price;
        }
    }
    printf("%d \n", min);
    return 0;
}