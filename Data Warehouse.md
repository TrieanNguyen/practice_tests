### Các khái niệm liên quan trong Data warehouse
#### ODBC
##### Khái niệm: 
* ODBC(Open Database Connectivity - kết nối cơ sở dữ liệu mới). Mục đích của ODBC là cung cấp cho các trình ứng dụng khả năng truy xuất dữ liệu bất kì mà không phải quan tâm đến việc hiện tại dữ liệu đang được quản lý bởi hệ quản trị cơ sở dữ liệu nào.
  ODBC làm được việc này bằng cách chèn một lớp trung gian vào giữa trình ứng dụng và hệ quản trị cơ sở dữ liệu. 
  Lớp trung gian đó được gọi là một database driver (trình điều vận cơ sở dữ liệu). Mục đích của lớp trung gian này là chuyển đổi những câu truy vấn của trình ứng dụng thành những lệnh mà hệ quản trị cơ sở dữ liệu hiểu. Để làm được việc này thì cả hai trình ứng dụng và hệ quản trị cơ sở dữ liệu phải hiểu biết ODBC, 
tức là trình ứng dụng phải có khả năng tạo ra những lệnh ODBC và hệ quản trị cơ sở dữ liệu phải có khả năng đáp lại những lệnh đó.
#### Data Factory:
* Cho phép bạn tạo và lập lịch các quy trình làm việc theo hướng dữ liệu (được gọi là đường ống) có thể nhập dữ liệu từ các kho dữ liệu khác nhau, xử lý / chuyển đổi dữ liệu bằng cách sử dụng các dịch vụ tính toán như Azure HDInsight Hadoop, Spark, Azure Data Lake Analytics và Azure Machine Learning, và xuất bản dữ liệu đầu ra tới các kho dữ liệu như Kho dữ liệu Azure SQL để các ứng dụng thông minh kinh doanh (BI) sử dụng. Cuối cùng, thông qua Azure Data Factory, dữ liệu thô có thể được sắp xếp thành các kho dữ liệu và hồ dữ liệu có ý nghĩa để đưa ra các quyết định kinh doanh tốt hơn.
#### Json
##### Khái niệm:
* Định dạng JSON sử dụng các cặp key – value để dữ liệu sử dụng. Nó hỗ trợ các cấu trúc dữ liệu như đối tượng và mảng.
* Object trong Json được thể hiện bằng dấu ngoặc nhọn {}. Khái niệm Object trong Json cũng khá tương đồng với Object trong Javascript. Tuy nhiên, Object trong Json vẫn có những giới hạn như:
Key: phải luôn nằm trong dấu ngoặc kép, không được phép là biến số.
Value: Chỉ cho phép các kiểu dữ liệu cơ bản: numbers, String, Booleans, arrays, objects, null. Không cho phép function, date, undefined.
Không cho phép dấy phẩy cuối cùng như Object trong Javascript.
Kiểu OBJECT
var nhat = {
   "firstName" : "Nhat",
   "lastName" : "Nguyen",
   "age" :  "34"
};
Kiểu OBJECT IN ARRAY
var employees = [{
   "name" : "Binh",
   "age" :  "38",
   "gender" : "male"
 
},
{
   "name" : "Nhu",
   "age" : "25",
   "gender" : "female"
}];
Kiểu NEST OBJECT
var employees = {
  "hieu" : {
  "name" : "Hieu",
  "age" :  "29",
  "gender" : "male" 
},
"nhu" : {
  "name" : "Nhu",
  "age" : "25",
  "gender" : "female"
}
}
