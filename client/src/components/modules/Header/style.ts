import styled from "styled-components";
import theme from "styles/theme";

export const Header = styled.div`
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 343px;
  height: 67px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px ${theme.color.lightShadow};
`;
