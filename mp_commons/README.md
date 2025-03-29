1. Create the folder strucuter as below
- mp_commons_py
    - mp_commons_py
        - __init__.py - Serve 2 purposes - 1. Whole directory should be treated as package. 2. Controll what is available when packaged is imported.
        - main.py - Store the functions you wish to publis
    - setup.py - Store all the dependencies like package.json (name should match your folder name)
    - README.md

2. Execute the command (In the setup.py directory)
pytthon setup.py sdist bdist_wheel
    - It will create a build + dist folder (wheel file in the dist is the 1 people will be using)

3. Test locally if the functions work (If installed, and you wish to refresh - perform a --force-reinstall)
pip install dist/<your wheel file>.whl

4. Go to pypi.org to create a account

5. twline upload dist/* - It will ask for credential