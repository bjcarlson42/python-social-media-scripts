from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from secrets import pwT
from random import randint


class TwitterBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://twitter.com/')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[1]/div/label/div/div[2]/div/input').send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[2]/div/label/div/div[2]/div/input').send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[3]/div').click()
        sleep(randint(3, 6))

    def tweet(self, msg):
        # click blue 'Tweet' button
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a').click()
        sleep(randint(2, 3))
        # Enter tweet
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span').send_keys(msg)
        sleep(randint(3, 5))
        # Tweet it!
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        sleep(2)

    def unfollow_users_that_follow_me(self, num):
        self.driver.get('https://twitter.com/bencarlsonblog')
        sleep(randint(2, 3))
        self.driver.get('https://twitter.com/bencarlsonblog/followers')
        sleep(randint(4, 7))
        num = 1
        num_unfollowed = 0
        while(True):
            user = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div/div['+str(num)+']/div/div/div/div[2]/div[1]/div[2]/div/div/span/span')
            if(user.get_attribute('innerHTML') == 'Following'):
                user.click()
                sleep(randint(2, 3))
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/span/span').click()
                num_unfollowed += 1
                sleep(1)
            num += 1
        print('Unfollowed', num_unfollowed, 'users who are following you')

    def unfollow_users_in_following(self, numToUnfollow):
        sleep(2)
        self.driver.get('https://twitter.com/bencarlsonblog/following')
        sleep(randint(2, 4))
        num = 1
        for i in range(numToUnfollow):
            # define next user and unfollow
            user = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div/div['+str(num)+']/div/div/div/div[2]/div/div[2]/div/div/span/span').click()
            sleep(2)
            # confirm
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]').click()
            sleep(randint(1, 2))
            num += 1
        print('Unfollowed', numToUnfollow, 'user(s)')

    def like_comment_feed(self, numToLike):
        sleep(2)
        num = 1
        for i in range(1, numToLike):
            try:
                # trys to fins a like btn with this xpath
                like_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                like_button.click()  # like
                num += 1
                print('liked', numToLike)
                sleep(randint(2, 5))
            except:
                print('not found', numToLike)
                sleep(randint(2, 5))

    def comment(self):
        print('comment')


def main():
    try:
        my_bot = TwitterBot('bencarlsonblog', pwT)
    except:
        print('Errror loggin in')
    # try:
    #     my_bot.tweet('Check out my new #blog post! Using #javascript to scramble a Rubiks cube!! \nbenjamincarlson.net//javascript/tutorial/rubiks%20cube/2020/02/28/using-javascript-to-scramble-a-rubiks-cube.html')
    # except:
    #     print('Error tweeting')
    # try:
    #     my_bot.unfollow_users_that_follow_me(5)
    # except:
    #     print('Error unfollow_users_that_follow_me()')
    # try:
    #     my_bot.unfollow_users_in_following(5)
    # except:
    #     print('Error unfollow_users_in_following()')
    my_bot.like_comment_feed(5)


if __name__ == '__main__':
    main()
