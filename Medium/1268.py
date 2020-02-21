"""
    Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
    
    Return list of lists of the suggested products after each character of searchWord is typed.
    """
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products = sorted(products)
        
        word = ""
        output = []
        i = 0
        
        for k,x in enumerate(searchWord):
            word += x
            i = bisect.bisect_left(products,word,i)
            currentSuggestion = [w for w in products[i:i+3] if w.startswith(word)]
            output.append(currentSuggestion)
        
        return output

