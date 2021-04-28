#include "lists.h"
#include "stdlib.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: pointer to head of list.
 * @number: the value to insert.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currentNode, *newNode;

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (0);
	newNode->n = number;

	if (*head == NULL || (*head)->n >= newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	currentNode = *head;

	while (currentNode->next && currentNode->next->n < newNode->n)
	{
		currentNode = currentNode->next;
	}

	newNode->next = currentNode->next;
	currentNode->next = newNode;
	return (newNode);
}