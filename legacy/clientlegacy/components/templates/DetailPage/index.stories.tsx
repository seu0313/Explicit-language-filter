import React from "react";
import { Story } from "@storybook/react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import DetailPage from "./index";

export default {
  title: "Templates/DetailPage",
  component: DetailPage,
};

const Template: Story = (): JSX.Element => (
  <GlobalThemeProvider>
    <DetailPage />
  </GlobalThemeProvider>
);

export const DetailPageStory = Template.bind({});
