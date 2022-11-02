import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders input labels", () => {
  render(<App />);
  const linkElement = screen.getByText("Name:");
  expect(linkElement).toBeInTheDocument();
});
