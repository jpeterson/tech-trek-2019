import React from "react";
import CalciteThemeProvider from "calcite-react/CalciteThemeProvider";
import Button from 'calcite-react/Button';
import TopNav, {
  TopNavBrand,
  TopNavTitle,
  TopNavList,
  TopNavLink,
  TopNavActionsList
} from "calcite-react/TopNav";

const Provider = ({ children }) => {
  return (
    <CalciteThemeProvider>
      <TopNav>
        <TopNavBrand href="#" src="/static/assets/esri-logo-black.svg" />
        <TopNavTitle href="#">Esri ❤️ The Modern Web</TopNavTitle>
        <TopNavList>
          <TopNavLink href="#" active={isActive([0, 40])}>
            JSAPI + Arcade
          </TopNavLink>
          <TopNavLink href="#" active={isActive([41, 53])}>Web AppBuilder + ExB</TopNavLink>
          <TopNavLink href="#" active={isActive([54, 57])}>Open Source</TopNavLink>
        </TopNavList>
        <TopNavActionsList>
          <TopNavLink href="#">Sign In</TopNavLink>
          <Button clear>Sign Up</Button>
        </TopNavActionsList>
      </TopNav>
      {children}
    </CalciteThemeProvider>
  );
};

const isActive = range => {
  if (typeof window === 'undefined') {
    return false;
  } else {
    const page = Number(window.location.pathname.substring(1));
    return page >= range[0] && page <= range[1];
  }
}

export default Provider;
