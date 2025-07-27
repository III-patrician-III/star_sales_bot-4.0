import logging
import hashlib
import hmac
from fastapi import FastAPI, Request, Header, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from starlette.responses import JSONResponse

from handlers import start, payment, admin, crypto
from utils.wallet_client import wallet_client_init
from utils.config import cfg

logging.basicConfig(level=logging.INFO)

app = FastAPI()
bot = Bot(token=cfg.bot_token, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

# Initialize Telethon client
wallet_client_init(cfg)

# Register handlers
dp.include_router(start.router)
dp.include_router(payment.router)
dp.include_router(admin.router)
dp.include_router(crypto.router)

@app.on_event("startup")
async def on_startup():
    webhook_url = f"{cfg.webhook_base}/telegram_webhook"
    await bot.set_webhook(webhook_url)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()

# Telegram webhook
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/telegram_webhook")

# CryptoCloud webhook
@app.post("/crypto_webhook")
async def crypto_webhook(request: Request, x_signature: str = Header(..., alias="X-Signature")):
    body = await request.body()
    secret = cfg.crypto_secret.encode()
    calculated_signature = hmac.new(secret, body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(calculated_signature, x_signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
    data = await request.json()
    logging.info("Crypto webhook received: %s", data)
    return JSONResponse(content={"status": "ok"})
