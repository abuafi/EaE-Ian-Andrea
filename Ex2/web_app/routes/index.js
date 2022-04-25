var parse = require('csv-parse')
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Experiment 2' });
});

/* GET testing page. */
router.get('/run', function(req, res, next) {
  res.render('experimentview.ejs', { words: ['hello', 'world'] });
});

module.exports = router;
