import React, { useState } from "react";
import HeaderHamburgerBtn from "components/atoms/HeaderHamburgerBtn";

const TestPage = () => {
  const [isMenuClicked, setIsMenuClicked] = useState(false);
  return (
    <div>
      <HeaderHamburgerBtn
        isMenuClicked={isMenuClicked}
        setIsMenuClicked={setIsMenuClicked}
      />
    </div>
  );
};

export default TestPage;
