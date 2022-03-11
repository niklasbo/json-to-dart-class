# JSON to Plain Old Dart Object (PODO) generator

In many use cases I have an JSON string to transform into Dart data classes.

This little script does the most boilerplate code for me.

Feel free to use it and or optimize it.


Run with Python 3.7 or newer.


## Input
A JSON string and a class name. Enter it directly in `main.py`.

## Output
A Dart class with JSON and Equatable boilerplate.

Check the infered data types and change it if needed.

If you do not use [Equatable](https://pub.dev/packages/equatable), do not forget to add `equatable: ^2.X.X` to your `pubspec.yml` file.
