/*You are assigned the task to design a browser history where a person can visit any page and go backward or forward in browser history in any number of steps. Suppose we have to go forward x steps, but we can go only y(where y<x) steps forward because of the last Node, then we return the last node. Similarly, we will return the first node while traveling back.

Design and implement a menu driven Program in C to implement the above operations using Doubly Linked List.
*/
#include<stdio.h>
#include<stdlib.h>


struct node
{
int page;
struct node *left;
struct node *right;
};


typedef struct node *NODEPTR;
NODEPTR list=NULL;


NODEPTR createlist(NODEPTR list,int page);
NODEPTR moveforward(NODEPTR list, int cp ,int steps);
NODEPTR movebackward(NODEPTR list, int cp, int steps);
void display();
NODEPTR getnode();

NODEPTR createlist(NODEPTR list, int page)
{
	NODEPTR p,q;
	p=getnode();
	p->page=page;
	p->left=NULL;
	p->right=NULL;
	if(list==NULL)
		list=p;
	else{
		for(q=list; q->right!=NULL; q=q->right)
		;
		q->right=p;
		p->left=q;

	}
	return(list);
}

	
NODEPTR moveforward(NODEPTR list, int cp,int steps)
{
	NODEPTR p,q;
 	int count=0,s;
	if(list==NULL)
		printf("\n Empty list");
	else{
		p=list;
                for(p=list,count=0;count<cp-1; count++)
                  p=p->right;
             
                for(q=p,s=0;s<steps;s++)
                 {
                    if(q->right==NULL)
		    	return(q);
		    q=q->right;
 		   }
                 return(q);
}
}

NODEPTR movebackward(NODEPTR list, int cp,int steps)
{
	NODEPTR p,q;
 	int count=0,s;
	if(list==NULL)
		printf("\n Empty list");
	else{
		p=list;
                for(p=list,count=0;count<cp-1; count++)
                  p=p->right;
             
                for(q=p,s=0;s<steps;s++)
                 {
                    if(q->left==NULL)
		            	return(q);
		           q=q->left;
 		   }
                 return(q);
    }
}


void display(NODEPTR list)
{
	NODEPTR p;
	p=list;
	if(p==NULL)
		printf("\nEmpty list");
	else
	{
		printf("\n The page list contains: ");
		for(p=list;p!=NULL;p=p->right) 
		{
			printf("%d<->",p->page);
		}
	}
}

NODEPTR getnode()
{
	NODEPTR r;
	r=(NODEPTR)malloc(sizeof(struct node));
	if(r==NULL)
	{
		printf("\n Node allocation failed");
		exit(0);
	}
	return(r);
}


void main()
{
		int page,choice,steps,cp;
 		char cont;
		NODEPTR p;
		do{
		printf("\n ...........MENU...........");
		printf("\n 1->CREATE LIST\t  2->MOVE FORWARD\t  3->MOVE BACKWARD\t 4->DISPLAY 5->EXIT");
		printf("\n Enter your choice");
		scanf("%d",&choice);
		switch(choice)
		{
		case 1:printf("\n CREATION OF DOUBLY LINKED LIST OF PAGES IS IN PROGRESS:\n");
			do{
              	        	  printf("Enter a page number:");
                        	  scanf("%d",&page);
              	 	 	  list = createlist(list,page);
              	 		  printf("Do you want to enter another page[Y/N]:");
               	 		  scanf(" %c",&cont);
              		 }while(cont=='Y' || cont=='y');
               		  display(list); 
			  break;
		 	
		case 2: printf("\n MOVE FORWARD:\n");
			printf("\nEnter the current page:");
                        scanf("%d",&cp);
			printf("Enter the number of steps to move forward");
			scanf("%d",&steps);
			p=moveforward(list,cp,steps);
			printf("\n Moved forward to  page %d from %dth page",p->page, cp);
			break;
		case 3: printf("\n MOVE BACKWARD:\n");
			printf("\nEnter the current page:");
                        scanf("%d",&cp);
			printf("Enter the number of steps to move backward");
			scanf("%d",&steps);
			p=movebackward(list,cp,steps);
			printf("\n Moved backwards to  page %d from %dth page",p->page, cp);
			break;
		case 4: display(list);
		        break;
		case 5:printf("\n Quitting operation List.....\n");
			break;
		default:printf("\n Invalid choice");
			break;
		}		
	}while(choice!=5);
}



sample output
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice1

 CREATION OF DOUBLY LINKED LIST OF PAGES IS IN PROGRESS:
Enter a page number:10
Do you want to enter another page[Y/N]:y
Enter a page number:20
Do you want to enter another page[Y/N]:y
Enter a page number:30
Do you want to enter another page[Y/N]:y
Enter a page number:40
Do you want to enter another page[Y/N]:y
Enter a page number:50
Do you want to enter another page[Y/N]:y
Enter a page number:60
Do you want to enter another page[Y/N]:n

 The page list contains: 10<->20<->30<->40<->50<->60<->
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice2

 MOVE FORWARD:

Enter the current page:3
Enter the number of steps to move forward3

 Moved forward to  page 60 from 3th page
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice
2

 MOVE FORWARD:

Enter the current page:5
Enter the number of steps to move forward4

 Moved forward to  page 60 from 5th page
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice3

 MOVE BACKWARD:

Enter the current page:4
Enter the number of steps to move backward3

 Moved backwards to  page 10 from 4th page
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice3

 MOVE BACKWARD:

Enter the current page:3
Enter the number of steps to move backward5 

 Moved backwards to  page 10 from 3th page
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice4

 The page list contains: 10<->20<->30<->40<->50<->60<->
 ...........MENU...........
 1->CREATE LIST   2->MOVE FORWARD         3->MOVE BACKWARD       4->DISPLAY 5->EXIT
 Enter your choice
5

 Quitting operation List.....
*/
#include <stdio.h>
#include <stdlib.h>

// Define the structure for the doubly linked list node
struct node {
    int page;           // To store the page number
    struct node *left;  // Pointer to the previous node
    struct node *right; // Pointer to the next node
};

// Typedef for node pointer
typedef struct node *NODEPTR;
NODEPTR list = NULL; // Initialize the list as NULL

// Function prototypes
NODEPTR createlist(NODEPTR list, int page);
NODEPTR moveforward(NODEPTR list, int cp, int steps);
NODEPTR movebackward(NODEPTR list, int cp, int steps);
void display(NODEPTR list);
NODEPTR getnode();

NODEPTR createlist(NODEPTR list, int page) {
    NODEPTR p, q;
    p = getnode();
    p->page = page;
    p->left = NULL;
    p->right = NULL;

    // If the list is empty, make the new node the head of the list
    if (list == NULL)
        list = p;
    else {
        // Traverse to the end of the list and link the new node
        for (q = list; q->right != NULL; q = q->right)
            ;
        q->right = p;
        p->left = q;
    }
    return list;
}

NODEPTR moveforward(NODEPTR list, int cp, int steps) {
    NODEPTR p, q;
    int count = 0, s;
    
    if (list == NULL) {
        printf("\n Empty list");
        return NULL;
    } else {
        p = list;
        
        // Traverse to the cp-th page (current page)
        for (p = list, count = 0; count < cp - 1; count++)
            p = p->right;
        
        // Move forward for the specified number of steps
        for (q = p, s = 0; s < steps; s++) {
            if (q->right == NULL)  // If we reach the last page, return it
                return q;
            q = q->right;
        } 
        return q;
    }
}

NODEPTR movebackward(NODEPTR list, int cp, int steps) {
    NODEPTR p, q;
    int count = 0, s;
    
    if (list == NULL) {
        printf("\n Empty list");
        return NULL;
    } else {
        p = list;
        
        // Traverse to the cp-th page (current page)
        for (p = list, count = 0; count < cp - 1; count++)
            p = p->right;
        
        // Move backward for the specified number of steps
        for (q = p, s = 0; s < steps; s++) {
            if (q->left == NULL)  // If we reach the first page, return it
                return q;
            q = q->left;
        }
        return q;
    }
}

void display(NODEPTR list) {
    NODEPTR p;
    p = list;
    if (p == NULL) {
        printf("\n Empty list");
    } else {
        printf("\n The page list contains: ");
        for (p = list; p != NULL; p = p->right) {
            printf("%d<->", p->page);
        }
    }
}

NODEPTR getnode() {
    NODEPTR r;
    r = (NODEPTR)malloc(sizeof(struct node));
    if (r == NULL) {
        printf("\n Node allocation failed");
        exit(0);
    }
    return r;
}

void main() {
    int page, choice, steps, cp;
    char cont;
    NODEPTR p;

    do {
        printf("\n ...........MENU...........");
        printf("\n 1->CREATE LIST\t  2->MOVE FORWARD\t  3->MOVE BACKWARD\t 4->DISPLAY 5->EXIT");
        printf("\n Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            printf("\n CREATION OF DOUBLY LINKED LIST OF PAGES IS IN PROGRESS:\n");
            do {
                printf("Enter a page number: ");
                scanf("%d", &page);
                list = createlist(list, page);
                printf("Do you want to enter another page [Y/N]: ");
                scanf(" %c", &cont);
            } while (cont == 'Y' || cont == 'y');
            display(list);
            break;

        case 2:
            printf("\n MOVE FORWARD:\n");
            printf("\nEnter the current page (1-based index): ");
            scanf("%d", &cp);
            printf("Enter the number of steps to move forward: ");
            scanf("%d", &steps);
            p = moveforward(list, cp, steps);
            if (p != NULL)
                printf("\nMoved forward to page %d from %d-th page", p->page, cp);
            break;

        case 3:
            printf("\n MOVE BACKWARD:\n");
            printf("\nEnter the current page (1-based index): ");
            scanf("%d", &cp);
            printf("Enter the number of steps to move backward: ");
            scanf("%d", &steps);
            p = movebackward(list, cp, steps);
            if (p != NULL)
                printf("\nMoved backwards to page %d from %d-th page", p->page, cp);
            break;

        case 4:
            display(list);
            break;

        case 5:
            printf("\n Quitting operation List.....\n");
            break;

        default:
            printf("\n Invalid choice");
            break;
        }

    } while (choice != 5);
}

  



