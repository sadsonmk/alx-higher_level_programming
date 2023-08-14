#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: is a double pointer to the beginning of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *behind = *head, *ahead = *head;
	listint_t *prev = NULL, *current = NULL, *next = NULL;
	listint_t *one = NULL, *two = NULL;

	while (ahead && ahead->next)
	{
		behind = behind->next;
		ahead = ahead->next->next;
	}
	current = behind;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	one = *head;
	two = prev;
	while (one && two)
	{
		if (one->n != two->n)
			return (0);
		one = one->next;
		two = two->next;
	}

	return (1);
}
