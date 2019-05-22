import React from 'react';
import PropTypes from 'prop-types';

import Label from 'calcite-react/Label'
import Card, { CardTitle, CardContent, CardImage } from 'calcite-react/Card';

const Person = props => {
  return (
    <Card bar="blue" style={{ maxWidth: '680px' }}>
      <CardContent>
        <CardTitle as="h2">Gavin Rehkemper</CardTitle>
        <div>@gavinrehkemper</div>
        <div>https://gavinr.com</div>
      </CardContent>
    </Card>
  );
};

Person.propTypes = {};

export default Person;
