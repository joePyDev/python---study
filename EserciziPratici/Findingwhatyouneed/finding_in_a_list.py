import pandas as pd

# importa il catalogo
book_catalog_df = pd.read_csv("book_catalog_10.csv")

book_catalog = book_catalog_df.to_dict(orient="records")


# helper function 1
def get_title(book):
    """Helper function to extract the title from a book dictionary."""
    return book["title"]


# helper function 2
def sort_catalog_by_title(catalog):
    """Sorts the book catalog alphabetically by title."""
    catalog.sort(key=get_title)


# Sort the catalog
sort_catalog_by_title(book_catalog)


# Display the sorted catalog
for book in book_catalog:
    print(
        f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}"
    )


# helper function: linear search
def search_books(catalog, query):
    """Searches for books by title or author using linear search."""
    results = []
    for book in catalog:
        if (
            query.lower() in book["title"].lower()
            or query.lower() in book["author"].lower()
        ):
            results.append(book)
    return results


query = "Dune"
search_results = search_books(book_catalog, query)


if search_results:
    print("\nSearch results:")
    for book in search_results:
        print(
            f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}"
        )
else:
    print("No books found matching your query.")


def binary_search_books(catalog, query):
    """Searches for books by title using binary search (assuming sorted catalog)."""
    low = 0
    high = len(catalog) - 1

    while low <= high:
        mid = (low + high) // 2
        if catalog[mid]["title"].lower() == query.lower():
            return catalog[mid]
        elif catalog[mid]["title"].lower() < query.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None  # Book not found


# This is like using a stopwatch to see how long it takes to find the books.
# We start the timer, do the search, then stop the timer and calculate how much time passed.
import time

# Loads the big_book_catalog which has which has ~271,380 rows!
big_book_catalog_df = pd.read_csv("big_book_catalog.csv", low_memory=False)

# Convert 'title' and 'author' to strings, handle NaN
big_book_catalog_df["title"] = big_book_catalog_df["title"].fillna("").astype(str)
big_book_catalog_df["author"] = big_book_catalog_df["author"].fillna("").astype(str)

sorted_df = big_book_catalog_df.sort_values(by=["title"])
big_book_catalog = big_book_catalog_df.to_dict(orient="records")

# Search for "The Great Gatsby" using Linear Search
query = "The Great Gatsby"  # Example query

start_time = time.time()  # Record start time

search_results = search_books(big_book_catalog, query)

end_time = time.time()  # Record end time

elapsed_time_linear = end_time - start_time
print(f"\nLinear search took {elapsed_time_linear:.5f} seconds.")

if search_results:
    print("\nSearch results:")
    for book in search_results:
        print(
            f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}"
        )
else:
    print("No books found matching your query.")


# This is like using a stopwatch to see how long it takes to find the books.
# We start the timer, do the search, then stop the timer and calculate how much time passed.
import time

# Loads the big_book_catalog which has which has ~271,380 rows!
big_book_catalog_df = pd.read_csv("big_book_catalog.csv", low_memory=False)

# Convert 'title' and 'author' to strings, handle NaN
big_book_catalog_df["title"] = big_book_catalog_df["title"].fillna("").astype(str)
big_book_catalog_df["author"] = big_book_catalog_df["author"].fillna("").astype(str)

sorted_df = big_book_catalog_df.sort_values(by=["title"])
big_book_catalog = sorted_df.to_dict(orient="records")

# Search for "The Great Gatsby" using Binary Search
query = "The Great Gatsby"  # Example query

start_time = time.time()

search_results = binary_search_books(big_book_catalog, query)

elapsed_time_binary = time.time() - start_time

print(f"\nBinary search took {elapsed_time_binary:.5f} seconds.")

if search_results:
    print("\nBinary Search Result for 'The Great Gatsby':")
    print(
        f"Title: {search_results['title']}, Author: {search_results['author']}, Publication Year: {search_results['publication_year']}"
    )
else:
    print("Binary Search: Book not found")
