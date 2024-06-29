import json
import os
from config.config_utils import get_config, get_model_name
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_get_config():
    try:
        config_path = "config/config.json"
        config_data = {
            "search_type": "keyword",
            "model_name": "bert-base-uncased"
        }

        # Ensure the config directory exists
        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        # Write the test config data to the config file
        with open(config_path, "w") as config_file:
            json.dump(config_data, config_file)

        config = get_config()
        assert config["search_type"] == "keyword"
        assert config["model_name"] == "bert-base-uncased"
        print(f"{Fore.GREEN}Configuration loading test succeeded.{Style.RESET_ALL}")
        return True
    except AssertionError:
        print(f"{Fore.RED}Configuration loading test failed.{Style.RESET_ALL}")
        return False

def test_get_model_name():
    try:
        config_path = "config/config.json"
        config_data = {
            "search_type": "keyword",
            "model_name": "bert-base-uncased"
        }

        # Ensure the config directory exists
        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        # Write the test config data to the config file
        with open(config_path, "w") as config_file:
            json.dump(config_data, config_file)

        model_name = get_model_name()
        assert model_name == "bert-base-uncased"
        print(f"{Fore.GREEN}Get model name test succeeded.{Style.RESET_ALL}")
        return True
    except AssertionError:
        print(f"{Fore.RED}Get model name test failed.{Style.RESET_ALL}")
        return False

config_tests = {
    "Load Configuration": test_get_config,
    "Get Model Name": test_get_model_name,
}
