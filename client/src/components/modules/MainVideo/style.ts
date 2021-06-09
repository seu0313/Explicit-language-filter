import styled from "styled-components";
import theme from "styles/theme";

export const MainVideo = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0px 4px 10px #e9e9e9;
  width: ${theme.size.customWidth};
  cursor: pointer;
`;

export const MetaSection = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  height: 78px;
`;
