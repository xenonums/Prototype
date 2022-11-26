function Pages(index,total,totalPage,rows){
		var html=[];
		var prev=0;
		var next=0;
		if(index>1){
			prev=index-1;
		} else {
			prev=1;
		}
		if(index<totalPage){
			next=index+1;
		} else {
			next=totalPage;
		}
		html.push('<div class="total_page">共'+total+'条记录 第（'+index+'/'+totalPage+'）页</div>');
		html.push('<div class=\"publicity_fenye\"><ul>');
		html.push('<li><a href="javascript:goPages(1)" class="current">首页</a></li>');
		html.push('<li><a href="javascript:goPages('+prev+')">上一页</a></li><li><a href="javascript:goPages('+next+')">下一页</a></li>');
		html.push('<li><a href="javascript:goPages('+totalPage+')">尾页</a></li>');
		html.push('</ul><div>第 <input type="txt" id="pageNum" name="pageNum" class="txt-input" /> 页 <input type="button" id="goPage" class="btn-input" value="GO" /></div>');
		html.push('</div><div style=\"clear:both;\"></div>');
		$(".publicity_page").html(html.join(""));
		$("#goPage").click(function(){
			var p = $("#pageNum").val();
			if(isInt(p)){
				p = parseInt(p);
			}  else {
				return;
			}
			goPages(p);
		});
		$("#pageNum").val(index);
	}
	function isInt(s){
		 var patrn=/^\d+$/;
			if (patrn.exec(s)) {
				return true;
			}else{
				return false;
			}
	}
	
	function formateDate(date){
		if(date){
			if(date.length>10){
				return date.substring(0,10);
			} else {
				return date;
			}
		} else {
			return "";
		}
	}
	var g_UserLoginId = '';
	var g_UserName = 'loadmin';    //登录用户名
	var g_PassWord = '*uniview123';    //登录用户密码
	var g_ServerIP = '60.165.208.210';    //服务器IP地址
	var g_Port ="8800";
	var g_imosActivePlayer = null;
	var g_curFrameNum = '1';
	var g_xmlActive = null;
	var g_PlayFrame1 = null;
	var gs_url = 'http://www.gsspaqw.org/sycms/html';