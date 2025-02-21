from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import sys
import config
import re


client = TelegramClient('session', config.api_id, config.api_hash, device_model='iPhone X')

options = [
    "1: Show current chats",
    "2: Close",
]


def progress(received_bytes, total):
    percentage = received_bytes / total
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(25 * percentage):{25}s}] {round((received_bytes / 10**6) * 100 ) / 100} MB [{int(100 * percentage)}%] ")
    sys.stdout.flush()


def check_name(name):
    folder_name = re.sub(r'[^a-zA-Z]', '', name)
    if not folder_name:
        folder_name = "New_Folder"
    return folder_name


async def download_media(chosen_dialog):
    photos_count = 0
    video_count = 0
    async for message in client.iter_messages(chosen_dialog.id, None):
        photo = message.photo
        if photo:
            org_filename = 'Downloads/' + check_name(chosen_dialog.name) + '/' + str(message.id) + '.jpg'
            photo_path = await client.download_media(photo, file=org_filename, progress_callback=progress)
            print(f" Photo saved to: {photo_path}")
            photos_count += 1
        elif message.video:
            org_filename = 'Downloads/' + check_name(chosen_dialog.name) + '/' + str(message.id) + '.mp4'
            video_path = await client.download_media(message.video, file=org_filename, progress_callback=progress)
            print(f" Video saved to: {video_path}")
            video_count += 1
    print(f"Successfully saved: {photos_count} photos")
    print(f"Successfully saved: {video_count} videos")


async def show_options():
    for option in options:
        print(option)
    choice = input("Choose an option: ")
    choice = int(choice)
    if choice == 1:
        dialogs = await client.get_dialogs()
        i = 1
        for dialog in dialogs:
            print(i, dialog.name)
            i += 1
        choice = input("Choose a chat to start download media: ")
        choice = int(choice)
        chosen_dialog = dialogs[choice - 1]
        await download_media(chosen_dialog)
        await show_options()
    else:
        client.disconnect()


async def do_login():
    phone_number = input("Enter your phone number: ")
    await client.send_code_request(phone_number)
    code = input("Enter the code you received: ")
    
    try:
        await client.sign_in(phone_number, code)
    except SessionPasswordNeededError:
        password = input("Enter your 2FA password: ")
        await client.sign_in(password=password)
    
    await show_options()


async def main():
    await client.connect()
    is_auth = await client.is_user_authorized()
    if is_auth:
        await show_options()
    else:
        await do_login()


if __name__ == "__main__":
    asyncio.run(main())
