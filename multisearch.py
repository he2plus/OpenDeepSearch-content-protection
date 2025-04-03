def find_connections(query, max_depth=2):
    """Simplified version for better understanding"""
    results = []
    current_query = query
    
    for _ in range(max_depth):
        # Basic implementation
        new_results = search(current_query)
        results.extend(new_results)
        
        # Simple term extraction
        new_terms = list(set(
            word.lower() for word in current_query.split() 
            if len(word) > 3
        ))
        current_query += " " + " ".join(new_terms[:3])
    
    return results
