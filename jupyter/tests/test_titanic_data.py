import testinfra
import unittest


class TestTitanicData(unittest.TestCase):

    def setUp(self):
        # We fetch every hosts that fit in the gatling group in a list
        jupyter_host = testinfra.get_host(
            "ansible://jupyter?ansible_inventory=.molecule/ansible_inventory"
        )

        # We set some information on the remote environment
        self.jupyter = {
            "host": jupyter_host
        }

    def test_titanic_data_archive_was_downloaded(self):
        f = self.jupyter.get("host").file("/root/titanic_0.1.0.tar.gz")
        self.assertTrue(f.exists)

    def test_titanic_data_archive_has_the_expected_digest(self):
        f = self.jupyter.get("host").file("/root/titanic_0.1.0.tar.gz")
        self.assertTrue(f.md5sum == "0c9110b21b4c9e1156ce73ebbedc2c33")


if __name__ == '__main__':
    unittest.main()
