echo "Ensure that you global env has 'virtualenv' installed via pip install virtualenv";
echo "Ranning the following command sh python_env.sh <Virtal Env> <Path to save Env>";
# sh python_env.sh cron_function server/cron/script/healthcheck
[[ -z "$1" ]] && { echo "Virtual Env is empty" ; exit 1; }
[[ -z "$2" ]] && { echo "Path is empty" ; exit 1; }
cd ./$2;
if [  -d "$1" ]; then
    echo "Virtual Env existed";
    echo $2;
    if [ -e "requirements.txt" ]; then
        echo "Installing from requirements.txt";
        pip install -r requirements.txt;
    else
        echo "No requirements.txt";
    fi
fi
if [ ! -d "$1" ]; then
  echo "$1 does not exist."
  python -m venv $1;
  source $1/Scripts/activate
  #Add the libraries you wish to install
  pip install requests
  pip install psutil
  #End of the libraries you wish to install
  pip freeze > requirements.txt
  pip list
fi

