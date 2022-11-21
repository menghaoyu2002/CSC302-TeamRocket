import { fireEvent, render, screen } from '@testing-library/react';
import App from './App';

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

test('renders input labels', () => {
  render(<App />);
  const countryNameLabel = screen.getByText('Country Name:');
  const startYearLabel = screen.getByText('Start Year:');
  const endYearLabel = screen.getByText('End Year:');

  expect(countryNameLabel).toBeInTheDocument();
  expect(startYearLabel).toBeInTheDocument();
  expect(endYearLabel).toBeInTheDocument();
});
