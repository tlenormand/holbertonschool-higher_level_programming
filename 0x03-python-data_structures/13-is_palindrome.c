#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *end = *head;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	return (check_palindrome(&end, end));
}


/**
 * check_palindrome - check if a singly linked list is a palindrome recursively
 * @head: pointer to head of list
 * @end: pointer to head of list using to go to the end recursively
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int check_palindrome(listint_t **head, listint_t *end)
{
	int palindrome = 0;

	if (end->next != NULL)
		check_palindrome(head, end->next);

	if ((*head)->n == end->n)
	{
		*head = (*head)->next;
		palindrome = 1;
		return (palindrome);
	}

	*head = (*head)->next;
	return (palindrome);
}
