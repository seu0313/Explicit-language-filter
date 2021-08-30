import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  type?: string;
  fontSize?: string;
  width?: string;
}

export const Label = styled.div<Props>`
  display: flex;
  justify-content: ${(props: Props) => props.type === "logo" ? "space-evenly" : "start"};
  align-items: center;
  width: ${(props: Props) => props.width};
`;

export const LabelText = styled.span<Props>`
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: bold;
  font-size: ${(props: Props) => props.fontSize};
  color: ${theme.color.primaryTextGray};
`;

export const LabelLogo = styled.span<Props>`
  font-weight: bold;
  font-size: ${(props: Props) => props.fontSize};
  color: ${theme.color.basicColor};
`;
