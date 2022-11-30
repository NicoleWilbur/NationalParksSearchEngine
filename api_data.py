import json
import requests
import re


def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_activities_parks():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get(
            "https://developer.nps.gov/api/v1/activities/parks?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    #json_object_list = response.json()["data"][0]
    #jprint(json_object_list)

    results = response.json()['data']

    insert_string = "INSERT INTO NPS_API_Data.activities_parks VALUES "
    for item in results:
        for park in item['parks']:
            results = "(\"" + park['parkCode'] + "\",\"" + park['states'] + "\",\"" + park['fullName'] + "\",\"" + item['name'] + "\"), "
            insert_string += results

    return insert_string[:-2]


def get_amenities_parks():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"

    try:
        response = requests.get("https://developer.nps.gov/api/v1/amenities/parksplaces?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    # json_object_list = response.json()["data"][0]
    # jprint(json_object_list)

    results = response.json()['data']
    insert_string = "INSERT INTO NPS_API_Data.amenities_parks VALUES "

    for item in results:
        for park in item[0]['parks']:
            for place in park['places']:
                string_builder = "(\"" + park['parkCode'] + "\",\"" + item[0]['name'] + "\",\"" + place['url'] + "\"), "
                insert_string += string_builder

    return insert_string[:-2]


def get_amenities_visitor_center():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"

    try:
        response = requests.get("https://developer.nps.gov/api/v1/amenities/parksvisitorcenters?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    # json_object_list = response.json()["data"][0]
    # jprint(json_object_list)

    results = response.json()['data']

    insert_string = "INSERT INTO NPS_API_Data.amenities_visitor_center VALUES "

    for item in results:
        for park in item[0]['parks']:
            for visitor_center in park['visitorcenters']:
                string_builder = "(\"" + park['parkCode'] + "\",\"" + item[0]['name'] + "\",\"" + visitor_center['name'] + \
                          "\",\"" + visitor_center['url'] + "\"), "
                insert_string += string_builder
    return insert_string[:-2]


def get_campgrounds():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get("https://developer.nps.gov/api/v1/campgrounds?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    # json_object_list = response.json()
    # jprint(json_object_list)

    results = response.json()['data']

    insert_string = "INSERT INTO NPS_API_Data.campgrounds VALUES "
    string_builder = ""

    for item in results:
        if roads := item['accessibility']['accessRoads']:
            for road in roads:
                string_builder += item['parkCode'] + "\",\"" + road
        else:
            string_builder += item['parkCode'] + "\",\"" + ""

        string_builder += "\",\"" + item['accessibility']['adaInfo']

        if classifications := item['accessibility']['classifications']:
            for classification in classifications:
                string_builder += "\",\"" + classification
        else:
            string_builder += "\",\"" + ""

        string_builder += "\",\"" + item['accessibility']['wheelchairAccess'] + "\",\"" + \
                          item['accessibility']['rvAllowed'] + "\",\"" + item['accessibility']['rvInfo'] + \
                          "\",\"" + item['accessibility']['rvMaxLength'] + "\",\"" + item['accessibility']['trailerAllowed']\
                          + "\",\"" + item['accessibility']['trailerMaxLength'] + "\",\"" + item['description'] + \
                          "\",\"" + item['id'] + "\",\"" + item['name'] + "\",\"" + item['url'] +"\",\"" + \
                          item['amenities']['cellPhoneReception'] + "\",\"" + item['amenities']['campStore'] \
                          + "\",\"" + item['amenities']['dumpStation'] + "\",\"" + item['amenities']['internetConnectivity']
        if water_present := item['amenities']['potableWater']:
            multiple = ""
            for water in water_present:
                multiple += water + " & "
            string_builder += "\",\"" + multiple[:-2]
        else:
            string_builder += "\",\"" + ""
        if shower_present := item['amenities']['showers']:
            multiple = ""
            for shower in shower_present:
                multiple += shower + " & "
            string_builder += "\",\"" + multiple[:-2]
        else:
            string_builder += "\",\"" + ""
        if toilet_present := item['amenities']['toilets']:
            multiple = ""
            for toilet in toilet_present:
                multiple += toilet + " & "
            string_builder += "\",\"" + multiple[:-2]
        else:
            string_builder += "\",\"" + ""

        string_builder += "\",\"" + item['campsites']['electricalHookups'] + "\",\"" + item['campsites']['group'] \
                          + "\",\"" + item['campsites']['horse'] + "\",\"" + item['campsites']['other'] \
                          + "\",\"" + item['campsites']['rvOnly'] + "\",\"" + item['campsites']['tentOnly'] \
                          + "\",\"" + item['campsites']['walkBoatTo'] + "\",\"" + item['campsites']['totalSites'] + \
                          "\",\"" + item['amenities']['staffOrVolunteerHostOnsite'] + "\"),(\""

    insert_string += "(\"" + string_builder + "\"), "
    return insert_string[:-7]


def get_parkinglots():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get("https://developer.nps.gov/api/v1/parkinglots?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    # json_object_list = response.json()["data"]
    # jprint(json_object_list)

    results = response.json()['data']

    insert_string = "INSERT INTO NPS_API_Data.parking_lots VALUES "
    string_builder = ""

    for item in results:
        string_builder += item['id'] + "\",\"" + item['name']

        for park in item['relatedParks']:
            string_builder += "\",\"" + park['parkCode']

        string_builder += "\",\"" + item['accessibility']['adaFacilitiesDescription'] + "\",\"" + \
                          str(item['accessibility']['isLotAccessibleToDisabled']) + "\",\"" + \
                          str(item['accessibility']['numberOfOversizeVehicleSpaces']) + "\",\"" + \
                          str(item['accessibility']['numberofAdaSpaces']) \
                          + "\",\"" + str(item['accessibility']['numberofAdaStepFreeSpaces']) + "\",\"" + \
                          str(item['accessibility']['numberofAdaVanAccessbileSpaces']) + "\",\"" + \
                          str(item['description']) + "\"),(\""
    insert_string += "(\"" + string_builder + "\"), "
    return insert_string[:-7]


def get_places():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get("https://developer.nps.gov/api/v1/places?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")
    results = response.json()['data']

    # json_object_list = response.json()["data"]
    # jprint(json_object_list)

    insert_string = "INSERT INTO NPS_API_Data.places VALUES "
    string_builder = ""

    for item in results:
        string_builder += item['id'] + "\",\"" + item['title'] + "\",\"" + item['url']
        multiple = ""
        for park in item['relatedParks']:
            multiple += park['parkCode'] + " & "

        string_builder += "\",\"" + multiple[:-2] + "\"),(\""

    insert_string += "(\"" + string_builder + "\"), "
    return insert_string[:-7]


def get_thingstodo():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get("https://developer.nps.gov/api/v1/thingstodo?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    results = response.json()['data']

    # json_object_list = response.json()["data"]
    # jprint(json_object_list)

    insert_string = "INSERT INTO NPS_API_Data.things_to_do VALUES "
    string_builder = ""


    for item in results:
        for names in item['activities']:
            string_builder += item['id'] + "\",\"" + names['name'] + "\",\"" + item['accessibilityInformation'] \
                          + "\",\"" + item['location'] + "\",\"" + item['title'] + "\",\""
        multiple = ""
        for parks in item['relatedParks']:
            multiple += parks['parkCode'] + ": " + parks['url'] + " & "
        # print(multiple)
        string_builder += "\",\"" + multiple[:-3]
        multiple = ""
        for topic in item['topics']:
            multiple += topic['name'] + " & "
        string_builder += "\",\"" + multiple[:-2] + "\"),(\""

    insert_string += "(\"" + string_builder + "\"), "
    insert_string = insert_string.replace("<a href=\"", "").replace("\">", " ").replace("Vall\\u00e9", "Valle")\
        .replace("Vallé", "Valle").replace("\"Rocking the Cradle\"", "Rocking the Cradle").replace("'", "\'").\
        replace("\"Vengeance or Justice?\"", "Vengeance or Justice?")

    scrubbed_string = re.sub('<[^<]+?>', '', insert_string)
    return scrubbed_string[:-7]


def get_topics_parks():
    api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
    try:
        response = requests.get("https://developer.nps.gov/api/v1/topics/parks?" + api_key)
    except ConnectionError:
        print("API: Connection error; please try again.")

    results = response.json()['data']

    # json_object_list = response.json()["data"]
    # jprint(json_object_list)

    insert_string = "INSERT INTO NPS_API_Data.topics VALUES "

    for item in results:
        for park in item['parks']:
            results = "(\"" + item['id'] + "\",\"" + item['name'] + "\",\"" + park['parkCode'] + "\"), "
            insert_string += results

    return insert_string[:-2]


# def get_tours():
#
#     api_key = "&api_key=WD2UnLZgaszW2QbHPYcs9LS5IFbv1YXZL8xTkcwC"
#     response = requests.get("https://developer.nps.gov/api/v1/tours?limit=2" + api_key)
#
#     results = response.json()['data']
#
#     json_object_list = response.json()["data"]
#     jprint(json_object_list)
#
#     insert_string = "INSERT INTO NPS_API_Data.tours VALUES "

    # for item in results:
    #     for park in item['parks']:
    #         results = "(\"" + item['id'] + "\",\"" + item['name'] + "\",\"" + park['parkCode'] + "\"), "
    #         insert_string += results
    #
    # return insert_string[:-2]
