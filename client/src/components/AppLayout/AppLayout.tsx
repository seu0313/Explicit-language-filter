import React from "react";
import styled from "styled-components";
import media from "../../styles/media";

type AppLayoutProps = {
  children: React.ReactNode;
};

type SideProps = {
  children: React.ReactNode;
};

type MainProps = {
  children: React.ReactNode;
};

export default function AppLayout({ children }: AppLayoutProps): JSX.Element {
  return <div>{children}</div>;
}

function Side({ children }: SideProps): JSX.Element {
  return <SideContainer>{children}</SideContainer>;
}

function Main({ children }: MainProps): JSX.Element {
  return <MainContainer>{children}</MainContainer>;
}

AppLayout.Side = Side;
AppLayout.Main = Main;

const SideContainer = styled.aside`
  width: 13.25rem;
  height: 100%;
  position: fixed;
  display: flex;
  ${media.xlabtop} {
    padding: 0;
  }
  background-color: white;
  box-shadow: 2px 2px 10px 1px rgba(85, 85, 85, 0.2);
`;

const MainContainer = styled.main`
  padding-left: 2rem;
  padding-top: 3rem;
  margin-left: 14.25rem;
  padding-bottom: 3rem;
`;
