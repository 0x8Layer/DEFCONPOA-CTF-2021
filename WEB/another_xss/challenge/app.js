const express = require('express');
const puppeteer = require('puppeteer');

const app = express();
app.use(express.json());
app.use(express.urlencoded({extended: true}));

function sleep(s){
	return new Promise(resolve => setTimeout(resolve, s*1000));

}

async function bot(url) {
	try{
		const cookies = [{name: 'FLAG', value: 'DC5551{xss_every_d4y!}', domain: '0.0.0.0'}];

		const browser = await puppeteer.launch({args: ['--no-sandbox'],});
		const page = await browser.newPage();
		await page.setCookie(...cookies);
		await page.goto(`${url}`);
		sleep(5);
		await browser.close();
	} catch(e) {
		return;
	}
}

app.get('/', (req, res) => {
	res.sendFile('index.html', {root: __dirname});
});

app.get('/admin', (req, res) => {
	res.sendFile('admin.html', {root: __dirname});
});

app.post('/admin/send', (req, res) => {
	bot(req.body.url);
	res.status(200).send('OK');
});

console.log("Server in port 5008");
app.listen(5008);
