# coffee-shop-challenge

This project is a coffee shop management system implemented in Python. It includes modules for managing customers, coffee orders, and related functionality.

## Installation

Make sure you have Python installed (version 3.x recommended).

You can install any dependencies using:

```bash
pip install -r requirements.txt
```

(Note: If you are using Pipenv, you can run `pipenv install` instead.)

## Running Tests

The tests are located in the `tests` directory. The test files are named with the pattern `*_test.py`.

To run all tests, use the following command:

```bash
python -m unittest discover -s tests -p "*_test.py"
```

This command discovers and runs all tests matching the pattern in the `tests` folder.

### Additional Test Information

- The tests cover the core functionality of the coffee shop system, including the Coffee, Customer, and Order classes.
- Each test file contains multiple test cases verifying initialization, properties, and behavior of the classes.
- Running the tests with the above command will execute all 16 test cases currently implemented.
- Ensure you run the command from the root directory of the project where the `tests` folder is located.
- If you add new test files, follow the naming pattern `*_test.py` to ensure they are discovered automatically.

## Project Structure

- `coffee.py`: Coffee related classes and logic
- `customer.py`: Customer related classes and logic
- `order.py`: Order related classes and logic
- `tests/`: Contains unit tests for the project modules

## Contributing

Feel free to fork the repository and submit pull requests.
