from tgt_grease import Grease


def test_runtime_process_args_simple():
    example = ["key1=val1", "key2=val2", "key3=val3"]
    processed = Grease.parse_data_args(example, "=")
    assert processed == {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}


def test_runtime_process_args_complex_case_1():
    example = ["key1=val1", "key2=val2", "key3=val3,val4"]
    processed = Grease.parse_data_args(example, "=")
    assert processed == {'key1': 'val1', 'key2': 'val2', 'key3': ['val3', 'val4']}


def test_runtime_process_args_complex_case_2():
    example = ["key1=val1", "key2=val2", "key3=val3, val4"]
    processed = Grease.parse_data_args(example, "=")
    assert processed == {'key1': 'val1', 'key2': 'val2', 'key3': ['val3', 'val4']}


def test_runtime_process_args_complex_case_3():
    example = ["key1=val1", "key2=val2", "key3=val3\\,val4"]
    processed = Grease.parse_data_args(example, "=")
    assert processed == {'key1': 'val1', 'key2': 'val2', 'key3': 'val3,val4'}
