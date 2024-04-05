# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import mysql.connector

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
    db_host = "localhost"
    db_user = "root"
    db_password = ""
    db_name = "data"
    
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        charset='utf8'
    )

   # Check if the connection was successful
    if conn.is_connected():
        print("Successfully connected to the database")
        
        # Create cursor object
        cursor = conn.cursor()

        update_query = "UPDATE users SET job = 'Web Developer', age = 60 WHERE id = 2"
        cursor.execute(update_query)
        conn.commit()


        # insert_query = "INSERT INTO users (name,age,job) VALUES ('Richard', 20, 'Fireman')"
        # cursor.execute(insert_query)
        # conn.commit()

        # SQL query
        # query = "SELECT * FROM users WHERE job='RPA Developer'"

        # Execute the query
        # cursor.execute(query)

        # results = cursor.fetchall()

        # for row in results:
        #     print(row)


    else:
        print("Failed to connect to the database")

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


if __name__ == '__main__':
    main()
