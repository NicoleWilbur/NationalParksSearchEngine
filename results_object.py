class ParkResults:

    def __init__(self, park_name, park_state, park_information, park_url="", park_phone_number="", park_tty_number="",
                 park_email_address=""):
        self.park_name = park_name
        self.park_information = park_information
        self.park_state = park_state
        self.park_url = park_url
        self.park_phone_number = park_phone_number
        self.park_tty_number = park_tty_number
        self.park_email_address = park_email_address

    def display_park(self):
        print(self.park_name, self.park_state, self.park_information, self.park_url, self.park_phone_number,
              self.park_tty_number, self.park_email_address)
        return self.park_name + ", " + self.park_state + ", " + self.park_information + ", " + self.park_url + ", " + \
               self.park_phone_number + ", " + self.park_tty_number + ", " + self.park_email_address

    # def save_to_file(self):
    #     with open('National Parks Information.txt', 'a') as f:
    #         f.write(self.display_park())
    #         f.write("")
    #         # for item in results:
    #         #     f.write('')
    #         #     f.write('Park Name: ' + item['fullName'])
    #         #
    #         # for place in item['places']:
    #         #     f.write('    Place: ' + place['title'])
    #         #     f.write('        For More Information: ' + place['url'])
    #     f.close()
