/*Suppose that you are given a list of integers stored in consecutive memory locations(arrays). Perform the following operations. (Note : Use pointers)
a.	Create an array of N Integer Elements by allocating memory dynamically
b.	Display of array Elements with Suitable Headings
c.	Insert an Element (ELEM) at a given valid Position (POS)
d.	Delete an Element at a given valid Position (POS)
e.	Search an element in the array  */


#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n, i, choice, pos, x, key, found;

    // Input size
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Allocate memory
    arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Input elements
    printf("Enter the elements: ");
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    // Display elements
    printf("The elements of the array are:\n");
    for (i = 0; i < n; i++)
        printf("arr[%d] = %d\n", i, arr[i]);

    // Menu loop
    while (1) {
        printf("\n1 -> INSERT  2 -> DELETE  3 -> SEARCH  4 -> UPDATE  5 -> EXIT\n");
        printf("Give your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1: // Insert
            printf("Enter the element to be inserted: ");
            scanf("%d", &x);
            printf("Enter the position to be inserted: ");
            scanf("%d", &pos);

            if (pos < 1 || pos > n + 1) {
                printf("Invalid position!\n");
                break;
            }

            arr = (int *)realloc(arr, (n + 1) * sizeof(int));
            if (arr == NULL) {
                printf("Memory reallocation failed!\n");
                return 1;
            }

            for (i = n; i >= pos; i--)
                arr[i] = arr[i - 1];
            arr[pos - 1] = x;
            n++;

            printf("After insertion the elements are:\n");
            for (i = 0; i < n; i++)
                printf("arr[%d] = %d\n", i, arr[i]);
            break;

        case 2: // Delete
            printf("Enter the position of the element to be deleted: ");
            scanf("%d", &pos);

            if (pos < 1 || pos > n) {
                printf("Invalid position!\n");
                break;
            }

            for (i = pos; i < n; i++)
                arr[i - 1] = arr[i];
            n--;

            arr = (int *)realloc(arr, n * sizeof(int));
            if (n > 0 && arr == NULL) {
                printf("Memory reallocation failed!\n");
                return 1;
            }

            printf("After deletion the elements are:\n");
            for (i = 0; i < n; i++)
                printf("arr[%d] = %d\n", i, arr[i]);
            break;

        case 3: // Search
            found = 0;
            printf("Enter the element to be searched: ");
            scanf("%d", &key);

            for (i = 0; i < n; i++) {
                if (arr[i] == key) {
                    found = 1;
                    printf("Search key %d found at position %d\n", key, i + 1);
                }
            }
            if (!found)
                printf("Search key %d is not found\n", key);
            break;

        case 4: // Update
            printf("Enter the position to update: ");
            scanf("%d", &pos);

            if (pos < 1 || pos > n) {
                printf("Invalid position!\n");
                break;
            }

            printf("Enter the new value: ");
            scanf("%d", &x);

            arr[pos - 1] = x;

            printf("After update the elements are:\n");
            for (i = 0; i < n; i++)
                printf("arr[%d] = %d\n", i, arr[i]);
            break;

        case 5: // Exit
            free(arr);
            printf("Exiting program...\n");
            return 0;

        default:
            printf("Invalid choice!\n");
        }
    }

    return 0;
}
