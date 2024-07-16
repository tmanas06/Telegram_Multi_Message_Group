#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChat, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os
import sys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
SLEEP_TIME = 10

class main():
    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            print(re+"[!] run python3 setup.py first !!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input(gr+'[+] Enter the code: '+re))

        chats = []
        last_date = None
        chunk_size = 200
        groups = []

        result = client(GetDialogsRequest(
                     offset_date=last_date,
                     offset_id=0,
                     offset_peer=InputPeerEmpty(),
                     limit=chunk_size,
                     hash=0
                 ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup or chat.gigagroup:
                    groups.append(chat)
            except:
                continue

        print(gr+'[+] Choose groups to send a message (comma separated indexes):'+re)
        i = 0
        for g in groups:
            print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
            i += 1

        print('')
        g_indexes = input(gr+"[+] Enter Numbers (comma separated): "+re).split(',')
        selected_groups = [groups[int(index)] for index in g_indexes]

        # Read messages from Google Sheets
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\tmana\OneDrive\Desktop\MultiBot\wh-work-424210-5530b9fc03be.json", scope)
            client_gspread = gspread.authorize(creds)
            sheet = client_gspread.open("message").sheet1
            messages = sheet.col_values(1)  # Assuming messages are in the first column
            print(gr+"[+] Successfully accessed Google Sheets")
        except gspread.exceptions.SpreadsheetNotFound:
            print(re+"[!] Error: The Google Sheet 'message' was not found. Please check the sheet name.")
            client.disconnect()
            sys.exit(1)
        except gspread.exceptions.APIError as e:
            print(re+f"[!] API Error accessing Google Sheets: {e}")
            client.disconnect()
            sys.exit(1)
        except Exception as e:
            print(re+"[!] Error accessing Google Sheets:", e)
            client.disconnect()
            sys.exit(1)

        if not messages:
            print(re+"[!] No messages found in the Google Sheet")
            client.disconnect()
            sys.exit(1)

        for message in messages:
            for target_group in selected_groups:
                try:
                    print(gr+"[+] Sending Message to group:", target_group.title)
                    if hasattr(target_group, 'megagroup') and target_group.megagroup:
                        receiver = InputPeerChannel(target_group.id, target_group.access_hash)
                    else:
                        receiver = InputPeerChat(target_group.id)

                    client.send_message(receiver, message)
                    print(gr+"[+] Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    print(
                        re+"[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
                    client.disconnect()
                    sys.exit()
                except Exception as e:
                    print(re+"[!] Error:", e)
                    print(re+"[!] Trying to continue...")

        client.disconnect()
        print("Done. Messages sent to the selected groups.")

if __name__ == "__main__":
    main.send_sms()
