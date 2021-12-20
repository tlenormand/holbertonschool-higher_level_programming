#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: list address
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 * Description: check if endless listint_t linked list exist
 */

int check_cycle(listint_t *list)
{
	listint_t *search = list, *start = list;

	while (search && search->next)
	{
		while (start != search && start != search->next)
			start = start->next;
		if (start == search->next)
			return (1);
		start = list;
		search = search->next;
	}

	return (0);
}
