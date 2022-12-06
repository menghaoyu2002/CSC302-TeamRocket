import axios from 'axios';

export default axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL || 'http://127.0.0.1:5000',
});
