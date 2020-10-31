
class Result:
    def __init__(self):
        self.result_file = open('results/result.log', 'w')

    def start_test(self, file_name):
        self.result_file.write('\n\n Testing of {} is started'.format(file_name))

    def start_case(self, test_name):
        self.result_file.write('\n\n Test case {}'.format(test_name))

    def add_pass(self, query, actual, parameter):
        self.result_file.write("\n\n Passed. Result is '{0}' Query is '{1}'. "
                               "Parameter: '{2}'".format(actual, query, parameter))

    def add_fail(self, query, actual, expected, parameter):
        self.result_file.write("\n\n Not passed. Result is '{0}', expected: '{1}'. Query is '{2}'. "
                               "Parameter: '{2}'".format(actual, expected, query, parameter))

    def finish_test(self):
        self.result_file.close()

