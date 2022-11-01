import { RowData } from "../types/RowData";

interface IDataListProps {
  data: RowData[];
}

export default function DataList({ data }: IDataListProps) {
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
