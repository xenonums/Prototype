/*
 * 扩展easyui重构的renderRow方法，自定义view，解决datagrid表单中属性包含子属性使用field.attr格式显示问题
 * */
var pb_extGridView = $.extend({}, $.fn.datagrid.defaults.view, {  
    renderRow: 
    	function(_721,_722,_723,_724,_725){
    	var opts=$.data(_721,"datagrid").options;
    	var cc=[];
    	if(_723&&opts.rownumbers){
    	var _726=_724+1;
    	if(opts.pagination){
    	_726+=(opts.pageNumber-1)*opts.pageSize;
    	}
    	cc.push("<td class=\"datagrid-td-rownumber\"><div class=\"datagrid-cell-rownumber\">"+_726+"</div></td>");
    	}
    	for(var i=0;i<_722.length;i++){
    	var _727=_722[i];
    	var col=$(_721).datagrid("getColumnOption",_727);
    	if(col){
    	var _728=_725[_727];
    	/*
    	 * 使datagrid的field支持属性的紫属性field.attr格式的显示
    	 * （优先采取原程序的方法如果在原程序方法获取不到的情况下使用新的方法来获取需要展示的值）
    	 * */
    	if(!Boolean(_728) && _727.indexOf('.')>0)  
    	{  
    		var names_1111=_727.split('.');
    		_728=_725[names_1111[0]];
    		for(var iii=1; iii<names_1111.length;iii++){
    			if(_728!=null){
    					_728=_728[names_1111[iii]];
    				}else{
    					break;
    				}
    		}
    	/*网上解决办法，但是当对象为空是出错*/
    	//_728=eval("_725['"+_727.replace(/\./g,"']['")+"']");
    	}
    	var css=col.styler?(col.styler(_728,_725,_724)||""):"";
    	var _729="";
    	var _72a="";
    	if(typeof css=="string"){
    	_72a=css;
    	}else{
    	if(css){
    	_729=css["class"]||"";
    	_72a=css["style"]||"";
    	}
    	}
    	var cls=_729?"class=\""+_729+"\"":"";
    	var _72b=col.hidden?"style=\"display:none;"+_72a+"\"":(_72a?"style=\""+_72a+"\"":"");
    	cc.push("<td field=\""+_727+"\" "+cls+" "+_72b+">");
    	var _72b="";
    	if(!col.checkbox){
    	if(col.align){
    	_72b+="text-align:"+col.align+";";
    	}
    	if(!opts.nowrap){
    	_72b+="white-space:normal;height:auto;";
    	}else{
    	if(opts.autoRowHeight){
    	_72b+="height:auto;";
    	}
    	}
    	}
    	cc.push("<div style=\""+_72b+"\" ");
    	cc.push(col.checkbox?"class=\"datagrid-cell-check\"":"class=\"datagrid-cell "+col.cellClass+"\"");
    	cc.push(">");
    	if(col.checkbox){
    	cc.push("<input type=\"checkbox\" "+(_725.checked?"checked=\"checked\"":""));
    	cc.push(" name=\""+_727+"\" value=\""+(_728!=undefined?_728:"")+"\">");
    	}else{
    	if(col.formatter){
    	cc.push(col.formatter(_728,_725,_724));
    	}else{
    	cc.push(_728);
    	}
    	}
    	cc.push("</div>");
    	cc.push("</td>");
    	}
    	}
    	return cc.join(""); 
    }  
}); 


/**  
 * 扩展两个方法  ,提示和关闭提示
 */  
$.extend($.fn.datagrid.methods, {   
    /** 
     * 开打提示功能  
     * @param {} jq  
     * @param {} params 提示消息框的样式  
     * @return {}  
      */  
     doCellTip : function(jq, params) {   
         function showTip(data, td, e) {   
             if ($(td).text() == "")   
                 return;   
             data.tooltip.text($(td).text()).css({   
                         top : (e.pageY + 10) + 'px',   
                         left : (e.pageX + 20) + 'px',   
                         'z-index' : $.fn.window.defaults.zIndex,   
                         display : 'block'   
                     });   
         };   
         return jq.each(function() {   
             var grid = $(this);   
             var options = $(this).data('datagrid');   
             if (!options.tooltip) {   
                 var panel = grid.datagrid('getPanel').panel('panel');   
                 var defaultCls = {   
                     'border' : '1px solid #333',   
                     'padding' : '1px',   
                     'color' : '#333',   
                     'background' : '#f7f5d1',   
                     'position' : 'absolute',   
                     'max-width' : '200px',   
                     'border-radius' : '4px',   
                     '-moz-border-radius' : '4px',   
                     '-webkit-border-radius' : '4px',   
                     'display' : 'none'   
                 }   
                 var tooltip = $("<div id='celltip'></div>").appendTo('body');   
                 tooltip.css($.extend({}, defaultCls, params.cls));   
                 options.tooltip = tooltip;   
                 panel.find('.datagrid-body').each(function() {   
                     var delegateEle = $(this).find('> div.datagrid-body-inner').length   
                             ? $(this).find('> div.datagrid-body-inner')[0]   
                             : this;   
                     $(delegateEle).undelegate('td', 'mouseover').undelegate(   
                             'td', 'mouseout').undelegate('td', 'mousemove')   
                             .delegate('td', {   
                                 'mouseover' : function(e) {   
                                     if (params.delay) {   
                                         if (options.tipDelayTime)   
                                             clearTimeout(options.tipDelayTime);   
                                         var that = this;   
                                         options.tipDelayTime = setTimeout(   
                                                 function() {   
                                                     showTip(options, that, e);   
                                                 }, params.delay);   
                                     } else {   
                                         showTip(options, this, e);   
                                     }   
   
                                 },   
                                 'mouseout' : function(e) {   
                                     if (options.tipDelayTime)   
                                         clearTimeout(options.tipDelayTime);   
                                     options.tooltip.css({   
                                                 'display' : 'none'   
                                             });   
                                 },   
                                 'mousemove' : function(e) {   
                                     var that = this;   
                                     if (options.tipDelayTime) {   
                                         clearTimeout(options.tipDelayTime);   
                                         options.tipDelayTime = setTimeout(   
                                                 function() {   
                                                     showTip(options, that, e);   
                                                 }, params.delay);   
                                     } else {   
                                         showTip(options, that, e);   
                                     }   
                                 }   
                             });   
                 });   
   
             }   
   
         });   
     },   
     /** 
      * 关闭消息提示功能  
      * @param {} jq  
      * @return {}  
      */  
     cancelCellTip : function(jq) {   
         return jq.each(function() {   
                     var data = $(this).data('datagrid');   
                     if (data.tooltip) {   
                         data.tooltip.remove();   
                         data.tooltip = null;   
                          var panel = $(this).datagrid('getPanel').panel('panel');   
                          panel.find('.datagrid-body').undelegate('td',   
                                  'mouseover').undelegate('td', 'mouseout')   
                                  .undelegate('td', 'mousemove')   
                      }   
                      if (data.tipDelayTime) {   
                          clearTimeout(data.tipDelayTime);   
                          data.tipDelayTime = null;   
                      }   
                  });   
      }   
  }); 

/*
 * 扩展easyui重构的renderRow方法，自定义view，解决treegrid表单中属性包含子属性使用field.attr格式显示问题
 * */
var pb_extTreeGridView = $.extend({}, $.fn.treegrid.defaults.view, {  
    renderRow: 
    	function(_860,_861,_862,_863,row){
    	var opts=$.data(_860,"treegrid").options;
    	var cc=[];
    	if(_862&&opts.rownumbers){
    	cc.push("<td class=\"datagrid-td-rownumber\"><div class=\"datagrid-cell-rownumber\">0</div></td>");
    	}
    	for(var i=0;i<_861.length;i++){
    	var _864=_861[i];
    	var col=$(_860).datagrid("getColumnOption",_864);
    	if(col){
    		//var _728=_725[_727];
    		var _999=row[_864];
        	/*
        	 * 使datagrid的field支持属性的紫属性field.attr格式的显示
        	 * （优先采取原程序的方法如果在原程序方法获取不到的情况下使用新的方法来获取需要展示的值）
        	 * */
        	if(!Boolean(_999) && _864.indexOf('.')>0)  
        	{  
        		var names_1111=_864.split('.');
        		_999=row[names_1111[0]];
        		for(var iii=1; iii<names_1111.length;iii++){
        			if(_999!=null){
        				_999=_999[names_1111[iii]];
        			}else{
        				break;
        			}
        		}
        	/*网上解决办法，但是当对象为空是出错*/
        	//_728=eval("_725['"+_727.replace(/\./g,"']['")+"']");
        	}
    	var css=col.styler?(col.styler(_999,row)||""):"";
    	var _865="";
    	var _866="";
    	if(typeof css=="string"){
    	_866=css;
    	}else{
    	if(cc){
    	_865=css["class"]||"";
    	_866=css["style"]||"";
    	}
    	}
    	var cls=_865?"class=\""+_865+"\"":"";
    	var _867=col.hidden?"style=\"display:none;"+_866+"\"":(_866?"style=\""+_866+"\"":"");
    	cc.push("<td field=\""+_864+"\" "+cls+" "+_867+">");
    	var _867="";
    	if(!col.checkbox){
    	if(col.align){
    	_867+="text-align:"+col.align+";";
    	}
    	if(!opts.nowrap){
    	_867+="white-space:normal;height:auto;";
    	}else{
    	if(opts.autoRowHeight){
    	_867+="height:auto;";
    	}
    	}
    	}
    	cc.push("<div style=\""+_867+"\" ");
    	if(col.checkbox){
    	cc.push("class=\"datagrid-cell-check ");
    	}else{
    	cc.push("class=\"datagrid-cell "+col.cellClass);
    	}
    	cc.push("\">");
    	if(col.checkbox){
    	if(row.checked){
    	cc.push("<input type=\"checkbox\" checked=\"checked\"");
    	}else{
    	cc.push("<input type=\"checkbox\"");
    	}
    	cc.push(" name=\""+_864+"\" value=\""+(_999!=undefined?_999:"")+"\">");
    	}else{
    	var val=null;
    	if(col.formatter){
    	val=col.formatter(_999,row);
    	}else{
    	val=_999;
    	}
    	if(_864==opts.treeField){
    	for(var j=0;j<_863;j++){
    	cc.push("<span class=\"tree-indent\"></span>");
    	}
    	if(row.state=="closed"){
    	cc.push("<span class=\"tree-hit tree-collapsed\"></span>");
    	cc.push("<span class=\"tree-icon tree-folder "+(row.iconCls?row.iconCls:"")+"\"></span>");
    	}else{
    	if(row.children&&row.children.length){
    	cc.push("<span class=\"tree-hit tree-expanded\"></span>");
    	cc.push("<span class=\"tree-icon tree-folder tree-folder-open "+(row.iconCls?row.iconCls:"")+"\"></span>");
    	}else{
    	cc.push("<span class=\"tree-indent\"></span>");
    	cc.push("<span class=\"tree-icon tree-file "+(row.iconCls?row.iconCls:"")+"\"></span>");
    	}
    	}
    	cc.push("<span class=\"tree-title\">"+val+"</span>");
    	}else{
    	cc.push(val);
    	}
    	}
    	cc.push("</div>");
    	cc.push("</td>");
    	}
    	}
    	return cc.join("");
    }  
});

/*
 * 扩展easyUI中form方法中“load”方法，解决级联对象赋值问题（如：parent.name）
 * 该方法需要在easyUI、和jquery之后引入
 * */
//新实现，解决了combogrid的加载的问题
$.extend($.fn.form.methods, {
extLoad : function (jq, param) {
	return jq.each(function () {
		load(this, param);
	});
function load(target, data) {
var opts = $.data(target, "form").options;
if (typeof data == "string") {
	var params = {};
	if (opts.onBeforeLoad.call(target, params) == false) {
		return;
	}
	$.ajax({
		url : data,
		data : params,
		dataType : "json",
		success : function(data) {
			loadData(data);
		},
		error : function() {
			opts.onLoadError.apply(target, arguments);
		}
	});
} else {
	loadData(data);
}
function loadData(data) {
	var form = $(target); 
	var formFields = form.find("input[name],select[name],textarea[name]"); 
	formFields.each(function(){  
	         var name = this.name;  
             var val = jQuery.proxy(function(){try{return eval('this.'+name);}catch(e){return "";}},data)();
             var rr = setNormalVal(name, val);
             if (!rr.length) {
     			var _4bb = setPlugsVal(name, val);
     			if (!_4bb) {
     				$("input[name=\"" + name + "\"]", form).val(val);
     				$("textarea[name=\"" + name + "\"]", form).val(val);
     				$("select[name=\"" + name + "\"]", form).val(val);
     			}
     		}
     		_4bd(name, val);

	}); 
	
	for ( var name1 in data) {
		var val1 = data[name1];
		var rr1 = setNormalVal(name1, val1);
		if (!rr1.length) {
			var _4bb1 = setPlugsVal(name1, val1);
			if (!_4bb1) {
				$("input[name=\"" + name1 + "\"]", form).val(val1);
				$("textarea[name=\"" + name1 + "\"]", form).val(val1);
				$("select[name=\"" + name1 + "\"]", form).val(val1);
			}
		}
		_4bd(name1, val1);
	}
	opts.onLoadSuccess.call(target, data);
	_4c4(target);
}
;

function _4c4(_4d1) {
	if ($.fn.validatebox) {
		var t = $(_4d1);
		t.find(".validatebox-text:not(:disabled)").validatebox("validate");
		var _4d2 = t.find(".validatebox-invalid");
		_4d2.filter(":not(:disabled):first").focus();
		return _4d2.length == 0;
	}
	return true;
}
;

function setNormalVal(name, val) {
	var rr = $(target).find(
			"input[name=\"" + name + "\"][type=radio], input[name=\""
					+ name + "\"][type=checkbox]");
	rr._propAttr("checked", false);
	rr
			.each(function() {
				var f = $(this);
				if (f.val() == String(val)
						|| $.inArray(f.val(), $.isArray(val) ? val
								: [ val ]) >= 0) {
					f._propAttr("checked", true);
				}
			});
	return rr;
}
;
function setPlugsVal(name, val) {
	var _4be = 0;
	var pp = [ "textbox", "numberbox", "slider" ];
	for (var i = 0; i < pp.length; i++) {
		var p = pp[i];
		var f = $(target).find("input[" + p + "Name=\"" + name + "\"]");
		if (f.length) {
			f[p]("setValue", val);
			_4be += f.length;
		}
	}
	return _4be;
}
;
function _4bd(name, val) {
	var form = $(target);
	var cc = [ "combobox", "combotree", "combogrid", "datetimebox",
			"datebox", "combo" ];
	var c = form.find("[comboName=\"" + name + "\"]");
	if (c.length) {
		for (var i = 0; i < cc.length; i++) {
			var type = cc[i];
			if (c.hasClass(type + "-f")) {
				if (c[type]("options").multiple) {
					c[type]("setValues", val);
				} else {
					c[type]("setValue", val);
				}
				return;
			}
		}
	}
}
;
};

}
}); 


/**
 * @requires jQuery,EasyUI
 * @author zenghb
 * 扩展EasyUI的tree树形表格,增加parentField属性
 */
$.fn.tree.defaults.loadFilter = function(data, parent) {
	var opt = $(this).data().tree.options;
	var idField, textField, parentField;
	if (opt.parentField) {
		idField = opt.idField || 'id';
		textField = opt.textField || 'text';
		parentField = opt.parentField;
		var i, l, treeData = [], tmpMap = [];
		for (i = 0, l = data.length; i < l; i++) {
			tmpMap[data[i][idField]] = data[i];
		}
		for (i = 0, l = data.length; i < l; i++) {
			if (getJsonObjValue(tmpMap[data[i][idField]],parentField) != null && "undefined" != typeof tmpMap[getJsonObjValue(data[i],parentField)] && data[i][idField] != getJsonObjValue(data[i],parentField)) {
				if (!tmpMap[getJsonObjValue(data[i],parentField)]['children'])
					tmpMap[getJsonObjValue(data[i],parentField)]['children'] = [];
				data[i]['text'] = data[i][textField];
				tmpMap[getJsonObjValue(data[i],parentField)]['children'].push(data[i]);
			} else {
				data[i]['text'] = data[i][textField];
				treeData.push(data[i]);
			}
		}
		return treeData;
	}
	return data;
};

/**
 * @requires jQuery,EasyUI
 * @author zenghb
 * 扩展treegrid,增加parentField属性
 */
$.fn.treegrid.defaults.loadFilter = function(data, parentId) {
	var opt = $(this).data().treegrid.options;
	var idField, treeField, parentField;
	if (opt.parentField) {
		
		//隐含通知total值
		if(data.total){
			if( typeof __setGridTmpTotal === 'function' ){
				__setGridTmpTotal(data.total);
			}
		}
		
		idField = opt.idField || 'id';
		treeField = opt.treeField || 'text';
		parentField = opt.parentField;
		var i, l, treeData = [], tmpMap = [];
		
		if(data.total == 0){
			return treeData;
		}
		
		for (i = 0, l = data.rows.length; i < l; i++) {
			tmpMap[data.rows[i][idField]] = data.rows[i];
		}
		
		for (i = 0, l = data.rows.length; i < l; i++) {
			if (getJsonObjValue(tmpMap[data.rows[i][idField]],parentField) != null && "undefined" != typeof tmpMap[getJsonObjValue(data.rows[i],parentField)] && data.rows[i][idField] != getJsonObjValue(data.rows[i],parentField)) {
				if (!tmpMap[getJsonObjValue(data.rows[i],parentField)]['children'])
					tmpMap[getJsonObjValue(data.rows[i],parentField)]['children'] = [];
				data.rows[i][treeField] = data.rows[i][treeField];
				tmpMap[getJsonObjValue(data.rows[i],parentField)]['children'].push(data.rows[i]);
			} else {
				data.rows[i][treeField] = data.rows[i][treeField];
				treeData.push(data.rows[i]);
			}
		}
		return treeData;
	}
	return data.rows;
};

/**
 * @requires jQuery,EasyUI
 * @author zenghb
 * 扩展combotree
 */
$.fn.combotree.defaults.loadFilter = $.fn.tree.defaults.loadFilter;

/**
 * @requires jQuery,EasyUI
 * @author zenghb
 * 扩展jquery的rasize方法 
 */
(function($, pb_h, pb_c) {
	var pb_a = $([]), pb_e = $.resize = $.extend($.resize, {}), i, k = "setTimeout", j = "resize", d = j
			+ "-special-event", b = "delay", f = "throttleWindow";
	pb_e[b] = 250;
	pb_e[f] = true;
	$.event.special[j] = {
		setup : function() {
			if (!pb_e[f] && this[k]) {
				return false
			}
			var l = $(this);
			pb_a = pb_a.add(l);
			$.data(this, d, {
				w : l.width(),
				pb_h : l.height()
			});
			if (pb_a.length === 1) {
				g()
			}
		},
		teardown : function() {
			if (!pb_e[f] && this[k]) {
				return false
			}
			var l = $(this);
			pb_a = pb_a.not(l);
			l.removeData(d);
			if (!pb_a.length) {
				clearTimeout(i)
			}
		},
		add : function(l) {
			if (!pb_e[f] && this[k]) {
				return false
			}
			var n;
			function m(s, o, p) {
				var q = $(this), r = $.data(this, d);
				r.w = o !== pb_c ? o : q.width();
				r.pb_h = p !== pb_c ? p : q.height();
				n.apply(this, arguments);
				return false;
			}
			if ($.isFunction(l)) {
				n = l;
				return m
			} else {
				n = l.handler;
				l.handler = m
			}
		}
	};
	function g() {
		i = pb_h[k](function() {
			pb_a.each(function() {
				var n = $(this), m = n.width(), l = n.height(), o = $.data(
						this, d);
				if (m !== o.w || l !== o.pb_h) {
					n.trigger(j, [ o.w = m, o.pb_h = l ])
				}
			});
			g()
		}, pb_e[b])
	}
})(jQuery, this);



//扩展combotree可编辑过滤选项
(function(){    
	$.fn.combotree.defaults.editable = true;     
	$.extend($.fn.combotree.defaults.keyHandler,{         
		up:function(){             
			console.log('up');         },         
	    down:function(){             
	    	console.log('down');         },         
	    enter:function(){             
	    	console.log('enter');         },        
	    query:function(q){
	    	var t = $(this).combotree('tree');             
	    	var nodes = t.tree('getChildren');            
	    	for(var i=0; i<nodes.length; i++){                
	    		var node = nodes[i];                 
	    		if (node.text.indexOf(q) >= 0){                    
	    			$(node.target).show();                 
	    			} else {                     
	    				$(node.target).hide();                 
	    				}             
	    		}             
	    	var opts = $(this).combotree('options');             
	    	if (!opts.hasSetEvents){                 
	    		opts.hasSetEvents = true;                 
	    		var onShowPanel = opts.onShowPanel;                 
	    		opts.onShowPanel = function(){                     
	    			var nodes = t.tree('getChildren');                     
	    			for(var i=0; i<nodes.length; i++){                         
	    				$(nodes[i].target).show();                     
	    				}                     
	    			onShowPanel.call(this);                 
	    			};                 
	    			$(this).combo('options').onShowPanel = opts.onShowPanel;             
	    			}         
	    	}     
	    	}); 
	})(jQuery);

/**
 * @author tanw
 * 
 * @requires jQuery,EasyUI
 * 
 * 扩展tree，使其可以获取实心节点,设置实心节点
 */
$.extend($.fn.tree.methods, {
	getCheckedExt : function(jq) {// 获取checked节点(包括实心)
		var checked = $(jq).tree("getChecked");
		var checkbox2 = $(jq).find("span.tree-checkbox2").parent();
		$.each(checkbox2, function() {
			var node = $.extend({}, $.data(this, "tree-node"), {
				target : this
			});
			checked.push(node);
		});
		return checked;
	},
	getSolidExt : function(jq) {// 获取实心节点
		var checked = [];
		var checkbox2 = $(jq).find("span.tree-checkbox2").parent();
		$.each(checkbox2, function() {
			var node = $.extend({}, $.data(this, "tree-node"), {
				target : this
			});
			checked.push(node);
		});
		return checked;
	},
	setSolidExt : function(jq,target) {// 设置实心节点
		//console.info("===========================");
		//console.info($(target));
		var ck = $(target).find(".tree-checkbox");
        //console.info(ck);
        if(ck){
        	ck.removeClass("tree-checkbox0 tree-checkbox1 tree-checkbox2");
            ck.addClass("tree-checkbox2");
        }
        //console.info("===========================");
	}
});




/**
 * @author 孙宇
 * 
 * @requires jQuery,EasyUI
 * 
 * 通用错误提示
 * 
 * 用于datagrid/treegrid/tree/combogrid/combobox/form加载数据出错时的操作
 */
var easyuiErrorFunction = function(XMLHttpRequest) {
	$.messager.progress('close');
	//$.messager.alert('错误', XMLHttpRequest.responseText);
};
$.fn.datagrid.defaults.onLoadError = easyuiErrorFunction;
$.fn.treegrid.defaults.onLoadError = easyuiErrorFunction;
$.fn.tree.defaults.onLoadError = easyuiErrorFunction;
$.fn.combogrid.defaults.onLoadError = easyuiErrorFunction;
$.fn.combobox.defaults.onLoadError = easyuiErrorFunction;
$.fn.form.defaults.onLoadError = easyuiErrorFunction; 


/**
 * @author tanw
 * 
 * @requires jQuery,EasyUI
 * 
 * 创建一个模式化的dialog
 * 
 * @returns $.modalDialog.handler 这个handler代表弹出的dialog句柄
 * 
 * @returns $.modalDialog.xxx 这个xxx是可以自己定义名称，主要用在弹窗关闭时，刷新某些对象的操作，可以将xxx这个对象预定义好
 */
$.modalDialog = function(options) {
	if ($.modalDialog.handler == undefined) {// 避免重复弹出
		var opts = $.extend({
			title : '',
			width : 840,
			height : 680,
			modal : true,
			onClose : function() {
				$.modalDialog.handler = undefined;
				$(this).dialog('destroy');
			},
			onOpen : function() {
				parent.$.messager.progress({
					title : '提示',
					text : '数据处理中，请稍后....'
				});
			}
		}, options);
		opts.modal = true;// 强制此dialog为模式化，无视传递过来的modal参数
		return $.modalDialog.handler = $('<div/>').dialog(opts);
	}
};

/**
 * @author tanw
 * 
 * @requires jQuery,EasyUI
 * 
 * 创建一个模式化的window
 * 
 * @returns $.modalWindow.handler 这个handler代表弹出的window句柄
 * 
 * @returns $.modalWindow.xxx 这个xxx是可以自己定义名称，主要用在弹窗关闭时，刷新某些对象的操作，可以将xxx这个对象预定义好
 */
$.modalWindow = function(options) {
	if ($.modalWindow.handler == undefined) {// 避免重复弹出
		var opts = $.extend({
			title : '',
			width : 840,
			height : 680,
			fit : false,
			collapsible : false,
			minimizable : false,
			resizable : false,
			draggable : false,
			modal : true,
			onClose : function() {
				$.modalWindow.handler = undefined;
				$(this).window('destroy');
			}
		}, options);
		opts.modal = true;// 强制此dialog为模式化，无视传递过来的modal参数
		return $.modalWindow.handler = $('<div/>').window(opts);
	}
};

/**
 * @author tanw
 * 
 * @requires jQuery
 * 
 * 改变jQuery的AJAX默认属性和方法
 */
$.ajaxSetup({
	type : 'POST',
	timeout : 30000//超时设置为8s
});

/**
 * @author tanw
 * 
 * 增加formatString功能
 * 
 * 使用方法：$.formatString('字符串{0}字符串{1}字符串','第一个变量','第二个变量');
 * 
 * @returns 格式化后的字符串
 */
$.formatString = function(str) {
	for ( var i = 0; i < arguments.length - 1; i++) {
		str = str.replace("{" + i + "}", arguments[i + 1]);
	}
	return str;
};

//扩展JavaScript String
String.prototype.startWith=function(str){ 
	var reg=new RegExp("^"+str); 
	return reg.test(this); 
}
String.prototype.endWith=function(str){ 
	var reg=new RegExp(str+"$"); 
	return reg.test(this); 
}
String.prototype.trim=function(){
    return this.replace(/(^\s*)|(\s*$)/g, "");
}
String.prototype.ltrim=function(){
    return this.replace(/(^\s*)/g,"");
}
String.prototype.rtrim=function(){
    return this.replace(/(\s*$)/g,"");
}

/** 
* 判断是否null 
*/
function isNull(data){ 
	return (data == "" || data == undefined || data == null) ? true : false; 
}
 
/**
 * 图片转换
 * @param picpath
 * @returns 转换后的图片地址
 */
function transPicpath(picpath){
	if(picpath == null || picpath.length < 9){
		return "";
	}else{
		if("_" == picpath.substring(8,9)){
			return "/upload/licpic/"+picpath.substring(0,6)+"/"+picpath.substring(6,8)+"/"+picpath;
		}
	}
	
	return "/upload/licpic/noPic.jpg";
}