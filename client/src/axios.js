import axios from 'axios';

export default axios.create({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? 'http://host.docker.internal:5000'
      : 'http://127.0.0.1:8000',
});
