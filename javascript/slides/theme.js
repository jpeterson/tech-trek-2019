import CalciteTheme from 'calcite-react/CalciteThemeProvider/CalciteTheme';
import { CalciteH1, CalciteH2, CalciteP, CalciteA } from 'calcite-react/Elements';

import Provider from './Provider';

export default {
  font: CalciteTheme.type.avenirFamily,
  Slide: {lineHeight: '1.55em', height: 'calc(100vh - 63px)'},
  components: {
    p: CalciteP,
    a: CalciteA
  },
  Provider
}