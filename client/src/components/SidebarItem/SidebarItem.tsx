import React from "react";
import { NavLink } from "react-router-dom";
import styled from "styled-components";
import theme from "../../styles/theme";
import Icon from "../Icon";
import { TSvg } from "../Icon/Icon";

type SidebarItemProps = {
  children: React.ReactNode;
  name: TSvg;
  to: string;
};

export default function SidebarItem({
  children,
  name,
  to,
}: SidebarItemProps): JSX.Element {
  return (
    <SidebarItemContainer>
      <NavLink className="nav-link" to={to}>
        <Icon name={name} />
        <span>{children}</span>
      </NavLink>
    </SidebarItemContainer>
  );
}

const SidebarItemContainer = styled.li`
  display: flex;
  justify-content: left;
  align-items: center;
  margin-bottom: 0.5rem;

  .nav-link {
    display: flex;
    /* justify-content: center; */
    align-items: center;
    padding-left: 1rem;
    width: 80%;
    height: 2.75rem;
    border-radius: 0.5rem;

    span {
      margin-left: 1rem;
      font-size: 1.1rem;
      font-weight: 600;
      color: ${theme.color.secondaryTextGray};
    }

    &:hover {
      background-color: ${theme.color.hover};
      span {
        color: ${theme.color.primaryTextWhite};
      }
      transition: all 0.3s ease-in;
    }

    &:active {
      background-color: ${theme.color.hover};
      span {
        color: ${theme.color.press};
      }
    }
  }
`;
