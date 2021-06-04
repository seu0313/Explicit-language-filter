import React from "react";
import { ThemeProvider } from "styled-components";
import { ModalProvider } from "styled-react-modal";
import GlobalStyle from "./GlobalStyle";
import FadingBackground from "./FadingBackground";
import theme from "./theme";

interface Props {
  children?: React.ReactElement | React.ReactElement[] | string;
}

const GlobalThemeProvider: React.FC<Props> = ({ children }): JSX.Element => {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <ModalProvider backgroundComponent={FadingBackground}>
        {children}
      </ModalProvider>
    </ThemeProvider>
  );
};

export default GlobalThemeProvider;
