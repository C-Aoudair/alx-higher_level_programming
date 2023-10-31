#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *  * main - check the code for Holberton School students.
 *   *
 *    * Return: Always 0.
 *     */
int main(void)
{
		listint_t *head;

			head = NULL;
				add_nodeint(&head, 98);
					print_listint(head);

						head->next = head;

							if (check_cycle(head) == 0)
										printf("Linked list has no cycle\n");
								else if (check_cycle(head) == 1)
											printf("Linked list has a cycle\n");

									head->next = NULL;

										free_listint(head);

											return (0);
}
