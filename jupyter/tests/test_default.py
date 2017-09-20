import testinfra
import unittest
import testinfra.host


class TestJupyterDistribution(unittest.TestCase):

    def setUp(self):
        """
        Some initializations are made.
        * We fetch the jupyter host from testinfra + Ansible inventory,
        * We set the user,
        * We set some information about the gatling distribution
            * distribution name,
            * version,
            * package name (=distribution + version),
            * zip name
        """

        # We fetch every hosts that fit in the gatling group in a list
        jupyter_host = testinfra.get_host(
            "ansible://jupyter?ansible_inventory=.molecule/ansible_inventory"
        )

        # We set some information on the remote environment
        self.jupyter = {
            "host": jupyter_host
        }

    def test_jupyter_envs_exist(self):
        self.assertTrue(self.jupyter.get("host"))

    def test_pip_is_installed(self):
        self.assertTrue(
            self.jupyter.get("host").package("python-pip").is_installed
        )


if __name__ == '__main__':
    unittest.main()
