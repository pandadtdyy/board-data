import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/ccpc/9th/online-qualification")
FETCH_URI = os.getenv(
    "FETCH_URI", "./raw/")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "第九届中国大学生程序设计竞赛网络预选赛"
    c.problem_quantity = 12
    c.start_time = utils.get_timestamp_second("2023-08-20 12:00:00")
    c.end_time = utils.get_timestamp_second("2023-08-20 17:00:00")

    c.fill_problem_id().fill_balloon_color()

    return c


def main():
    c = get_contest()
    common.work(DATA_DIR, FETCH_URI, c)


if __name__ == "__main__":
    main()
