from model_loader.model_loader import load_model
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_load_model():
    try:
        model_name = "bert-base-uncased"
        model = load_model(model_name)
        assert model is not None
        print(f"{Fore.GREEN}Model loading test succeeded.{Style.RESET_ALL}")
        return True
    except AssertionError:
        print(f"{Fore.RED}Model loading test failed.{Style.RESET_ALL}")
        return False

model_loader_tests = {
    "Load Model": test_load_model,
}
