export default function DataList({ data }) {
  return (
    <ul>
      {data.map((row) => (
        <li>
          name: {row.name} | undernourishment %: {row.undernourishment} | year:{" "}
          {row.year}
        </li>
      ))}
    </ul>
  );
}