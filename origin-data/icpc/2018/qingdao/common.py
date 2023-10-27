import os
import time

from xcpcio_board_spider import logger, Contest, Teams, Image, constants, utils
from xcpcio_board_spider.spider.zoj.v2.zoj import ZOJ

log = logger.init_logger()


def get_basic_contest():
    c = Contest()
    c.logo = Image(preset="ICPC")

    return c


def handle_teams(teams: Teams):
    for team in teams.values():
        team.members = None
        type = ZOJ.get_team_type(team)

        if "type1" in type:
            team.official = 1

        if "unofficial" in type:
            team.unofficial = 1

        if "girls" in type:
            team.girl = 1


def work(data_dir: str, fetch_uri_prefix: str, c: Contest):
    utils.ensure_makedirs(data_dir)
    utils.output(os.path.join(data_dir, "config.json"), c.get_dict)
    utils.output(os.path.join(data_dir, "team.json"), {}, True)
    utils.output(os.path.join(data_dir, "run.json"), [], True)

    while True:
        log.info("loop start")

        try:
            z = ZOJ(c, fetch_uri_prefix)

            z.fetch().parse_teams().parse_runs()

            handle_teams(z.teams)

            utils.output(os.path.join(data_dir, "config.json"), c.get_dict)
            utils.output(os.path.join(data_dir, "team.json"), z.teams.get_dict)
            utils.output(os.path.join(data_dir, "run.json"), z.runs.get_dict)

            log.info("work successfully")
        except Exception as e:
            log.error("work failed. ", e)

        log.info("sleeping...")
        time.sleep(1)
