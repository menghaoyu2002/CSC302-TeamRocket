import { useState } from 'react';
import './App.css';
import DataList from './components/DataList';
import GetDataForm from './components/GetDataForm';

function App() {
  const [rowData, setRowData] = useState([]);

  const setError = (error) => {
    alert(error);
  };

  return (
    <div className="App">
      <GetDataForm setData={setRowData} setError={setError}></GetDataForm>
      <DataList data={rowData}></DataList>
    </div>
  );
}

export default App;
