var fs = require('fs')
// var fetch = require('node-fetch')
var express = require('express');
const { assert } = require('console');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  // res.render('index', { title: 'Experiment 2' });
  res.render('../views/index.ejs');
});

/* GET testing page. */
router.get('/run',async function(req, res, next) {
  res.render('experimentview.ejs');
});

const data_keys = ["correct","time","style","correctI"]
const data_path = __dirname + "/../public/data.csv"
router.patch('/data',function(req, res, next) {
  req.on('data', (d) => {
    let data = JSON.parse(d)
    let f = ''
    for (let line of data) {
      for (let key of data_keys) {
        f += line[key] + ","
      }
      f += '\n'
    }
    fs.appendFile(data_path, f, () => {
      res.status(200).end()
    })
  })
})

module.exports = router;
