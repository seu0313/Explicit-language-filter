import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
  }
  body {
    box-sizing: border-box;
    font-family: Helvetica, Arial, sans-serif;
    background-color: #FFFFFF;
  }
  ul, ol {
    list-style: none;
  }
  button {
    border: none;
    padding: 0;
  }
  button:focus {
    outline: none;
  }
`;

export default GlobalStyle;
