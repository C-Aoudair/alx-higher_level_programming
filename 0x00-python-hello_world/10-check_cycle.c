#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle int it.
 * @list: The list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *curt;
	listint_t *head;

	if (list == NULL)
		return (0);

	for (head = list; head != NULL; head = head->next)
		for (curt = head; curt != NULL; curt = curt->next)
		{
			if (curt == head)
				return (1);
		}

	return (0);
}
