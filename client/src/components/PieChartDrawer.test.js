import { render, screen } from '@testing-library/react';
import PieChartDrawer from './PieChartDrawer';

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

test('renders with selected country name', () => {
  const countryName = 'world';

  render(<PieChartDrawer countryName={countryName} />);

  setTimeout(() => {
    const countryNameText = screen.getByText(countryName);

    expect(countryNameText).toBeInTheDocument();
  }, 1);
});

test('renders button to remove country', () => {
  const mockRemoveCountry = jest.fn();

  render(
    <PieChartDrawer countryName={'world'} removeCountry={mockRemoveCountry} />
  );

  const removeButton = screen.getByTestId('remove-button');

  removeButton.click();

  expect(mockRemoveCountry).toHaveBeenCalled();
});
