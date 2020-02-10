from logging import getLogger

import gokart

logger = getLogger(__name__)


class Sample(gokart.TaskOnKart):
    task_namespace = 'log_test'

    def output(self):
        logger.critical("critical")
        logger.exception("exception")
        logger.warning("waring")
        logger.fatal("fatal")
        return self.make_target('data/sample.pkl')

    def run(self):
        self.dump('sample output')
