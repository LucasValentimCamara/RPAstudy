"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from botcity.plugins.http import BotHttpPlugin

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Implement here your logic...
    base_url = 'https://reqres.in/api'
    
    # GET list of users
    http = BotHttpPlugin(base_url+'/users?page=2')
    print(http.get().text)

    #POST Login
    http = BotHttpPlugin(base_url+'/login')
    params = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    http.set_params(params)
    print(http.post().text)

    #POST Register 
    http = BotHttpPlugin(base_url+'/register')
    params = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    http.set_params(params)
    print(http.post().json()['token'])



    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


if __name__ == '__main__':
    main()
