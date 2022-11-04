from pyfcm import FCMNotification

from notice_app_server.settings import FCM_SERVER_KEY

push_service = FCMNotification(api_key=FCM_SERVER_KEY)

def send_notification(title, body, imagelink):
    result = push_service.notify_topic_subscribers(topic_name="EVERYONE", message_title=title,
                                                   data_message={'image': imagelink},
                                                   message_body=body, sound=True,
                                                   extra_notification_kwargs={'image': imagelink})

    print(result)