from adjacent import Client
from product import *

client = Client()
client.publish(Comments.product.get_cent_answers_channel_name(), product .as_compact_dict())
response = client.send()
print('sent to channel {}, got response from centrifugo: {}'.format(answer.question.get_cent_answers_channel_name(),
                                                                    response))
