### Các khái niệm liên quan trong Data warehouse
#### ODBC
##### Khái niệm: 
* ODBC(Open Database Connectivity - kết nối cơ sở dữ liệu mới). Mục đích của ODBC là cung cấp cho các trình ứng dụng khả năng truy xuất dữ liệu bất kì mà không phải quan tâm đến việc hiện tại dữ liệu đang được quản lý bởi hệ quản trị cơ sở dữ liệu nào.
  ODBC làm được việc này bằng cách chèn một lớp trung gian vào giữa trình ứng dụng và hệ quản trị cơ sở dữ liệu. 
  Lớp trung gian đó được gọi là một database driver (trình điều vận cơ sở dữ liệu). Mục đích của lớp trung gian này là chuyển đổi những câu truy vấn của trình ứng dụng thành những lệnh mà hệ quản trị cơ sở dữ liệu hiểu. Để làm được việc này thì cả hai trình ứng dụng và hệ quản trị cơ sở dữ liệu phải hiểu biết ODBC, 
tức là trình ứng dụng phải có khả năng tạo ra những lệnh ODBC và hệ quản trị cơ sở dữ liệu phải có khả năng đáp lại những lệnh đó.
  
