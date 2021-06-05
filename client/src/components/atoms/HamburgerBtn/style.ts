import styled, { css } from "styled-components";
import theme from "styles/theme";

export interface Props {
  isMenuClicked: boolean;
}

export const HamburgerWrapper = styled.ul<Props>`
  transform: translate(0%, 0%);
  width: 26px;
  height: 26px;
  cursor: pointer;

  li:nth-of-type(1) {
    top: 20%;
  }
  li:nth-of-type(2) {
    top: 50%;
  }
  li:nth-of-type(3) {
    top: 80%;
  }

  ${(props: Props) =>
    props.isMenuClicked &&
    css`
      li:nth-of-type(1) {
        top: 50%;
        transform: translateY(-50%) rotate(45deg);
      }
      li:nth-of-type(2) {
        top: 50%;
        transform: translateY(-50%) rotate(-45deg);
      }
      li:nth-of-type(3) {
        left: -100%;
        opacity: 0;
      }
    `}};
`;

export const HamburgerList = styled.li`
  list-style: none;
  position: absolute;
  left: 0;
  background: ${theme.color.primaryTextGray};
  width: 100%;
  height: 4px;
  border-radius: 8px;
  transform: translateY(-50%);
  transition: 0.4s;
`;
