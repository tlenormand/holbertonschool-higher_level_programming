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

	if (*head == NULL || number < (*head)->n)
	{
		add_nodeint(head, number);
		return (*head);
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (current == NULL || current->n >= number)
	{
		new->next = new;
		*head = new;

		return (new);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new->n = number;
	new->next = current->next;
	current->next = new;

	return (new);
}


/**
* add_nodeint - adding a new node at the beginning of the linked list
* @head: addres of the linked list
* @n: value to add to the linked list
* Return: address of the new node
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
