/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 class Solution {
 public:
  ListNode* rotateRight(ListNode* head, int k) {
    if (head == nullptr || k == 0) return head;
    int n = 1;
    ListNode* cur = head;
    for (ListNode* cur = head; cur->next; cur = cur->next, ++n);
    k %= n;
    if (k == 0) return head;
    ListNode *slow = head, *fast = head;
    while (k-- > 0 && fast->next) fast = fast->next;
    while (fast->next) {
      slow = slow->next;
      fast = fast->next;
    }
    ListNode* ret = slow->next;
    slow->next = fast->next;
    fast->next = head;
    return ret;
  }
 };