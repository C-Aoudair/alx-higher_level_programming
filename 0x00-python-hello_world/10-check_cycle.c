#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle int it.
 * @list: The list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	for (current = list->next; current != NULL; current = current->next)
	{
		if (current == list)
			return (1);
	}

	return (0);
}
