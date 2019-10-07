from core import misc


def load_modules():
    try:
        misc.loader.load_package('private_modules')
    except (ImportError, ModuleNotFoundError):
        pass
    misc.loader.load_packages(f"modules.{item}" for item in [
        'base',  # User management and base Middlewares
        # 'get',  # GETs in chats
        'captcha_button',  # Captcha for new joined users
        'voteban',  # Voteban in chats
        'nsfw',  # Checking media for nsfw
        'amd_builds',  # AMD Builds from reddit
        'tail',  # Handle all unhandled actions
    ])
