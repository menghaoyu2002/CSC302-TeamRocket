import { useState } from "react";
import "./App.css";
import DataList from "./components/DataList";
import GetDataForm from "./components/GetDataForm";
import LineGraph from "./components/Graph";
import { getRandomColor } from "./helpers/helpers";

function App() {
  const [rowData, setRowData] = useState([]);
  const [allData, setAllData] = useState([]);

  const setError = (error) => {
    alert(error);
  };

  /* Updates the all the data for the main graph */
  const updateAllData = (data) => {
    // name for the most recently collected data
    const name = data ? data[0].name : null;
    setRowData(data);

    if (name) {
      setAllData((allData) => {
        if (allData.find((data) => data.name === name)) {
          // do not change allData if the name is already there
          return allData;
        } else {
          // otherwise add the data for that name
          return [
            ...allData,
            { name: name, color: getRandomColor(), data: data },
          ];
        }
      });
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
