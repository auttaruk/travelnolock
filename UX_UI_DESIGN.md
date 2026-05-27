# UX/UI Design Blueprint - Global AI Travel Automation

## Product Positioning

เว็บนี้ควรวางตัวเป็น **AI Travel Command Center** ไม่ใช่เว็บแนะนำบริการทั่วไป ผู้ใช้เปิดเข้ามาเพื่อควบคุมทริปจริง ดูสถานะปัจจุบัน สั่ง AI วางแผน เดินทาง ข้ามประเทศ เช็กค่าใช้จ่าย และส่ง itinerary เป็น PDF/email ได้จากหน้าเดียว

กลุ่มผู้ใช้หลัก:
- นักเดินทางที่ใช้ Telegram bot อยู่แล้ว และต้องการ dashboard เห็นภาพรวม
- ผู้ดูแลหรือ demo operator ที่ต้องการจำลอง GPS/geofence/wallet/session
- ผู้ใช้ที่ต้องการสร้าง trip itinerary พร้อม flight options และเอกสารส่งออก

## Core UX Principle

1. เปิดหน้าแรกแล้วใช้งานได้ทันที
2. สถานะสำคัญต้องมองเห็นใน 5 วินาที: current location, active trip, wallet, AI provider, sync status
3. Action หลักต้องอยู่ใกล้บริบท: วางแผนทริปใกล้ destination, อัปเดต GPS ใกล้ location, บันทึก expense ใกล้ wallet
4. เว็บควรเป็น operational dashboard ที่แน่นแต่ไม่รก ใช้ card เฉพาะข้อมูลซ้ำหรือ widget ไม่ทำหน้า marketing hero

## Information Architecture

### 1. Top App Bar

เนื้อหา:
- Brand: Global AI Travel
- Active session selector
- AI provider status: Gemini / Claude / Mock
- Server sync status
- ปุ่มเปิด Telegram / Export PDF / Settings

UX:
- Session switcher ควรเป็น dropdown + search แทนปุ่ม Alice/Bob แบบ hardcoded
- ถ้าไม่มี session ให้แสดง Default Session

### 2. Main Dashboard

Layout desktop:
- Left sidebar: navigation
- Main canvas: trip workspace
- Right rail: live context and alerts

Layout mobile:
- Top tabs: Dashboard, Plan, Wallet, GPS, Files
- Action bar fixed bottom เฉพาะคำสั่งหลัก

Navigation:
- Dashboard
- Trip Planner
- Live Location
- Wallet & Expenses
- Tickets & Scan
- Itinerary Files
- Settings

## First Screen Design

### Primary Dashboard Band

แสดง 4 status widgets:
- Current Location: district, province, country, GPS
- Wallet: primary/secondary balance and currency
- Active Trip: origin, destination, date range, status
- AI Agent: provider, model, last response, mode

ควรใช้ grid 4 ช่องบน desktop และ 2x2 บน tablet/mobile

### Main Workspace

แบ่งเป็น 2 คอลัมน์:
- ซ้าย: Travel Assistant command panel
- ขวา: Live itinerary preview

Travel Assistant command panel:
- Textarea: "Ask your travel agent..."
- Quick actions:
  - Plan trip
  - Find flights
  - Scan ticket
  - Log expense
  - Send itinerary
- Input chips: destination, days, email, budget, travel style

Live itinerary preview:
- Flight recommendation list
- 3-day timeline
- Banner image preview from `images/trip_banner_day_*.png`
- PDF status with link to `Trip_Itinerary.pdf`

## Screen Designs

### Dashboard

Purpose:
ให้ผู้ใช้เห็นภาพรวมระบบและทำงานเร็ว

Components:
- Status cards
- Recent AI actions timeline
- Travel command box
- Current itinerary preview
- Latest geofence alert

Empty state:
"Start by choosing a destination or syncing a Telegram session."

### Trip Planner

Purpose:
สร้างทริปจาก destination, date, budget, preferences

Sections:
- Trip form
- Flight options table
- Day-by-day itinerary timeline
- Visual banners
- Export panel: PDF, email

Fields:
- Origin
- Destination
- Depart date
- Return date
- Days
- Traveler count
- Email recipient
- Preferences

### Live Location

Purpose:
แสดงและทดสอบ geofence

Sections:
- Map-like location panel
- Country preset buttons: Thailand, Japan, Singapore, Korea
- Latitude/longitude editor
- Resolved location
- Geofence event log
- Auto wallet switch explanation as compact status, not long text

### Wallet & Expenses

Purpose:
ติดตามเงินข้ามสกุลและค่าใช้จ่ายจาก AI

Sections:
- Primary wallet
- Secondary wallet
- Currency selector
- Expense input
- Recent transactions
- Spending by category

Suggested chart:
- Small bar chart for daily spending
- Currency badges: THB, JPY, SGD, KRW, USD

### Tickets & Scan

Purpose:
ตรวจตั๋วหรือรูปภาพการเดินทาง

Components:
- Upload zone
- OCR/AI scan result
- Validity checklist
- Extracted price/PNR/passenger/route
- Button: "Save as expense"

### Itinerary Files

Purpose:
รวม output ของระบบ

Components:
- Latest PDF preview card
- Generated banner gallery
- Email delivery status
- Download/open actions

### Settings

Purpose:
ตั้งค่าระบบแบบไม่ทำให้ dashboard รก

Sections:
- AI provider
- Model
- API key status only, never show raw key
- SMTP status
- Telegram bot status
- Session management

## Visual Direction

Style:
- Modern operational travel dashboard
- Light-first interface with dark mode option
- ใช้สีหลายชุดอย่างควบคุม ไม่ให้กลายเป็นโทนเดียว

Palette:
- Base: `#F7F9FC`, `#FFFFFF`, `#111827`
- Travel blue: `#2563EB`
- Success green: `#16A34A`
- Alert amber: `#F59E0B`
- Expense red: `#DC2626`
- Route teal: `#0D9488`

Typography:
- Font: Inter, Noto Sans Thai, system sans-serif
- Dashboard title: 24-28px
- Card heading: 14-16px
- Body: 14px
- Numeric wallet values: 24-32px

Card style:
- Border radius 8px
- Soft border `#E5E7EB`
- Minimal shadow
- No nested cards

Icon style:
- Use lucide-style icons if moving to React/frontend framework
- Use icons for GPS, Wallet, Plane, File, Mail, Bot, Settings

## Component System

Buttons:
- Primary: blue filled
- Secondary: white with border
- Danger: red outline
- Icon buttons for refresh, download, settings, scan

Inputs:
- Compact labels
- Clear helper/error text
- Currency fields aligned right

Tables:
- Use dense rows for flight options and transactions
- Keep important columns visible: airline, flight no, time, duration, cabin, price

Toasts:
- Geofence alert
- PDF generated
- Email sent/failed
- Expense saved

## Recommended Implementation Plan

### Phase 1 - Clean Existing FastAPI Page

- Split HTML/CSS/JS out of `interfaces/web/web_main.py`
- Add `/static` folder for CSS/JS/images
- Keep current APIs:
  - `GET /api/dashboard`
  - `GET /api/sessions`
  - `POST /api/location/update`
- Fix duplicate `fetchState` and remove invalid `async def fetchState()` from embedded JS

### Phase 2 - Build Dashboard UI

- Build dashboard, location sandbox, wallet panel, preferences panel
- Replace hardcoded Alice/Bob buttons with dynamic sessions from `/api/sessions`
- Add activity timeline from existing context or temporary client-side log

### Phase 3 - Add Trip Planner UI

- Add form for destination/email/days
- Add backend endpoint that calls `run_active_trip_delivery`
- Show generated flights, itinerary, banners, PDF status

### Phase 4 - Add Files & Scan UX

- Add PDF preview/download
- Add image upload for ticket scan
- Add expense confirmation flow

## Suggested Page Wireframe

```text
+--------------------------------------------------------------------------------+
| Global AI Travel       Session: Default v      Gemini Active      Server Online |
+----------------------+---------------------------------------------------------+
| Dashboard            | Current Location | Wallet        | Active Trip | AI     |
| Trip Planner         | Bangkok, TH      | USD / JPY     | Tokyo       | Ready  |
| Live Location        +---------------------------------------------------------+
| Wallet & Expenses    | Ask AI Travel Agent                                      |
| Tickets & Scan       | [Plan my Tokyo trip for 3 days...] [Send] [Quick Action]|
| Itinerary Files      +-----------------------------+---------------------------+
| Settings             | Itinerary Timeline          | Live Context              |
|                      | Day 1 image + schedule      | GPS simulator             |
|                      | Day 2 image + schedule      | Geofence events           |
|                      | Day 3 image + schedule      | Preferences               |
+----------------------+-----------------------------+---------------------------+
```

## UX Copy Examples

Primary action:
- "Plan Trip"
- "Find Flights"
- "Scan Ticket"
- "Log Expense"
- "Send PDF"

Status text:
- "Synced from Telegram"
- "Wallet switched for Japan"
- "PDF ready"
- "Waiting for destination"

Empty text:
- "No itinerary yet. Create one from the travel command box."
- "No geofence events in this session."
- "No expenses recorded yet."

## Key Improvement Over Current UI

หน้าปัจจุบันมี dashboard พื้นฐานดีแล้ว แต่ยังเน้น demo/sandbox มากกว่า workflow ผู้ใช้จริง ดีไซน์ใหม่ควรย้ายจาก "ดู state" ไปเป็น "ทำงานกับทริป" โดยให้ dashboard เป็นศูนย์ควบคุม และแยกฟีเจอร์หนักอย่าง Trip Planner, Wallet, Scan, Files ออกเป็นหน้าหรือแท็บที่ชัดเจน
