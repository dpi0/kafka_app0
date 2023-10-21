# from __future__ import print_function

# # import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint

# # Configure API key authorization: api-key
# configuration = sib_api_v3_sdk.Configuration()
# configuration.api_key[
#     "api-key"
# ] = "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"

# api_instance = sib_api_v3_sdk.AccountApi(
#     sib_api_v3_sdk.ApiClient(configuration)
# )

# try:
#     api_response = api_instance.get_account()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling AccountApi->get_account: %s\n" % e)

from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key[
    "api-key"
] = "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"

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)
subject = "from the Python SDK!"
sender = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
# replyTo = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
to = [{"email": "dvynsh24@gmail.com", "name": "bruh"}]
params = {"parameter": "My param value", "subject": "New Subject"}

send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=to,
    # bcc=bcc,
    # cc=cc,
    # reply_to=reply_to,
    # headers=headers,
    html_content=html_content,
    sender=sender,
    subject=subject,
)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
