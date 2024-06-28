from prettytable import PrettyTable
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_results(search_term, search_type, hits):
    print(f"{Fore.GREEN}{Style.BRIGHT}Search Results for '{search_term}' ({search_type} Search):{Style.RESET_ALL}")
    
    table = PrettyTable()
    table.field_names = [f"{Fore.YELLOW}Title{Style.RESET_ALL}", f"{Fore.YELLOW}Content{Style.RESET_ALL}", f"{Fore.YELLOW}Score{Style.RESET_ALL}"]

    seen_titles = set()
    for hit in hits:
        title = hit['_source']['title']
        content = hit['_source']['content']
        score = hit['_score']

        if title not in seen_titles:
            seen_titles.add(title)
            table.add_row([f"{Fore.CYAN}{title}{Style.RESET_ALL}", content, f"{Fore.MAGENTA}{score:.4f}{Style.RESET_ALL}"])

    print(table)
