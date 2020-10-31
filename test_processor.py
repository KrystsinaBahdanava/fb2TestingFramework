import glob


class TestProcessor:
    def __init__(self, config, connector, logger):
        self.config = config
        self.connector = connector
        self.logger = logger

    def process(self):
        test_data_files = self.check_test_folder()

        for f in test_data_files:
            self.do_testing(f)

    def check_test_folder(self):
        test_data_folder = self.config.get_test_data_folder()
        return [f for f in glob.glob(test_data_folder + '/*.json', recursive=True)]

    def do_testing(self, file_name):
        result = []
        self.logger.start_test(file_name)

        with open(file_name) as f:
            test_data = eval(f.read())

        for test in test_data['tests']:
            self.logger.start_case(test['name'])
            query = test['query']
            pre_exec_query = test['pre_execute']
            expected_result = test['expected']
            sign = test['sign']
            parameter = test['parameter']
            if pre_exec_query != "":
                result = self.connector.execute_many(pre_exec_query)
            if parameter == "yes":
                for res in result:
                    actual_result = self.connector.execute_par(query, res)
                    if actual_result > expected_result:
                        self.logger.add_pass(query, actual_result, res)
                    else:
                        self.logger.add_fail(query, actual_result, expected_result, res)
            else:
                actual_result = self.connector.execute(query)
                # compare actual result with expected
                if sign == "=":
                    if expected_result == actual_result:
                        self.logger.add_pass(query, actual_result, "")
                    else:
                        self.logger.add_fail(query, actual_result, expected_result, "")
                elif sign == ">":
                    if actual_result > expected_result:
                        self.logger.add_pass(query, actual_result, "")
                    else:
                        self.logger.add_fail(query, actual_result, expected_result, "")

        print(test_data)
