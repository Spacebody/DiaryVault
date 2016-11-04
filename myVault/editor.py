import configparser
import os
import tempfile
from subprocess import call

import config
import crypto.cryptoRSA as RSA
from crypto.hybirdCrypto import HybirdCrypto


class Editor(object):
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._check_config()
        self._editor = os.environ.get('EDITOR', self._config.get("basic", "editor"))
        self._initMessage = self._config.get("basic", "init_msg")

    def _init_config(self):
        self._config.add_section("basic")
        self._config.set("basic", "version", config.version)
        self._config.set("basic", "editor", config.editor)
        self._config.set("basic", "init_msg", config.init_message)
        length, driver_name = RSA.generate()
        self._config.add_section("RSA")
        self._config.set("RSA", "length", str(length))
        self._config.set("basic", "driver_name", driver_name)
        with open(config.name, "w") as config_file:
            self._config.write(config_file)

    def _check_config(self):
        if not self._config.read(".myVault"):
            self._init_config()

    def _new_msg(self):
        with tempfile.NamedTemporaryFile(mode='w+') as temp:
            temp.write(self._initMessage)
            temp.flush()
            call([self._editor, temp.name])
            temp.seek(0)
            return temp.read()

    @staticmethod
    def _save(file_name, data):
        with open(file_name, mode='w+b') as writer:
            writer.write(data)

    def load_file(self):
        file_name = input('Load File Name:')
        hybird_crypto = HybirdCrypto(self._config.getint("RSA", "length"),
                                     self._config.get("basic", "driver_name"),
                                     init_mode='read')
        with open(file_name, mode='rb') as reader:
            raw = reader.read()
            data = hybird_crypto.decrypt(raw)
            with tempfile.NamedTemporaryFile(mode='w+b') as temp:
                temp.write(data)
                temp.flush()
                call([self._editor, temp.name])

    def new_file(self):
        write_encrypt = HybirdCrypto(self._config.getint("RSA", "length"),
                                     self._config.get("basic", "driver_name"))
        self._save(input('New File Name:'),
                   write_encrypt.encrypt(self._new_msg()))
