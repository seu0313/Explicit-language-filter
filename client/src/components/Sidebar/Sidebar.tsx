import React from "react";
import { NavLink, Link } from "react-router-dom";
import styled from "styled-components";
import theme from "../../styles/theme";
import Icon from "../Icon";
import { TSvg } from "../Icon/Icon";

type SidebarItemProps = {
  children: React.ReactNode;
  name: TSvg;
  to: string;
};

export default function Sidebar(): JSX.Element {
  return (
    <SidebarContainer>
      <Link className="logo" to="/">
        Mung
      </Link>
      <SidebarList>
        <SidebarItem name="textIcon" to="text">
          텍스트 필터링
        </SidebarItem>
        <SidebarItem name="audioIcon" to="audio">
          오디오 필터링
        </SidebarItem>
        <SidebarItem name="videoIcon" to="video">
          비디오 필터링
        </SidebarItem>
      </SidebarList>
    </SidebarContainer>
  );
}

const SidebarItem = ({ children, name, to }: SidebarItemProps): JSX.Element => {
  return (
    <SidebarItemContainer>
      <NavLink className="nav-link" to={to}>
        <Icon name={name} />
        <span>{children}</span>
      </NavLink>
    </SidebarItemContainer>
  );
};

const SidebarContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  .logo {
    font-family: "Do Hyeon", sans-serif;
    margin-top: 1.5rem;
    margin-left: 2rem;
    font-size: 2rem;
    text-decoration: none;
    color: ${theme.color.basicColor};
  }
`;

const SidebarList = styled.ul`
  margin-top: 4rem;
  margin-left: 1rem;
  list-style: none;
`;

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
