//require user login
function imgUpload(file,callback) {
	var filePath = $(file).val();
	var file_type = filePath.substring(filePath.lastIndexOf('.'),filePath.length);
	var fileName = filePath.substring(filePath.lastIndexOf('\\') + 1,filePath.length);
	
	if (file_type == '.gif' || file_type == '.jpg' || file_type == '.jpeg'|| file_type == '.bmp' || file_type == '.png') {
		jQuery().picUploadLR(file.id,callback,false);
	} else {
		$.messager.alert("提示", "只能上传图片！", "warning");
		$(file).val("");
	}
}

//public no user
function imgUpload4pub(file,callback) {
	var filePath = $(file).val();
	var file_type = filePath.substring(filePath.lastIndexOf('.'),filePath.length);
	var fileName = filePath.substring(filePath.lastIndexOf('\\') + 1,filePath.length);
	
	if (file_type == '.gif' || file_type == '.jpg' || file_type == '.jpeg'|| file_type == '.bmp' || file_type == '.png') {
		jQuery().picUploadLR(file.id,callback,true);
	} else {
		$.messager.alert("提示", "只能上传图片！", "warning");
		$(file).val("");
	}
}

(function($) {
		$.fn.picUploadLR = function (id,callback,isPub) {

			var input = document.querySelector('#'+id);
			
	        lrz(input.files[0], {
	        	
	        	width:1600, 
	        	
	        	quality:0.6,
	            
	        	before: function() {
	                //console.log('压缩开始');
	            },
	            fail: function(err) {
	                //console.error(err);
	            },
	            always: function() {
	                //console.log('压缩结束');
	            },
	            done: function (results) {
	            // 你需要的数据都在这里，可以以字符串的形式传送base64给服务端转存为图片。
	            //console.log(results);

	            setTimeout(function () {

	                // 发送到后端
	                var xhr = new XMLHttpRequest();
	                var data = {
	                    base64: results.base64,
	                    size: results.base64.length // 校验用，防止未完整接收
	                };
	                if(isPub){//pub
	                	xhr.open('POST', '/billyexjg/pub/file/webuploader.do',true);
	                }else{
	                	xhr.open('POST', '/billyexjg/sys/file/webuploader.do',true);
	                }
	                
	                xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
	                xhr.onreadystatechange = function () {
	                	if (xhr.readyState==4 && xhr.status ==200) {
	                		if(xhr.responseText && xhr.responseText.length<100){//响应文本太长可能是网页数据
	                			callback(xhr.responseText,id);
	                		}else{
	                			$.messager.alert("提示", "上传图片出错!", "warning");
	                		}
	             		}
	                };
	                xhr.send(JSON.stringify(data)); // 发送base64
	            }, 100);
	            }
	        });
	    
	}
	})(jQuery);
	

	        
