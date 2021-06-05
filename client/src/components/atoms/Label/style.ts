import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  size?: string;
  width?: string;
}

export const Label = styled.div<Props>`
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: ${(props: Props) => props.width};
`;

export const LabelText = styled.span<Props>`
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: bold;
  font-size: ${(props: Props) => props.size};
  color: ${theme.color.primaryTextGray};
`;

export const LabelLogo = styled.span<Props>`
  font-weight: bold;
  font-size: ${(props: Props) => props.size};
  color: ${theme.color.basicColor};
`;
