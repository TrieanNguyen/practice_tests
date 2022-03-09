## Spark
### 1. Khái niệm Map-Reduce, Partition, Shuffe
### 1.1. Mô hình MapReduce
* Mô hình lập trình MapReduce được thiết kế độc quyền bởi google.
* MapReduce giúp xử lý các tập dữ liệu lớn song song và phân tán trên 1 cụm máy tính.
* MapReduce bao gồm 4 quá giai đoạn:
     * Splits: Input của quy trình MapReduce sẽ được chia thành các phần có kích thước cố định được gọi là input split. Mỗi input split sẽ được làm input cho                       giai đoạn tiếp theo, chính là Mapping.
     * Mapping: Nhận input split là đầu vào, xử lý và cho ra output là các tập dữ liệu các dạng key-value.
     * Shuffling: Nhóm các key-value có cùng key lại thành 1 nhóm. Mỗi nhóm được tạo ra sẽ làm input cho giai đoạn tiếp theo, đó là Reducing.
     * Reducing: Nhận input từ quá trình split, xử lý và cho ra kết quả như bài toán yêu cầu.
### 1.2. Partition
* Partition là các phần dữ liệu được phân tán từ RDD, nhiều Partition sẽ là một RDD.
* Partition sẽ được lưu trên Ram
* Partition kết hợp với cơ chế lazy evaluation giúp xử lý dữ liệu 1 cách nhanh chóng.
### 1.3. Shuffe
* Shuffe là quá trình trộn các Partition khi gặp wide Tranformation
### 2. Các khái niệm cần biết trong Spark
#### 2.1. DataFrame
 * DataFrame là cấu trúc dữ liệu được gắn nhãn hai chiều và đặt biệt mỗi cột là mỗi Series.
 * DataFrame tương tự như SQL tables hoặc bảng tính mà bạn làm việc trong Excel hoặc Calc.
 * DataFrame xây dựng từ nhiều nguồn: có cấu trúc, Hive,...
#### 2.2. RDD
 * RDD là cấu trúc dữ liệu cơ bản của spark
 * Nó là một tập hợp bất biến phân tán của một đối tượng. Mỗi dataset trong RDD được chia ra thành nhiều phần vùng logical. Có thể được tính toán trên các node khác nhau của một cụm máy chủ (cluster).
 * RDD được chia thành nhiều partition, mỗi partition là nơi dữ liệu được phân tán từ RDD.
 * Spark cung cấp các Tranformation và Action để thao tác với RDD.
 * Có 3 cách tạo RDD: 
     * từ dataset hệ thống lưu trữ bên ngoài như HDFS, Hbase hoặc các cơ sở dữ liệu quan hệ.
     * từ một RDD khác
     * từ một tập hợp dữ liệu có sẵn trong ngôn ngữ sử dụng như Java, Python, Scala.
#### 2.3. Cơ bản về Parquet
* Parquet là file chứa dữ liệu, dữ liệu được tổ chức theo dạng cột
* Cải thiện Tốc độ read/write của file txt trong hệ sinh thái Hadoop.
#### 2.4. Transformtion
* Biến đổi một RDD này sang RDD khác là một Transformation
Có 2 loại Transformation:
* Narrow Transformation: Là quá trình biến đổi dữ liệu từ 1 RDD không có sự can thiệp của RDD khác
     * Một số Function thường gặp: map(), mapPartition(), flatMap(), filter(), union().
* Wide Transformation: Là quá trình tính toán sẽ phụ thuộc vào các Partition của các RDD khác để có kết quả cuối cùng.
     * Một số Function: groupByKey(), aggregateByKey(), aggregate(), join(), repartition()
#### 2.5. Action 
* Sau tất cả các phép biến đổi, khi muốn tương tác với kết quả cuối cùng (VD xem kết quả, collect kết quả, ghi kết quả…) ta gọi 1 action.
* Các loại action thường gặp:

     * reduce: thực hiện hàm reduce trên RDD để thu về 1 giá trị duy nhất.

     * count: đếm số dòng trong RDD.

     * countApprox: đếm xấp xỉ số dòng trong RDD, nhưng phải cung cấp timeout vì có thể không nhận được kết quả.

     * list: lấy giá trị đầu tiên của RDD.

     * take: lấy một lượng giá trị từ RDD.        

    
        
 
     
     
     
     
     

