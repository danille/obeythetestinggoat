from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about new cool to-do app.
        # So I go to check it's homepage in browser
        self.browser.get('http://localhost:8000')

        # Edith notices the page title and header mention to-do lists
        self.assertIn('To-Doer', self.browser.title)
        self.fail('Finish the test!')


        # She is invited to enter to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When Edith hits Enter, the page reloads, and now the page lists
        # "1: Buy peacock feathers" as an item in to-do list

        # There is still textbox inviting her to add another to-do item.
        # She enters "Use peacock feathers to make a fly" and hits Enter.

        # Page reloads again, and now shows both items on list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for here - there some explanatory
        # text about it.

        # She visits that URL - her to-do list is still available.

        # Satisfied she leaves the site.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
