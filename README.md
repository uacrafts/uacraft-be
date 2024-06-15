## Start Project:

1. **Clone the repository:**

    ```bash
    git clone git@github.com:uacrafts/uacraft-be.git
    ```

2. **Navigate to the project directory:**

   ```bash
    cd uacraft-be
    ```

3. In root project [uacraft-be](./):

   *if you don't have .env:*
    - create file `.env`
      ```bash
      cp .env-example .env
      ```
    - Fill in the actual values for your local setup in the `.env` file.
4. Install packages:
   
   - Use Poetry
   ```bash
   poetry install
   ```
   or
   - Pip
   ```bash
   pip install -r requirements/development.txt
   ```
5. Make migrate:
   
   ```bash
   python manage.py mirgate
   ```