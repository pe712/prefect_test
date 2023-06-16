
from prefect import flow, get_run_logger

@flow
def my_flow():
    logger = get_run_logger()
    logger.warning("This will never be logged")

pass