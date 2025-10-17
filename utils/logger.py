# utils/logger.py
"""
Logger utility for the automation framework.

Usage:
    from utils.logger import get_logger
    logger = get_logger()
    logger.info("message")
"""

import logging
import logging.handlers
import os
from datetime import datetime

# Create logs directory if not present
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Build a log filename with timestamp to avoid collisions
LOG_FILENAME = os.path.join(LOG_DIR, "automation_log.log")

def _configure_logger():
    """
    Configure and return a logger instance.
    - Writes to a rotating file (5 files, 5MB each).
    - Also logs to console (stderr).
    - Uses a clear format with timestamps and levels.
    """
    logger = logging.getLogger("FYC_Automation_Logger")

    # If already configured (e.g., multiple imports), return existing logger
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S")
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # Optional: also create a "latest" copy for quick access
    try:
        latest_path = os.path.join(LOG_DIR, "automation_log_latest.log")
        with open(latest_path, "w", encoding="utf-8") as f:
            f.write(f"Log started: {datetime.utcnow().isoformat()}Z\n")
    except Exception:
        # Don't fail the whole framework if creating this file fails
        pass

    # Prevent logging from propagating to root logger multiple times
    logger.propagate = False

    return logger

def get_logger():
    """
    Return a configured logger instance.
    Call this at the top of any module to log messages:
        logger = get_logger()
        logger.info("Starting step")
    """
    return _configure_logger()
