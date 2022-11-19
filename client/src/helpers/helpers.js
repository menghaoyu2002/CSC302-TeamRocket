/* Return a string representing a random color */
export const getRandomColor = () => {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
};

export function capitalizeFirstLetter(string) {
  return string.toLowerCase().charAt(0).toUpperCase() + string.slice(1);
}

export function toTitleCase(str) {
  return str.replace(/\w\S*/g, capitalizeFirstLetter);
}
