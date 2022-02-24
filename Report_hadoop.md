## Hadoop
### 1. Hadoop
#### 1.1. Hệ thống file DFS:
- Là một hệ thống tệp được phân phối trên nhiều máy chủ tệp hoặc nhiều vị trí.
- Nó cho phép các chương trình truy cập hoặc lưu trữ các tệp riêng biệt như chúng làm với các tệp cục bộ, cho phép các lập trình viên truy cập tệp từ bất kỳ mạng hoặc máy tính nào.
#### 1.2. So sánh ưu nhược điểm các hệ thống DFS phổ biến

|DFS|Ưu điểm|Nhược điểm|
|:--:|:--|:--|
|HDSF| + Mã nguồn mở <br> + Khả năng lưu trữ cao <br> + Có khả năng mở rộng và chịu lỗi cao <br> + Ít tốn chi phí vì lưu trữ trên phần cứng <br> + Khả năng phục hồi dữ liệu nhanh khi gặp sự cố | + Một máy phải xử lý một lượng lớn request dữ liệu nếu dữ liệu đó chỉ nằm trên một máy <br> + Client phải copy dữ liệu về máy rồi mới thao tác được trên dữ liệu đó <br> + Không có gì để đảm bảo một máy có thể bị sập bất cứ lúc nào|
|Ceph| + Mã nguồn mở <br> + Sử dụng thuật toán CRUSH thay vì metadata giúp khả năng truy cập vào dữ liệu cao <br> + Có khả năng mở rộng <br> + Dữ liệu được bảo mật và tính linh họat cao | + Yêu cầu cấu hình hệ thống mạng đủ mạnh <br> + Tốn nhiều thời gian để cấu hình <br>|
|MooseFS| + Cấu hình đơn giản, dễ dàng quản lý <br> + Hỗ trợ cơ chế mở rộng trực tuyến, giúp nâng cao khả năng mở rộng <br> + Khả năng chịu lỗi cao <br> + Việc khôi phục dữ liệu tương đối dễ dàng| + Node MFS master tiêu tốn bộ nhớ <br> + Đối với các tệp nhỏ hơn 64KB, tỉ lệ sử dụng bộ nhớ thấp |
|GlusterFS| + Mã nguồn mở <br> + Hỗ trợ POSIX, PUSE giúp truy cập qua nhiều giao thức với tính linh hoạt cao <br> + Hỗ trợ cơ chế mở rộng trực tuyến, giúp nâng cao khả năng mở rộng <br> + Khả năng chịu lỗi cao <br> + Cung cấp command line đơn giản về dễ sử dụng <br> + Dễ dàng thêm các node vào cụm| + Tính linh hoạt càng mạng thì càng nhiều lớp trải dài, do đó ảnh hưởng đến hiệu quả xử lý IO <br> + Thường xuyên đọc và viết dẫn đến xuất hiện nhiều tập tin rác làm ảnh hưởng đến bộ nhớ |
|FastDFS| + Không hỗ trợ POSIX, giúp giảm độ phức tạp của hệ thống và có hiệu quả xử lý cao hơn <br> + Hỗ trợ cơ chế mở rộng trực tuyến, giúp nâng cao khả năng mở rộng <br> + Khả năng chịu lỗi và tính khả dụng cao | + Không hỗ trợ POSIX làm tính linh hoạt giảm <br> + Quá trình đồng bộ hóa qua mạng nên có độ trễ cao <br> + Cơ chế đồng bộ hóa không hỗ trợ xác minh tệp, điều này làm giảm tính linh hoạt của hệ thống|
#### 1.3. Kiến trúc của Hadoop
##### 1.3.1. Khái niệm Hadoop:
- Hadoop là hệ thống file phân tán được phát hành bởi Apache, sử dụng để lưu trữ dữ liệu phân tán và xử lý dữ liệu song song trên các tập dữ liệu lớn.
- Hadoop được viết bằng java và có hỗ trợ các ngôn ngữ C++, Python,...
- Hadoop không phải là OLAP (online analytical processing)
- Một cụm Hadoop bao gồm 1 master và nhiều node slave/worker. Toàn bộ chứa 2 lớp: Mapreduce layer và HDFS layer. 
- Master Node bao gồm: JobTracker, TaskTracker, NameNode, và DataNode.
- Slave/worker Node bao gồm: TaskTracker, DataNode. Slave cụ thể là nơi trực tiếp lưu trữ và xử lý dữ liệu.
##### 1.3.2. HDFS(Hadoop Distrubuted file system):
- HDFS là hệ thống lưu trữ file phân tán của Hadoop.
- HDFS sử dụng kiến trúc Master/slave:
Master gồm 1 node được gọi 1 NameNode để quản lý metadata, metadata bao gồm: tên của file, kích thước file, thông tin của block,... Đồng thời điều phối các tác vụ xóa, tạo, nhân bản các block
Slave gồm 1 hoặc nhiều DataNode để lưu trữ dữ liệu.
- Một file được lưu trữ trên HDFS sẽ được chia nhỏ thành các block với kích thước mặc định là 128MB (có thể thay đổi được), mỗi block sẽ được nhân bản để lưu trên nhiều DataNode. Chính điều này giúp HDFS có khả năng chịu lỗi và tính sẵn sàng cao.
- Rack là tập hợp các DataNode sử dụng cùng 1 switch (thường là khoảng 40 đến 50 DataNode). 
- Hadoop tin rằng, các NameNode trên cùng 1 Rack sẽ giao tiếp với nhau tốt hơn là khác Rack.
- Thuật toán Rack Awareness quy định:
    * Thông thường có 3 block, 1 block cùng 1 DataNode, 1 block còn lại nằm ở DataNode khác 
    * Không có quá 2 nhân bản của 1 block trên cùng 1 Rack.
- Thuật toán Rack Awareness giúp NameNode có thể chọn dược DataNode gần nhất giúp đạt được hiệu suất tối đa khi đọc và ghi dữ liệu.
##### 1.3.3. Map-Reduce:
- Map-reduce giúp Hadoop xử lý dữ liệu song song.
- Đây là hệ thống dựa trên YARN dùng để xử lý song song các tập dữ liệu lớn.
- 1 Map-Reduce gồm 4 giai đoạn:
  - Splits: Input của quy trình MapReduce sẽ được chia thành các phần có kích thước cố định được gọi là input split. Mỗi input split sẽ được làm input cho giai đoạn tiếp theo, chính là Mapping.
  - Mapping: Nhận input split là đầu vào, xử lý và cho ra output là các tập dữ liệu các dạng key-value.
  - Shuffling: Nhóm các key-value có cùng key lại thành 1 nhóm. Mỗi nhóm được tạo ra sẽ làm input cho giai đoạn tiếp theo, đó là Reducing. 
  - Reducing: Nhận input từ quá trình split, xử lý và cho ra kết quả như bài toán yêu cầu.
- Hadoop chia 1 job ra thành nhiều task. Trong đó có 2 loại task: Map task (Splits và Mapping) và Reduce tasks (Shuffing và Reducing)
- MapReduce cũng sử dụng kiến trúc master/slave:
   - Master - Job Tracker: Lên lịch cho các task và phân công xuống và theo dõi Tasktracker.
   - Slave - Task Tracker: Theo dõi các task và báo cáo trạng thái các task cho Job Tracker
##### 1.3.4. YARN (Yet Another Resource Negotiator)
* YARN là một framework cung cấp các daemon và API cần thiết giúp phát triển ứng dụng phân tán.
* YARN chịu trách nhiêm xử lý và lập lịch sử dụng tài nguyên tính toán (CPU hay memory) cũng như giám sát quá trình thực thi các ứng dụng đó.
* YARN có 2 trình xử lý:
    * ResourceManager: quản lý toàn bộ tài nguyên tính toán của cụm.
    * NodeManager: giảm sát việc sử dụng tài nguyên (CPU, memory, disk, network,...) của container và báo cáo với ResourceManager.
* ResourceManager có hai thành phần quan trọng:
    * Scheduler: Có trách nhiệm phân bổ tài nguyên cho các ứng dụng khác nhau.
    * ApplicationManager: Có chức năng:
        * Nhận một job được submit
        * Tìm 1 container hợp lý để thực thi ApplicationMaster.
        * Khởi động lại container ApplicationMaster khi không thành công.
##### 1.3.5. Hadoop Common
* Hadoop Common là một bộ các library hoặc utilities giúp hỗ trợ các module khác của Hadoop.
* Người ta còn gọi với 1 cái tên khác là Hadoop Core.






       
    
