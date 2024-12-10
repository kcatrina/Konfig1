import os
import tarfile
import unittest
from io import StringIO
from contextlib import redirect_stdout
import tkinter as tk

# Импортируем ваши классы из основного кода
from main import VirtualFileSystem, ShellEmulator

class TestShellEmulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_config = {
            'User': 'testuser',
            'Host': 'testhost',
            'Log': 'test_log.xml',
            'StartScript': None
        }
        tar_path = r'C:\Users\Vovawork\PycharmProjects\kari\ezy.tar'

        if not os.path.exists(tar_path):
            raise FileNotFoundError(f"Test archive not found: {tar_path}")

        cls.vfs = VirtualFileSystem(tar_path)
        cls.root = tk.Tk()
        cls.shell = ShellEmulator(cls.root, cls.test_config, cls.vfs)

        # Перенаправление вывода для тестов
        cls.original_write_output = cls.shell.write_output
        cls.test_output = StringIO()
        cls.shell.write_output = lambda text: cls.test_output.write(text)

    def setUp(self):
        # Очищаем тестовый вывод перед каждым тестом
        self.test_output.seek(0)
        self.test_output.truncate(0)

    def test_cd_root(self):
        self.shell.execute_command('cd /')
        self.assertEqual(self.shell.vfs.current_dir, '/bs')

    def test_ls(self):
        self.shell.execute_command('ls')
        dirs, files = self.vfs.list_dir(self.shell.vfs.current_dir)
        output = self.test_output.getvalue().strip()
        if dirs or files:
            self.assertTrue(any(item in output for item in dirs + files))
        else:
            self.assertEqual(output, "")

    def test_ls_with_flags(self):
        self.shell.execute_command('ls -l')
        dirs, files = self.vfs.list_dir(self.shell.vfs.current_dir)
        output = self.test_output.getvalue().strip()
        if dirs or files:
            self.assertTrue(any(item in output for item in dirs + files))
        else:
            self.assertEqual(output, "")

    def test_copy_file(self):
        self.shell.execute_command('cp names/vadim.txt names/vadim_copy.txt')
        self.assertIn('vadim_copy.txt', self.vfs.get_node('/bs/names'))

    def test_command_not_found(self):
        self.shell.execute_command('unknown_command')
        self.assertIn("command not found", self.test_output.getvalue())

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.shell.execute_command('exit')

    @classmethod
    def tearDownClass(cls):
        cls.shell.write_output = cls.original_write_output
        cls.root.destroy()
