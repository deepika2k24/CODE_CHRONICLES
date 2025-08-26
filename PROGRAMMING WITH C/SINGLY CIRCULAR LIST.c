/*Design, Develop and Implement a Program in C for the following operations on Singly Circular Linked List (SCLL) with header nodes
a.	Represent a Polynomial of the form P(x,y,z) = 6x2 y 2 z-4 yz5 +3x3 yz+2xy5 z-2xyz3
b.	Evaluate the polynomial
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Node structure for SCLL
struct node {
    int coefficient;
    int x_power;
    int y_power;
    int z_power;
    struct node* next;
};
typedef struct node *NODEPTR;

// Function prototypes
NODEPTR createNode(int coeff, int x, int y, int z);
NODEPTR insertEnd(NODEPTR list, int coeff, int x, int y, int z);
void displayPolynomial(NODEPTR list);
double evaluatePolynomial(NODEPTR list, double x, double y, double z);

// Create a new node
NODEPTR createNode(int coeff, int x, int y, int z) 
{
    NODEPTR p= (NODEPTR)malloc(sizeof(struct node *));
    p->coefficient = coeff;
    p->x_power = x;
    p->y_power = y;
    p->z_power = z;
    p->next = p; // Self-loop for circular nature
    return p;
}

// Insert a node at the end of the SCLL
NODEPTR insertEnd(NODEPTR list, int coeff, int x, int y, int z) {
    NODEPTR p= createNode(coeff, x, y, z);
    if (list == NULL) {
        list = p;
    } else {
        NODEPTR q = list;
        while (q->next != list) {
            q = q->next;
        }
        q->next = p;
        p->next = list;
    }
    return list;
}

// Display the polynomial
void displayPolynomial(NODEPTR list) {
    if (list == NULL) {
        printf("Polynomial is empty.\n");
        return;
    }
    NODEPTR p= list;
    do {
        printf("%dx^%dy^%dz^%d ", p->coefficient, p->x_power, p->y_power, p->z_power);
        p = p->next;
    } while (p != list);
    printf("\n");
}

// Evaluate the polynomial for given x, y, and z values
double evaluatePolynomial(NODEPTR list, double x, double y, double z) 
{
    double result = 0.0;
    if (list == NULL) 
 {
        return result;
    }
NODEPTR q = list;
    do {
        result = result += q->coefficient * pow(x, q->x_power) * pow(y, q->y_power) * pow(z, q->z_power);
        q = q->next;
    } while (q != list);
    return result;
}

// Main function
int main() {
    NODEPTR poly = NULL;

    // Represent the polynomial P(x,y,z) = 6x^2y^2z - 4yz^5 + 3x^3yz + 2xy^5z - 2xyz^3
    poly= insertEnd(poly, 6, 2, 2, 1);
    poly = insertEnd(poly, -4, 0, 1, 5);
 //   poly = insertEnd(poly, 3, 3, 1, 1);
  //  poly = insertEnd(poly, 2, 1, 5, 1);
//  poly= insertEnd(poly, -2, 1, 1, 3);

    // Display the polynomial
    printf("Polynomial: ");
    displayPolynomial(poly);

    // Evaluate the polynomial
    double x, y, z;
    printf("\nEnter values for x, y, z: ");
    scanf("%lf %lf %lf", &x, &y, &z);

    double result = evaluatePolynomial(poly, x, y, z);
    printf("Result of evaluation: %.2lf\n", result);
    return 0;
}


/**Smple output
Enter values for x, y, z: 1 2 3
Polynomial: +6x^2y^2z^1 -4x^0y^1z^5 +3x^3y^1z^1 +2x^1y^5z^1 -2x^1y^1z^3 
Result of evaluation: ------