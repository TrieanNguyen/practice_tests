## SPARK
### 1.DataFrame
 * DataFrame là cấu trúc dữ liệu được gắn nhãn hai chiều và đặt biệt mỗi cột là mỗi Series.
 * DataFrame tương tự như SQL tables hoặc bảng tính mà bạn làm việc trong Excel hoặc Calc.
 * DataFrame xây dựng từ nhiều nguồn: có cấu trúc, Hive,...
### 2.RDD
 * RDD là cấu trúc dữ liệu cơ bản của spark
 * Nó là một tập hợp bất biến phân tán của một đối tượng. Mỗi dataset trong RDD được chia ra thành nhiều phần vùng logical. Có thể được tính toán trên các node khác nhau của một cụm máy chủ (cluster).
 * RDD được chia thành nhiều partition, mỗi partition là nơi dữ liệu được phân tán từ RDD.
 * Spark cung cấp các Tranformation và Action để thao tác với RDD.
 * Có 3 cách tạo RDD: 
        * từ dataset hệ thống lưu trữ bên ngoài như HDFS, Hbase hoặc các cơ sở dữ liệu quan hệ.
        * từ một RDD khác
        * từ một tập hợp dữ liệu có sẵn trong ngôn ngữ sử dụng như Java, Python, Scala.
        
 
     
     
     
     
     

