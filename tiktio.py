import subprocess
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.options import Options
import pickle
from uiautomator import Device
def open_browser():
    global driver
    options = Options()
    #options.add_argument('--user-data-dir=sesion')
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)

    driver.maximize_window()
con = 0
errrrroo = 0
stop_def_like_con = 0
Subscribe_erro_stop_time= 'start'
like_erro_stop_time = 'start'
stop_def_Subscribe = 'start'
stop_def_like = 'start'
stop_def_pinterest = 'start'
stop_def_instagram = 'start'
stop_def_instagram_follow = 'start'
stop_def_instagram_like = 'start'
def cookis_like():
    global driver
    for cookie in cookies:

        fields = cookie.strip().split('\t')
        if len(fields) >= 7:
            cookie_dict = {'name': fields[5],'value': fields[6],'domain': fields[0],'path': fields[2],'expires': int(fields[4]),'secure': bool(fields[3])}
            driver.add_cookie(cookie_dict)
    driver.refresh()

def like3like_login():
    global email
    global driver
    current_url = driver.current_url
    if current_url=='https://www.like4like.org/login/':

        print('https://www.like4like.org/login/')
        for cookies_totel in os.listdir(os.getcwd()):
            cookies_totel_1 = cookies_totel.split('_cookies')[0]
            if cookies_totel_1=='like':
                email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
                print(email)
                password = '1234thelove'
                driver.get("https://www.like4like.org/login/")
                #time.sleep(2)
                driver.find_element(By.ID, 'username').send_keys(email)
                #time.sleep(2)
                driver.find_element(By.ID, 'password').send_keys(password)
                time.sleep(2)
                driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)
                time.sleep(2)
                driver.get("https://www.like4like.org/user/")
                time.sleep(2)
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/user/':
                    print(current_url)
                    print('login_usearname_passowrd')
                    driver.get("https://www.like4like.org/#social-media-platform-list")
                    time.sleep(2)
                    cookies_add = "like_cookies_{}.pkl".format(email)
                    pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
                    '''
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like_1 = 'true_login'
                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like_1}}
                    )
                    '''
                    print('login_usearname_passowrd_true')

                else:
                    print('first_logon_cookies')
                    driver.get("https://www.like4like.org/#social-media-platform-list")
                    cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
                    for cookie in cookies:
                        try:
                            driver.add_cookie(cookie)
                        except Exception as ss:
                            print(ss)
                            continue
                    driver.get("https://www.like4like.org/user/")
                    time.sleep(15)
                    current_url = driver.current_url
                    if current_url=='https://www.like4like.org/user/':
                        '''
                        email_to_find = email
                        user_data = collection.find_one({"email": email_to_find})
                        new_login_like_2 = 'login_cookies'
                        collection.update_one(
                            {"email": email_to_find},
                            {"$set": {"login_like": new_login_like_2}}
                        )
                        print('first_logon_cookies_true')
                        '''
                        pass
                    else:
                        print('first_logon_cookies_flase')
                        '''
                        email_to_find = email
                        user_data = collection.find_one({"email": email_to_find})
                        new_login_like = 'false'

                        collection.update_one(
                            {"email": email_to_find},
                            {"$set": {"login_like": new_login_like}}
                        )
                        driver.quit()
                        '''
                        pass
def like3like_login_first():

    for cookies_totel in os.listdir(os.getcwd()):
        cookies_totel_1 = cookies_totel.split('_cookies')[0]
        if cookies_totel_1=='like':
            email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
            print(email)
            password = '1234thelove'
            driver.get("https://www.like4like.org/login/")
            #time.sleep(2)
            driver.find_element(By.ID, 'username').send_keys(email)
            #time.sleep(2)
            driver.find_element(By.ID, 'password').send_keys(password)
            time.sleep(2)
            driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.get("https://www.like4like.org/user/")
            time.sleep(20)
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/user/':
                print(current_url)
                driver.get("https://www.like4like.org/#social-media-platform-list")
                time.sleep(1)
                cookies_add = "like_cookies_{}.pkl".format(email)
                pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
                '''
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like_4 = 'login_fisrt_cookies'
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like_4}}
                )
                '''
            else:
                print('else')
                driver.get("https://www.like4like.org/#social-media-platform-list")
                cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
                for cookie in cookies:
                    try:
                        driver.add_cookie(cookie)
                    except Exception as ss:
                        print(ss)
                        continue
                driver.get("https://www.like4like.org/user/")
                time.sleep(1)
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/user/':
                    print('login_cookies')
                    '''
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like_6 = 'login_cookies'
                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like_6}}
                    )
                    '''
                else:
                    print('false_cookies')
                    '''
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like = 'false_cookies'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like}}
                    )
                    driver.quit()
                    sys.exit()
                    '''

'''
email_confirm = 'theloveme_{}@fextemp.com'.format(email.split('_')[-1])
password = '1234thelove'
driver.get("https://www.pinterest.com/")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '[data-test-id="simple-login-button"]').click()
time.sleep(1)
driver.find_element(By.ID, 'email').send_keys(email_confirm)
time.sleep(1)
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '[data-test-id="registerFormSubmitButton"]').click()
time.sleep(5)



    if cookies_totel_1=='youtube':
        driver.get("https://www.youtube.com/")
        print(cookies_totel)

        for cookies_totel in os.listdir(os.getcwd()):
            cookies_totel_1 = cookies_totel.split('_cookies')[0]
            if cookies_totel_1=='youtube':

                email = cookies_totel.split('youtube_cookies_')[-1].split('.txt')[0]
                with open(cookies_totel, 'r') as file:
                    cookies = file.readlines()
                cookis_like()
                driver.get("https://www.youtube.com/account")
                time.sleep(1)
                account_true = driver.current_url
                if account_true=='https://www.youtube.com/account' or account_true=='https://www.youtube.com/account/':

                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_youtube = 'youtube_cookies_true'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_youtube": new_login_youtube}}
                        )
                else:

                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_youtube = 'youtube_cookies_false'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_youtube": new_login_youtube}}
                        )
                    driver.quit()
                    sys.exit()
                '''

def like4like_login_instgram():
    global stop_def_instagram_follow
    global stop_def_instagram_like
    for cookies_totel in os.listdir(os.getcwd()):
        cookies_totel_1 = cookies_totel.split('_cookies')[0]
        print(cookies_totel_1)
        if cookies_totel_1=='instagram':
            driver.get("https://www.instagram.com")
            try:
                driver.find_element(By.XPATH,'//*[text()="Allow all cookies"]').click()
            except:
                pass
            time.sleep(10)
            try:
                email_2 = cookies_totel.split('instagram_cookies_')[-1].split('_pas_')[0]
                password_2 = cookies_totel.split('_pas_')[-1].split('_n')[0]
                print(email_2)
                driver.find_element(By.NAME, 'username').send_keys(email_2)
                time.sleep(1)
                driver.find_element(By.NAME, 'password').send_keys(password_2)
                time.sleep(1)
                driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
            except Exception as s:
                print(s)
            time.sleep(5)
            driver.get("https://www.instagram.com/direct/inbox/")
            time.sleep(5)
            login_instgram_true_login = driver.current_url.split('accounts/')[-1].split('/?')[0]
            login_instgram = driver.current_url
            if login_instgram== 'https://www.instagram.com/direct/inbox/' or login_instgram== 'https://www.instagram.com/direct/inbox':
                print('login_username_password')
            else:
                print('erro_username_password')
                print(current_url)
                print('erro_username_password')


            '''
            with open('{}'.format(cookies_totel), 'r') as file:
                cookies = file.readlines()
            for cookie in cookies:
                fields = cookie.strip().split('\t')
                if len(fields) >= 7:
                    cookie_dict = {'name': fields[5],'value': fields[6],'domain': fields[0],'path': fields[2],'expires': int(fields[4]),'secure': bool(fields[3])}
                    driver.add_cookie(cookie_dict)

            driver.get("https://www.instagram.com/direct/inbox/")

            time.sleep(10)
            login_instgram = driver.current_url
            login_instgram_true = driver.current_url.split('accounts/')[-1].split('/?')[0]
            if login_instgram=='https://www.instagram.com/direct/inbox/' or login_instgram=='https://www.instagram.com/direct/inbox':
                print('login_true_insgram')
            elif login_instgram_true =='login':
                email_2 = cookies_totel.split('instagram_cookies_')[-1].split('_pas_')[0]
                password_2 = cookies_totel.split('_pas_')[-1].split('_n')[0]
                time.sleep(1)
                driver.find_element(By.NAME, 'username').send_keys(email_2)
                time.sleep(1)
                driver.find_element(By.NAME, 'password').send_keys(password_2)
                time.sleep(1)
                driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
                time.sleep(5)
                driver.get("https://www.instagram.com/direct/inbox/")
                time.sleep(5)
                login_instgram_true_login = driver.current_url.split('accounts/')[-1].split('/?')[0]
                login_instgram = driver.current_url
                if login_instgram=='https://www.instagram.com/direct/inbox/' or login_instgram=='https://www.instagram.com/direct/inbox':
                    print('login_username_password')

                    cookies = driver.get_cookies()
                    with open('{}'.format(cookies_totel), 'w', encoding='utf-8') as file:
                        for cookie in cookies:
                            # Check if 'expiry' exists in the cookie dictionary
                            expiry = cookie.get('expiry', 0)

                            file.write(
                                f"{cookie['domain']}\t"  # Domain
                                f"{str(cookie['domain'].startswith('.'))}\t"  # Domain Flag
                                f"{cookie['path']}\t"  # Path
                                f"{str(cookie['secure'])}\t"  # Secure Flag
                                f"{expiry}\t"  # Expiry
                                f"{cookie['name']}\t"  # Cookie Name
                                f"{cookie['value']}\n"  # Cookie Value
                            )


                elif login_instgram_true_login=='suspended':
                    print('suspended_instagram')
                    stop_def_instagram_follow = 'stop'
                    stop_def_instagram_like  = 'stop'
                    sys.exit()
                '''

        else:
            pass
            #print('errroo')
            #print(driver.current_url)
            #sys.exit()

def limeit_all_ike4like():
    global driver
    if like_erro_stop_time == 'stop':#Subscribe_erro_stop_time == 'stop' and

        email_to_find = email
        user_data = collection.find_one({"email": email_to_find})
        failed_stop_all = 'Sub_like'
        collection.update_one(
            {"email": email_to_find},
            {"$set": {"limit": failed_stop_all}})
        print('failed_stop_all_like4like')
        sys.exit()
def check_driver_open():
    try:
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as ddfrs:
        print('check_driver_open: ' , ddfrs)
def no_Window_driver():
    global driver
    print('NoSuchWindowException_stop')
    folder_path = '/home/developer/.mozilla/firefox'
    file_names = os.listdir(folder_path)

    for name in file_names:
        name_firefox = name.split('default-')[-1]
        if name_firefox == 'release':
            name_path_firefox = '/home/developer/.mozilla/firefox/' + name
            print(name_path_firefox)
    firefox_options = webdriver.FirefoxOptions()
    profile_path = name_path_firefox
    firefox_options.profile = profile_path
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options)#, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.like4like.org/#social-media-platform-list")
    time.sleep(10)
    like3like_login()
    print('NoSuchWindowException_open')
def failed_success_minutes():
    global Subscribe_erro_stop_time
    global like_erro_stop_time
    global driver
    global stop_def_Subscribe
    global stop_def_like
    global stop_def_like_con
    global stop_def_pinterest
    global stop_def_instagram_follow
    global stop_def_instagram_like
    try:
        erro_minutes=driver.find_element(By.ID, 'error-text').text
        You_have_failed  = erro_minutes.split(' success rate validation')[0]
        if You_have_failed == str('You have failed our'):
            print('You have failed our')


            minutes_to_add =  erro_minutes.split('next ')[-1].split(' minutes.')[0]
            print(minutes_to_add)
            current_time = datetime.utcnow()
            time_delta = timedelta(minutes=int(minutes_to_add))
            new_time = current_time + time_delta
            new_date = new_time.date()
            formatted_time = new_time.strftime('%H:%M')
            failed_success= "date:" + str(new_date) + "time:"+ str(formatted_time)
            print(failed_success)
            print('You have failed our')
            print('You have failed our')
            print('You have failed our')
            input('You have failed our')
            seconds_to_wait = minutes_to_add * 60
            # الانتظار لعدد الثواني المحدد
            time.sleep(seconds_to_wait)
            '''
            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            '''


            current_url = driver.current_url
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtubes':
                print('Subscribe_erro_stop_time')
                Subscribe_erro_stop_time = 'stop'
                stop_def_Subscribe= 'stop'
                collection.update_one(
                {"email": email_to_find},
                {"$set": {"limit_sub": failed_success}})
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtube':
                print('like_erro_stop_time')
                like_erro_stop_time = 'stop'
                stop_def_like  = 'stop'
                collection.update_one(
                {"email": email_to_find},
                {"$set": {"limit_like": failed_success}})
            ##instagram
            '''
            if current_url=='https://www.like4like.org/user/earn-instagram-follow.php':
                stop_def_instagram_follow = 'stop'

            if current_url=='https://www.like4like.org/user/earn-instagram-like.php':
                stop_def_instagram_like = 'stop'
            '''
        if erro_minutes == 'No tasks are currently available, please try again later...':
            print('No tasks are currently available')
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtubes':
                print('Subscribe_erro_stop_time')
                stop_def_Subscribe= 'stop'
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtube':
                print('like_erro_stop_time')
                if stop_def_like_con == 3:
                    print('stop_def_like_con')
                    stop_def_like  = 'stop'
                stop_def_like_con +=1
                print('stop_def_like_con',stop_def_like_con)
            if current_url=='https://www.like4like.org/user/earn-pinterest-follow.php"':
                print('pinteresterro_stop_time')
                stop_def_pinterest  = 'stop'
                print('stop_def_pinterest_con',stop_def_pinterest)
        #driver.quit()
    except NoSuchWindowException:
        print('failed_success_minutes')
        no_Window_driver()
        like3like_login()

    except NoSuchElementException:
        limeit_all_ike4like()
        like3like_login()
        print('NoSuchElementException_failed_success_minutes')
    except Exception as ssssd2:
        like3like_login()
        print('failed_success_minutes:  ',ssssd2)
def Subscribe_erroo():
    global driver
    global con_sub
    failed_success_minutes()
    limeit_all_ike4like()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
    time.sleep(10)
    like3like_login()
    check_driver_open()
    if Subscribe_erro_stop_time == 'stop':
        print('stop_Subscribe')
        #like()
    con_sub +=1
    if con_sub == 5:
        print('con_sub')
        #like()
def Subscribe():
    global driver
    global con_sub
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
    con_sub = 0
    for s in range(25):
        try:

            driver.maximize_window()
            driver.implicitly_wait(15)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
            time.sleep(5)
            if stop_def_Subscribe == 'stop':
                print('stop_def_Subscribe_stop_def_Subscribe_stop_def_Subscribe')
                break
            driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()

            #element_control_click.click()
            driver.switch_to.window(driver.window_handles[-1])
            subscribe_button = driver.find_element(By.CSS_SELECTOR, "div#subscribe-button button span.yt-core-attributed-string").text
            if subscribe_button== "Subscribe" or subscribe_button == "اشتراك":
                sub_old_count = driver.find_element(By.ID, 'subscriber-count').text
                time.sleep(2)
                driver.find_element(By.ID, 'subscribe-button').click()
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                sub_new_count = driver.find_element(By.ID, 'subscriber-count').text
                if sub_new_count == sub_old_count:
                    print('sub_old_count:',sub_old_count)
                    print('==')
                    print('sub_new_count:',sub_new_count)
                    if 'K' in sub_new_count or 'ألف' in sub_new_count:
                        result = "find"
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(5)
                        driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
                    else:
                        result = "no fond"
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(5)
                        driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")

                    print(result)


                elif sub_old_count < sub_new_count  :
                    print('_______________________________________________________________')
                    print('sub_old_count:',sub_old_count)
                    print('<')
                    print('sub_new_count:',sub_new_count)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()

                elif sub_old_count > sub_new_count:
                    print('_______________________________________________________________')
                    print('sub_old_count:',sub_old_count)
                    print('>')
                    print('sub_new_count:',sub_new_count)
                    '''
                    driver.find_element(By.CSS_SELECTOR, "#items > ytd-menu-service-item-renderer:nth-child(4)").click()
                    time.sleep(2)
                    driver.find_element(By.CSS_SELECTOR, "#confirm-button > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill").click()
                    time.sleep(2)
                    '''
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
                else:
                    print('خطاء')



            else:
                print('unsubscribe')
                '''
                driver.switch_to.window(driver.window_handles[1])

                driver.find_element(By.ID, 'subscribe-button').click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[4]]").click()
                time.sleep(2)
                '''
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.randrange(3, 7))
                driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")



            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            if user_data:
                current_sub_value = int(user_data.get("sub", 0))
                new_sub_value = current_sub_value + 1
                print('sub', int(new_sub_value))
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"sub": new_sub_value}}
                )

            else:

                pass
        except NoSuchWindowException:
            print('sub: NoSuchWindowException_stop')
            no_Window_driver()
            like3like_login()
            print('sub: NoSuchWindowException_open')
        except NoSuchElementException:
            print('NoSuchElementException_sub')
            Subscribe_erroo()


        except Exception as s2:
            print('Subscribe_erroo:   ',s2)
            Subscribe_erroo()

def like_erro():
    global driver
    global con_like
    limeit_all_ike4like()
    failed_success_minutes()
    try:
        if like_erro_stop_time == 'stop':
            print('Subscribe__stop_time_NoSuchElementException')
            Subscribe()
        con_like+=1
        if con_like == 5:
            print('con_like')
            stop_def_like  = 'stop'
            #Subscribe()

        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(10)
        like3like_login()
        check_driver_open()


    except Exception as s3:
        print(s3)

def like():
    global driver
    global con_like
    my_list_like = []
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    con_like = 0
    con_like_2 = 0
    con_like_3 = 0

    for s in range(100):
        try:

            driver.maximize_window()
            driver.implicitly_wait(15)


            if stop_def_like == 'stop':
                print('stop_def_like_stop_def_like_stop_def_like')
                driver.quit()
                break
            time.sleep(5)
            element_control_click = driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']")
            driver.execute_script("arguments[0].click();", element_control_click)
            onclick_value = element_control_click.get_attribute("onclick").split('https://www.youtube.com/watch?v=')[-1].split("'")[0]
            value_to_search = onclick_value

            if value_to_search in my_list_like:
                print("skip")
                driver.find_element(By.CSS_SELECTOR, "a.cursor").click()
            else:
                print("no_skip")
                element_control_click = driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(2)
                element_with_aria_label = driver.find_element(By.ID, 'segmented-like-button')
                aria_label_elements = element_with_aria_label.find_elements(By.XPATH, './/*[@aria-label]')
                aria_label_values = [element.get_attribute("aria-label") for element in aria_label_elements]
                for value_aria_label in aria_label_values:
                        print(value_aria_label)
                like_old_count = value_aria_label.replace('like this video along with', '').replace('other people', '').strip().replace('likes', '').strip().replace('معجبين', '').strip().replace('أبدى إعجابه بهذا الفيديو إضافة إلى', '').strip().replace('شخصًا آخر', '').strip().replace('معجبًا', '').strip().replace('أشخاص آخرين', '').strip()#.split(',')
                time.sleep(2)
                driver.find_element(By.ID, 'segmented-like-button').click()
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                element_with_aria_label_2 = driver.find_element(By.ID, 'segmented-like-button')
                aria_label_elements_2 = element_with_aria_label_2.find_elements(By.XPATH, './/*[@aria-label]')
                aria_label_values_2 = [element_2.get_attribute("aria-label") for element_2 in aria_label_elements_2]
                for value_aria_label_2 in aria_label_values_2:
                        print(value_aria_label_2)
                like_new_count = value_aria_label_2.replace('likes', '').strip().replace('like this video along with', '').replace('other people', '').strip().replace('معجبين', '').strip().replace('أبدى إعجابه بهذا الفيديو إضافة إلى', '').strip().replace('شخصًا آخر', '').strip().replace('معجبًا', '').strip().replace('أشخاص آخرين', '').strip()#.split(',')
                if like_new_count == like_old_count:
                    my_list_like.append(onclick_value)
                    if con_like_2 == 5:
                        print('con_like_2')
                        break
                    con_like_2 +=1
                    print('like_old_count:',like_old_count)
                    print('==')
                    print('like_new_count:',like_new_count)
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
                    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                elif like_old_count < like_new_count  :
                    print('_______________________________________________________________')
                    print('like_old_count:',like_old_count)
                    print('<')
                    print('like_new_count:',like_new_count)
                    con_like_3 +=1
                    if con_like_3 == 3:
                        print('con_like_2')
                        con_like_2 = 0

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()

                elif like_old_count > like_new_count:
                    my_list_like.append(onclick_value)
                    print('_______________________________________________________________')
                    print('like_old_count:',like_old_count)
                    print('>')
                    print('like_new_count:',like_new_count)
                    time.sleep(2)
                    driver.find_element(By.ID, 'segmented-like-button').click()
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
                    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                else:
                    print('errro')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
                    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})

                if user_data:
                    current_sub_value = int(user_data.get("like", 0))

                    # تعديل القيمة وإضافة +     1
                    new_sub_value = current_sub_value + 1
                    print('like', int(new_sub_value))
                    # تحديث الوثيقة بالقيمة الجديدة لـ sub
                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"like": new_sub_value}}
                        )
        except NoSuchWindowException:
            print('like: NoSuchWindowException_stop')
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            no_Window_driver()
            print('like: NoSuchWindowException_open')
        except NoSuchElementException:
            print('NoSuchElementException_like')
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            like_erro()
        except Exception as s:
            print('Subscribe_erroo:   ',s)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            like_erro()

def pinterest():
    global driver
    driver.get("https://www.like4like.org/user/earn-pinterest-follow.php")

    for s in range(2):
        try:

            if stop_def_pinterest == 'stop':
                print('stop_def_pinterest')
                break
            driver.maximize_window()
            driver.implicitly_wait(15)
            driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="user-follow-button"]').click()
            time.sleep(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
        except Exception as a:
            print(a)
            failed_success_minutes()
            check_driver_open()
            no_Window_driver()
def pinterest_save():
    global driver
    driver.get("https://www.like4like.org/earn-credits.php?feature=pinterestrep")

    for s in range(5):
        try:

            driver.maximize_window()
            driver.implicitly_wait(15)
            driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="quick-save-button"]').click()
            time.sleep(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
        except Exception as a:
            print(a)
            driver.get("https://www.like4like.org/earn-credits.php?feature=pinterestrep")
            failed_success_minutes()
            check_driver_open()
            no_Window_driver()
def instagram_follow_erro():
    current_url = driver.current_url
    challenge_node_id  = current_url.split('instagram.com/')[-1].split('/?challenge_node_id')[0]
    if challenge_node_id == 'challenge':
        print('challenge')
        print(current_url)
        print('challenge_node_id')
        #driver.find_element(By.XPATH, "//*[text()='Change Password']")
        #sys.exit()
        try:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
        except:
            pass
        try:
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
        except:
            pass
        input('stop_________________challenge_node_id')
    challenge_nw  = current_url.split('instagram.com/')[-1].split('/?next')[0]
    if challenge_nw == 'challenge':
        print('challenge_challenge_challenge_challenge_challenge_challenge_challenge_challenge_challenge')
        driver.find_element(By.XPATH, "//*[text()='Dismiss']").click()
        print('challenge_challenge_challenge_challenge_challenge_challenge_challenge_challenge_challenge')

    if current_url == 'https://www.instagram.com/?__coig_restricted=1' or  current_url == 'https://www.instagram.com/?__coig_restricted=1/':
        print('coig_restricte___')
        print('coig_restricte___')
        print('coig_restricte___')
        print(current_url)
        print('coig_restricte___')
        print('coig_restricte___')
        print('coig_restricte___')
        driver.delete_all_cookies()
        like4like_login_instgram()
        like3like_login_first()
        print('coig_restricte')

    if current_url == 'https://www.like4like.org/user/bonus-page.php' or  current_url == 'https://www.like4like.org/user/bonus-page.php/':
        print('erro_https://www.like4like.org/user/bonus-page.php')
        print('erro_https://www.like4like.org/user/bonus-page.php')
        print('erro_https://www.like4like.org/user/bonus-page.php')
        print('erro_https://www.like4like.org/user/bonus-page.php')
        ##result > div > a:nth-child(8)
        ##result > div > a:nth-child(6)

        for a in range(8):
            rand = random.randrange(2,8)
            print(a)
            try:
                driver.find_element(By.CSS_SELECTOR, "#result > div > a:nth-child({})".format(rand)).click()
                break
            except:
                print('errobonus-page.php')
        #input('erro_https://www.like4like.org/user/bonus-page.php')
def instagram_follow():
    global driver
    my_list_like = []
    try:
        with open('unfollowing.txt', 'r') as file:
            flowws = file.readlines()
        for addfw in flowws:
            my_list_like.append(addfw.strip())
    except:
        print('add_list')
    driver.get("https://www.like4like.org/user/earn-instagram-follow.php")
    time.sleep(5)
    page_height = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(1920, page_height)
    con_follows = 1
    con_follows_stop = 0
    for s in range(15):
        try:

            if stop_def_instagram_follow == 'stop':
                print('stop_def_instagram_follow')
                break
            #driver.maximize_window()
            driver.implicitly_wait(15)
            element_control_click = driver.find_element(By.CSS_SELECTOR,"a[class^='cursor earn_pages_button profile_view_img']")
            onclick_value = element_control_click.get_attribute("onclick").split('instagram.com/')[-1].split("'")[0]
            if onclick_value in my_list_like:
                print("skip")
                driver.find_element(By.CSS_SELECTOR, "a.cursor").click()
            else:
                driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
                driver.switch_to.window(driver.window_handles[1])

                time.sleep(2)
                login_instgram_true_2 = driver.current_url.split('accounts/')[-1].split('/?')[0]
                instagram_follow_erro()
                if login_instgram_true_2=='suspended':
                    print('suspended')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.close()
                    input('suspended_suspended')
                    break
                try:
                    driver.find_element(By.XPATH, "//*[text()='Follow']").click()
                    time.sleep(5)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(2)
                    driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()

                    if con_follows == con_follows_stop:

                        break
                    con_follows_stop +=1
                    print('follows_{}'.format(con_follows_stop))
                    #time.sleep(random.randrange(80, 200))
                    #time.sleep(random.randrange(50,200))
                except:

                    try:
                        driver.find_element(By.XPATH, "//*[text()='Following']")
                        print('unfollowing')
                        my_list_like.append(onclick_value)
                        with open('unfollowing.txt', 'a', encoding='utf-8') as result:
                            result.write("\n")
                            result.write(onclick_value)
                        time.sleep(5)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(2)
                        driver.get("https://www.like4like.org/user/earn-instagram-follow.php")
                        time.sleep(5)
                        page_height = driver.execute_script("return document.body.scrollHeight;")
                        driver.set_window_size(1920, page_height)
                    except:
                        text_instgeram = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/span").text
                        print(text_instgeram)
                        my_list_like.append(onclick_value)
                        with open('unfollowing.txt', 'a', encoding='utf-8') as result:
                            result.write("\n")
                            result.write(onclick_value)
                        time.sleep(5)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(2)
                        driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()


        except Exception as a:
            print(a)
            driver.save_screenshot('1.png')
            instagram_follow_erro()
            failed_success_minutes()
            check_driver_open()
            #no_Window_driver()
            driver.get("https://www.like4like.org/user/earn-instagram-follow.php")
            time.sleep(5)
            page_height = driver.execute_script("return document.body.scrollHeight;")
            driver.set_window_size(1920, page_height)
def instagram_like():
    global driver
    driver.get("https://www.like4like.org/user/earn-instagram-like.php")
    time.sleep(5)
    page_height = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(1920, page_height)
    for s in range(1):
        try:
            if stop_def_instagram_like == 'stop':
                print('stop_def_instagram_like ')
                break
            #driver.maximize_window()
            driver.implicitly_wait(15)
            driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            login_instgram_true_3 = driver.current_url.split('accounts/')[-1].split('/?')[0]
            instagram_follow_erro()
            if login_instgram_true_3=='suspended':
                print('suspended_instagram_like')
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                break
            try:

                elements = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Like"]')
                last_element = elements[-1]
                last_element.click()
            except:
                text_instgeram = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/span").text
                print(text_instgeram)
            time.sleep(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
            time.sleep(10)
            break
        except Exception as a:
            print(a)
            failed_success_minutes()
            check_driver_open()
            #no_Window_driver()
            driver.get("https://www.like4like.org/user/earn-instagram-like.php")
            instagram_follow_erro()
            time.sleep(5)
            page_height = driver.execute_script("return document.body.scrollHeight;")
            driver.set_window_size(1920, page_height)
def follow_tiktok():
    my_list_like = []
    try:
        with open('unfollowing.txt', 'r') as file:
            flowws = file.readlines()
        for addfw in flowws:
            my_list_like.append(addfw.strip())
    except:
        print('add_list')
    driver.get("https://www.like4like.org/user/earn-tiktok-follow.php")
    page_height = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(1920, page_height)
    for s in range(999999999999999):
        try:

            element_control_click = driver.find_element(By.CSS_SELECTOR,"a[class^='cursor earn_pages_button profile_view_img']")
            onclick_value = element_control_click.get_attribute("onclick").split('tiktok.com/')[-1].split("'")[0]
            print(onclick_value)
            if onclick_value in my_list_like:
                print("skip")
                driver.find_element(By.CSS_SELECTOR, "a.cursor").click()
            else:
                

                time.sleep(2)
                current_url = driver.current_url
                my_list_like.append(onclick_value)
                driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(2)
                with open('unfollowing.txt', 'a', encoding='utf-8') as result:
                        result.write("\n")
                        result.write(onclick_value)
                subprocess.run('adb shell am start -a android.intent.action.VIEW -d "{}"'.format(current_url), shell=True, capture_output=True, text=True)
                d = Device()
                d.wait.idle(timeout=10000)
                contact_name = "Follow"
                d(text=contact_name).click()
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()

        except Exception as s:
            print(s)
            driver.get("https://www.like4like.org/user/earn-tiktok-follow.php")
            page_height = driver.execute_script("return document.body.scrollHeight;")
            driver.set_window_size(1920, page_height)

open_browser()
like3like_login_first()
follow_tiktok
