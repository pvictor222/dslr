"""


"""
def compile_describe_num(describe_dict):
    describe_dict_num = describe_dict[0]
    num_headers = describe_dict[2]
    values_dict = {head: {"min": "", "max" : ""} for head in num_headers[1:]}
    for header in num_headers[1:]:
        values_dict[header]["min"] = describe_dict_num[num_headers.index(header)][4]
        values_dict[header]["max"] = describe_dict_num[num_headers.index(header)][8]
    return values_dict