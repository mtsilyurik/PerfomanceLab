import sys
import json

values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]

with open(values_path, 'r') as f_values, open(tests_path, 'r') as f_tests:
    values_data = json.load(f_values)
    tests_data = json.load(f_tests)


def put_values(values, tests):
    for test_item in tests:
        for value_item in values:
            if test_item.get('id') == value_item.get('id'):
                test_item['value'] = value_item.get('value')
                values.remove(value_item)

            if 'values' in test_item:
                put_values(values, test_item['values'])


put_values(values_data.get('values'), tests_data.get('tests'))

with open(report_path, 'w') as f_report:
    f_report.write(json.dumps(tests_data))