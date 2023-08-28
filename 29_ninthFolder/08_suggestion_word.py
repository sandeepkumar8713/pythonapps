# https://leetcode.com/problems/search-suggestions-system/
# Similar : 14_trie/05_auto_complete
# Question : You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord
# is typed. Suggested products should have common prefix with searchWord. If there are more than three products
# with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.
#
# Example : Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
#
# Question Type : Asked
# Used : Optimal solution is to use Trie with DFS but this one much easier.
#        Sort the products.
#        Do binary search in the product list for the search word.
#        From the returned index, pick next 3 item in the list
# Logic: products.sort()
#        res, prefix, i = [], '', 0
#        for c in searchWord:
#           prefix += c
#           i = bisect.bisect_left(products, prefix, i)
#           res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
#        return res
# Complexity : O(n log n) + O(m log n) where n is count of products and m is length of search word.

import bisect


def suggestedProducts(products, searchWord):
    products.sort()
    res, prefix, i = [], '', 0
    for c in searchWord:
        prefix += c
        i = bisect.bisect_left(products, prefix, i)
        res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
    return res


if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))
