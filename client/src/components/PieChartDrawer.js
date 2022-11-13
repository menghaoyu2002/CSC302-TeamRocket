import PieChartComponent from './PieChart';
import { capitalizeFirstLetter } from '../helpers/helpers';
import '../styles/PieChartDrawer.css';

export default function PieChartDrawer({ countryName }) {
  let drawerBody = <></>;

  if (countryName) {
    drawerBody = (
      <>
        <h1>
          Average Undernourishment for {capitalizeFirstLetter(countryName)}
        </h1>
        <PieChartComponent countryName={countryName}></PieChartComponent>
        <button className="removeButton">Remove</button>
      </>
    );
  }
  return <div style={{ padding: '50px' }}>{drawerBody}</div>;
}
