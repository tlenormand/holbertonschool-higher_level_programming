#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of the linked list
 * @number: number to insert
 * Return: new address or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (current == NULL || current->n >= number)
	{
		new->next = new;
		*head = new;
		return (new);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;
	return (new);
}
