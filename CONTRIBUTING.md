# Contributing to the AI Agent Project

We welcome contributions to this project! Whether it's reporting a bug, suggesting an enhancement, or submitting a code change, your help is greatly appreciated.

Please take a moment to review this document to ensure a smooth contribution process.

## How to Contribute

### 1. Reporting Bugs

If you find a bug, please open an issue on our [GitHub Issues page](https://github.com/your-username/mindsdb-ai-agent/issues).
When reporting a bug, please include:

* A clear and concise description of the bug.
* Steps to reproduce the behavior.
* Expected behavior.
* Actual behavior.
* Screenshots or error messages (if applicable).
* Your operating system, MindsDB version, Python version, and any other relevant environment details.

### 2. Suggesting Enhancements

Have an idea for a new feature or an improvement to an existing one? We'd love to hear it!
Please open an issue on our [GitHub Issues page](https://github.com/your-username/mindsdb-ai-agent/issues) and describe your suggestion in detail.

### 3. Submitting Code Changes

We follow a standard Git workflow for contributions.

1.  **Fork the Repository**:
    Click the "Fork" button at the top right of the project's GitHub page.

2.  **Clone Your Fork**:
    ```bash
    git clone [https://github.com/your-username/mindsdb-ai-agent.git](https://github.com/your-username/mindsdb-ai-agent.git)
    cd mindsdb-ai-agent
    ```
    Replace `your-username` with your GitHub username.

3.  **Create a New Branch**:
    Create a new branch for your feature or bug fix. Use a descriptive name.
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/fix-issue-123
    ```

4.  **Make Your Changes**:
    Implement your changes, ensuring they adhere to the project's coding style and best practices.

    * **SQL Queries**: Keep SQL files clear and well-commented.
    * **Python Scripts**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines. Add comments where necessary.
    * **Documentation**: If your changes affect how the project is used or installed, please update the relevant documentation files in the `docs/` directory or the `README.md`.

5.  **Test Your Changes**:
    Before submitting, ensure your changes work as expected and don't introduce new issues. If applicable, add new tests or update existing ones.

6.  **Commit Your Changes**:
    Write clear, concise commit messages.
    ```bash
    git add .
    git commit -m "feat: Add new feature for X"
    # or
    git commit -m "fix: Resolve issue with Y"
    ```

7.  **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```

8.  **Open a Pull Request (PR)**:
    * Go to your forked repository on GitHub.
    * You should see a "Compare & pull request" button. Click it.
    * Provide a clear title and description for your PR, explaining the changes you've made and why they are necessary.
    * Link to any relevant issues (e.g., `Closes #123`).

## Code Style

* **Python**: We generally follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
* **SQL**: Keep queries readable, use consistent capitalization for keywords, and add comments for complex logic.
* **Markdown**: Ensure consistent heading levels and formatting in documentation files.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for your contribution!