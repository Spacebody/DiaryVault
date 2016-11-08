from . import config
from .crypto import cryptoRSA
from .editor import Editor
from .menu import Menu


def main():
    print("------------My Vault v%s------------\n" % config.version)
    editor = Editor()
    menu = Menu(
        ('New File','Load File','New KeyPair','Exit'),
        (editor.new_file,
         editor.load_file,
         editor.new_rsa_keypair,
         exit))
    while True:
        menu.display()

if __name__ == '__main__':
    main()

