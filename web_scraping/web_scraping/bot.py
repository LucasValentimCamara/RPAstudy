# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from botcity.plugins.crawler import BotCrawlerPlugin
import pandas as pd

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

    # Instantiate the plugin and enable JavaScript
    crawler = BotCrawlerPlugin(javascript_enabled=True)

    pages_to_extract = 5
    page_counter = 1

    df = pd.DataFrame(columns=['Title','Price'])

    while page_counter <= pages_to_extract:
        url = f"https://books.toscrape.com/catalogue/page-{page_counter}.html"
        html = crawler.request(url)

        books_prices = [element.current.text for element in html.query_selector_iter_all("p.price_color")]
        html.reset()
        books_titles = [element.get_attribute('title') for element in html.query_selector_iter_all("h3>a")]

        for book_title, book_price in zip(books_titles, books_prices):
            new_row = {'Title': book_title, 'Price': book_price}
            df = df._append(new_row, ignore_index = True)

        page_counter += 1

    df.to_excel("Data.xlsx", index = False)

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


if __name__ == '__main__':
    main()
