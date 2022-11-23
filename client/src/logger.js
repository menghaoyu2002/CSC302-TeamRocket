import axios from './axios';

export default class Logger {
  static debug(message) {
    console.debug(message);
    axios
      .post('/logger/', {
        severity: 'DEBUG',
        message: message,
      })
      .catch((err) => console.error(err));
  }

  static info(message) {
    console.info(message);
    axios
      .post('/logger/', {
        severity: 'INFO',
        message: message,
      })
      .catch((err) => console.error(err));
  }

  static warn(message) {
    console.warn(message);
    axios
      .post('/logger/', {
        severity: 'WARNING',
        message: message,
      })
      .catch((err) => console.error(err));
  }

  static fatal(message) {
    console.log(message);
    axios
      .post('/logger/', {
        severity: 'FATAL',
        message: message,
      })
      .catch((err) => console.error(err));
  }

  static error(message) {
    console.error(message);
    axios
      .post('/logger/', {
        severity: 'ERROR',
        message: message,
      })
      .catch((err) => console.error(err));
  }
}
