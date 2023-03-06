#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle is 0.
 *         If there is a cycle is 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *x;

	if (list == NULL || list->next == NULL)
		return (0);

	a = list->next;
	x = list->next->next;

	while (a && x && x->next)
	{
		if (a == x)
			return (1);

		a = a->next;
		x = x->next->next;
	}

	return (0);
}

