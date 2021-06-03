import React from "react";
import { ThemeProvider } from "styled-components";
import GlobalStyle from "./GlobalStyle";
import theme from "./theme";

interface Props {
  children?: React.ReactElement | React.ReactElement[] | string;
}

const GlobalThemeProvider: React.FC<Props> = ({ children }) => {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      {children}
    </ThemeProvider>
  );
};

export default GlobalThemeProvider;
