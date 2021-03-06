var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var fs = require('fs');
var csv = require('csv-parser')

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

var words = []
fs.createReadStream("./public/words.csv")
  .pipe(csv())
  .on('data', (data) => {
    new_data = {"words": []}
    for (d in data) {
      if (d[0] == "_") new_data["words"].push(data[d])
      else new_data[d] = data[d]
      }
    words.push(new_data) 
  })

app.get(`/words`, async function(req, res) {
  i = parseInt(req.query.i) || 0
  is = req.query.is || "is1"
  cs = req.query.cs || "cs1"
  if (i >= words.length || i < 0) res.status(400).end()
  else {
    data = words[i]
    data["index"] = data[is]
    data["case"] = (data["defcase"] == "camelcase") ^ (cs == "cs1") ? "camelcase" : "kebabcase"
    res.json(data)
  }
})

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
