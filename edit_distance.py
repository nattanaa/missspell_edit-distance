db_at = ['ดีพเลินนิ่ง', 'ทรานสเรชั่น', 'เด็กฝึกงาน', 'เมตาเวิร์ส', 'เบื้องหลัง', 'เทคโนโลยี', 'รู้เรื่อง', 'ไม่เข้าใจ', 'ผลิตภัณฑ์', 'คอนเซ็ปต์', 'นวัตรกรรม', 'แนะนำตัว', 'ประโยชน์', 'เปิดเพลง', 'ร้องเพลง', 'โปรดักส์', 'แพลชชั่น', 'โปรดักต์', 'บอร์ดแคส', 'ก่อตั้ง', 'มายเซ็ต', 'ฮัลโหล ', 'เจ้าของ', 'ศักยภาพ', 'พี่น้อง', 'ข้อเสีย', 'ถึงชื่อ', 'ใช้ชื่อ', 'อยู่ไหม', 'อุปกรณ์', 'เอสซีจี', 'เดินทาง', 'จุดเด่น', 'หัวหน้า', 'ที่อยู่', 'โปรเจ็ค', 'เหนื่อย', 'สุดยอด', 'ประกอบ', 'ใช้งาน', 'เข้าใจ', 'ได้ยิน', 'สบายดี', 'เป็นไง', 'รู้สึก', 'พูดได้', 'กี่โมง', 'กี่วัน', 'กี่บูธ', 'วันไหน', 'ท้าทาย', 'คลาวด์', 'ปลอบใจ', 'เทคซอส', 'โปรเจค', 'หมดแรง', 'จัดงาน', 'สามารถ', 'ยูทูป', 'กี่ปี', 'สร้าง', 'ข้อดี', 'กี่คน', 'โฟกัส', 'เอดจ์', 'เบื่อ', 'ทอล์ก', 'คำย่อ', 'ทักษะ', 'ทำงาน', 'วิทยุ', 'เกิด', 'ราคา', 'หนัก', 'ญาติ', 'เก่ง', 'เป็น', 'ชื่อ', 'เจ๋ง', 'โชว์', 'บ้าน', 'what', 'ปลอบ', 'อยู่', 'ภาษา', 'อายุ', 'เปิด', 'ขาย', 'คุย', 'สูง', 'ฟัง', 'แฟน', 'หิว', 'พูด', 'ของ', 'why', 'แลป', 'กิน', 'พัก', 'งาน', 'ย่อ', 'คติ', 'ทำ', 'สี', 'งง']
db_kg = ['รู้ใจ', 'วีดู', 'เอ็นแอลพี', 'ปัญญาประดิษฐ์',  'บูธ', 'นิวเอชซีไอ', 'ไอโอที', 'ทีทีเอส', 'เอสทีที']
db_at.sort(key = len, reverse = True)
db_kg.sort(key = len, reverse = True)

#query word
q = 'ดูดี'

#calculate edit distance
import stringdist
A=[]
for i in db_kg:
    A.append(stringdist.levenshtein_norm(q,i))
index = A.index(min(A))
result = db_kg[index]