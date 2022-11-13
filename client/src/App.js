import { useState } from 'react';
import './App.css';
import GetDataForm from './components/GetDataForm';
import LineGraph from './components/Graph';
import PieChartDrawer from './components/PieChartDrawer';
import { getRandomColor } from './helpers/helpers';

function App() {
  const [allData, setAllData] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState('');

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

  const removeCountryByName = (name) => {
    setAllData((allData) =>
      allData.filter((data) => data.name.toLowerCase() !== name.toLowerCase())
    );
    setSelectedCountry('');
  };

  const onLegendClick = (event) => {
    const name = event.value;
    if (name) {
      // setAllData((allData) => allData.filter((data) => data.name !== name));
      setSelectedCountry(name);
    }
  };

  return (
    <div className="App">
      <div className='MainGraphContainer'>
        <h2>Undernourishment vs Time</h2>
        <LineGraph
          className='MainGraph'
          data={allData}
          onLegendClick={onLegendClick}
        ></LineGraph>
      </div>
      <GetDataForm
        data={allData}
        setData={updateAllData}
        setError={setError}
      ></GetDataForm>
      <PieChartDrawer
        countryName={selectedCountry}
        removeCountry={() => removeCountryByName(selectedCountry)}
      ></PieChartDrawer>
    </div>
  );
}

export default App;
