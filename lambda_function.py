"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
from meraki_api import MerakiAPI
import requests
import json
import re
import os

def get_org_by_name(meraki, name):
    orgs = meraki.organizations().index().json()
    for item in orgs:
        if item['name'] == name:
            return item
    raise ValueError("not found: name={}".format(name))

def get_network_by_name(meraki, org_id, name):
    nets = meraki.organizations(org_id).networks().index().json()
    for item in nets:
        if item['name'] == name:
            return item
    raise ValueError("not found: org_id={} name={}".format(org_id, name))

def get_ssid_by_name(meraki, org_id, net_id, name):
    ssids = meraki.organizations(org_id).networks(net_id).ssids().index().json()
    for item in ssids:
        if item['name'] == name:
            return item
    raise ValueError("not found: org_id={} net_id={} name={}".format(org_id, net_id, name))

# def meraki.organizations(ORGID).networks().index().json()


####################################################

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_orgs_response():
    session_attributes = {}
    card_title = "My Meraki Organizations"
    response = meraki.organizations().index()
    json = response.json()
    print(json)
    speech_output = "{0} - organizations found, {1}".format(str(len(json)), json[0]['name'])
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Meraki Dev Kit" 
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Welcome to the Meraki Dev Kit" 
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_network_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "networks"
    speech_output = "Nothing implemented yet " 
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Nothing implemented yet " 
                    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Meraki Kit " \
                    "More Power. More Choice. More Protection!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(guest_network, intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print(intent_name)
    # Dispatch to your skill's intent handlers
    if intent_name == "guestnetON":
        return guest_network.enable()
    if intent_name == "guestnetOFF":
        return guest_network.disable()
    if intent_name == "guestnetPASSWORD":
        return guest_network.password()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

class GuestNetwork:
    def __init__(self, meraki, org_id, net_id, ssid):
        self.meraki             = meraki
        self.org_id             = org_id
        self.net_id             = net_id
        self.ssid               = ssid

    def enable(self):
        session_attributes = {}
        card_title = "Guest Network On"
        reprompt_text = ""
        response = self.meraki.organizations(self.org_id).networks(self.net_id).ssids(self.ssid['number']).update({"enabled": True})
        if response.status_code == 200:
            speech_output = "Success ! Enabling guest wi-fi"
        else:
            speech_output = "Sorry could not Enable Guest Wi-fi"
        print(speech_output)
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, False))

    def disable(self):
        session_attributes = {}
        card_title = "Guest Network Off"
        reprompt_text = ""
        response = self.meraki.organizations(self.org_id).networks(self.net_id).ssids(self.ssid['number']).update({"enabled": False})
        if response.status_code == 200:
            speech_output = "Success ! Disabled guest wi-fi"
        else:
            speech_output = "Sorry could not Disable Guest Wi-fi"
        print(speech_output)
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, False))

    def password(self):
        session_attributes = {}
        card_title = "Guest Network Password"
        speech_output = "The password for {0} - is {1}".format(str(self.ssid['name']),  self.ssid['psk'])
        reprompt_text = ""
        should_end_session = True
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))



# --------------- Main handler ------------------

def lambda_handler(event, context):
    MERAKI_API_KEY   = os.environ['MERAKI_API_KEY']
    MERAKI_ORG_NAME  = os.environ['MERAKI_ORG_NAME']
    MERAKI_NET_NAME  = os.environ['MERAKI_NET_NAME']
    MERAKI_SSID_NAME = os.environ['MERAKI_SSID_NAME']

    meraki           = MerakiAPI(MERAKI_API_KEY)
    org              = get_org_by_name(meraki, MERAKI_ORG_NAME)
    net              = get_network_by_name(meraki, org['id'], MERAKI_NET_NAME)
    ssid             = get_ssid_by_name(meraki, org['id'], net['id'], MERAKI_SSID_NAME)
    guest_network    = GuestNetwork(meraki, org['id'], net['id'], ssid)
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # """
    # Uncomment this if statement and populate with your skill's application ID to
    # prevent someone else from configuring a skill that sends requests to this
    # function.
    # """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(guest_network, event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])