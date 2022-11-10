import { useState } from "react";
import "./App.css";
import GetDataForm from "./components/GetDataForm";
import LineGraph from "./components/Graph";
import { getRandomColor } from "./helpers/helpers";

function App() {
  const [allData, setAllData] = useState([]);

  const setError = (error) => {
    alert(error);
  };

  /* Updates the all the data for the main graph */
  const updateAllData = (data) => {
    // name for the most recently collected data
    const name = data ? data[0].name : null;

    setAllData((allData) => [
      ...allData,
      { name: name, color: getRandomColor(), data: data },
    ]);
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
      <GetDataForm
        data={allData}
        setData={updateAllData}
        setError={setError}
      ></GetDataForm>
    </div>
  );
}

export default App;
