import { PieChart, Pie, Tooltip } from 'recharts';
import { useEffect, useState } from 'react';
import axios from '../axios';

const style = {
  margin: 'auto',
};

const redText = {
  color: 'red',
};

export default function PieChartComponent({ countryName }) {
  const [data, setData] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    setErrorMessage('');
    axios
      .get(`data/${countryName}/average`)
      .then((res) => {
        const average = res.data.data.average;
        setData([
          {
            name: 'average percentage of unnourished',
            value: parseFloat(average.toFixed(2)),
            fill: '#e87272',
          },
          {
            name: 'average percentage of nourished',
            value: parseFloat((100 - average).toFixed(2)),
            fill: '#dbdbdb',
          },
        ]);
      })
      .catch((error) => {
        setErrorMessage(error.message);
      });
  }, [countryName]);
  return (
    <div>
      <PieChart width={730} style={style} height={250}>
        <Pie
          data={data}
          dataKey="value"
          nameKey="name"
          cx="50%"
          cy="50%"
          outerRadius={80}
          label
          tickFormatter={(value) => value.toFixed(2)}
        ></Pie>
        <Tooltip />
      </PieChart>
      <p style={redText}>{errorMessage}</p>
    </div>
  );
}
