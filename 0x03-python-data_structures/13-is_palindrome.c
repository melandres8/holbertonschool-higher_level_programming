#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *prev, *fast = *head, *sl = *head;

	for (; fast != NULL && fast->next != NULL;)
	{
		fast = fast->next->next;
		sl = sl->next;
	}
	current = sl;
	prev = NULL;
	while (current)
	{
		fast = current->next;
		current->next = prev;
		prev = current;
		current = fast;
	}
	fast = *head;
	current = prev;
	while (prev)
	{
		if (fast->n != prev->n)
			break;
		fast = fast->next;
		prev = prev->next;
	}
	prev = NULL;
	while (current)
	{
		fast = current->next;
		current->next = prev;
		prev = current;
		current = fast;
	}
	return (0);
}
