# -*- coding: utf-8 -*-

""" {{ cookiecutter.macro_name }} """


def lambda_handler(event, context):
    """
    {{ cookiecutter.macro_name }} Lambda Handler
    """
    response = {
        "status": "success",
        "requestId": event['requestId']
    }
    region = event['region']
    account_id = event['accountId']
    transform_id = event['transformId']
    fragment = event['fragment']
    params = event['params']
    param_values = event['templateParameterValues']

    ## ADD YOUR CHANGES HERE ##

    response['fragment'] = fragment
    return response
