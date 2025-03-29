from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()
setup(
    name='mp_commons_py',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        #Add dependencies
        #e.g 'numpy>=1.11.1'
        'requests>=2.32.3'
    ],
    entry_points={
        "console_scripts":[
            "initEnaas = mp_commons_py:initEnaas"
        ]
    },
    long_description=description,
    long_description_content_type="textt/markdown"
)