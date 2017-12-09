# -*- encoding: utf-8 -*-
import unittest, requests

main_url = 'http://demo6144383.mockable.io/'
member_attr = {'id', 'name', 'role', 'level'}

class TestApiUsingRequests(unittest.TestCase):

    def get_data(self, url):
        r = requests.get(url)
        data = r.json()
        print(r)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['content-type'], 'application/json; charset=UTF-8')
        self.assertIsInstance(data, dict)
        return data
        print(r)

    def test_get_members(self):
        data = self.get_data('{}/members'.format(main_url))
        team_members = data['team_members']
        self.assertIsInstance(team_members, list)
        [self.assertSetEqual(set(member), member_attr) for member in team_members]
        return team_members

    def test_get_member(self):
        team_members = self.test_get_members()
        data = self.get_data('{}/member/{}'.format(main_url, team_members[0]['id']))
        self.assertIsInstance(data, dict)
        self.assertSetEqual(set(data), member_attr)


if __name__ == '__main__':
    unittest.main()
