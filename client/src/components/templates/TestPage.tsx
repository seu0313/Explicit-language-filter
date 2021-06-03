import React, { useState } from "react";
import Header from "components/modules/Header";
import cloud from "assets/image/cloud.png";

const TestPage = () => {
  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);
  return (
    <div>
      <Header
        src={cloud}
        text="LINGO FILTER"
        isMenuClicked={isMenuClicked}
        setIsMenuCliecked={setIsMenuClicked}
        isUploadClicked={isUploadClicked}
        setUploadClicked={setIsUploadClicked}
      />
    </div>
  );
};

export default TestPage;
