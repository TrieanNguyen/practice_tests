### KIẾN THỨC CƠ BẢN VỀ SQL
#### Khái niệm database:
* là phân hệ trung tâm của các hệ thống nghiệp vụ xử lý dữ liệu giao dịch.
* Database bao gồm một tập hợp dữ liệu có cấu trúc và một bản thông tin mô tả dữ liệu có cấu trúc đó
(metadata), được thiết kế cho nhu cầu lưu trữ và xử lý thông tin của tổ chức, doanh
nghiệp. Một database thường được cài đặt kèm theo một hệ quản trị cơ sở dữ liệu
(DBMS – Database Management System), tức là một phần mềm cho phép người dùng
định nghĩa, tạo mới, điều khiển và quản trị một database.
* Thiết kế của một database thường được đưa về dạng chuẩn 3 (3NF – 3th Normal Form), quy định rằng mỗi thực thể trong database phải thoả mãn các điều kiện sau:
   - Giá trị của một thuộc tính phải là giá trị nguyên tố, tức là không phải một danh sách các giá trị hoặc giá trị phức hợp (Chuẩn 1).
   - Các thuộc tính không phải khoá phải phụ thuộc đầy đủ vào thuộc tính khóa(Chuẩn 2).
   - Các thuộc tính không phải khoá phụ thuộc trực tiếp vào thuộc tính khóa(Chuẩn 3).
#### Data Warehouse:
* Database thông thường lại không thoả mãn các yêu cầu về phân tích dữ liệu,database thông thường chỉ hỗ trợ tốt các nghiệp vụ hàng ngày và điểm mạnh nhất của nó
là đảm bảo toàn vẹn dữ liệu, xử lý giao dịch, truy cập song song. Database thông thường đó được gọi là database nghiệp vụ (operational database) hoặc hệ thống xử lý giao dịch thời gian thực (online transaction processing – OLTP). Thông thường các database nghiệp vụ chỉ lưu trữ dữ liệu chi tiết cho thời điểm hiện tại, không lưu dữ liệu lịch sử, dữ liệu trong database được thiết kế chuẩn hoá rất cao nên thường có hiệu năng kém khi truy vấn phức tạp (join nhiều bảng dữ liệu với nhau) hoặc khối lượng dữ liệu lớn. Thêm nữa,việc truy vấn dữ liệu từ nhiều nguồn khác nhau là gần như không thể nếu chỉ dùng database nghiệp vụ.
#### 1. TRIGGER
##### 1.1. Khái niệm:
* Trigger là một đối tượng được định danh trong CSDL và luôn gắn chặc với một sự kiên xảy ra trên một bản nào đó. Các sự kiện ở đây có thể là: insert, update, deleted. Có nghĩa có l khi một sự kiện nào xảy ra ở một bảng nào đó trong csdl sẽ tác động đến câu lệnh sql được viết trong phần trigger được tạo.
* Ví dụ: 
  * Query: CREATE TRIGGER INSERT_DATA_DONHANG AFTER INSERT on donhang for EACH ROW INSERT into account values (100,1000)
  * Câu query trên có nghĩa là sau khi ta insert giá trị vào bảng donhang thì trong bảng account sẽ tự insert data một cách tự động.  
#### 2. PROCEDURE
##### 1.1 Khái niệm:
* Là một thủ tục, một hàm phương thức sử dụng câu lệnh sql để thực hiện một nghiệp vụ nhất định.
* Ví dụ: 
   * DELIMITER // CREATE PROCEDURE database_test.test2() BEGIN	SELECT *  FROM database_test.donhang; END // DELIMITER ; 
#### 3. INDEX 
##### 1.1 Khái niệm:
*  Công cụ tìm kiếm cơ sở dữ liệu có thể sử dụng để tăng nhanh thời gian và hiệu suất truy xuất dữ liệu. Hiểu đơn giản, một chỉ mục là một con trỏ chỉ tới từng giá trị xuất hiện trong bảng/cột được đánh chỉ mục. 
*  Các kiểu index có trong SQL:
    * Single-Column Index: là đánh index cho một cột duy nhất
      * Cú Pháp:
         * CREATE INDEX ten_index ON ten_bang (ten_cot);
    * Unique Index: là chỉ mục duy nhất, được sử dụng để tăng hiệu suất và đảm bảo tính toàn vẹn dữ liệu. Một chỉ mục duy nhất không cho phép chèn bất kỳ giá trị trùng lặp nào được chèn vào bảng
      * Cú Pháp:
         * CREATE UNIQUE INDEX ten_index ON ten_bang (ten_cot);
    * Composite Index:  là chỉ mục kết hợp dành cho hai hoặc nhiều cột trong một bảng.
       * Cú Pháp:
         * CREATE UNIQUE INDEX ten_index ON ten_bang (cot1, cot2);




