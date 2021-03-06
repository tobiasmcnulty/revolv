var gulp = require('gulp');
var gulpif = require('gulp-if');
var notify = require('gulp-notify');
var cssmin = require('gulp-cssmin');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var livereload = require('gulp-livereload');
var fileExists = require('file-exists');
var isThere = require('is-there');

var spawn = require('child_process').spawn;
var argv = require('yargs')
  .default('port', 8000)
  .default('address', 'localhost')
  .argv;

// External dependencies you do not want to rebundle while developing,
// but include in your application deployment
var dependencies = [
];

var sassTask = function (options) {
  if (options.development) {
    var run = function () {
      var start = new Date();
      gulp.src(options.src)
        .pipe(gulpif(options.development, livereload()))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(options.dest))
        .pipe(notify(function () {
          console.log('CSS built in ' + (Date.now() - start) + 'ms');
        }))
      ;
    };
    run();
    gulp.watch(options.watch, run);
  } else {
    gulp.src(options.src)
      .pipe(sass().on('error', sass.logError))
      .pipe(cssmin())
      .pipe(gulp.dest(options.dest))
    ;
  }
}

function rebuild(options) {
  var options = options || {};

  sassTask({
    development: options.development,
    src: './revolv/static/scss/**/index.scss',
    watch: './revolv/static/scss/**/*.scss',
    dest: './revolv/static/dist/css/'
  });
}

// Starts our development workflow
gulp.task('default', function (cb) {
  if (!isThere("venv/bin/python")) {
    console.log(chalk.red("No venv found, so we can't run the dev server. Please see README.md to set up your venv."));
    console.log(chalk.red("Maybe you forgot to run `venv/bin/activate`?"));
    return;
  }
  livereload.listen();

  rebuild({
    development: true,
  });

  console.log("Starting Django runserver http://"+argv.address+":"+argv.port+"/");
  var args = ["manage.py", "runserver", argv.address+":"+argv.port];
  var runserver = spawn("venv/bin/python", args, {
    stdio: "inherit",
  });
  runserver.on('close', function(code) {
    if (code !== 0) {
      console.error('Django runserver exited with error code: ' + code);
    } else {
      console.log('Django runserver exited normally.');
    }
  });
});

gulp.task('deploy', function() {
  rebuild({
    development: false,
  })
});
