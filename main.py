from telethon import TelegramClient
import asyncio

client = TelegramClient('session', 123456, "YOUR_API_HASH", device_model='iPhone X')

options = [
    "1: Show current chats",
    "2: Close",
]


async def download_media(chosen_dialog):
    photos_count = 0
    video_count = 0
    async for message in client.iter_messages(chosen_dialog.id, None):
        photo = message.photo
        if photo:
            org_filename = chosen_dialog.name + '_' + str(message.id) + '.jpg'
            photo_path = await client.download_media(photo, file='self/' + org_filename)
            print(f"Photo saved to: {photo_path}")
            photos_count += 1
        elif message.video:
            org_filename = chosen_dialog.name + '_' + str(message.id) + '.mp4'
            video_path = await client.download_media(message.video, file='self/' + org_filename)
            print(f"Video saved to: {video_path}")
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
            print(i, dialog.name, '(', dialog.id, ')')
            i += 1
        choice = input("Choose a chat to download self destructing photo inside it: ")
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
    await client.sign_in(phone_number, code)
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
