# AIDev
First Time Setup in VSCode:
===========================
1. Go to Source Control (left sidebar) → Click Clone Repository → Paste the GitHub URL https://github.com/SaravananRamanathan25/AIDEV --> Select the destination location --> Open
2. Click on the branch name in the bottom-left corner of VS Code (e.g., main or master) --> Select "Create new branch..." --> Enter a name for your new branch (e.g., feature/login-page)
3. Go to Terminal --> New Terminal (powershell) and enter,
    >conda create -p venv python==3.13
    Proceed ([y]/n)? y
4. Kill and Open new Terminal
5. In the Terminal, enter
    >conda activate venv/
    (if error appears, execute this line and open new Terminal) >conda init
    >pip install -r requirements.txt
6. Add .env file (hierarchy similar to README.md file) with below and update the credentials			
OPENAI_API_KEY=""
GROQ_API_KEY=""
GROQ_MODEL="qwen/qwen3-32b"

To run a script:
================
1. Open the Terminal, enter
    >conda activate venv/
    >cd <<path where the python file exists>>
    >python <<name of the fil>>.py
    