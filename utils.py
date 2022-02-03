# Global imports
import time
import yagmail
from prettytable import PrettyTable
from math import inf

# Local imports
from firebaseinit import Firebase
from scraper import Scraper


fire = Firebase()
scrape = Scraper()


class Utils:
    yagmail.register('thriftypricechecker@gmail.com', 'igotthemkeyskeyskeys')
    yag = yagmail.SMTP('thriftypricechecker@gmail.com')

    def signup(self, name, email, password):
        try:
            user = fire.auth.create_user_with_email_and_password(email, password)
            time.sleep(5)
            UID = user['localId']
            info = {'name': name, 'email': email}
            print("\nSuccessfully signed up!\n")

            data = {'UID': UID, 'info': info}

            return data

        except:            
            return "Signup error."

    def signin(self, email, password):
        try:
            user = fire.auth.sign_in_with_email_and_password(email, password)
            print("\nSuccessfully signed in!\n")

            UID = user['localId']
            
            return UID

        except:
            return "Sign in error."

    def add(self, UID, URL, nick):
        if "https://" in URL:
            try:
                data = scrape.fetch(URL)
                fire.db.child('users').child(UID).child('tracking-data').child(nick).update(data)

                return True

            except:
                return False

        else:
            return False

    def delete(self, UID, key):
        try:
            fire.db.child('users').child(UID).child('tracking-data').child(key).remove()

            return "Successful."

        except:
            return "Failed."

    def show(self, UID):
        table = PrettyTable(['#', 'Category', 'Best website', 'Best price'])
        count = 0
        websites = []
        required = {}

        try:
            best = self.compare(UID)
            for nick, data in best.items():
                count += 1
                for url, price in data.items():
                    website = url.split('.')[1].capitalize()
                    required.update({nick: {"URL": url, "website": website, "price": price}})
                    # table.add_row([count, nick, website, price])
                    # websites.append(website)

            beauty = f"\n{table}"

            return required
            # return beauty, websites

        except:
            return "Retrieval error."

    def compare(self, UID):
        best = {}

        try:
            items = dict(fire.db.child('users').child(UID).child('tracking-data').get().val())

            for nick, data in items.items():
                req = []
                
                for plat, info in data.items():
                    if not type(info['price']) == str:
                        req.append({'url': info['url'], 'price': info['price']})

                    else:
                        req.append({'url': info['url'], 'price': inf})

                s_req = sorted(req, key=lambda x: float(x['price']))

                best_price = s_req[0]['price']
                best_website = s_req[0]['url']

                best.update({nick: {best_website: best_price}})

            return best

        except:
            return "Error."

    def monitor(self, UID):
        changed = {}

        name = fire.db.child('users').child(UID).child('user-data').child('name').get().val()
        email = fire.db.child('users').child(UID).child('user-data').child('email').get().val()
        subject = "Your price tracking report is here!"
        message = f"Dear {name.title()}, there's a reduction of price!\n"

        keys = fire.db.child('users').child(UID).child('tracking-data').get()
        for key in keys.each():
            key = key.key()

            temp = dict(fire.db.child('users').child(UID).child('tracking-data').child(key).get().val())

            for plat, data in temp.items():
                self.add(UID, data['url'], key)

        old_data = self.compare(UID)
        time.sleep(1800)
        new_data = self.compare(UID)

        if len(old_data) == len(new_data):
            for key in keys.each():
                key = key.key()

                new_price = list(new_data[key].values())[0]
                old_price = list(old_data[key].values())[0]

                if new_price < old_price :
                    changed.update({key: (old_price, new_price)})

            if len(changed) != 0:
                for item, prices in changed.items():
                    s = f"The price of {item} has gone down from {prices[0]} to {prices[1]}!"
                    message += f"{s}\n"

                message += '\nCheck now to not miss out on a possible deal!\n\nRegards,\nThe Thrifty Team'

                self.sendMail(email, subject, message)

            return None

        else:
            self.monitor(UID)

    def sendMail(self, email, subject, message):
        yagmail.register('thriftypricechecker@gmail.com', 'igotthemkeyskeyskeys')
        yag = yagmail.SMTP('thriftypricechecker@gmail.com')

        try:
            yag.send(email, subject, message)
        
        except:
            return "Error."
