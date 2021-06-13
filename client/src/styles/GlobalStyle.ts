import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    text-decoration: none;
  }
  body {
    box-sizing: border-box;
    font-family: Helvetica, Arial, sans-serif;
    background-color: #FFFFFF;
    -ms-overflow-style:none; 
  }

  body::-webkit-scrollbar { display:none; }

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
