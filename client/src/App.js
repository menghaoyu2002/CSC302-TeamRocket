import { useState } from "react";
import "./App.css";
import DataList from "./components/DataList";
import GetDataForm from "./components/GetDataForm";
import LineGraph from "./components/Graph";

function App() {
  const [rowData, setRowData] = useState([]);
  const [allData, setAllData] = useState([]);

  const setError = (error) => {
    alert(error);
  };

  const getRandomColor = () => {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  };

  const updateAllData = (data) => {
    const name = data ? data[0].name : null;

    setRowData(data);

    if (name && !(name in allData)) {
      setAllData((allData) =>
        !allData.find((data) => data.name === name)
          ? [...allData, { name: name, color: getRandomColor(), data: data }]
          : allData
      );
    }
  };

  const onLegendClick = (event) => {
    console.log(event);
    const name = event.value;
    if (name) {
      setAllData((allData) => allData.filter((data) => data.name !== name));
    }
  };

  return (
    <div className='App'>
      <LineGraph data={allData} onLegendClick={onLegendClick}></LineGraph>
      <GetDataForm setData={updateAllData} setError={setError}></GetDataForm>
      <DataList data={rowData}></DataList>
    </div>
  );
}

export default App;
