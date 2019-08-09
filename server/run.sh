if [[ -z $1 ]]; then
    echo "Provide me a flask server file"
    exit 1
fi

export FLASK_APP=$1
flask run --reload