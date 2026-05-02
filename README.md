# Flask Session Counter App
## Overview
This is a simple Flask web application that demonstrates how to use sessions to track user activity. The app keeps track of:
* Number of visits to the homepage
* A counter value that users can increment, reset, or customize
## Project Structure

```
project/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## How It Works

### Routes

* `/`
  Displays:

  * Total visits
  * Current counter value

* `/increment`
  Increases counter by 2

* `/reset`
  Resets counter to 0

* `/set_increment` (POST)
  Increases counter by a user-defined value

* `/destroy_session`
  Clears all session data

## Session Details

* Sessions are stored securely using Flask’s `secret_key`
* Data stored:

  * `visits`
  * `counter`

## Notes

* Make sure you have a `templates/index.html` file to render the UI.
* Debug mode is enabled (`debug=True`) — disable it in production.

## Example Use Cases

* Learning Flask sessions
* Building simple stateful web apps
