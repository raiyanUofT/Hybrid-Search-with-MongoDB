from test_runner import run_tests, summarize_results
from test_mongodb import mongodb_tests
from test_elasticsearch import elasticsearch_tests

if __name__ == "__main__":
    all_tests = {
        **mongodb_tests,
        **elasticsearch_tests,
        # Add other tests here in the future
    }

    results = run_tests(all_tests)
    summarize_results(results)
