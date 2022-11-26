/**
 * 根据json对象属性名获取对应值，支持parent.id属性包含子属性
 * 
 * @param jsonObj
 *            jsong数据
 * @param propertyName
 *            json数据中属性名，只是parent.id
 * @returns
 */
function getJsonObjValue(jsonObj, propertyName) {
	var result = jsonObj[propertyName];
	/*
	 * 使datagrid的field支持属性的紫属性field.attr格式的显示
	 * （优先采取原程序的方法如果在原程序方法获取不到的情况下使用新的方法来获取需要展示的值）
	 */
	if (!Boolean(result) && propertyName.indexOf('.') > 0) {
		var singleNames = propertyName.split('.');
		result = jsonObj[singleNames[0]];
		for (var i = 1; i < singleNames.length; i++) {
			if (result != null) {
				result = result[singleNames[i]];
			} else {
				break;
			}
		}
		/* 网上解决办法，但是当对象为空是出错 */
		// _728=eval("_725['"+_727.replace(/\./g,"']['")+"']");
	}
	return result;
};
/**
 *  * @author zenghb
 */
$(function(){
	var doc = window.document, input = doc.createElement('input');
	if( typeof input['placeholder'] == 'undefined' ) // 如果不支持placeholder属性
	{
	    $('input').each(function( ele )
	    {
	        var me = $(this);
	 
	        var ph = me.attr('placeholder');
	 
	        if( ph && !me.val() )
	        {
	            me.val(ph).css('color', '#aaa').css('line-height', me.css('height'));
	        }
	        me.on('focus', function()
	        {
	            if( me.val() === ph)
	            {
	                me.val(null).css('color', '');
	            }
	        }).on('blur', function()
	        {
	            if( !me.val() )
	            {
	                me.val(ph).css('color', '#aaa').css('line-height', me.css('height'));
	            }
	        });
	    });
	}
});
/**
 * @param arg1 除数
 * @param arg2 被除数
 * @author zenghb
 * 除法函数，用来得到精确的除法结果 说明：javascript的除法结果会有误差，在两个浮点数相除的时候会比较明显。这个函数返回较为精确的除法结果。
 * 调用：accDiv(arg1,arg2) 返回值：arg1除以arg2的精确结果 返回精确除法运算结果
 */
function accDiv(arg1, arg2) {
	var t1 = 0, t2 = 0, r1, r2;
	try {
		t1 = arg1.toString().split(".")[1].length
	} catch (e) {
	}
	try {
		t2 = arg2.toString().split(".")[1].length
	} catch (e) {
	}
	with (Math) {
		r1 = Number(arg1.toString().replace(".", ""));
		r2 = Number(arg2.toString().replace(".", ""));
		return (r1 / r2) * pow(10, t2 - t1);
	}
};
/**
 * @param arg1 乘数
 * @param arg2 被乘数
 * @author zenghb
 * 说明：javascript的乘法结果会有误差，在两个浮点数相乘的时候会比较明显。这个函数返回较为精确的乘法结果。
 */

function accMul(arg1, arg2) {
	var m = 0, s1 = arg1.toString(), s2 = arg2.toString();
	try {
		m += s1.split(".")[1].length
	} catch (e) {
	}
	try {
		m += s2.split(".")[1].length
	} catch (e) {
	}
	return Number(s1.replace(".", "")) * Number(s2.replace(".", ""))
			/ Math.pow(10, m);
};

/**
 * 格式化浮点数,小数点后保留3位,去除小数点后的0
 * @param value	待处理的浮点数
 * @returns
 */
function formatterFloat(value){
	value = parseFloat(value + "").toFixed(3);
	value = value + "";
	if (value.indexOf(".") > 0) {
		value = value.replace(/0+?$/g, "");// 去掉多余的0
		value = value.replace(/[.]$/g, "");// 如最后一位是.则去掉
	}
	return value;
}

/**
 * 格式化日期字符串,去年最后的 00:00:00
 * @param value	待处理的日期字符串
 * @returns
 */
function formatterDate(value){
	//ie浏览器不支持new Date("2016-07-28 00:00:00")；
	//JavaScript中Date的构造参数是2016/07/28或2016/07/28 00:00:00之类的字符串
	//将日期格式2016-07-28 00:00:00，替换成2016/07/28 00:00:00的格式,解决浏览器兼容的问题
	if(!value) return "";
	value = value.replace(/-/g,'/').replace(/T|Z/g,' ').trim();
	if (value != null) {
	var date = new Date(value);
	return date.getFullYear() + '-' + (date.getMonth() + 1) + '-'
	+ date.getDate();
	}
}


function formatterLot(lotnumber){
	var lotnumbers=new Date((lotnumber).replace(/-/,"/"))+"";
	return 	lotnumbers.substring(0,10)+" 00:00:00 CST "+lotnumbers.substring(11,15);
}
/**
 * 将业务字典列表json字符串处理成map
 * 
 * 依赖于json2.js
 * 
 * @param value	待处理的json字符串
 * @returns
 */
function jsonStr2dictMap(dictsJson){
	var ret = new HashMap();
	var jsonList = JSON.parse(dictsJson);
	for(var i=0; i < jsonList.length; i++){
		ret.put(jsonList[i].dvalue,jsonList[i].dname);
	}
	return ret;
}

function json2dictMap(jsonList){
	var ret = new HashMap();
	for(var i=0; i < jsonList.length; i++){
		ret.put(jsonList[i].dvalue,jsonList[i].dname);
	}
	return ret;
}


/**
 * 简单的JS HashMap实现
 * @author tanw
 */
function HashMap() {
	/** Map 大小 **/
	var size = 0;
	/** 对象 **/
	var entry = new Object();

	/** 存 **/
	this.put = function(key, value) {
		if (!this.containsKey(key)) {
			size++;
		}
		entry[key] = value;
	};

	/** 取 **/
	this.get = function(key) {
		return this.containsKey(key) ? entry[key] : null;
	};

	/** 删除 **/
	this.remove = function(key) {
		if (this.containsKey(key) && (delete entry[key])) {
			size--;
		}
	};

	/** 是否包含 Key **/
	this.containsKey = function(key) {
		return (key in entry);
	};

	/** 是否包含 Value **/
	this.containsValue = function(value) {
		for ( var prop in entry) {
			if (entry[prop] == value) {
				return true;
			}
		}
		return false;
	};

	/** 所有 Value **/
	this.values = function() {
		var values = new Array();
		for ( var prop in entry) {
			values.push(entry[prop]);
		}
		return values;
	};

	/** 所有 Key **/
	this.keys = function() {
		var keys = new Array();
		for ( var prop in entry) {
			keys.push(prop);
		}
		return keys;
	};

	/** Map Size **/
	this.size = function() {
		return size;
	};

	/* 清空 */
	this.clear = function() {
		size = 0;
		entry = new Object();
	};
}



/**
 * 普通表单提交时调用easyui validate
 * @param aForm  		要提交的表单对象
 * @author tanw
 * @requires jQuery,EasyUI
 */
function checkForm(oneForm){
	if( typeof hack_checkForm === 'function' ){
		if(! hack_checkForm(oneForm)){
			return false;
		}
	}
	//表单校验
	return $(oneForm).form('validate');
}

/**
 * @author tanw
 * 
 * @requires jQuery
 * 
 * 将form表单元素的值序列化成对象
 * 
 * @returns object
 */
$.serializeObject = function(form) {
	var o = {};
	$.each(form.serializeArray(), function(index) {
		if (o[this['name']]) {
			o[this['name']] = o[this['name']] + "," + this['value'];
		} else {
			o[this['name']] = this['value'];
		}
	});
	return o;
};


//日期格式转换
function pb_longDateFormatter(pb_value, pb_row, pb_index) {
	if(pb_value == null){
		return "";
	} 
	var date = new Date(pb_value);
	var year = date.getFullYear().toString(); 
	var month = (date.getMonth() + 1); 
	var day = date.getDate().toString(); 
	var hour = date.getHours().toString();
	var minutes = date.getMinutes().toString();
	var seconds = date.getSeconds().toString();
	if (month < 10) {
		month = "0" + month;
	}
	if (day < 10) {
		day = "0" + day;
	}
	if (hour < 10) {
		hour = "0" + hour;
	}
	if (minutes < 10) {
		minutes = "0" + minutes;
	}
	if (seconds < 10) {
		seconds = "0" + seconds;
	} 
	return year + "-" + month + "-" + day + " " + hour + ":" + minutes + ":"
			+ seconds;
};

function pb_dataFlush(pb_isTreeGridTable){
	 if(pb_isTreeGridTable){
	     $('#baseGrid').treegrid('reload');// reload the user data
	     }else {
	     $('#baseGrid').datagrid('reload'); // reload the user data
	  }
};

/**
 * 枚举类型格式化基础工具方法
 * @param listJsonStr
 * @returns
 */
function pb_baseEnumFormatter(pb_listJsonStr,pb_enumValue) {
	//alert(items);
	var pb_itemsObj = JSON.parse(pb_listJsonStr);
	for(var pb_index in pb_itemsObj){
		var pb_item = pb_itemsObj[pb_index];
		if(pb_enumValue == pb_item.value){
			return pb_item.label;
		}
	}
	return pb_enumValue;
}; 

/**
 * 扩展combobox下拉框增加全部属性，提供查询使用
 * @param pb_domId  下拉框的属性id ，pb_jsonAttr远程得到数据, hasAll是否添加全部
 * @returns
 */
function pb_comboboxSelect(pb_domId,pb_jsonAttr,hasAll){
	var gradeAttr;
	if(hasAll){
		gradeAttr = [{"dname":"全部","dvalue":""}]; 
	}else{
		gradeAttr = []; 
	}
	
	$.each(pb_jsonAttr,function(index,child){
		gradeAttr.push(child);
	})
	$("#"+pb_domId).combobox("loadData",gradeAttr); 
};


//低版本IE不兼容placeholder属性时改用js处理
$(function(){
	var doc = window.document, input = doc.createElement('input');
	if( typeof input['placeholder'] == 'undefined' ) // 如果不支持placeholder属性
	{
	    $('input').each(function( ele )
	    {
	        var me = $(this);
	 
	        var ph = me.attr('placeholder');
	 
	        if( ph && !me.val() )
	        {
	            me.val(ph).css('color', '#aaa').css('line-height', me.css('height'));
	        }
	        me.on('focus', function()
	        {
	            if( me.val() === ph)
	            {
	                me.val(null).css('color', '');
	            }
	        }).on('blur', function()
	        {
	            if( !me.val() )
	            {
	                me.val(ph).css('color', '#aaa').css('line-height', me.css('height'));
	            }
	        });
	    });
	}
})

/**
 * 通过文件名称，对图片路径进行拆分，并返回图片路径
 * @param picpath
 * @returns {String}
 */
/*function transPicpathJs(picpath){
	if(picpath == null || picpath.length < 9){
		return "";
	}else{
		if("_" == (picpath.substring(8,9))){
			return  picpath.substring(0,6) + "/" +picpath.substring(6,8) + "/" + picpath;
		}
	}
	return "noPic.jpg";
}*/
/**
 * 通过文件名称，对图片路径进行拆分，并返回图片路径
 * @param picpath
 * @returns {String}
 */
function transPicpathJs(picpath){
	if(picpath == null || picpath.length < 9){
		return "";
	}else{
		if("_" == (picpath.substring(8,9))){
			return  picpath.substring(0,6) + "/" +picpath.substring(6,8) + "/" + picpath;
		} else {
			return picpath="2011XX/"+picpath;
		}
		
	}
	return "noPic.jpg";
}
/**
 * 打开文件
 * @param path
 * @param fileid
 */
function lookUploadfile(path,fileid){
	var filename = $("#"+fileid).val();
	var url=path+filename.substring(0,6)+"/"+filename.substring(6,8);
	 url += "/"+filename;
	window.open(url,"文件下载","");
} 


/**
 * 
 * ===============================================================================================
 * 以下方法为内网监管添加的
 */

function isFloat(s){
    if(!s)
    	return false;
	var patrn=/^(-?\d+)(\.\d+)?$/;
	if (patrn.exec(s)) {
		return true;
	}else{
		return false;
	}
}

   //输出JS对象内部属性
   function dump_obj(myObject) {
    	  var s = "";
    	  for (var property in myObject) {
    	      s = s + "\n "+property +": " + myObject[property] ;
    	  }
    	  alert(s);
   }
   
   
   var $parent = self.parent.$;
   function clickMainDialog(){
   	//清空mask div
   	$parent('#mask').empty();
   	//清空主面板的样式为window的节点
   	$parent('.window').remove();
   	//清空主面板的样式为window-shadow的节点
   	$parent('.window-shadow').remove();
   	//清空主面板的样式为window-mask的节点
   	$parent('.window-mask').remove();
   	$parent('#mask').append("<div id='mainDialog'></div>");
   	$.parser.parse($parent('#mask'));
   };
   
   function openPage(title,url){
		clickMainDialog();
		$parent('#mainDialog').dialog({
		          modal:true,
		          href:url,
		          width:960,
		          height:520,
		          top:(screen.height-570)/3,
		          left:(screen.width-900)/2,
		          collapsible:false,
		          minimizable:false,
		          maximizable:false,
		          resizable:false,
		          title:title,
		          onClose:function(){
		        	  $('#baseGrid').datagrid('reload');
		          }
		});
	}
   function openDialog(title,url){
	   parent.$.modalDialog({
			title : title,
			width : 960,
			height : 520,
			href : url,
			closable : true
		}); 
		//定义模式化窗口的回调函数，用户在本页面设置相关业务值。
		parent.$.modalDialog.callBack = function (data){
			$('#baseGrid').datagrid('reload');
		}
		//2秒后关闭进度条
		setTimeout(function(){
			//关闭进度条
			parent.$.messager.progress('close');
		},4000);
	}
	
   //查看资质图片信息
   function openpic(path,imgpath,data){
		  var url=path+"/static/html/look_img.html?imgurl="+imgpath;
		  $.ajax({ 
			    type: "POST",      //http请求方式
				url:path+"/supervise/onlineinspect/addRecord.do",   //服务器段url地址
				data:data,     //发送给服务器段的数据 
				dataType: "json"
				});
		  window.open(url);
	}
   
   function openmodalDialogPicture(prepath,imgpath,data){
		//调用模式对话框，设置参数修改模式对话框的参数
		parent.$.modalDialog({
			title : '查看图片',
			width : 1000,
			height : 600,
			href : prepath+'/comm/choose/pictureView.do?picpath='+imgpath,
			closable : true
		}); 
		 $.ajax({ 
			    type: "POST",      //http请求方式
				url:prepath+"/supervise/onlineinspect/addRecord.do",   //服务器段url地址
				data:data,     //发送给服务器段的数据 
				dataType: "json"
				});
		//2秒后关闭进度条
		setTimeout(function(){
			//关闭进度条
			parent.$.messager.progress('close');
		},50);
	}
   
   
  //以静态模式 用iframe打开一个页面,不需要回调
   function openIframeLayer(title,url,width,height){
   	layer.open({
           type: 2,
           title: title,
           shadeClose: true,
           shade: 0.8,
           area: [width, height],
           content: url
       });
   }

   //以静态模式 用iframe打开一个页面,传递回调函数会，关闭页面会回调 父页面
   function openIframeLayerCallback(title,url,width,height,callback){
   	layer.open({
           type: 2,
           title: title,
           shadeClose: true,
           shade: 0.8,
           area: [width, height],
           content: url,
           cancel:callback//右上角关闭回调
       });
   }
   //弹出框提醒
   function layeralert(text){
		layer.alert(text,{
			  icon: 1,
			  skin: 'layer-ext-moon'
		 });
	}
   
//每个table页下加上一个记分项  一户一档
function scoreappend(pre,fsuserid,patrolnum,patroltype){
	var url = pre+"/comm/inspectscore/eachscore.do?id="+fsuserid+"&patrolnum="+patrolnum+"&patroltype="+patroltype+"&flag=1";
	$('#scoreappend').dialog({    
	    title: '违法记分',    
	    width: 600,    
	    height: 400,    
	    closed: false,    
	    cache: false,    
	    href: url,    
	    modal: true
	}); 
}
//网上巡查
function inspectappend(pre,fsuserid,patrolnum,patroltype){
	var url = pre+"/comm/inspectscore/eachscore.do?id="+fsuserid+"&patrolnum="+patrolnum+"&patroltype="+patroltype+"&flag=2";
	$('#scoreappend').dialog({    
	    title: '网上巡查',    
	    width: 600,    
	    height: 400,    
	    closed: false,    
	    cache: false,    
	    href: url,    
	    modal: true
	}); 
}


//锁定用户
function mandleuser(pre,userid,regno,entname,enttype,isvalid){
	var title;
	if(isvalid=='0'){
		title='锁定商户';
	}else if(isvalid=='1'){
		title='解锁商户';
	}
	var url = pre+"/fs/userlock/showReason.do?userid="+userid+"&regno="+regno+"&entname="+entname+"&enttype="+enttype+"&isvalid="+isvalid;
	$('#scoreappend').dialog({    
	    title: title,    
	    width: 600,    
	    height: 250,    
	    closed: false,    
	    cache: false,    
	    href: url,    
	    modal: true
	}); 
}

function modifystate(pre,userid,regno,entname,enttype,isvalid,remarks){
	$.ajax({
		  url: pre+"/fs/userlock/modifystate.do",
		  data: {
			     userid:  userid,
			     regno:  regno,
			     entname:  entname,
			     enttype: enttype,
			     isvalid: isvalid,
			     remarks: remarks
			    },
		  async: false,
		  type: "POST",      //http请求方式
          success: function(data){
        	if(data.msg=="ok") {
        		alert("该商户锁定成功！");
        	}else if(data.msg=="unok") {
        		alert("该商户解锁成功！");
        	}else if(data.msg=="same"){
        		alert("该商户已经被锁定,不能重复锁定！");
        	}else if(data.msg=="unsame"){
        		alert("该商户已经解锁,不能重复解锁！");
        	}else if(data.msg=="nouser"){
        		alert("该商户还未锁定,不能解锁！");
        	}
        }
    }); 	
}

//==========================多张图片===================================
function openmodalDialogPicture(prepath,type){
	//调用模式对话框，设置参数修改模式对话框的参数
	parent.$.modalDialog({
		title : '选择图片',
		width : 800,
		height : 300,
		href : prepath+'/comm/choose/picture.do?type='+type,
		closable : true
	}); 
	//定义模式化窗口的回调函数，用户在本页面设置相关业务值。
	parent.$.modalDialog.callBack = function (data){
		$("#lic_picpath").textbox("setValue",data);
		$('#btn').next().remove();
		$('#btn').after($('<a onclick="seepic(\''+ prepath + '\',\''+ data + '\')" class="btn-picview-style" target="_blank" style="margin-left: 13px;">查看</a>'));
	}
	//2秒后关闭进度条
	setTimeout(function(){
		//关闭进度条
		parent.$.messager.progress('close');
	},50);
}

function seepic(prepath,data){
    if(data!=null && data!=''){  	
    		parent.$.modalDialog({
    			title : '查看图片',
    			width : 800,
    			height : 300,
    			href : prepath+'/comm/choose/pictureView.do?picpath='+data,
    			closable : true
    		}); 
    		//2秒后关闭进度条
    		setTimeout(function(){
    			//关闭进度条
    			parent.$.messager.progress('close');
    		},50);
	}else{
		alert("没有图片，不能查看!");
	}
}