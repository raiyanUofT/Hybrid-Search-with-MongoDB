from prettytable import PrettyTable
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_results(search_term, search_type, hits):
    # Display search information
    print(f"{Fore.GREEN}{Style.BRIGHT}Search Term:{Style.RESET_ALL} {search_term}")
    print(f"{Fore.GREEN}{Style.BRIGHT}Search Type:{Style.RESET_ALL} {search_type}")

    # Create a PrettyTable to display results
    table = PrettyTable()
    table.field_names = ["Title", "Content", "Score"]

    # Populate the table with results
    for hit in hits:
        source = hit['_source']
        score = hit['_score']
        table.add_row([source['title'], source['content'], f"{score:.4f}"])

    # Print the table
    print(table)
