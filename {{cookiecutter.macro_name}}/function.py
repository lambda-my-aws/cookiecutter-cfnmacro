# -*- coding: utf-8 -*-

""" {{ cookiecutter.macro_name }} """


def lambda_handler(event, context):
    """
    {{ cookiecutter.macro_name }} Lambda Handler
    """
    region = event['region']
    account_id = event['accountId']
    request_id = event['requestId']
    transform_id = event['transformId']
    fragments = event['fragment']
    params = event['params']
    param_values = event['templateParameterValues']
