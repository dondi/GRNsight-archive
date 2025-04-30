var path = require("path");
var rootPath = path.normalize(__dirname + "/..");

module.exports = {
    development: {
        host: "localhost",
        port: 5001,
        url: "http://" + this.host + "/" + this.port,
        root: rootPath,
        app: {
            name: "GRNsight"
        },
        serviceRoot: "//localhost:5000"
    },

    production: {
        host: "localhost",
        port: 8080,
        url: "http://" + this.host + "/" + this.port,
        root: rootPath,
        app: {
            name: "GRNsight"
        },
        serviceRoot: "//localhost:5000"
    }
};
