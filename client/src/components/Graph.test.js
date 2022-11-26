import { render, screen } from '@testing-library/react';
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
  const countryName = 'world';

  const data = [
    {
      name: countryName,
      color: '#000000',
      data: [{ name: countryName, year: 2001, undernourishment: 0.2 }],
    },
  ];
  render(<LineGraph data={data} />);

  setTimeout(() => {
    const countryNameText = screen.getByText(countryName);

    expect(countryNameText).toBeInTheDocument();
  }, 1);
});

test('handles clicks on legend items', () => {
  const countryName = 'world';

  const data = [
    {
      name: countryName,
      color: '#000000',
      data: [{ name: countryName, year: 2001, undernourishment: 0.2 }],
    },
  ];

  const mockOnLegendClick = jest.fn();

  render(<LineGraph data={data} onLegendClick={mockOnLegendClick} />);

  setTimeout(() => {
    const countryNameText = screen.getByText(countryName);
    countryNameText.click();

    expect(mockOnLegendClick).toHaveBeenCalled();
  }, 1);
});
