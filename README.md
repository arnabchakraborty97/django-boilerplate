# Boilerplate for a Django Application

## Key Requirements

- django
- django-cors-headers (To bypass cors headers block policy in production)
- Pillow (For ImageFields)
- djangorestframework (To support APIs)
- python-decouple (To keep a seperate env file to store sensitive information)


## Static files

- The static files have been initialised with bootstrap 5.0.1
- Customised css and js files included for project particular changes.


## Steps to get started

- git clone this project
    ```
    git clone https://github.com/arnabchakraborty97/
    ```
- Initialise environment for the project 
     ```
    virtualenv env
    source env/bin/activate
    ```
- Once inside environment, install the required python packages in [requirements.txt](./requirements.txt)
    ```
    pip install -r requirements.txt
    ```
- (Optional) You may check if the dependencies have been installed using the following command
    ```
    pip freeze
    ```
- Get inside the project directory
    ```
    cd project
    ```
- Initialise database
    ```
    python manage.py migrate
    ```
- Create a superuser to access site's admin portal and enter requred details
    ```
    python manage.py createsuperuser
    ```

## Environment variables

- The environment variables to be used should be stored in the .env file.
- Use the [.env.example](./.env.example) file as a reference and create a .env file with all required values.

## Run the server

- After going through the above steps, run your local server using:
    ```
    python manage.py runserver
    ```

### Hope this works for you.
### Raise an issue if something is not working. Thanks!