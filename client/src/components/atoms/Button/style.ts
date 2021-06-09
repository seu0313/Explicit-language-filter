import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  width: string;
  height: string;
  fontSize: string;
}

export const Button = styled.input<Props>`
  border: none;
  cursor: pointer;
  font-weight: bold;
  font-size: ${(props: Props) => props.fontSize};
  background-color: ${theme.color.basicColor};
  color: ${theme.color.primaryTextWhite};
  width: ${(props: Props) => props.width};
  height: ${(props: Props) => props.height};
`;
