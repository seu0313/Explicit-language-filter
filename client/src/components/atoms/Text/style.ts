import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  fontSize?: string;
}

export const TextWrapped = styled.div<Props>`
  display: flex;
  justify-content: space-evenly;
  align-items: center;
`;

export const Text = styled.span<Props>`
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: bold;
  font-size: ${(props: Props) => props.fontSize};
  color: ${theme.color.secondaryTextGray};
`;
