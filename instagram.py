from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# from secrets import pw
from random import randint
from datetime import date, time, datetime
import getpass


class InstagramBot():
    #
    # This function logs into Instagram
    #
    # username -- Instagram username
    # password -- Instagram password
    #
    def __init__(self, username):
        password = getpass.getpass(
            prompt='Password for Instagram account ' + username + ' : ', stream=None)
        print('Logging in...')
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(randint(2, 5))
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        # click signin
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        sleep(randint(4, 6))
        # click 'not now'
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()
        print('Logged in at ' + str(datetime.now()))
        sleep(randint(3, 6))

    #
    # This function gets stats before the program executes
    #
    def get_before_stats(self):
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        print('Collecting before stats...')
        # get and print basic profile stats
        posts = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').get_attribute('innerHTML')
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('innerHTML')
        self.get_followers_list()  # a list of the actual users that follow you
        following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('innerHTML')
        self.get_following_list()  # a list of the actual users you are following
        print('You have ' + posts + ' posts')
        print('You have ' + followers + ' followers')
        print('You are following ' + following + ' users')
        print('Finished collecting before stats')

    #
    # This function gets stats after the program is finsihed executing
    #
    def get_after_stats(self):
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        print('Collecting after stats...')
        # get and print basic profile stats
        posts = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').get_attribute('innerHTML')
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('innerHTML')
        self.get_followers_list()  # a list of the actual users that follow you
        following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('innerHTML')
        self.get_following_list()  # a list of the actual users you are following
        print('You have ' + posts + ' posts')
        print('You have ' + followers + ' followers')
        print('You are following ' + following + ' users')
        print('Finished collecting after stats')

    #
    # This function likes and comments on a certian number of posts
    # under a certain hashtag
    #
    # hashtag -- the hashtag you want to use
    # numToLikeAndComment - the number of posts you want to like and comment on
    #
    def like_comment_posts_by_hashtag(self, hashtag, numToLikeAndComment):
        sleep(2)
        self.driver.get('https://www.instagram.com/')
        sleep(3)
        # types the hashtag you want into the searchbar
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('#'+hashtag)
        sleep(3)
        # press enter
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').send_keys(Keys.ENTER)
        sleep(5)
        # gets first post and clicks it
        first_thumbnail = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]')
        first_thumbnail.click()
        sleep(randint(2, 5))
        self.like()
        sleep(randint(1, 2))
        self.comment()
        sleep(randint(1, 2))
        for i in range(1, numToLikeAndComment):
            if (i == 1):  # first click xpath is different
                next_post = self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div/a').click()
                self.like()
                sleep(randint(1, 5))
                self.comment()
                sleep(randint(2, 3))
            else:
                next_post = self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div/a[2]').click()
                self.like()
                sleep(randint(1, 5))
                self.comment()
                sleep(randint(2, 3))
        print('Liked and commented on ' + numToLikeAndComment + ' posts')

    #
    # This function likes a post
    #
    def like(self):
        sleep(randint(2, 4))
        self.driver.find_element_by_class_name(
            'wpO6b ').click()

    #
    # This function comments on a post
    #
    def comment(self):
        sleep(randint(1, 2))
        comment_options = ['Nice!!', 'Great post!',
                           'Awesome post. When you get a chance, check out my latest blog post!', 'Awesome!!', 'So cool!', 'Awesome stuff! When you get a chance, check out my website for computer science related articles!']
        # clicks comment box
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form').click()
        # writes the comment
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(comment_options[randint(0, 5)])
        sleep(1)
        # sends the comment
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
        sleep(randint(2, 5))

    #
    # This function follows users from an account passed in
    #
    # accountUrl -- account name to follow users from
    # numToFollow -- number of users to follow
    #
    def follow_users_from_account(self, accountUrl, numToFollow):
        sleep(1)
        # go to google developers account
        self.driver.get(accountUrl)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()  # open follower list
        sleep(3)
        follow_num = 1  # index of the users
        total_num_users_followed = 0  # total number of users followed
        # scroll to bottom and load all users
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        for i in range(1, 20): # scroll 20 times to load users
            sleep(1)
            self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # end scroll
        while (numToFollow > 0):
            potential_follow = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li['+str(follow_num)+']/div/div[3]/button')
            # check to make sure we aren't already following
            if (potential_follow.get_attribute('innerHTML') == 'Follow'):
                potential_follow.click()
                numToFollow = numToFollow - 1
                total_num_users_followed += 1
                sleep(randint(1, 5))
            follow_num += 1
            potential_follow = '/html/body/div[4]/div/div[2]/ul/div/li[' + \
                str(follow_num)+']/div/div[3]/button'
        print('Total number of users followed from' +
              accountUrl + ': ' + total_num_users_followed)

    #
    # This function unfollows all users in my followers list
    #
    def unfollow_users_followers(self):
        print('unfollow_users_followers method starting...')
        unfollow_num = 1
        number_of_users_unfollowed = 0
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        sleep(randint(2, 3))
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('innerHTML')
        # open follower list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(3)
        # scroll to bottom
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while(last_ht != ht):
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # end scroll
        button_text = scroll_box.find_elements_by_tag_name('button')
        unfollowNum = [
            name.text for name in button_text if name.text == 'Following']
        # loop through every user, if btn text == following, then unfollow
        print('Beginning to unfollow ' + unfollowNum + ' users')
        j = int(followers)
        for i in range(j, 0, -1):
            curr_user = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li['+str(j)+']/div/div[2]/button')
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", curr_user)  # scroll the current user into view
            if (curr_user.get_attribute('innerHTML') == 'Following'):
                curr_user.click()
                sleep(randint(2, 3))
                # click confirm
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div[3]/button[1]').click()
                j = int(j)-1
                sleep(randint(1, 2))
            else:
                j = int(j)-1
        print('Successfully unfollowed all users that follow you that you (used to) follow back')

    #
    # This function unfollows users from following list
    #
    # num_to_unfollow -- number of people to unfollow
    #
    def unfollow_users_following(self, num_to_unfollow):
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        sleep(randint(3, 5))
        num_following = following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('innerHTML')
        print('You are following ' + num_following + ' users before def')
        sleep(randint(2, 3))
        # open following list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(randint(2, 4))
        # scroll to bottom and load all users
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while(last_ht != ht):
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # end scroll
        # start unfollowing users from the bottom
        # '/html/body/div[4]/div/div[2]/ul/div/li[47]/div/div[2]/button' <- what the xpath looks like. li[47] is equal to the number following
        # range(start, stop, step)
        j = num_following
        for i in range(num_to_unfollow, 0, -1):
            sleep(randint(1, 3))
            # click unfollow
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li['+str(j)+']/div/div[2]/button').click()
            sleep(randint(2, 3))
            # click confirm
            self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[3]/button[1]').click()
            j = int(j)-1
            sleep(randint(1, 2))
        print('Unfollowed: ' + num_to_unfollow + ' users')

    #
    # This function likes and comments on posts in your feed
    #
    # numToLikeAndComment -- number of posts you want to like and comment
    #
    def scroll_through_feed(self, numToLikeAndComment):
        comment_options = ['Nice!!', 'Great post!',
                           'Awesome post. When you get a chance, check out my latest blog post!', 'Awesome!!', 'So cool!']
        sleep(randint(3, 6))
        num = 1
        for i in range(numToLikeAndComment):
            self.driver.execute_script('window.scrollBy(0, 500)')
            '//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[1]/div[2]/section[3]/div/form'
            '//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[1]/div[2]/section[3]/div/form/button'

            '//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[2]/div[2]/section[3]/div/form'
            '//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[2]/div[2]/section[3]/div/form/button'

    #
    # This function gets a list of your followers
    #
    def get_followers_list(self):
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        sleep(randint(2, 3))
        # open follower list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(3)
        # scroll to bottom
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while(last_ht != ht):
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # end scroll
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # for name in names:
        #     print(name)
        print('Usernames of users that are following you:')
        print(names)

    #
    # This function gets a list of who you follow
    #
    def get_following_list(self):
        self.driver.get('https://www.instagram.com/bencarlsonblog/')
        sleep(randint(2, 3))
        # open following list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(3)
        # scroll to bottom
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while(last_ht != ht):
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # end scroll
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # for name in names:
        #     print(name)
        print('Usernames of users that you are following:')
        print(names)


def main():
    # try:
    my_bot = InstagramBot('bencarlsonblog')
    # except:
    #     print("Couldn't log in")
    try:
        my_bot.get_before_stats()
    except:
        print('Error get_before_stats()')
    try:
        my_bot.unfollow_users_followers()
    except:
        print('Error unfollowing users')
    try:
        my_bot.unfollow_users_following(5)
    except:
        print('Error unfollowing users')
    # my_bot.scroll_through_feed(2)
    try:
        my_bot.like_comment_posts_by_hashtag('webdeveloper', 10)
    except:
        print('Error commenting and liking hashtag')
    try:
        my_bot.follow_users_from_account(
            'https://www.instagram.com/google/', 15)
    except:
        print('Error following users')
    try:
        my_bot.get_after_stats()
    except:
        print('Error get_after_stats()')


if __name__ == '__main__':
    main()
