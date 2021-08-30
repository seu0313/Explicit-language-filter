import theme from "./theme";

const mediaQuery = (maxWidth: number): string => `
  @media (max-width: ${maxWidth}px)
`;

const media = {
  mobile: mediaQuery(theme.size.mobile),
  tablet: mediaQuery(theme.size.tablet),
  labtop: mediaQuery(theme.size.labtop),
  xlabtop: mediaQuery(theme.size.xlabtop),
  desktop: mediaQuery(theme.size.desktop),
  custom: mediaQuery,
};

export default media;
