import React from 'react';
import CalciteThemeProvider from 'calcite-react/CalciteThemeProvider';
import Button from 'calcite-react/Button';
import TopNav, {
  TopNavBrand,
  TopNavTitle,
  TopNavList,
  TopNavLink,
  TopNavActionsList
} from 'calcite-react/TopNav';

const Provider = ({ children }) => {
  return (
    <CalciteThemeProvider>
      <TopNav>
        <TopNavBrand
          href={getLink(0)}
          src="/static/assets/esri-logo-black.svg"
        />
        <TopNavTitle href={getLink(0)}>Python @ Esri</TopNavTitle>
        <TopNavList>
          <TopNavLink href={getLink(0)} active={isActive([0, 26])}>
            Intro
          </TopNavLink>
          <TopNavLink href={getLink(27)} active={isActive([27, 39])}>
            Python Environments
          </TopNavLink>
          <TopNavLink href={getLink(40)} active={isActive([40, 72])}>
            Administering your GIS
          </TopNavLink>
          <TopNavLink href={getLink(73)} active={isActive([73, 88])}>
            Analysis
          </TopNavLink>
          <TopNavLink href={getLink(89)} active={isActive([89, 1000])}>
            Advanced Workflows
          </TopNavLink>
        </TopNavList>
        <TopNavActionsList>
          <TopNavLink href={getLink()}>Sign In</TopNavLink>
          <Button clear>Sign Up</Button>
        </TopNavActionsList>
      </TopNav>
      {children}
    </CalciteThemeProvider>
  );
};

const getLink = slide => {
  if (typeof window === 'undefined') {
    return '#';
  } else {
    return `${window.location.origin}/${slide || '#'}`;
  }
};

const isActive = range => {
  if (typeof window === 'undefined') {
    return false;
  } else {
    const page = Number(window.location.pathname.substring(1));
    return page >= range[0] && page <= range[1];
  }
};

export default Provider;
