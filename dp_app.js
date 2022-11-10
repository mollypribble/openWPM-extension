const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
  // res.writeHead(200, { 'content-type': 'text/html' })
  // fs.createReadStream('dp_preview.html').pipe(res)

  res.writeHead(200, {'Content-Type': 'text/html'});
  fs.readFile('./dp_preview.html', null, function (error, data) {
      if (error) {
          res.writeHead(404);
          res.write('Whoops! File not found!');
      } else {
          res.write(data);
      }
  });

  res.writeHead(200, {'Content-Type': 'application/javascript'});
  fs.readFile('./dp_extension.js', null, function (error, data) {
      if (error) {
          res.writeHead(404);
          res.write('Whoops! File not found!');
      } else {
          res.write(data);
      }
  });
})

server.listen(process.env.PORT || 3000)