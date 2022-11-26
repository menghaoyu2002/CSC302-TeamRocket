import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Label,
  Legend,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

export default function LineGraph({ data, onLegendClick }) {
  return (
    <ResponsiveContainer width="100%" height="100%" minHeight={400}>
      <LineChart>
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="year" allowDuplicatedCategory={false} height={50}>
          <Label value="Year" position={'insideBottom'} />
        </XAxis>
        <YAxis type="number" domain={[0, 100]}>
          <Label
            value="Undernourishment in % of Population"
            angle={-90}
            position={'insideLeft'}
            style={{
              textAnchor: 'middle',
            }}
          />
        </YAxis>
        <Tooltip />
        <Legend onClick={onLegendClick} data-testid="legend" />
        {data.map((line) => (
          <Line
            key={line.name}
            type="monotone"
            dataKey="undernourishment"
            data={line.data}
            name={line.name}
            stroke={line.color}
          />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
}
