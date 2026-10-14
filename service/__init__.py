"""Counter service package."""
import logging
import sys

from flask import Flask

app = Flask(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

from service import routes  # noqa: E402,F401

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")