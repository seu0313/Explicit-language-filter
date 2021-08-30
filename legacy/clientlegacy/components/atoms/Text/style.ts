import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  fontSize?: string;
}

export const TextWrapped = styled.div<Props>`
  display: flex;
  justify-content: start;
  align-items: center;
  
`;

export const Text = styled.span<Props>`
  width: 300px;
  font-size: ${(props: Props) => props.fontSize};
  color: ${theme.color.secondaryTextGray};
`;
