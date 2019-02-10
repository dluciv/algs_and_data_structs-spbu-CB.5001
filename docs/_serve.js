let os = require('os');

switch(os.hostname()) {
  case 'universum':
    var NM = 'C:\\Users\\d\\AppData\\Roaming\\npm\\node_modules';
    var RJ = 'D:\\JsPrg\\reveal.js';
    break;
  case 'aureolo':
    var NM = 'C:\\Users\\dluciv\\AppData\\Roaming\\npm\\node_modules';
    var RJ = 'D:\\JsPrg\\reveal.js';
    break;
  case 'esperanto':
    var NM = '/usr/lib/node_modules';
    var RJ = os.homedir() + '/_/reveal.js';
}

((glmpn_path, reveal_path) => {
  module.paths.push(glmpn_path);
  let express = require('express')
  let server = express();

  server.use("/", express.static(__dirname));
  server.use("/reveal.js", express.static(reveal_path));

  server.listen(8080);
})(NM, RJ);
