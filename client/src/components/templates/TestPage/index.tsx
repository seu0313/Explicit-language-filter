import React, { useState } from "react";
import Header from "components/modules/Header";
import cloud from "assets/image/cloud.png";
import thumbnail from "assets/image/thumbnail.png";
import thumbnail2 from "assets/image/thumbnail2.png";

// Test page
import MainVideo from "components/modules/MainVideo";
import * as S from "./style";

const TestPage = (): JSX.Element => {
  const dummy = [
    {
      id: "1",
      text: "Mountains | Beautiful Chill Mix WAAAAA~",
      date: "2021-06-04T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "2",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
    {
      id: "3",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "4",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
  ];

  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);
  return (
    <S.Container>
      <S.Elements>
        <Header
          src={cloud}
          text="LINGO FILTER"
          isMenuClicked={isMenuClicked}
          setIsMenuCliecked={setIsMenuClicked}
          isUploadClicked={isUploadClicked}
          setUploadClicked={setIsUploadClicked}
        />
        <div style={{ display: "inline-block", width: "343px" }} />
        {dummy.map((deep) => (
          <div>
            <MainVideo
              id={deep.id}
              text={deep.text}
              date={deep.date}
              src={deep.src}
            />
            <div style={{ display: "inline-block", width: "343px" }} />
          </div>
        ))}
      </S.Elements>
    </S.Container>
  );
};

export default TestPage;
