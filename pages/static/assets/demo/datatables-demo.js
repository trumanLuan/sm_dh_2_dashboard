// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable();

  $('#dataTable tbody').on('click', '.myButton', function() {
    var itemName = $(this).data('item-name'); // 获取按钮上存储的项目名称
    console.log(itemName);

    var csrftoken = "{{csrf_token}}";

    // 发送AJAX请求到后端视图函数，并传递项目ID和名称作为参数
    $.ajax({
      url: '/pages/browse_results/',
      type: 'POST',
      data: {
        'item_name': itemName
      },
      success: function(response) {
        // 处理成功响应
        console.log(response);
        // 在此处执行您希望的操作，例如根据响应数据更新页面内容
      },
      error: function(xhr, textStatus, error) {
        // 处理错误响应
        console.log(xhr.responseText);
        // 在此处执行适当的错误处理逻辑
      }
    });
  });
});
