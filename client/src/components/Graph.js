import { useEffect, useState } from 'react';
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Label,
  Legend,
  Tooltip,
  ResponsiveContainer,
  ReferenceArea,
} from 'recharts';
import '../styles/Graph.css';

export default function LineGraph({ data, onLegendClick }) {
  const [slicedData, setSlicedData] = useState(data);
  const [state, setState] = useState({
    refAreaLeft: '',
    refAreaRight: '',
    top: 100,
    bottom: 0,
  });

  /**
   * @param from - Where the x axis starts from
   * @param to - Where the x axis ends at
   * @returns - The domain of the Y axis given the x axis' domain
   */
  const getAxisYDomain = (from, to) => {
    const offset = 1;
    let [bottom, top] = [100, 0];
    data.forEach((entry) => {
      entry.data.forEach((row) => {
        if (row.year >= from && row.year <= to) {
          if (row.undernourishment > top) top = row.undernourishment;
          if (row.undernourishment < bottom) bottom = row.undernourishment;
        }
      });
    });

    return [Math.max(bottom - offset, 0), Math.min(top + offset, 100)];
  };

  /**
   * @param from - Where the x axis starts from
   * @param to - Where the x axis ends at
   * @returns - A subset of data given the x axis' domain
   */
  const getSlicedData = (from, to) => {
    return data.map((entry) => ({
      ...entry,
      data: entry.data.filter((row) => {
        return row.year >= from && row.year <= to;
      }),
    }));
  };

  /**
   * Zooms in to the selected area of the graph
   */
  const zoom = () => {
    let { refAreaLeft, refAreaRight } = state;

    if (refAreaLeft === refAreaRight || !refAreaRight) {
      setState({
        ...state,
        refAreaLeft: '',
        refAreaRight: '',
      });
      return;
    }

    // xAxis domain
    if (refAreaLeft > refAreaRight)
      [refAreaLeft, refAreaRight] = [refAreaRight, refAreaLeft];

    // yAxis domain
    const [bottom, top] = getAxisYDomain(refAreaLeft, refAreaRight);

    const newSlicedData = getSlicedData(refAreaLeft, refAreaRight);

    setSlicedData(newSlicedData);
    setState({
      ...state,
      refAreaLeft: '',
      refAreaRight: '',
      bottom: bottom,
      top: top,
    });
  };

  /**
   * Zooms out of the graph
   */
  const zoomOut = () => {
    setSlicedData(data);
    setState({
      refAreaLeft: '',
      refAreaRight: '',
      top: 100,
      bottom: 0,
    });
  };

  useEffect(() => {
    setSlicedData(data);
  }, [data]);

  useEffect(zoomOut, [data]);

  return (
    <>
      {slicedData !== data && (
        <button type="button" className="zoomOutButton" onClick={zoomOut}>
          Zoom Out
        </button>
      )}
      <ResponsiveContainer width="100%" height="100%" minHeight={400}>
        <LineChart
          onMouseDown={(e) =>
            e && setState({ ...state, refAreaLeft: e.activeLabel })
          }
          onMouseMove={(e) =>
            state.refAreaLeft &&
            setState({ ...state, refAreaRight: e.activeLabel })
          }
          onMouseUp={zoom}
        >
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="year" allowDuplicatedCategory={false} height={50}>
            <Label value="Year" position={'insideBottom'} />
          </XAxis>
          <YAxis
            type="number"
            allowDataOverflow
            domain={[state.bottom, state.top]}
            tickFormatter={(value) => value.toFixed(0)}
          >
            <Label
              value="Undernourishment in % of Population"
              angle={-90}
              position={'insideLeft'}
              style={{
                textAnchor: 'middle',
              }}
            />
          </YAxis>
          <Tooltip />
          <Legend onClick={onLegendClick} data-testid="legend" />
          {slicedData.map((line) => (
            <Line
              key={line.name}
              type="monotone"
              dataKey="undernourishment"
              data={line.data}
              name={line.name}
              stroke={line.color}
            />
          ))}
          {state.refAreaLeft && state.refAreaRight ? (
            <ReferenceArea
              x1={state.refAreaLeft}
              x2={state.refAreaRight}
              strokeOpacity={0.3}
            />
          ) : null}
        </LineChart>
      </ResponsiveContainer>
    </>
  );
}
