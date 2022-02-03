from firebaseinit import Firebase
from utils import Utils


fire = Firebase()
utils = Utils()

user = fire.auth.sign_in_with_email_and_password('pes2202100384@pesu.pes.edu', 'asdfghjk')
UID = user['localId']

URL0 = [
    'https://www.flipkart.com/lenovo-ideapad-5-pro-ryzen-7-octa-core-5800u-16-gb-512-gb-ssd-windows-11-home-14acn6-thin-light-laptop/p/itm2644244e142bc?pid=COMG8ZHDVJH8E8GT&lid=LSTCOMG8ZHDVJH8E8GTUGDFC5&marketplace=FLIPKART&q=ideapad+5+pro+&store=6bo%2Fb5g&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=72bd99d9-f931-4725-ac71-e017bb307a80.COMG8ZHDVJH8E8GT.SEARCH&ppt=hp&ppn=homepage&ssid=xvwr190y280000001641968601843&qH=1aa27417bacabd17',
    'https://www.amazon.in/Lenovo-Ideapad-Keyboard-Warranty-82L700D0IN/dp/B09M41GR4K/ref=sr_1_3?crid=32OSBOD6X7EDM&keywords=lenovo%2Bideapad%2B5%2Bpro&qid=1641968581&sprefix=lenovo%2Bideapad%2B5%2B%2Caps%2C513&sr=8-3&th=1'
]

URL1 = [
    'https://www.amazon.in/Samsung-Phantom-Storage-Additional-Exchange/dp/B08LRCM9LQ/ref=sr_1_1?crid=20PEDUIVG7GS1&keywords=samsung+galaxy+s21&qid=1641490938&sprefix=samsung+galaxy+s2%2Caps%2C270&sr=8-1',
    'https://www.flipkart.com/samsung-galaxy-s21-phantom-violet-128-gb/p/itm916d671b27b8d?pid=MOBFZ3TM5FT52G79&lid=LSTMOBFZ3TM5FT52G79RTBHT2&marketplace=FLIPKART&q=galaxy+s21&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_2_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_8_na_na_na&fm=SEARCH&iid=b7037d90-ba88-481d-b1a3-ccf048f123e8.MOBFZ3TM5FT52G79.SEARCH&ppt=hp&ppn=homepage&ssid=oglzg3sszk0000001641490944624&qH=a440a1393ca5c12d'
]

URL2 = [
    'https://www.amazon.in/Harry-Potter-Chamber-Secrets/dp/1408855666/ref=sr_1_3?crid=D1DGJZAAT9M2&keywords=harry+potter&qid=1642147659&sprefix=harry+potter+%2Caps%2C405&sr=8-3',
    'https://www.flipkart.com/harry-potter-philosopher-s-stone/p/itm98ddd52c1eb42?pid=9781408855652&lid=LSTBOK9781408855652OQYZXT&marketplace=FLIPKART&q=harry+potter+and+the+philosophers+stone&store=bks&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&fm=SEARCH&iid=ba12cbc3-686b-46ba-88e7-45c618e6a86c.9781408855652.SEARCH&ppt=hp&ppn=homepage&ssid=fxy0vmlxg00000001642147673190&qH=beeb7e4ebd65dc7c'
]

URL3 = [
    'https://www.amazon.in/Lenovo-39-62cm-Windows-Keyboard-82JW0052IN/dp/B09DMWJH96/ref=sr_1_3?keywords=Lenovo%2Blegion%2B5%2B5800h&qid=1639501786&sr=8-3&th=1',
    'https://www.flipkart.com/lenovo-legion-5-ryzen-7-octa-core-5800h-16-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-rtx-3050-15ach6-gaming-laptop/p/itm50d5ba7a10251?pid=COMG62ZASBMGDC5M&lid=LSTCOMG62ZASBMGDC5MRQSUJN&marketplace=FLIPKART&q=lenovo+legion&store=search.flipkart.com&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=ba962896-dbc7-474c-b6fa-3bae3dce1c8f.COMG62ZASBMGDC5M.SEARCH&ppt=sp&ppn=sp&ssid=a4i46g498g0000001639500094619&qH=5dc4906269c2c6e5'
]

URL4 = [
    'https://www.amazon.in/beyerdynamic-990-Studio-Headphones-Black/dp/B0011UB9CQ',
    'https://www.flipkart.com/beyerdynamic-dt-990-pro-open-studio-headphones-250-ohms-wired-without-mic-headset/p/itm249dec86fb314'
]

URL5 = [
    'https://www.amazon.in/HP-15-6-inch-7-5800H-Refresh-15-en1037AX/dp/B091FJYLV7/ref=sr_1_4?crid=38DAW5HZRK2K6&keywords=hp+omen+15&qid=1643481688&sprefix=hp+omen+1%2Caps%2C506&sr=8-4',
    'https://www.flipkart.com/hp-omen-15-ryzen-7-octa-core-5800h-16-gb-1-tb-ssd-windows-10-home-8-gb-graphics-nvidia-geforce-rtx-3070-165-hz-15-en1037ax-gaming-laptop/p/itm156c4fcb0bed7?pid=COMG3US8G8RGVGT5&lid=LSTCOMG3US8G8RGVGT5PWYXQ2&marketplace=FLIPKART&q=hp+omen+15&store=search.flipkart.com&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=9c76ed0c-634b-4c96-9a1b-747fbb06b222.COMG3US8G8RGVGT5.SEARCH&ppt=hp&ppn=homepage&ssid=le4stf4u800000001643481698086&qH=89314842243d558f'
]

for url in URL0:
    print(utils.add(UID, url, 'IP 5 Pro'))

for url in URL1:
    print(utils.add(UID, url, 'phone'))

for url in URL2:
    print(utils.add(UID, url, 'Harry Potter'))

for url in URL3:
    print(utils.add(UID, url, 'Legion 5'))

for url in URL4:
    print(utils.add(UID, url, 'headphones'))

for url in URL5:
    print(utils.add(UID, url, 'Omen'))
