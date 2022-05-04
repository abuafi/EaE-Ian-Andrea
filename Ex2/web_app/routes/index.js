var fs = require('fs')
var express = require('express');
const { assert } = require('console');
var router = express.Router();

/* GET start page. */
router.get('/', function(req, res, next) {
  // res.render('index', { title: 'Experiment 2' });
  res.render('../views/index.ejs');
});

const indexSets = 2
const caseSets = 2
counts = {}
for (j = 1; j <= caseSets; j++) {
  for (i = 1; i <= indexSets; i++) {
    counts[JSON.stringify({is:'is'+i, cs:'cs'+j})] = 0
  }
}

/* GET experiment page. */
router.get('/run',async function(req, res, next) {
  k = Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? b : a)
  j = JSON.parse(k)
  res.render('experimentview.ejs', {is:j['is'], cs:j['cs']});
});

/* GET ending page. */
router.get('/done',async function(req, res, next) {
  res.render('doneview.ejs');
});

const data_keys = ["uid","correct","time","style","correctI","correctS"]
const data_path = __dirname + "/../public/data.csv"
router.patch('/data',function(req, res, next) {
  req.on('data', (d) => {
    let data = JSON.parse(d)
    let groups = {is:data['is'], cs:data['cs']}
    counts[JSON.stringify(groups)]++
    let f = ''
    for (let line of JSON.parse(data['data'])) {
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

router.delete('/data',function(req, res, next) {
  fs.writeFile(data_path, data_keys.join(",")+"\n", () => {
    res.status(200).end()
  })
})

var uid = 0
router.get('/uid', function(req, res, next) {
  res.send(uid++ + "")
})

module.exports = router;
