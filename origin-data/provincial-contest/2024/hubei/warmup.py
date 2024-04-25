import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/provincial-contest/2024/hubei-warmup")

FETCH_URI = os.getenv(
    "FETCH_URI", "")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "The 2024 International Collegiate Programming Contest in Hubei Province, China - Warming Up"
    c.problem_quantity = 4
    c.start_time = utils.get_timestamp_second("2024-04-26 14:45:00")
    c.end_time = utils.get_timestamp_second("2024-04-26 17:15:00")

    c.fill_problem_id().fill_balloon_color()

    return c


def main():
    c = get_contest()
    common.work(DATA_DIR, c, FETCH_URI)


if __name__ == "__main__":
    main()