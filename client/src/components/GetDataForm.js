import { useState } from 'react';
import axios from 'axios';

export default function GetDataForm({ setData, setError }) {
  const [name, setName] = useState('');
  const [startYear, setStartYear] = useState(new Date().getFullYear());
  const [endYear, setEndYear] = useState(new Date().getFullYear());

  const handleSubmit = async (event) => {
    event.preventDefault();
    // TODO: change endpoint to getDataByNameAndYearRange
    await axios
      .get(`http://host.docker.internal:5000/data/${name}`)
      .then((res) => {
        if (res.status === 200) {
          setData(res.data.data);
        }
      })
      .catch((error) => {
        if (error.response) {
          setError(error.response.data.error.msg);
        } else {
          setError('Something went wrong...');
        }
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Name: </label>
      <input
        type="text"
        className="rounded ring-2 ring-slate-400 p-1"
        name="name"
        id="name"
        required={true}
        onChange={(e) => setName(e.target.value)}
      ></input>
      <label htmlFor="start-year">Start Year: </label>
      <input
        type="number"
        className="rounded ring-2 ring-slate-400 p-1"
        name="start-year"
        id="start-year"
        required={true}
        onChange={(e) => setStartYear(parseInt(e.target.value))}
      ></input>
      <label htmlFor="end-year">End Year: </label>
      <input
        type="number"
        name="end-year"
        id="end-year"
        required={true}
        onChange={(e) => setEndYear(parseInt(e.target.value))}
      ></input>
      <input type="submit" value="Submit"></input>
    </form>
  );
}
