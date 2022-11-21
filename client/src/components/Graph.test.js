import { render, screen } from '@testing-library/react';
import App from '../App';
import LineGraph from './Graph';

jest.mock('recharts', () => {
  const OriginalModule = jest.requireActual('recharts');

  return {
    ...OriginalModule,
    ResponsiveContainer: ({ height, children }) => (
      <OriginalModule.ResponsiveContainer width={800} height={height}>
        {children}
      </OriginalModule.ResponsiveContainer>
    ),
  };
});

// jest.mock('./Graph', () => {
//   const OriginalModule = jest.requireActual('./Graph');

//   const data = [
//     {
//       name: 'world',
//       color: '#000000',
//       data: [{ name: 'world', year: 2001, undernourishment: 0.2 }],
//     },
//   ];
//   return <OriginalModule.LineGraph data={data} />;
// });

const { ResizeObserver } = window;

beforeEach(() => {
  delete window.ResizeObserver;
  window.ResizeObserver = jest.fn().mockImplementation(() => ({
    observe: jest.fn(),
    unobserve: jest.fn(),
    disconnect: jest.fn(),
  }));
});

afterEach(() => {
  window.ResizeObserver = ResizeObserver;
  jest.restoreAllMocks();
});

test('renders with country in legend when given data', () => {
  const data = [
    {
      name: 'world',
      color: '#000000',
      data: [{ name: 'world', year: 2001, undernourishment: 0.2 }],
    },
  ];
  render(<LineGraph data={data} />);

  const countryName = screen.getByTestId('legend');

  setTimeout(() => expect(countryName).toBeInTheDocument(), 1000);
});
