# PAGES · แดชบอร์ดความคืบหน้า
# PAGES • แดชบอร์ดความคืบหน้า

กรอกสัปดาห์ที่ 1 แล้วอัปเดตทุกครั้งที่ commit — อาจารย์ดูไฟล์นี้ + `git log` แทนการถาม

**หัวข้อ:** เว็บคำนวณ GPA
**data.json เก็บอะไร (field):** subject, credit, grade, semester, status
**คัดลอก data.json -> data.sample.json แล้ว:** [ ]


## team — หน้าทีม (สัปดาห์ 0)
- [ ] กรอก `team.json` ครบทุกคน (ชื่อ, รหัส, บทบาท, งานที่รับผิดชอบ)
- [ ] เปิด /team เห็นชื่อทุกคน
- [ ] commit `team: members filled` + push


## page1 — ผู้รับผิดชอบ: วนัชนันท์ สันติวิชัยกุล • แบบมาจาก catalog: list
- [ ] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [ ] ใช้ field ของ data.json ของกลุ่ม
- [ ] เปิด /page1 ได้ ไม่มี TODO
- [ ] `check.bat` -> /page1 [x] ไม่มี warning
- [ ] commit `page1: ...`


## page2 — ผู้รับผิดชอบ: ปภาวี คำเก่ง • แบบมาจาก catalog: form
- [ ] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [ ] ใช้ field ของ data.json ของกลุ่ม
- [ ] เปิด /page2 ได้ ไม่มี TODO
- [ ] `check.bat` -> /page2 [x] ไม่มี warning
- [ ] commit `page2: ...`


## page3 — ผู้รับผิดชอบ: นัฐณิชา ถ้ำหิน • แบบมาจาก catalog: calculator
- [ ] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [ ] ใช้ field ของ data.json ของกลุ่ม
- [ ] เปิด /page3 ได้ ไม่มี TODO
- [ ] `check.bat` -> /page3 [x] ไม่มี warning
- [ ] commit `page3: ...`


## models.py — ผู้รับผิดชอบ: นัฐณิชา ถ้ำหิน
- [ ] เปลี่ยนชื่อ class ให้ตรงหัวข้อ, field ตรง data.json
- [ ] method 1 ตัวที่มีประโยชน์ (ไม่เหลือ TODO)
- [ ] มีหน้าใดหน้าหนึ่งใช้ class นี้ (เช่น แบบ detail)
- [ ] `python check_project.py` -> class [x] 9/9
- [ ] commit `models: ...`


## ส่งงาน
- [ ] `check.bat` -> 60/60, pytest 4 passed, ไม่มี warning
- [ ] ทุกคนอยู่ใน `git log`
- [ ] นำเสนอ: ทุกคนอธิบายหน้าของตัวเอง 1 นาที