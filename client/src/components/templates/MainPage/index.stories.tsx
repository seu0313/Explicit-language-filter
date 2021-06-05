import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import MainPage from "./index";

export default {
  title: "Templates/MainPage",
  component: MainPage,
};

const Template: Story = (): JSX.Element => (
  <GlobalThemeProvider>
    <MainPage />
  </GlobalThemeProvider>
);

export const MainPageStory = Template.bind({});
