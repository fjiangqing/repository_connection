// JavaScript Document
var net = require('net');
var fs = require('fs');

var uploadingName = 'undefine';


console.log('run server');
//建立云端TCP服务，负责接收上传文件保存 名称为fileServer
console.log('wait new uploading connection!');
var fileServer = net.createServer(function(uploadingConn){

	console.log('new uploading connection');
	//建立写入文件流
	// var ws = fs.createWriteStream(uploadingName);
	var ws;
	console.log('fs.createWriteStream(uploadingName)');
	var i = 1;

	var nameFlag = 0;
	//从网络链接接受数据
	uploadingConn.on('data', function(data){
		if(nameFlag == 0){
			try {
				var ojb = JSON.parse(data);
				console.log('uploading name:' + ojb.uploadingName);
				uploadingName = 'copy-' + ojb.uploadingName;
				nameFlag = 1;
				ws = fs.createWriteStream(uploadingName);
				uploadingConn.write('{"upFlag":1}');
			} catch (e) {
				console.log(e);
			}
		}else{
			//数据写入文件
			ws.write(data);
			console.log('uploadingRead:' + i);
			i = i + 1;
		}
	});

	//链接断开时监控
	uploadingConn.on('close', function(){
		//关闭文件
		ws.end();
		nameFlag = 0;
		console.log('close uploading!');
		console.log('wait new uploading connection!');
	})
}).listen(9998);

//建立云端TCP服务，负责分发交互数据名称为Server

//在线数计数
var UCount = 0;
//用户组 指向connetion
var users = [];

console.log('wait new data connection!');
var dataServer = net.createServer(function(dataConn){

	//设定编码
	dataConn.setEncoding('utf8');
	console.log('new data connection!');
	//定义当前链接用户
	var isUser = UCount;
	users[UCount] = dataConn;
	++UCount;
	console.log('data online:',UCount);

	dataConn.on('data', function(data){
		try {
			var ojb = JSON.parse(data);
			console.log('uploading name:' + ojb.uploadingName);
			uploadingName = 'copy-' + ojb.uploadingName;
		} catch (e) {
			console.log(e);
		}
		for (var i in users) {
			if (i != isUser) {
				//去除空消息
				if ( data != ''){
					users[i].write(data);
				}
			}
		}
	});

}).listen(9999);
