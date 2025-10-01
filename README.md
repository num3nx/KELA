# Google URL Validation Test (Selenium & Docker) 🐳

This project contains a simple Selenium test case designed to run inside a Docker container.The test navigates to Google, captures the final URL, validates the URL, and writes the captured URL to a file.

The setup uses the official **`selenium/standalone-chrome`** Docker image to ensure a stable and isolated execution environment.

## 📁 Project Files

The necessary files for this project are:

  * **`URL_Validation.py`**: The core Selenium test script, configured with options for headless container execution.
  * **`requirements.txt`**: Specifies the necessary Python package (`selenium`).
  * **`Dockerfile`**: Instructions for building the container image, including Python installation and environment setup.
  * **`README.md`**: This documentation file.

## 🛠️ Prerequisites

To build and run this project, you need:

1.  **Docker Desktop** (or Docker Engine) installed and running on your system (Windows, macOS, or Linux).

## 🚀 Build the Docker Image

Build the image and tag it with a version number (e.g., `v1.0.0`). Run this command from the directory containing your `Dockerfile`:

```bash
docker build -t google-url-validator:v1.0.0 .
```

  * **Tip:** You can verify the image was created successfully using `docker images`.

## ▶️ Running the Test

Run the test by executing the container. The **Volume Mount (`-v`)** is **essential** to ensure the output file created by the test is saved back to your local machine.

### Command Line Execution

Navigate to your project folder and run the command appropriate for your operating system's terminal:

| Terminal | Command |
| :--- | :--- |
| **PowerShell (Windows)** | `docker run --rm -v "${PWD}:/app" google-url-validator:v1.0.0` |
| **Command Prompt (CMD)** | `docker run --rm -v "%cd%:/app" google-url-validator:v1.0.0` |
| **Linux/macOS (Bash)** | `docker run --rm -v "$(pwd):/app" google-url-validator:v1.0.0` |

### Command Breakdown

  * `docker run`: Executes a command in a new container.
  * `--rm`: Automatically removes the container instance after it exits.
  * `-v ...:/app`: **Volume Mount.** Links your local directory to the container's working directory (`/app`), allowing the container to write files to your host machine.
  * `google-url-validator:v1.0.0`: The image name and tag to execute.

-----

## ✅ Expected Results

1.  **Console Output:** The container will print the script's output, showing the navigation status.

    ```
    Navigating to: https://www.google.com
    OK, Current URL is https://www.google.com, same as expected
    Browser closed.
    ```

    *(Note: The script's current logic checks the expected string against the static URL variable, not the live URL from the browser.)*

2.  **Output File:**
    A file named **`URL_validation.txt`** will be created in your local project directory, containing the final URL captured by the browser.
