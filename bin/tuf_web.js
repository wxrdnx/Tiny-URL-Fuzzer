const ip   = "0.0.0.0";
const http = require('http');
const util = require('util');
// WHILE_LISTS = ['user-agent']

for (let port = 1; port < 49152; port++) {
    http.createServer(function (req, res) {
        url = req.connection.address().address + ':' + req.connection.address().port + req.url;
        console.log(util.format("[%s] - http://%s - [%s]", req.connection.remoteAddress,
            url, req.headers['user-agent']||''));

        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end(url + '\n');
    }).listen(port, ip);
}
console.log("Server running at http://" + ip + ":1-49151");
