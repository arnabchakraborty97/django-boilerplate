# Boilerplate for a Django Application

## Key Requirements Added
 
- django
- django-cors-headers (To bypass cors headers block policy in production)
- Pillow (For ImageFields)
- djangorestframework (To support APIs)
- python-decouple (To keep a seperate env file to store sensitive information)


## Steps to get started

- git clone 
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