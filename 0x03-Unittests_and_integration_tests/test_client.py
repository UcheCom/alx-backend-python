#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
import json
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, inp, mock):
        """Tests the `org` method returns the correct value."""
        expected = {"org": inp}
        mock.return_value = expected

        gh_client = GithubOrgClient(inp)
        result = gh_client.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{inp}')
        self.assertEqual(result, expected)

    def test_public_repos_url(self) -> None:
        """ This tests public repos url method"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("Google")._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """Tests the `public_repos` method."""
        test_payload = [{"name": "Google"}, {"name": "repo2"}]
        mock_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub:

            mock_pub.return_value = 'hello/people'
            test_client = GithubOrgClient('testorg')
            result = test_client.public_repos()

            chk = [i["name"] for i in test_payload]
            self.assertEqual(result, chk)

            mock_pub.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """Tests the `has_license` method."""
        gh_client = GithubOrgClient.has_license(repo, key)
        self.assertEqual(gh_client, expected)


@parameterized_class([
        {
            'org_payload': TEST_PAYLOAD[0][0],
            'repos_payload': TEST_PAYLOAD[0][1],
            'expected_repos': TEST_PAYLOAD[0][2],
            'apache2_repos': TEST_PAYLOAD[0][3],
        },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """This performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """Get Payload"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        test_client = GithubOrgClient("google")

        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("XLICENSE"), [])
        self.assertEqual(test_client.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down all tests."""
        cls.get_patcher.stop()
