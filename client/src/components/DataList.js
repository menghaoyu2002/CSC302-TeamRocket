export default function DataList({ data }) {
  return (
    <ul>
      {data.map((row, index) => (
        <li key={index}>
          name: {row.name} | undernourishment %: {row.undernourishment} | year:{" "}
          {row.year}
        </li>
      ))}
    </ul>
  );
}
