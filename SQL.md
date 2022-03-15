### KIẾN THỨC CƠ BẢN VỀ SQL
#### 1. TRIGGER
##### 1.1. Khái niệm:
* Trigger là một đối tượng được định danh trong CSDL và luôn gắn chặc với một sự kiên xảy ra trên một bản nào đó. Các sự kiện ở đây có thể là: insert, update, deleted. Có nghĩa có
l khi một suự kiện nào xảy ra ở một bảng nào đó trong csdl sẽ tác động đến câu lệnh sql được viết trong phần trigger được tạo.
* Ví dụ: 
  * Query: CREATE TRIGGER INSERT_DATA_DONHANG AFTER INSERT on donhang for EACH ROW INSERT into account values (100,1000)
  * Câu query trên có nghĩa là sau khi ta insert giá trị vào bảng donhang thì trong bảng account sẽ tự insert data một cách tự động.  
