const express = require("express")
const http = require('http');
const https = require('http');

var external_server = express();
var internal_server = express();

external_server.use(express.json());
external_server.use(express.urlencoded({extended: true}));

external_server.set('view engine', 'ejs');
external_server.set('views', './views/');

external_server.get('/', function(req, res){
	res.render('index', {content: 0});
	return;
});

external_server.post('/', function(req, res){
	let url = req.body.url;

	if (url.indexOf('file')!=-1 || url.indexOf('localhost')!=-1 || url.indexOf('127.0.0.1')!=-1 || url.indexOf('0.0.0.0')!=-1){
		res.render('index', {content: 0});
		return;
	} else {
		https.get(url, (response) => {
			let data = '';

			response.on('data', (chunk) =>{
				data += chunk;
			});

			response.on('end', () => {
				res.render('index', {content: Buffer.from(data).toString('base64')});
				res.end();
			});
		}).on("error", (err) => {
			console.log("Error: " + err.message);
		});
		return;
	}
});
external_server.listen(5002);


internal_server.get('/', function(req, res){
	res.status(200).send('<!DOCTYPE html><html><head><title>localhost</title></head><body><a href="/flag">???</a></body></html>');
	res.end();
});

internal_server.get('/flag', function(req, res){
	res.status(200).send('DC5551{???_ssRF!1}');
	res.end();
});
internal_server.listen(80);
