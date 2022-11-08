import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Legend,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function LineGraph({ data, onLegendClick }) {
  return (
    <ResponsiveContainer width='100%' height='100%' minHeight={400}>
      <LineChart width={400} height={400}>
        <CartesianGrid stroke='#ccc' />
        <XAxis dataKey='year' allowDuplicatedCategory={false} />
        <YAxis />
        <Tooltip />
        <Legend onClick={onLegendClick} />
        {data.map((line) => (
          <Line
            key={line.name}
            type='monotone'
            dataKey='undernourishment'
            data={line.data}
            name={line.name}
            stroke={line.color}
          />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
}
