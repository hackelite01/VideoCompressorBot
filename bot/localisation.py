#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @hackelite01

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram <b>Video Compressor Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as a small video file!</b> \n\n/help for more details. \n\nSupport Group: @hackelite01"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set a custom thumbnail, send a photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading ... 📥 \n"
    
    UPLOAD_START = "📤 Uploading ... 📤 \n"
    
    COMPRESS_START = "📈 Trying to compress ... 📈"
    
    RCHD_BOT_API_LIMIT = "size greater than the maximum allowed size (50MB). Nevertheless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📈 Compressed in {}\n\n📤 Uploaded in {}\n\nBy @hackelitebotlist"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "❌ Custom thumbnail cleared successfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "❌ Media cleared successfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom Thumbnail found."
    
    NO_VOID_FORMAT_FOUND = "No one is going to help you.\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @hackelite01"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
