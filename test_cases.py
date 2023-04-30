import unittest
import linter

class test_cases(unittest.TestCase):
    def test_blank_lines(self):
        self.assertEqual(linter.add_lines(["hej jag heter mossab. jag pluggar på bth!"]), ["hej jag heter mossab.\n", "jag pluggar på bth!\n", ""])
        self.assertEqual(linter.add_blank_lines(["hej det här är en subsection \n \subsection"], 2), ['hej det här är en subsection \n', '\n\n\\subsection'])

if __name__ == '__main__':
    unittest.main()