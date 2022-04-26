var fs = require('fs')
// var fetch = require('node-fetch')
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  // res.render('index', { title: 'Experiment 2' });
  res.render('../views/index.ejs');
});

/* GET testing page. */
router.get('/run',async function(req, res, next) {
  res.render('experimentview.ejs', { words: ['hello,world,ciao,mondo'] });
});

module.exports = router;
