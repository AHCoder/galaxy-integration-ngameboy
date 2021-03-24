import configparser
import textwrap

CONFIG_LOC = r"%LOCALAPPDATA%\GOG.com\Galaxy\Configuration\plugins\ngameboy\config.ini"

class Config:
    def __init__(self):
        self.cfg = configparser.ConfigParser(allow_no_value=True)
        self.cfg.set("DEFAULT", "; Make sure to use / instead of \ in file paths.")
        self.cfg["DEFAULT"]["roms_path"] = "C:/Games/Gameboy"
        self.cfg["DEFAULT"]["emu_path"] = "C:/Program Files/mGBA/mGBA.exe"
        self.cfg["DEFAULT"]["api_key"] = None
        self.cfg["DEFAULT"]["emu_fullscreen"] = False
        
        self.cfg.add_section("Paths")
        self.cfg.set("Paths", textwrap.dedent(
                """\
                ; Set your roms folder, path to your mGBA.exe here\
                """
            )
        )

        self.cfg.add_section("Method")
        self.cfg.set("Method", textwrap.dedent(
                """\
                ; Set your API key here\
                """
            )
        )
        
        self.cfg.add_section("EmuSettings")
        self.cfg.set("EmuSettings", textwrap.dedent(
                """\
                ; emu_fullscreen: Set to True if you want to launch in fullscreen by default\
                """
            )
        )