/**
 * @author lvxy
 * validatebox扩展验证
 * 
 * 注意：自定义验证名称不支持数字
 */

$.extend(
		$.fn.validatebox.defaults.rules,{
		idcard : {// 验证身份证
			validator : function(value) {
				return /^\d{15}(\d{2}[A-Za-z0-9])?$/i.test(value);
			},
			message : '身份证号码格式不正确'
		},
		minLength : {
			validator : function(value, param) {
				return value.length >= param[0];
			},
			message : '请输入至少（2）个字符.'
		},
		length : {
			validator : function(value, param) {
				var len = $.trim(value).length;
				return len >= param[0] && len <= param[1];
			},
			message : "输入内容长度必须介于{0}和{1}之间."
		},
		phone : {// 验证电话号码
			validator : function(value) {
				//return /^((\(\d{2,3}\))|(\d{4}\-))?(\(0\d{2,3}\)|0\d{2,3}-)?[1-9]\d{6,7}(\-\d{1,4})?$/i.test(value);
				return /^(0[0-9]{2,3}\-)?([2-9][0-9]{6,7})+(\-[0-9]{1,4})?$/i.test(value);
			},
			message : '格式不正确,请使用下面格式:12345678901、1234-12345678-1234'
		},
		mobile : {// 验证手机号码移动、联通、电信、虚拟运行商170
			validator : function(value) {
				return /^(13|14|15|17|18|19|16)\d{9}$/i.test(value);
			},
			message : '手机号码格式不正确'
		},
		intOrFloat : {// 验证整数或小数
			validator : function(value) {
				return /^\d+(\.\d+)?$/i.test(value);
			},
			message : '请输入数字，并确保格式正确'
		},
		currency : {// 验证货币
			validator : function(value) {
				return /^\d+(\.\d+)?$/i.test(value);
			},
			message : '货币格式不正确'
		},
		qq : {// 验证QQ,从10000开始
			validator : function(value) {
				return /^[1-9]\d{4,9}$/i.test(value);
			},
			message : 'QQ号码格式不正确'
		},
		integer : {// 验证整数
			validator : function(value) {
				return /^[+]?[1-9]+\d*$/i.test(value);
			},
			message : '请输入整数'
		},
		age : {// 验证年龄
			validator : function(value) {
				return /^(?:[1-9][0-9]?|1[01][0-9]|120)$/i
						.test(value);
			},
			message : '年龄必须是0到120之间的整数'
		},

		chinese : {// 验证中文
			validator : function(value) {
				return /^[\Α-\￥]+$/i.test(value);
			},
			message : '请输入中文'
		},
		english : {// 验证英语
			validator : function(value) {
				return /^[A-Za-z]+$/i.test(value);
			},
			message : '请输入英文'
		},
		unnormal : {// 验证是否包含空格和非法字符
			validator : function(value) {
				return /.+/i.test(value);
			},
			message : '输入值不能为空和包含其他非法字符'
		},
		loginname : {// 验证用户名
			validator : function(value) {
				return /^[a-zA-Z][a-zA-Z0-9_]{5,15}$/i.test(value);
			},
			message : '帐号不合法（字母开头，允许6-16字节，允许字母数字下划线）'
		},
		mycode : {// 验证自编码，字母,数字或下划线
			validator : function(value) {
				return /^[a-zA-Z0-9][a-zA-Z0-9_]{2,13}$/i.test(value);
			},
			message : '编码不合法（允许3-13字符，允许字母数字下划线）'
		},
		faxno : {// 验证传真
			validator : function(value) {
				// return /^[+]{0,1}(\d){1,3}[ ]?([-]?((\d)|[
				// ]){1,12})+$/i.test(value);
				return /^((\(\d{2,3}\))|(\d{3}\-))?(\(0\d{2,3}\)|0\d{2,3}-)?[1-9]\d{6,7}(\-\d{1,4})?$/i.test(value);
			},
			message : '传真号码不正确'
		},
		zip : {// 验证邮政编码
			validator : function(value) {
				return /^[1-9]\d{5}$/i.test(value);
			},
			message : '邮政编码格式不正确'
		},
		ip : {// 验证IPV4地址
			validator : function(value) {
				return /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/i.test(value);
			},
			message : 'IPV4地址格式不正确'
		},
		name : {// 验证姓名，可以是中文或英文
			validator : function(value) {
//				return /^[\Α-\￥]+$/i.test(value)
//						| /^\w+[\w\s]+\w+$/i.test(value);
				return true;
			},
			message : '请输入中文或英文名字'
		},
		date : {// 验证日期
			validator : function(value) {
				// 格式yyyy-MM-dd或yyyy-M-d
				return /^(?:(?!0000)[0-9]{4}([-]?)(?:(?:0?[1-9]|1[0-2])\1(?:0?[1-9]|1[0-9]|2[0-8])|(?:0?[13-9]|1[0-2])\1(?:29|30)|(?:0?[13578]|1[02])\1(?:31))|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)([-]?)0?2\2(?:29))$/i.test(value);
			},
			message : '请输入合适的日期格式'
		},
		msn : {
			validator : function(value) {
				return /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
						.test(value);
			},
			message : '请输入有效的msn账号(例：abc@hotnail(msn/live).com)'
		},
		same : {
			validator : function(value, param) {
				if ($("#" + param[0]).val() != "" && value != "") {
					return $("#" + param[0]).val() == value;
				} else {
					return true;
				}
			},
			message : '两次输入的密码不一致！'
		},
		ipSex : {// ipv6 格式验证
			validator : function(value) {
				return /^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/i.test(value);			
			},
			message : '请输入正确的ipv6地址'
		},
		compareDate : {// 日期、时间验证大小，结束日期应该大于开始日期
			validator: function(value, param){
				var date = $("input[name="+param[0]+"]").val();
				var start = $.fn.datebox.defaults.parser(date);
		        var end = $.fn.datebox.defaults.parser(value);
		        if(date == null || date=="" || date==''){
		        	//$.fn.validatebox.defaults.rules.compareDate.message = '起始日期为空';
		        	return true;
		        }else if(end < start){
		        	$.fn.validatebox.defaults.rules.compareDate.message = '结束日期应该大于等于开始日期';
		        	return false;     
		        }else{
		        	return true;
		        }                  
			},
			message : ''
		},
		menuUrl : {// menu Url 格式验证
			validator : function(value) {
				return /^[A-Za-z0-9_/.]*$/i.test(value);			
			},
			message : '请输入正确url地址'
		},
		equalTo:{
			/**
			 * 校验是否和某个字段相同，用于密码及确认密码校验
			 * @author:ZengHB
			 * 2015年3月2日
			 * @param param:目标元素 
			 * @param value:待比对的元素 
			 */
			validator:function(value,param){
				return param[0] == value;
			},
			message:'字段不匹配'
		},
		checkPassword:{
			/**
			 * 在修改密码是，校验输入的当前密码是否正确
			 * @author:ZengHB
			 * 2015年3月2日
			 * @param param:待校验数据的id 
			 * @param value:输入待校验的密码 
			 */
			validator:function(value,param){
				var postdata = {};
	            postdata['id'] = param[2];
	            postdata['password'] = value;
	            var tag = false;
				$.ajax({ 
	            	type: "POST",      //http请求方式
	                url: param[0],     //服务器段url地址
	                data:postdata,     //发送给服务器段的数据 
	                dataType: 'json',   
	                async: false,  
	                cache: false,
	                success: function(data){
	                	if(data.success == "1"){
	                		tag = true;
	                	}
	                }
	            })
	            $.fn.validatebox.defaults.rules.checkPassword.message = param[1];
	            return tag;
			},
			message:''
		},
		isParentNodeValidity:{
			/**
			 * 在修改树形节点时，判断父节点的合法性，若选择的父节点与当前节点相同或为当前节点的子孙节点，则视为不合法
			 * @author:ZengHB
			 * 2015年3月16日
			 * @param param:数组参数 
			 * @param value:所选择的父节点 
			 */
			validator:function(value,param){
				var postdata = {};
	            postdata['id'] = param[1];
	            postdata['pid'] = param[2];
	            var tag = false;
				$.ajax({ 
	            	type: "POST",      //http请求方式
	                url: param[0],     //服务器段url地址
	                data:postdata,     //发送给服务器段的数据 
	                dataType: 'json',   
	                async: false,  
	                cache: false,
	                success: function(data){
	                	if(data.flag == "true"){
	                		tag = true;
	                	}
	                }
	            })
	            $.fn.validatebox.defaults.rules.isParentNodeValidity.message = param[3];
	            return tag;
			},
			message:''
		}
	});

/*
 *扩展了远程重复属性值的验证
 *参数：  远程url	  提交参数字段     验证失败提示    更新时排除本条记录ID
 */
$.extend($.fn.validatebox.defaults.rules, {
   checkRepeat: {
        validator: function(value, param) {
            var postdata = {};
            postdata[param[1]] = value;
            if(param[3] && param[3] != 0 ){
            	postdata['id'] = param[3];
            }
            var m_result =$.ajax({ 
            	type: "GET",      //http请求方式
                url: param[0],     //服务器段url地址
                data:postdata,     //发送给服务器段的数据  
                dataType: 'json',   
                async: false,  
                cache: false  
            }).responseText;
            
            if(m_result == "false"){
        		return true;
        	}else{
        		$.fn.validatebox.defaults.rules.checkRepeat.message = param[2];
                return false;
        	}
        },
        message: ''
    }
});