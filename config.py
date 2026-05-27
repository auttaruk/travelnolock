# -*- coding: utf-8 -*-
"""
1. CONFIGURATION LAYER
ระบบโหลดและตรวจสอบความถูกต้องของ Configuration ผ่าน Pydantic Settings
อ้างอิงและพัฒนาต่อจากมาตรฐานความปลอดภัยและการจัดการสภาพแวดล้อม (Environment Variables)
"""

import os
import sys
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# ป้องกันปัญหา UnicodeEncodeError บนระบบปฏิบัติการ Windows เมื่อมีตัวอักษรภาษาไทยในการพิมพ์ข้อความลง Console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

class Settings(BaseSettings):
    # กำหนดค่าตัวแปรระบบพร้อมระบุชนิดข้อมูล (Type Hinting) และกำหนดค่า Default หากไม่มีการระบุไว้
    telegram_token: str = Field(
        default="YOUR_TELEGRAM_TOKEN_HERE", 
        validation_alias="TELEGRAM_TOKEN"
    )
    gemini_api_key: str = Field(
        default="YOUR_GEMINI_API_KEY_HERE", 
        validation_alias="GEMINI_API_KEY"
    )
    gemini_model: str = Field(
        default="gemini-2.0-flash", 
        validation_alias="GEMINI_MODEL"
    )
    ai_provider: str = Field(
        default="gemini",
        validation_alias="AI_PROVIDER"
    )
    claude_api_key: str = Field(
        default="YOUR_CLAUDE_API_KEY_HERE",
        validation_alias="CLAUDE_API_KEY"
    )
    claude_model: str = Field(
        default="claude-3-5-haiku-20241022",
        validation_alias="CLAUDE_MODEL"
    )
    port: int = Field(
        default=8000, 
        validation_alias="PORT"
    )
    host: str = Field(
        default="0.0.0.0", 
        validation_alias="HOST"
    )
    smtp_server: str = Field(
        default="smtp.gmail.com",
        validation_alias="SMTP_SERVER"
    )
    smtp_port: int = Field(
        default=587,
        validation_alias="SMTP_PORT"
    )
    smtp_username: str = Field(
        default="YOUR_EMAIL@gmail.com",
        validation_alias="SMTP_USERNAME"
    )
    smtp_password: str = Field(
        default="YOUR_SMTP_APP_PASSWORD_HERE",
        validation_alias="SMTP_PASSWORD"
    )
    smtp_from_email: str = Field(
        default="ai-travel-concierge@gmail.com",
        validation_alias="SMTP_FROM_EMAIL"
    )

    # กำหนดลักษณะเฉพาะในการโหลดไฟล์ .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # หากมีค่าตัวแปรอื่นๆ ใน .env ที่ไม่ได้ประกาศใน Settings ให้ละเว้นเพื่อไม่ให้เกิด Error
        extra="ignore"
    )

# ทำการ Initialize โหลดการตั้งค่าทั้งหมดขึ้นมาใช้งาน
try:
    settings = Settings()
except Exception as e:
    print(f"[!] Warning: ไม่สามารถโหลดไฟล์ .env ได้อย่างสมบูรณ์ หรือโครงสร้างผิดพลาด: {e}")
    # Fallback กลับไปใช้ Default หรือ Environment variables ดิบ
    class FallbackSettings:
        telegram_token = os.environ.get("TELEGRAM_TOKEN", "YOUR_TELEGRAM_TOKEN_HERE")
        gemini_api_key = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
        gemini_model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
        ai_provider = os.environ.get("AI_PROVIDER", "gemini")
        claude_api_key = os.environ.get("CLAUDE_API_KEY", "YOUR_CLAUDE_API_KEY_HERE")
        claude_model = os.environ.get("CLAUDE_MODEL", "claude-3-5-haiku-20241022")
        port = int(os.environ.get("PORT", "8000"))
        host = os.environ.get("HOST", "0.0.0.0")
        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", "587"))
        smtp_username = os.environ.get("SMTP_USERNAME", "YOUR_EMAIL@gmail.com")
        smtp_password = os.environ.get("SMTP_PASSWORD", "YOUR_SMTP_APP_PASSWORD_HERE")
        smtp_from_email = os.environ.get("SMTP_FROM_EMAIL", "ai-travel-concierge@gmail.com")
    settings = FallbackSettings()
