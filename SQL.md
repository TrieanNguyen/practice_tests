### KIẾN THỨC CƠ BẢN VỀ SQL
#### Khái niệm database:
* là phân hệ trung tâm của các hệ thống nghiệp vụ xử lý dữ liệu giao dịch.
* Database bao gồm một tập hợp dữ liệu có cấu trúc và một bản thông tin mô tả dữ liệu có cấu trúc đó
(metadata), được thiết kế cho nhu cầu lưu trữ và xử lý thông tin của tổ chức, doanh
nghiệp. Một database thường được cài đặt kèm theo một hệ quản trị cơ sở dữ liệu
(DBMS – Database Management System), tức là một phần mềm cho phép người dùng
định nghĩa, tạo mới, điều khiển và quản trị một database.
* Thiết kế của một database thường được đưa về dạng chuẩn 3 (3NF – 3th Normal Form), quy định rằng mỗi thực thể trong database phải thoả mãn các điều kiện sau:
   - Giá trị của một thuộc tính phải là giá trị nguyên tố, tức là không phải một danh
   sách các giá trị hoặc giá trị phức hợp (Chuẩn 1).
   - Các thuộc tính không phải khoá phải phụ thuộc đầy đủ vào thuộc tính khóa(Chuẩn 2).
   - Các thuộc tính không phải khoá phụ thuộc trực tiếp vào thuộc tính khóa(Chuẩn 3).
#### 1. TRIGGER
##### 1.1. Khái niệm:
* Trigger là một đối tượng được định danh trong CSDL và luôn gắn chặc với một sự kiên xảy ra trên một bản nào đó. Các sự kiện ở đây có thể là: insert, update, deleted. Có nghĩa có
l khi một suự kiện nào xảy ra ở một bảng nào đó trong csdl sẽ tác động đến câu lệnh sql được viết trong phần trigger được tạo.
* Ví dụ: 
  * Query: CREATE TRIGGER INSERT_DATA_DONHANG AFTER INSERT on donhang for EACH ROW INSERT into account values (100,1000)
  * Câu query trên có nghĩa là sau khi ta insert giá trị vào bảng donhang thì trong bảng account sẽ tự insert data một cách tự động.  
#### 2. PROCEDURE
##### 1.1 Khái niệm:
* Là một thủ tục, một hàm phương thức sử dụng câu lệnh sql để thực hiện một nghiệp vụ nhất định.
* Ví dụ: 
   * DELIMITER // CREATE PROCEDURE database_test.test2() BEGIN	SELECT *  FROM database_test.donhang; END // DELIMITER ; 
