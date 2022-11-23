import PieChartComponent from './PieChart';
import { toTitleCase } from '../helpers/helpers';
import '../styles/PieChartDrawer.css';

export default function PieChartDrawer({ countryName, removeCountry }) {
  let drawerBody = <></>;

  if (countryName) {
    drawerBody = (
      <>
        <h1>Average Undernourishment for {toTitleCase(countryName)}</h1>
        <PieChartComponent countryName={countryName}></PieChartComponent>
        <button
          className="removeButton"
          onClick={removeCountry}
          data-testid="remove-button"
        >
          Remove
        </button>
      </>
    );
  }
  return <div style={{ paddingBottom: '5rem' }}>{drawerBody}</div>;
}
