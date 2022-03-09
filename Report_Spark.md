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
 ### 3. Các khái niệm quan trọng trong Spark
 * Spark được hỗ trợ quản lý cụm b 4 cụm:
   * Hadoop Yarn
   * Standalone
   * kubernetes
   * Apache Mesos
 #### 3.1. CLient-Mode
 * Khi một spark job được deploy với client-mode thì Spark Driver sẽ được chạy bên trong máy submit job và Spark Context sẽ sống ở máy submit.
 * Ta có thể xem log ngay trên máy submit job, nếu nhấn Ctrl + C thì job sẽ bị dừng.
 * Thường được sử dụng để debug hoặc cho job cần có sự tương tác.
 * Khi một máy submit là máy bên trong cụm thì nên ưu tiên dùng chế độ này, vì nếu dùng cluster thì có thể sẽ tốn thời gian chuyển file jar nếu file jar quá lớn.
 #### 3.2. Cluster-Mode
 * Khi một Spark Job được deploy với cluster-mode thì Spark Driver sẽ được chạy trong bất cứ worker nào được chỉ định, và Spark Context sẽ sống ở worker đó.
 * Ta có thể xem log ở giao diện Web.
 * Khi một máy submit ở xa với cụm thì nên ưu tiên sử dụng chế độ này, vì nếu dùng client thì hiệu suất của job sẽ bị ảnh hưởng bởi đường truyền mạng.
 #### 3.3. Drive
 * Khái niệm:
   * Driver là một Java process.
   * Process thực thi được các chương trình viết bằng Scala, Java, Python.
   * Thực thi code và tạo một SparkSession hoặc SparkContext.SparkSession có trách nhiệm tạo các DataFrame, DataSet, RDD, truy vấn SQL, thực hiện Transformation và Action,...
 * Chịu trách nhiệm:
   * Hàm main của chương trình được chạy trong một Driver process: tạo SparkSession hoặc SparkContext.
   * Chuyển code của chương trình thành các Task (Transformation và Action) và xác định số Task.
   * Giúp tạo Lineage, Logical Plan và Physical Plan.
   * Lineage: Khi một RDD mới được tạo từ một RDD cha thông qua Transformatoin thì RDD mới đó sẽ chứa một con trỏ, trỏ đến RDD cha. Spark sẽ theo dõi mối quan hệ giữa các RDD này bằng cách sử dụng một thành phần được gọi là Linage. Khi một RDD bị mất dữ liệu thì Linage sẽ có nhiệm vụ khôi phục lại dữ liệu.

 * Logical Plan: Là kế hoạch mô tả những đầu ra mong đợi sau khi áp dụng một loạt các Transformation như join, filter, where, groupBy,...
 * Physical Plan: Là kế hoạch quyết định loại join và trình tự thực hiện các lệnh filter, where, groupBy, ...
 * Khi một Physical Plan được tạo, Driver sẽ kết hợp với Cluster Manager lập lịch thực thi những Task.
 * Theo dõi metadata ở các Executor.
#### 3.4. Worker
* Worker là thành phần của một cụm Spark cụ thể, nơi mà các executor sống để thực thi các task. Người ta thường gọi là các node tính toán trong Spark.
* Worker chia ram và core được yêu cầu cho các executor thực thi bên trong đó.
* Nếu một worker gặp vấn đề thì những task được của các executor bên trong worker đó sẽ được chuyển sang các executor ở các worker khác.

### 3.5. Executor, memory, cores của worker
* Executor nằm trong các worker, mỗi worker có thể chứa nhiều executor nếu nó có đủ memory và core. 
* Mỗi executor sẽ dùng lượng memory và core cho phép.
* Số lượng core trong mỗi executor nên đặt trong khoảng từ 2 đến 5. Vì nếu quá nhiều core dẫn đến việc có quá nhiều request đọc dữ liệu từ HDFS, làm giảm hiệu suất của executor. Hoặc nếu chỉ có 1 executor thì không tận dụng được ưu điểm xử lý đa luồng của JVM.
* Executor thực thi các task được giao và trả kết quả về cho driver thông qua cluster manager.

### 3.6. Executor, memory, cores của driver
* Driver cũng sử dụng lượng memory và core được yêu cầu để đảm nhiệm các công việc như đã nói ở phần trên.
* Driver đa số không cần xử lý đa luồng nên số lượng core nên đặt mặc định là 1.
* Tuy nhiên để tăng tốc độ xử lý của driver thì lượng memory cần được đặt bằng hoặc lớn hơn lượng memory trong executor.

### 3.7. Applications, tasks, stages, jobs
* Application là một chương trình tính toán dùng để chạy code do người dùng cung cấp. Nó bao gồm driver và các executor.
* Job là một công việc tính toán song song bao gồm nhiều Task. Một job được sinh ra khi có 1 action được gọi trong code.
* Mỗi job sẽ được chia thành nhiều Stage. Một Stage được sinh ra nếu gặp wide transformation (ví dụ: reduceByKey,...)
* Mỗi stage gồm một nhóm các Task, mỗi task trên mỗi partition.

    
        
 
     
     
     
     
     

