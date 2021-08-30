import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import MainPage, { Props } from "./index";

export default {
  title: "Templates/MainPage",
  component: MainPage,
};

const Template: Story<Props> = (args): JSX.Element => (
  <GlobalThemeProvider>
    <MainPage {...args} />
  </GlobalThemeProvider>
);

export const MainPageStory = Template.bind({});

MainPageStory.args = {
  isMenuClicked: false,
  isUploadClicked: false,
};
