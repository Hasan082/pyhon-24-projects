# Public API Project Using Flask

This is a simple Flask-based public API project hosted on PythonAnywhere.

## Main Site
Access the main site [here](https://hasan082.pythonanywhere.com/).

## Endpoints

### Random Endpoint
Retrieve a random response:
- **URL:** [https://hasan082.pythonanywhere.com/random](https://hasan082.pythonanywhere.com/random)

### Random Endpoint with Arguments
Customize the random response with query arguments:
- **URL:** [https://hasan082.pythonanywhere.com/random](https://hasan082.pythonanywhere.com/random)
- **Query Arguments:**
  - `number`: An integer (default: `100`)
  - `text`: A string (default: `default_text`)
- **Example Request:**  
  [https://hasan082.pythonanywhere.com/random?number=100&text=default_text](https://hasan082.pythonanywhere.com/random?number=100&text=default_text)

---

### How to Use
1. **Main Endpoint:** Simply visit the main site for basic functionality.
2. **Query Arguments:** Pass `number` and `text` as query arguments to customize the response.

For example:
```shell
curl "https://hasan082.pythonanywhere.com/random?number=50&text=HelloWorld"
