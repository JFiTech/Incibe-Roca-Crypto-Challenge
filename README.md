# This is the solution for [Incibe's "ROCA" crypto Challenge](https://www.incibe.es/sites/default/files/paginas/academiahacker/retos-descargables/ficheros/roca.7z)

This repo contains the writeup from the challenge in PDF format, the files that were originally included with it, as well as the Python script to perform the decryption of the flag.

## Python script usage:
Make sure you have Python 3 installed on your system.

1. Create a Python venv (virtual environment) named `roca`:

    ```bash
    python -m venv roca
    ```

2. `cd` into the venv's directory:

    ```bash
    cd roca
    ```

3. Activate the Python virtual environment (venv):

    UNIX based systems (Linux/MacOS):

    ```bash
    source bin/activate
    ```

    Windows:

    ```cmd
    .\Scripts\activate
    ```

4. Clone the repository:

    ```bash
    git clone https://github.com/JFiTech/Incibe-Roca-Crypto-Challenge.git
    ```

5. cd into the `Incibe-Roca-Crypto-Challenge` directory:

    ```bash
    cd Incibe-Roca-Crypto-Challenge
    ```

6. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

7. Running the program:

    ```bash
    python roca.py 
    ```

8. Deactivating the virtual environment (venv):

    ```bash
    deactivate
    ```