# Global imports
import webbrowser
import os

import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from math import inf

# Local imports
from utils import Utils
from firebaseinit import Firebase


fire = Firebase()
utils = Utils()


pygame.init()

# Main screen
WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Window attributes
CAPTION = 'Thrifty' 
pygame.display.set_caption(CAPTION)

ICON = pygame.image.load(os.path.join('Assets', 'wallet-icon.png'))
pygame.display.set_icon(ICON)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (233, 245, 219)
TEA_GREEN = (207 ,225, 185)
LAUREL_GREEN = (181, 201, 154)
ASPARAGUS = (151, 169, 124)
MOSS_GREEN = (135, 152, 106)
FERN_GREEN = (113, 131, 85)
BROWN = (127, 96, 0)
DARK_BROWN = (102, 51, 0)
GOLD = (204, 163, 0)
HOVERED_GREY = (222, 226, 230)
SELECTED_GREY = (108, 117, 125)

# Other attributes
FPS = 60
clock = pygame.time.Clock()

run = True
user = {'name': '', 'UID': '', 'content': ''}

# Landing page
def landing():
    global run

    home_surface = pygame.Surface((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')


    LOGO = pygame.image.load(os.path.join('Assets', 'wallet-logo.png'))
    logo_scale = 0.2
    logo_width, logo_height = LOGO.get_width(), LOGO.get_height()
    LOGO = pygame.transform.scale(LOGO, (int(logo_width*logo_scale), int(logo_height*logo_scale)))
    logo_rect = LOGO.get_rect()
    logo_rect.center = (195, 150)


    title_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 94)
    title = title_font.render('THRIFTY', True, BROWN, BEIGE)
    title_rect = title.get_rect()
    title_rect.center = (460, 165)


    tag_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 28)
    tag = tag_font.render('Get Thrifty.', True, BLACK, BEIGE)
    tag_rect = tag.get_rect()
    tag_rect.center = (570, 235)

    
    login_button_rect = pygame.Rect(ORIGIN, (170, 70))
    login_button_rect.center = (540, 460)
    login_button = pygame_gui.elements.UIButton(relative_rect=login_button_rect, 
                                                text="LOGIN", 
                                                manager=manager, 
                                                object_id=ObjectID("login_button"))
                                              
    signup_button_rect = pygame.Rect(ORIGIN, (170, 70))
    signup_button_rect.center = (260, 460)
    signup_button = pygame_gui.elements.UIButton(relative_rect=signup_button_rect, 
                                                text="SIGNUP", 
                                                manager=manager, 
                                                object_id=ObjectID("signup_button"))


    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == login_button:
                    login()

                if event.ui_element == signup_button:
                    signup()

        home_surface.fill(BEIGE)
        
        manager.update(time_delta)
        home_surface.blit(LOGO, logo_rect)
        home_surface.blit(title, title_rect)
        home_surface.blit(tag, tag_rect)
        SCREEN.blit(home_surface, ORIGIN)
        manager.draw_ui(SCREEN)

        pygame.display.update()


# Login page
def login():
    global run

    login_surface = pygame.Surface((WIDTH, HEIGHT))
    
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')


    title_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Medium.ttf'), 69)
    title = title_font.render('LOGIN', True, BLACK, BEIGE)
    title_rect = title.get_rect()
    title_rect.center = (400, 65)


    helper_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 16)
    email_helper = helper_font.render('Enter your email address: ', True, BLACK, BEIGE)
    password_helper = helper_font.render('Enter your password: ', True, BLACK, BEIGE)
    email_helper_rect = email_helper.get_rect()
    password_helper_rect = password_helper.get_rect()
    email_helper_rect.bottomleft = (170, 180)
    password_helper_rect.bottomleft = (170, 300)


    email_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 180), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("regular_text_entry_line"))

    password_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 300), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("password_text_entry_line"))
    password_text_box.set_text_hidden(is_hidden=True)                                                              

    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((440, 440), (160, 70)),
                                                text="LOGIN",
                                                manager=manager,
                                                object_id=ObjectID("login_button"))

    cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 440), (160, 70)),
                                                text="CANCEL",
                                                manager=manager,
                                                object_id=ObjectID("signup_button"))


    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == login_button:
                    email = email_text_box.get_text()
                    password = password_text_box.get_text()

                    try:
                        UID = utils.signin(email, password)
                        fire.db.child('users').child(UID).child('user-data').update({'isLoggedIn': True})
                        user_name = fire.db.child('users').child(UID).child('user-data').child('name').get().val()
                        user.update({'name': user_name, 'UID': UID})
                        home()

                    except:
                        error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                        error_window_rect.center = (400, 300)
                        error_message = "Sign in failed, check password and email ID. If you do not have an account, please sign up."
                        error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

                if event.ui_element == cancel_button: 
                    print('cancel')
                    landing()

        login_surface.fill(BEIGE)
        
        manager.update(time_delta)
        SCREEN.blit(login_surface, ORIGIN)
        SCREEN.blit(title, title_rect)
        SCREEN.blit(email_helper, email_helper_rect)
        SCREEN.blit(password_helper, password_helper_rect)
        pygame.draw.line(SCREEN, BROWN, (100, 100), (700, 100), width=2)
        manager.draw_ui(SCREEN)

        pygame.display.update()

# Sign up page
def signup():
    global run

    user_info = {'isLoggedIn': False}

    signup_surface = pygame.Surface((WIDTH, HEIGHT))

    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')


    title_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Medium.ttf'), 69)
    title = title_font.render('SIGN UP', True, BLACK, BEIGE)
    title_rect = title.get_rect()
    title_rect.center = (400, 65) 


    helper_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 16)
    name_helper = helper_font.render('Enter your full name: ', True, BLACK, BEIGE)
    email_helper = helper_font.render('Enter your email address: ', True, BLACK, BEIGE)
    password_helper = helper_font.render('Enter your password: ', True, BLACK, BEIGE)
    confirm_password_helper = helper_font.render('Please confirm your password: ', True, BLACK, BEIGE)
    name_helper_rect = name_helper.get_rect()
    email_helper_rect = email_helper.get_rect()
    password_helper_rect = password_helper.get_rect()
    confirm_password_helper_rect = confirm_password_helper.get_rect()
    name_helper_rect.bottomleft = (170, 160)
    email_helper_rect.bottomleft = (170, 240)
    password_helper_rect.bottomleft = (170, 320)
    confirm_password_helper_rect.bottomleft = (170, 400)


    name_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 160), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("regular_text_entry_line"))
    
    email_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 240), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("regular_text_entry_line"))

    password_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 320), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("password_text_entry_line"))
    password_text_box.set_text_hidden(is_hidden=True)
    
    confirm_password_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((165, 400), (470, 50)), 
                                                        manager=manager, 
                                                        object_id=ObjectID("password_text_entry_line"))                                                        
    confirm_password_text_box.set_text_hidden(is_hidden=True)
    
    signup_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((440, 480), (160, 70)),
                                                text="SIGN UP",
                                                manager=manager,
                                                object_id=ObjectID("login_button"))

    cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 480), (160, 70)),
                                                text="CANCEL",
                                                manager=manager,
                                                object_id=ObjectID("signup_button"))

    confirmation_window_rect = pygame.Rect(ORIGIN, (460, 360))
    confirmation_window_rect.center = (400, 300)
    

    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == signup_button:
                    name = name_text_box.get_text()
                    email = email_text_box.get_text()
                    password = password_text_box.get_text()
                    c_password = confirm_password_text_box.get_text()

                    if password == c_password and len(name) != 0:
                        try:
                            data = utils.signup(name, email, password)
                            user_info.update(data['info'])
                            UID = data['UID']
                            fire.db.child('users').child(UID).child('user-data').update(user_info)

                            signin_confirmation_window_rect = pygame.Rect(ORIGIN, (460, 360))
                            signin_confirmation_window_rect.center = (400, 300)
                            signin_confirmation_window = pygame_gui.windows.UIConfirmationDialog(rect=signin_confirmation_window_rect, 
                                                                        manager=manager, 
                                                                        action_long_desc='Would you like to sign in?', 
                                                                        window_title='ATTENTION!', 
                                                                        action_short_name='LOGIN',
                                                                        blocking=True,)

                        except:
                            error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                            error_window_rect.center = (400, 300)
                            error_message = "Sign up failed. Please try again."
                            error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

                    else:
                        error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                        error_window_rect.center = (400, 300)
                        error_message = "Passwords do not match, or there is a field left blank. Please try again."
                        error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

                if event.ui_element == cancel_button:
                    print('cancel')
                    landing()

            if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                if event.ui_element == signin_confirmation_window:
                    print('confirm')
                    try:
                        UID = utils.signin(email, password)
                        fire.db.child('users').child(UID).child('user-data').update({'isLoggedIn': True})
                        user_info['isLoggedIn'] = True

                        user_name = fire.db.child('users').child(UID).child('user-data').child('name').get().val()
                        user.update({'name': user_name, 'UID': UID})

                        home()

                    except:
                        error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                        error_window_rect.center = (400, 300)
                        error_message = "Sign in failed. Redirecting to landing page."
                        error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

        signup_surface.fill(BEIGE)

        manager.update(time_delta)
        SCREEN.blit(signup_surface, ORIGIN)
        SCREEN.blit(title, title_rect)
        SCREEN.blit(name_helper, name_helper_rect)
        SCREEN.blit(email_helper, email_helper_rect)
        SCREEN.blit(password_helper, password_helper_rect)
        SCREEN.blit(confirm_password_helper, confirm_password_helper_rect)
        pygame.draw.line(SCREEN, BROWN, (100, 100), (700, 100), width=2)
        manager.draw_ui(SCREEN)

        pygame.display.update()

# Home page
def home():
    global run

    home_surface = pygame.Surface((WIDTH, HEIGHT))
    dashboard_surface = pygame.Surface((740, 465))
    number_surface = pygame.Surface((740, 465))
    
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
    dashboard_manager = pygame_gui.UIManager((740, 465), 'theme.json')


    # Dashboard title
    title_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 40)
    title = title_font.render('DASHBOARD', True, BLACK, BEIGE)
    title_rect = title.get_rect()
    title_rect.bottomleft = (27, 80)


    # Dashboard content attributes
    number_rect = pygame.Rect(ORIGIN, (40, 40))
    number_rect.center = (20, 18)
    number = pygame_gui.elements.UILabel(relative_rect=number_rect, 
                                        text='#',
                                        manager=dashboard_manager,
                                        object_id=ObjectID('dashboard_table_label'))

    name_rect = pygame.Rect(ORIGIN, (135, 40))
    name_rect.center = (110, 18)
    name = pygame_gui.elements.UILabel(relative_rect=name_rect, 
                                        text='NAME',
                                        manager=dashboard_manager,
                                        object_id=ObjectID('dashboard_table_label'))

    best_price_rect = pygame.Rect(ORIGIN, (160, 40))
    best_price_rect.center = (255, 18)
    best_price = pygame_gui.elements.UILabel(relative_rect=best_price_rect, 
                                        text='BEST PRICE',
                                        manager=dashboard_manager,
                                        object_id=ObjectID('dashboard_table_label'))

    best_site_rect = pygame.Rect(ORIGIN, (145, 40))
    best_site_rect.center = (410, 18)
    best_site = pygame_gui.elements.UILabel(relative_rect=best_site_rect, 
                                        text='BEST SITE',
                                        manager=dashboard_manager,
                                        object_id=ObjectID('dashboard_table_label'))

    url_rect = pygame.Rect(ORIGIN, (260, 40))
    url_rect.center = (610, 18)
    url = pygame_gui.elements.UILabel(relative_rect=url_rect, 
                                        text='URL',
                                        manager=dashboard_manager,
                                        object_id=ObjectID('dashboard_table_label'))


    # Core Buttons
    add_button_rect = pygame.Rect(ORIGIN, (155, 50))
    add_button_rect.center = (180, 540)
    add_button = pygame_gui.elements.UIButton(relative_rect=add_button_rect,
                                                text='ADD',
                                                manager=manager,
                                                object_id=ObjectID('dashboard_button'))

    view_button_rect = pygame.Rect(ORIGIN, (155, 50))                                                
    view_button_rect.center = (400, 540)
    view_button = pygame_gui.elements.UIButton(relative_rect=view_button_rect,
                                                text='VIEW',
                                                manager=manager,
                                                object_id=ObjectID('dashboard_button'))

    delete_button_rect = pygame.Rect(ORIGIN, (155, 50))                                                
    delete_button_rect.center = (620, 540)
    delete_button = pygame_gui.elements.UIButton(relative_rect=delete_button_rect,
                                                text='DELETE',
                                                manager=manager,
                                                object_id=ObjectID('dashboard_button'))
    

    # Core
    current_y = 70
    delta_y = 40
    count = 0

    isClicked = False

    hover_rects = []

    try:
        required = utils.show(user['UID'])
        keys = list(required.keys())

    except:
        required = 'Your list is empty! Please add some items.'

    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0


        if required != 'Your list is empty! Please add some items.':
            isEmpty = False

            # Tabulation
            new_number_rect = pygame.Rect(ORIGIN, (40, 40))
            new_number_rect.center = (20, current_y)

            new_name_rect = pygame.Rect(ORIGIN, (135, 40))
            new_name_rect.center = (110, current_y)

            new_best_price_rect = pygame.Rect(ORIGIN, (160, 40))
            new_best_price_rect.center = (255, current_y)

            new_best_site_rect = pygame.Rect(ORIGIN, (145, 40))
            new_best_site_rect.center = (410, current_y)

            new_url_rect = pygame.Rect(ORIGIN, (260, 40))
            new_url_rect.center = (610, current_y)
            
            if len(required) != count:
                for nick, data in required.items():
                    pygame_gui.elements.UILabel(relative_rect=new_number_rect, 
                                                text=str(count+1), 
                                                manager=dashboard_manager, 
                                                object_id=ObjectID('dashboard_table_label'))

                    pygame_gui.elements.UILabel(relative_rect=new_name_rect, 
                                                text=nick, 
                                                manager=dashboard_manager, 
                                                object_id=ObjectID('dashboard_table_label'))
                    
                    pygame_gui.elements.UILabel(relative_rect=new_best_price_rect, 
                                                text=str(data['price'] if data['price'] != inf else 'Out of stock'), 
                                                manager=dashboard_manager, 
                                                object_id=ObjectID('dashboard_table_label'))

                    pygame_gui.elements.UILabel(relative_rect=new_best_site_rect, 
                                                text=data['website'], 
                                                manager=dashboard_manager, 
                                                object_id=ObjectID('dashboard_table_label'))

                    pygame_gui.elements.UILabel(relative_rect=new_url_rect, 
                                                text=data['URL'][:21] + '.'*3, 
                                                manager=dashboard_manager, 
                                                object_id=ObjectID('dashboard_table_label'))

                    hover_rect = pygame.Rect(ORIGIN, (740, 40))
                    hover_rect.center = (370, current_y + 100)
                    
                    hover_rects.append(hover_rect)
                    
                    current_y += delta_y
                    
                    new_number_rect.center = (20, current_y)
                    new_name_rect.center = (110, current_y)
                    new_best_price_rect.center = (255, current_y)
                    new_best_site_rect.center = (410, current_y)
                    new_url_rect.center = (610, current_y)

                    count += 1

            else:
                pass
        

            # Tile selection
            pos = pygame.mouse.get_pos()
            for hover_rect in hover_rects:
                w, h = hover_rect.width, hover_rect.height
                hovered_surface = pygame.Surface((w, h))

                x, y = hover_rect.x, hover_rect.y
                hover_rect.x += 30

                if hover_rect.collidepoint(pos):
                    hovered_surface.set_alpha(128)
                    hovered_surface.fill(HOVERED_GREY)
                    dashboard_surface.blit(hovered_surface, (x, y - 100))

                    if pygame.mouse.get_pressed()[0]:
                        isClicked = True
                        selected_rect = hover_rect
                        ind = hover_rects.index(hover_rect)

                    if pygame.mouse.get_pressed()[2]:
                        isClicked = False
                        selected_rect = None
                        ind = None

                else:
                    hovered_surface.set_alpha(128)
                    hovered_surface.fill(WHITE)
                    dashboard_surface.blit(hovered_surface, (x, y - 100))

                hover_rect.x, hover_rect.y = x, y

        else:
            isEmpty = True

            message_font = pygame.font.Font('Assets/Montserrat-Regular.ttf', 28)
            message = message_font.render(required, True, BLACK, WHITE)
            message_rect = message.get_rect()
            message_rect.center = (370, 232)

        if isClicked:
            view_button.enable()
            delete_button.enable()

            content = required[keys[ind]]
            key = keys[ind]
            user.update({'content': content})

            w, h = selected_rect.width, selected_rect.height
            x, y = selected_rect.x, selected_rect.y
            selected_surface = pygame.Surface((w, h))
            selected_surface.set_alpha(128)
            selected_surface.fill(SELECTED_GREY)
            dashboard_surface.blit(selected_surface, (x, y - 100))
        
        else:
            view_button.disable()
            delete_button.disable()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            manager.process_events(event)
            dashboard_manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == add_button:
                    add()

                if event.ui_element == view_button:
                    req = dict(fire.db.child('users').child(user['UID']).child('tracking-data').child(key).get().val())
                    for platform, data in req.items():
                        webbrowser.open_new_tab(data['url'])

                if event.ui_element == delete_button:
                    delete_confirmation_window_rect = pygame.Rect(ORIGIN, (460, 360))
                    delete_confirmation_window_rect.center = (400, 300)
                    delete_confirmation_window = pygame_gui.windows.UIConfirmationDialog(rect=delete_confirmation_window_rect, 
                                                                manager=manager, 
                                                                action_long_desc=f'Are you sure you would like to delete {key}?', 
                                                                window_title='ATTENTION!', 
                                                                action_short_name='DELETE',
                                                                blocking=True,)

            if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                if event.ui_element == delete_confirmation_window:
                    utils.delete(user['UID'], key)

                    home()
            
        
        home_surface.fill(BEIGE)
        number_surface.fill(WHITE)

        manager.update(time_delta)
        dashboard_manager.update(time_delta)
        SCREEN.blit(home_surface, ORIGIN)
        pygame.draw.rect(SCREEN, BROWN, pygame.Rect((28, 103), (744, 469)))

        if isEmpty:
            dashboard_surface.blit(message, message_rect)

        SCREEN.blit(dashboard_surface, (30, 105))
        SCREEN.blit(title, title_rect)
        pygame.draw.line(SCREEN, BLACK, (25, 75), (300, 75), width=2)
        dashboard_surface.blit(number_surface, ORIGIN)
        manager.draw_ui(SCREEN)
        dashboard_manager.draw_ui(dashboard_surface)

        pygame.display.update()

# Item add page
def add():
    global run

    add_surface = pygame.Surface((WIDTH, HEIGHT))
    
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')


    title_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Medium.ttf'), 69)
    title = title_font.render('ADD NEW ITEMS', True, BLACK, BEIGE)
    title_rect = title.get_rect()
    title_rect.center = (400, 65)


    helper_font = pygame.font.Font(os.path.join('Assets', 'Montserrat-Regular.ttf'), 16)
    name_helper = helper_font.render('Category name: ', True, BLACK, BEIGE)
    amazon_url_helper = helper_font.render('Amazon URL: ', True, BLACK, BEIGE)
    flipkart_url_helper = helper_font.render('Flipkart URL: ', True, BLACK, BEIGE)
    name_helper_rect = name_helper.get_rect()
    amazon_url_helper_rect = amazon_url_helper.get_rect()
    flipkart_url_helper_rect = flipkart_url_helper.get_rect()
    name_helper_rect.bottomleft = (120, 180)
    amazon_url_helper_rect.bottomleft = (120, 267)
    flipkart_url_helper_rect.bottomleft = (120, 355)


    name_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((115, 180), (570, 50)),
                                                        manager=manager,
                                                        object_id=ObjectID('regular_text_entry_line'))

    amazon_url_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((115, 267), (570, 50)),
                                                                manager=manager,
                                                                object_id=ObjectID('regular_text_entry_line'))

    flipkart_url_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((115, 355), (570, 50)),
                                                                manager=manager,
                                                                object_id=ObjectID('regular_text_entry_line'))

    add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((440, 480), (160, 70)),
                                                text='ADD',
                                                manager=manager,
                                                object_id=ObjectID('login_button'))

    cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 480), (160, 70)),
                                                text='CANCEL',
                                                manager=manager,
                                                object_id=ObjectID('signup_button'))

    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == add_button:
                    name = name_text_box.get_text()
                    amazon_url = amazon_url_text_box.get_text()
                    flipkart_url = flipkart_url_text_box.get_text()

                    URL = []

                    if (len(name) != 0) and (len(amazon_url) != 0) and (len(flipkart_url) != 0):
                        URL.extend([amazon_url, flipkart_url])
                        count = 0
                        success = False

                        try:
                            for url in URL:
                                if utils.add(user['UID'], url, name):
                                    count += 1

                            if count == 2:
                                success = True

                        except:
                            success = False
                                                
                        if success:
                            success_window_rect = pygame.Rect(ORIGIN, (460, 360))
                            success_window_rect.center = (400, 300)
                            success_message = f"You're now tracking {name}!"
                            success_window=pygame_gui.windows.UIMessageWindow(success_window_rect, success_message, manager=manager, window_title='SUCCESS!')

                        else:
                            error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                            error_window_rect.center = (400, 300)
                            error_message = "Addition of data failed. Please ensure correctness of data."
                            error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

                    else:
                        error_window_rect = pygame.Rect(ORIGIN, (460, 360))
                        error_window_rect.center = (400, 300)
                        error_message = "None of the fields can be empty! Please fill them in."
                        error_window=pygame_gui.windows.UIMessageWindow(error_window_rect, error_message, manager=manager, window_title='ERROR!')

                if event.ui_element == cancel_button:
                    home()

        add_surface.fill(BEIGE)

        manager.update(time_delta)
        SCREEN.blit(add_surface, ORIGIN)
        SCREEN.blit(title, title_rect)
        SCREEN.blit(name_helper, name_helper_rect)
        SCREEN.blit(amazon_url_helper, amazon_url_helper_rect)
        SCREEN.blit(flipkart_url_helper, flipkart_url_helper_rect)
        pygame.draw.line(SCREEN, BROWN, (100, 100), (700, 100), width=2)
        manager.draw_ui(SCREEN)

        pygame.display.update()

if __name__ == '__main__':
    landing()
