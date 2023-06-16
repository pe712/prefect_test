
from prefect import flow, get_run_logger

@flow
def another_flow():
    logger = get_run_logger()
    logger.warning("This will never be logged")

pass