#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle int it.
 * @list: The list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t **nodes = NULL;
	int i, j;

	/*if (list == NULL)
		return (0);

	if (list->next == list)
		return (1);

	for (head = list; head != NULL; head = head->next)
		for (curt = list; curt != head; curt = curt->next)
			if (head->next == curt)
				return (1);*/
	i = 0;
	while (list)
	{
		nodes = realloc(nodes, (i + 1) * sizeof(listint_t));
		for (j = 0; j < i; j++)
			if (list == nodes[j])
			{
				free(nodes);
				return (1);
			}
		nodes[i] = list;
		list = list->next;
		i++;
	}
	free(nodes);

	return (0);
}
