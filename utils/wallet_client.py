from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = """1ApWapzMBu0RmqT9vD1KMD2O-5Cm7ZCybMM7GM9r4MwhdPjqMqbPTHiVCJvQwmhhR-ldRWEUxMu5sjwPsHB3SBBaienbIw8thf40iFSg8O7dzp_sVC-xC2WYQPwi8bx2oDaGWmkhhm15OxktxsVxvBdByF6aK2ycttSaqeBiCdXDMIDWAA_kmD0_QMUBcn0z14T0JDhzqPRW6E_r1Iqdqe-EA1uo5oiR9iKPFGh0TLuLT0h91gH7LhSa6n6GxRudJ_KQUrns2ejtGs2B_0w0aOj7a-pIYl_Cyv0WXdKfRQJO9Nre6abmXz8xYNrgpJTIKbCc5c4sDdsb3FHiLqmSxtf9HW34Tj-0="""

wallet_client = TelegramClient(StringSession(session_string), api_id, api_hash)
