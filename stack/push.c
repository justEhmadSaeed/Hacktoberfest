#include <stdio.h>
#include <stdlib.h>
#define max 5
int arr[max];
int top = 0;
void push(int element)
{
    if (top == 5)
    {
        printf("stack is full \n");
        return;
    }

    arr[top] = element;
    top++;
}

void display()
{
    int count = 0;
    printf("\n the elements are : ");

    while (count != top)
    {
        printf(" %d ", arr[count]);

        count++;
    }
}
int main()
{

    printf("enter the number of elements u want to insert : ");

    int loop, element;
    ;
    scanf("%d", &loop);

    for (int i = 0; i < loop; i++)
    {

        printf("enter the element : ");

        scanf("%d", &element);

        push(element);
    }

    display();
}