// JavaScript Document
// 本地服务端口为9500
// 云端服务端口为9998
//负责本地数据图片上传到云端代码

var net = require('net');
var fs = require('fs');
// var client = new net.Socket();
var information = new net.Socket();
// var fileName;
// var rs;
// host = "192.168.43.197"
// localhost
information.connect('9998', '192.168.43.197', function () {
	console.log('建立本地数据转发服务端口·9998,本地端口9500');
});

var i = 1;
var rs = fs.createReadStream();
var client = new net.Socket();

var informationConn = net.createServer(function(inforConn){
	
	inforConn.on('data', function(data){
		try {
			var ojb = JSON.parse(data);
			console.log('uploadingName:' + ojb.uploadingName);
			var uploadingName = ojb.uploadingName;
			client.connect('9998', '192.168.43.197', function () {
				console.log('net connect');
				client.write(data);
			});

			client.on('data', function(data){
				try {
					var ojb = JSON.parse(data);
					console.log('upFlag:' + ojb.upFlag);
				 	rs = fs.createReadStream(uploadingName);
					
					//使用异步方式读取文件数据
					rs.on('data', function (data) {
						client.write(data);
						console.log('data read:' + i);
						i = i + 1;
					});

					//文件读取完毕
					rs.on('end', function () {
						//断开云端链接
						// 始终关闭文件描述符！
						// rs.end();
						// rs.end();
						rs.close(null, (err) => {
							if (err) throw err;
						});
						client.end();
						client.close();
						inforConn.end();
						inforConn.close();
						console.log('data end');
						i = 1;
					});
				} catch (e) {
					console.log(e);
				}
			});
		} catch (e) {
			console.log(e);
		}

		client.on('end', function(data){
			
		});
	});
}).listen(9500);
