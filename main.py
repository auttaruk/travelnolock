# -*- coding: utf-8 -*-
"""
GLOBAL AI TRAVEL AUTOMATION - MAIN RUNNER
มัดรวมระบบทั้งหมดให้รันเคียงคู่กันบน Async Event Loop เดียวกันผ่าน Asyncio
ประกอบด้วย:
1. การลงทะเบียน Geofencing & Location Change Callback (Skills -> Context)
2. รัน FastAPI Web Dashboard API (Uvicorn Server) แบบ Non-blocking
3. รัน Telegram Bot (Aiogram 3 Dispatcher Polling) แบบ Non-blocking
"""

import asyncio
import uvicorn
import sys

from config import settings
from core.context import global_context
from skills.location_trigger.behavior import handle_location_change
from interfaces.web.web_main import app
from interfaces.bot.bot_main import start_telegram_bot

async def main() -> None:
    print("==================================================")
    print("🚀 Global AI Travel Automation System Starting... 🚀")
    print("==================================================")
    
    # 1. การเชื่อมต่อ Hook: ลงทะเบียน Geofence Callback สำคัญของระบบ
    # เมื่อใดก็ตามที่มีการขยับพิกัดผ่าน API หรือ Telegram Bot ฟังก์ชันนี้จะรันทันทีเพื่อป้อนข้อมูล MCP
    global_context.register_location_callback(handle_location_change)
    print("[System Startup] 🛡️ ลงทะเบียน Geofence & Location Changed Callback สำเร็จ!")
    
    # 2. คอนฟิก Uvicorn สำหรับการทำงานแบบ Non-blocking Async
    web_config = uvicorn.Config(
        app=app,
        host=settings.host,
        port=settings.port,
        log_level="info",
        # กำหนด loop=asyncio เพื่อให้เข้ากันได้กับ event loop หลักของระบบ
        loop="asyncio"
    )
    web_server = uvicorn.Server(web_config)
    
    # 3. จัดเตรียมรันเซิร์ฟเวอร์แบบคู่ขนาน (Async Concurrent Tasks)
    print(f"[System Startup] 🌐 Web Dashboard API รันที่: http://{settings.host}:{settings.port}")
    print(f"[System Startup] 🤖 Telegram Bot เตรียมความพร้อมในโหมด Polling...")
    print("--------------------------------------------------")
    
    try:
        # สั่งรันทั้ง Web Server และ บอท Telegram พร้อมกันบน Single Event Loop
        await asyncio.gather(
            web_server.serve(),
            start_telegram_bot()
        )
    except Exception as e:
        print(f"[System Error] เกิดความเสียหายระหว่างรันระบบหลัก: {e}", file=sys.stderr)
        raise e

if __name__ == "__main__":
    try:
        # สตาร์ท Async Event Loop สำหรับระบบย่อยทั้งหมด
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n==================================================")
        print("🛑 [System Shutdown] ปิดระบบเรียบร้อยแล้วอย่างปลอดภัย! สวัสดีครับ")
        print("==================================================")
