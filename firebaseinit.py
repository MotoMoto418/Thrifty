class Firebase:
    def __init__(self):
        import pyrebase

        firebaseConfig = {
            'apiKey': "AIzaSyCaQWEJH7f3rhY5WTwACzBPrZI3MQqr2fs",
            'authDomain': "price-tracker-b10f5.firebaseapp.com",
            'databaseURL': "https://price-tracker-b10f5-default-rtdb.asia-southeast1.firebasedatabase.app",
            'projectId': "price-tracker-b10f5",
            'storageBucket': "price-tracker-b10f5.appspot.com",
            'messagingSenderId': "334244448099",
            'appId': "1:334244448099:web:3968d02d8e6ec6ea1e3556",
            'measurementId': "G-E1MXWZ9BY7"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)

        self.db = firebase.database()
        self.auth = firebase.auth()
        self.storage = firebase.storage()
