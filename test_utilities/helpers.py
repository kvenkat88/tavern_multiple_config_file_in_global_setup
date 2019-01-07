import datetime
import json
import yaml
import os

def assert_quick_response(response):
    """
    Make sure that a request doesn't take too long
    :param response: Interact with the response object of the API interacted
    :return:
    """
    print "Validating the performance of the stages available"
    assert response.elapsed < datetime.timedelta(seconds=20)

def save_response(response):
    filename='file4.json'
    with open(filename, 'w') as f:
        json.dump(response.json(), f)

def json_validator(response):
    """
    Method to validate whether response retrieved is in form of json format
    :param response: json response
    :return: True | False
    """
    '''
    try:
        json.loads(response)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False'''
    pass
    #print response.content

def retrieve_json_response(response):
    """
    Method to retrieve and capture the json response of api call requested
    :param response: response
    :return: returns the response object of api call for further usage
    """
    pass
    #return response

def retrieve_user_by_id(response,index):
    """
        Retrieve the id from the post response with index value of the list
    :param response: response object from tavern test
    :param index: index of the list to parse
    :return: {"id":1}
    """
    return {"fetched_id":response.json()[index]['id']} #Most often result would be enclosed in {}

def retrieve_user_details_form_of_dict(response,index):
    """
        Return the post by using index
    :param response: response object from tavern test
    :param index: index of the list to parse
    :return: {fetched_post_resp:{"a":1,"b":2,"body":"444444"}}
    """
    return {"fetched_post_resp":response.json()[index]}

def retrieve_user_details_form_of_dict1(response):
    """
        Return the post by using index
    :param response: response object from tavern test
    :return: {fetched_post_resp:{"a":1,"b":2,"body":"444444"}}
    """
    return {"fetched_post_resp1":response.json()['id']}

configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../configs'))
file_name_path = configPath + '/environment.yaml'

def parse_yaml_file(file_name):
    yaml_file = None
    with open(file_name, 'r') as stream:
        try:
            yaml_file = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return yaml_file


def retrieve_user_info_yaml_file(user_name):
    yaml_file_loaded = parse_yaml_file(file_name_path)

    for a in range(len(yaml_file_loaded['variables']['usersInfo'])):
        if user_name in yaml_file_loaded['variables']['usersInfo'][a]:
            return {'user_name_retrieved':yaml_file_loaded['variables']['usersInfo'][a][user_name]['username']}
        else:
            return {}


def retrieve_user_info_based_upon_fixtures(commandline_options_single_user_test):
    print retrieve_user_info_yaml_file(retrieve_user_info_yaml_file)
    return retrieve_user_info_yaml_file(retrieve_user_info_yaml_file)

def validate_response_utility(response):
    assert response.json()['userId'] == 1
    assert response.json()['id'] == 3
    assert response.json()['title'] ==  "ea molestias quasi exercitationem repellat qui ipsa sit aut"

def print_resp(response):
    print response.json()
    return {'requested_resp': response.json()}



'''
sf = parse_yaml_file(file_name_path)
name = "type2_diabetes"
for a in range(len(sf['variables']['usersInfo'])):
    if name in sf['variables']['usersInfo'][a]:
        print sf['variables']['usersInfo'][a][name]['username']
    else:
        print "no_user_name"
        '''
