from locust import TaskSet, HttpLocust, task, seq_task
import queue
import itertools
import logging
import socket
from logging.handlers import RotatingFileHandler
from solarmanRequests import *

def append_file_logger():
    root_logger = logging.getLogger()
    log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler('./locust.log', maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

append_file_logger()
counter = itertools.count()


class LoginTest(TaskSet):


    def login(self, headers):
        name = "getToken"
        resource = "/oauth_s/oauth/token"

        with self.client.post(resource, data=self.user, headers=headers, name=name) as response:
            if response.status_code == 200:
                access_token = response.json()['access_token']
            else:
                print("token response: {}".format(response.json()))
        return "Bearer " + access_token


    @task(1)
    def login_task(self):
        try:
            self.user = self.locust.user_data_queue.get_nowait()
            self.logger = logging.getLogger('locust-%03d' % counter.__next__())
            data = {"region": {"nationId": None, "level1": None, "level2": None, "level3": None, "level4": None,
                               "level5": None}, "following": True}
            headers = {"User-Agent": "Apache-HttpClient/4.1.1 (java 1.5)",
                       "Content-Type": "application/x-www-form-urlencoded"}
            Authorization1 = self.login(headers)
            login_user(self.client, Authorization1)
            self.user['org_id'] = my_org(self.client, Authorization1)
            headers['Authorization'] = Authorization1
            Authorization2 = self.login(headers)
            login_user(self.client, Authorization2)
            role_info(self.client, Authorization2)
            tag_list(self.client, Authorization2)
            search_area_by_level(self.client, Authorization2)
            # station_stats(self.client, Authorization2)
            get_rank(self.client, Authorization2, "fullPowerHoursDay")
            search_station(self.client, Authorization2, data, self.logger)
            get_gen_summary(self.client, Authorization2)
            history_gen_stats(self.client, Authorization2)
            self.locust.user_data_queue.put_nowait(self.user)
        except Exception as e:
            print(e)
`

class LoginUsers(HttpLocust):
    # host = "http://192.168.30.71"
    host = "http://www.p-qa.igen"
    # host = "http://group-e.p-qa.igen:9181"
    task_set = LoginTest
    min_wait = 1000
    max_wait = 1000
    user_data_queue = queue.Queue()

    try:
        user_file = 'data/login_users.json'
        with open(user_file, 'r') as f:
            users = json.load(f)
        f.close()
        for user in users:
            user['identity_type'] = 2
            user['clear_text_pwd'] = 123456
            user_data_queue.put_nowait(user)
    except Exception as e:
        print(e)