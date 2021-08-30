import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import theme from "../../styles/theme";
import SidebarItem from "../SidebarItem";

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

const SidebarContainer = styled.div`
  display: flex;
  width: 100%;
  height: 100%;
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
