import os
import sys
from utils.logger import get_logger

logger = get_logger()

try:
    # Run behave tests with allure result directory
    cmd = "behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f pretty"
    exit_code = os.system(cmd)

    if exit_code == 0:
        logger.info("Behave tests executed successfully. Generating Allure report...")
        os.system("allure generate reports/allure-results -o reports/allure-report --clean")
        logger.info("Allure report generated at: reports/allure-report")
    else:
        logger.error("Behave tests failed. Check allure-results for details.")
except Exception as e:
    logger.error(f"Error running tests: {e}")
    sys.exit(1)
