const BASE_URL = 'http://localhost:3000';

describe('Home Page', () => {
  beforeEach(() => {
    cy.visit(BASE_URL);
  });

  it('should load on visit', () => {
    cy.get('.recharts-surface').should('be.visible');
  });

  it('should allow new countries to be added', () => {
    cy.get('#name').type('Canada');
    cy.get('input[type="submit"]').click();

    cy.get('.recharts-legend-item-text')
      .should('be.visible')
      .and('have.text', 'canada');
    cy.get('path[name="canada"]').should('be.visible');
  });

  it('should display a piechart for the country when clicked', () => {
    cy.get('#name').type('Canada');
    cy.get('input[type="submit"]').click();

    cy.get('.recharts-legend-item-text').click();
    cy.get('g.recharts-pie-sector:nth-child(2) > path:nth-child(1)').should(
      'be.visible'
    );
    cy.get('.App > div:nth-child(3) > h1:nth-child(1)').should(
      'have.text',
      'Average Undernourishment for Canada'
    );
  });

  it('should allow removal of countries in the graph', () => {
    cy.get('#name').type('Canada');
    cy.get('input[type="submit"]').click();
    cy.get('.recharts-legend-item-text').click();
    cy.get('.removeButton').click();
    cy.get('.recharts-legend-item-text').should('not.exist');
    cy.get('path[name="canada"]').should('not.exist');
  });

  it('should allow data within a specified range to be displayed', () => {
    cy.get('#name').type('Canada');
    cy.get('#start-year').type('2000');
    cy.get('#end-year').type('2010');
    cy.get('input[type="submit"]').click();

    cy.get('.recharts-legend-item-text')
      .should('be.visible')
      .and('have.text', 'canada');
    cy.get('path[name="canada"]').should('be.visible');
  });

  it('should allow multiple countries to be added and deleted at once', () => {
    cy.get('#name').type('Canada');
    cy.get('input[type="submit"]').click();

    cy.get('#name').clear();
    cy.get('#name').type('India');
    cy.get('input[type="submit"]').click();

    cy.get('path[name="canada"]').should('be.visible');
    cy.get('path[name="india"]').should('be.visible');

    cy.get('li.recharts-legend-item:nth-child(1) > span:nth-child(2)').click();
    cy.get('.removeButton').click();

    cy.get('path[name="canada"]').should('not.exist');
    cy.get('path[name="india"]').should('be.visible');
  });
});
