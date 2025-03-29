import os
import subprocess
import sys
# Function to install missing packages using pip
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing package {package}: {e}")
        sys.exit(1)

def initEnaas():
    print("Hello from mp_common.py")
    if os.name == 'nt':
        print("source mp_commons_py/Scripts/Activate")
    elif os.name == 'posix':
        venv_path = './mp_commons_py/bin/python'
        print('source mp_commons_py/bin/python')
    else:
        print("Unknown OS")
    # Check if running inside a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Running inside a virtual environment")
        try:
            import requests
        except ImportError:
            print("'requests' library not found. Installing it now...")
            install_package('requests')
        import requests
        url = 'https://www.google.com'
        token = 'testing'
        params = {}
        headers = {
            'Authorization' : f'Bearer {token}'
        }
        response = requests.get(url, headers=headers, params=params)
        #Sample to get env....
        env_vars = os.environ
        print(env_vars.get('VSCODE_GIT_ASKPASS_MAIN'))
        if response.status_code == 200:
            print(response) #If response is in JSON....
        else:
            print('Error:', response.status_code)

    else:
        print("Not running inside a virtual environment")
        sys.exit()

