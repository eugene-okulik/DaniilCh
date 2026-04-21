import allure


def log_request(method, url, **kwargs):
    body = kwargs.get("json")
    headers = kwargs.get("headers")

    allure.attach(
        name="Request method",
        body=method,
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        name="Request url",
        body=url,
        attachment_type=allure.attachment_type.TEXT
    )

    if headers:
        allure.attach(
            name="Request headers",
            body=str(headers),
            attachment_type=allure.attachment_type.TEXT
        )

    if body:
        allure.attach(
            name="Request body",
            body=str(body),
            attachment_type=allure.attachment_type.TEXT
        )


def log_response(response):
    allure.attach(
        name="Response status code",
        body=str(response.status_code),
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        name="Response body",
        body=response.text,
        attachment_type=allure.attachment_type.TEXT
    )