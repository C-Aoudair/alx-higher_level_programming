#include "lists.h"


/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 1 if there is a cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr1 = list->next;
	ptr2 = list->next->next;

	while (ptr1 && ptr2 && ptr2->next)
	{
		if (ptr1 == ptr2)
			return (1);

		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
	}

	return (0);
}
