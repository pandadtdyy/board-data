import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/icpc/49th/xian-invitational-warmup")

FETCH_URI = os.getenv(
    "FETCH_URI", "")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "第 49 届 ICPC 国际大学生程序设计竞赛邀请赛西安站 - 热身赛"
    c.problem_quantity = 4
    c.start_time = utils.get_timestamp_second("2024-05-19 08:00:00")
    c.end_time = utils.get_timestamp_second("2024-05-19 09:30:00")

    c.fill_problem_id().fill_balloon_color()

    return c


def main():
    c = get_contest()
    common.work(DATA_DIR, c, FETCH_URI)


if __name__ == "__main__":
    main()
