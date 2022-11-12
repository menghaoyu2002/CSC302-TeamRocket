import { PieChart, Pie, Tooltip } from 'recharts';
import { useEffect, useState } from 'react';
import axios from '../axios';

export default function PieChartComponent({ countryName }) {
  const [data, setData] = useState([]);
  useEffect(() => {
    const name = countryName;
    try {
      axios.get(`data/${name}/average`).then((res) => {
        console.log(res.data.data);
        setData([
          {
            name: 'average percentage of unnourished',
            value: res.data.data.average,
            fill: '#e87272',
          },
          {
            name: 'average percentage of nourished',
            value: 100 - res.data.data.average,
            fill: '#dbdbdb',
          },
        ]);
      });
    } catch (e) {
      console.log(e);
    }
  }, []);
  return (
    <PieChart width={730} height={250}>
      <Pie
        data={data}
        dataKey="value"
        nameKey="name"
        cx="50%"
        cy="50%"
        outerRadius={50}
        label
      ></Pie>
      <Tooltip />
    </PieChart>
  );
}
