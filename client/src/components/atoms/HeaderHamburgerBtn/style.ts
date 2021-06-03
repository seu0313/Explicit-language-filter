import styled, { css } from "styled-components";

export interface Props {
  isMenuClicked: boolean;
}

export const Container = styled.div`
  display: flex;
  width: 25px;
  justify-content: center;
  align-items: center;
`;

export const HeaderHamburgerWrapper = styled.ul<Props>`
  transform: translate(0%, 0%);
  width: 25px;
  height: 25px;
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

export const HeaderHamburgerList = styled.li`
  list-style: none;
  position: absolute;
  left: 0;
  background: black;
  width: 90%;
  height: 3px;
  border-radius: 6px;
  transform: translateY(-50%);
  transition: 0.4s;
`;
