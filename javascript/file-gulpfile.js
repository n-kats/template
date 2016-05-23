const gulp = require('gulp');
const babel = require('gulp-babel');

gulp.task('compile-es6', () => {
  return gulp
  .src('src/**/*.js')
  .pipe(
    babel({
      presets: ['es2015', 'react'],
      plugins: [
        'syntax-trailing-function-commas',
        'transform-class-properties',
        'transform-inline-environment-variables',
        'transform-object-rest-spread',
      ]
    })
  )
  .pipe(gulp.dest('app'));
});

gulp.task('compile-html', () => {
  return gulp
  .src('src/**/*.html')
  .pipe(gulp.dest('app'));
});

gulp.task(
  'compile',
  [
    'compile-es6',
    'compile-html'
  ]
);
