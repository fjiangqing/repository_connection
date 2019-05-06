// JavaScript Document
// 本地服务端口为9999
// 云端服务端口为9998
// 云端下载服务端口为9996

var net = require('net');
var fs = require('fs');
var client = new net.Socket();
var information = new net.Socket();
var downloadName = 'copy-get-123.png';

// var dataName['downloadName'] = downloadName;
var dataName = '{"downloadName":"get-123.png" }';

client.connect('9993', 'localhost', function () {
    var i = 0;
    client.write(dataName);
    var ws = fs.createWriteStream('copy+' + downloadName);
    client.on('data',function(data){
        ws.write(data);
        console.log('doanload data:' + i);
        ++i;
    });
    client.on('close',function(){
        ws.end();
        console.log('finish download');
        i = 0;
    });
});
