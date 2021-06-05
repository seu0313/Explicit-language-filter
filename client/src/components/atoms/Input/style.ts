import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  width: string;
  height: string;
  fontSize: string;
}

export const Input = styled.input<Props>`
  padding-left: 10px;
  border: none;
  width: ${(props: Props) => props.width};
  height: ${(props: Props) => props.height};
  font-size: ${(props: Props) => props.fontSize};
  background-color: ${theme.color.lightGray}};
`;
