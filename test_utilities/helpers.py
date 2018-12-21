import datetime
import json

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