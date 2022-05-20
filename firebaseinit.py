class Firebase:
    def __init__(self):
        import pyrebase

        firebaseConfig = {
            'apiKey': "NO",
            'authDomain': "price-tracker-b10f5.firebaseapp.com",
            'databaseURL': "NO",
            'projectId': "NO",
            'storageBucket': "price-tracker-b10f5.appspot.com",
            'messagingSenderId': "334244448099",
            'appId': "1:334244448099:web:3968d02d8e6ec6ea1e3556",
            'measurementId': "G-E1MXWZ9BY7"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)

        self.db = firebase.database()
        self.auth = firebase.auth()
        self.storage = firebase.storage()
