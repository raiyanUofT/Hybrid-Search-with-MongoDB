from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def run_tests(test_functions):
    results = {}

    for test_name, test_func in test_functions.items():
        try:
            result = test_func()
            results[test_name] = result
            if result:
                print(f"{Fore.GREEN}{test_name} passed.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{test_name} failed.{Style.RESET_ALL}")
        except Exception as e:
            results[test_name] = False
            print(f"{Fore.RED}{test_name} failed with exception: {e}{Style.RESET_ALL}")

    return results

def summarize_results(results):
    passed = sum(result for result in results.values() if result is not None)
    failed = len(results) - passed

    print("\nTest Summary:")
    for test, result in results.items():
        if result:
            print(f"{Fore.GREEN}{test} passed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{test} failed.{Style.RESET_ALL}")
    
    # Print aggregate statistics
    total_tests = len(results)
    print(f"\n{Fore.CYAN}Aggregate Statistics:{Style.RESET_ALL}")
    print(f"Total tests: {total_tests}")
    print(f"{Fore.GREEN}Passed: {passed}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed: {failed}{Style.RESET_ALL}")

if __name__ == "__main__":
    from test_mongodb import mongodb_tests
    from test_elasticsearch import elasticsearch_tests
    from test_config import config_tests
    from test_model_loader import model_loader_tests
    from test_search_algorithms import search_algorithms_tests

    all_tests = {
        **mongodb_tests,
        **elasticsearch_tests,
        **config_tests,
        **model_loader_tests,
        **search_algorithms_tests,
        # Add other tests here in the future
    }

    results = run_tests(all_tests)
    summarize_results(results)
