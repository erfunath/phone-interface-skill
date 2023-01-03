from mycroft import MycroftSkill, intent_file_handler


class PhoneInterface(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interface.phone.intent')
    def handle_interface_phone(self, message):
        name = message.data.get('name')
        count = ''

        self.speak_dialog('interface.phone', data={
            'count': count,
            'name': name
        })


def create_skill():
    return PhoneInterface()

