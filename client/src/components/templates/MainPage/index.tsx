/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable no-console */
/* eslint-disable-next-line consistent-return */

import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import thumb from "assets/image/thumbnail2.png";
import Header from "components/modules/Header";
import MainVideo from "components/modules/MainVideo";
import ModalContainer from "components/modules/ModalContainer";
import * as S from "./style";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const MainPage = (): JSX.Element => {
  const [deeps, setDeeps] = useState<any[]>([]);

  useEffect(() => {
    async function fetchData() {
      const url = "http://127.0.0.1:8000/api/v1/deeps/";

      try {
        const res = await axios.get(url);
        setDeeps(res.data.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, []);

  const renderHandler = async () => {
    const url = "http://127.0.0.1:8000/api/v1/deeps/";

    try {
      const res = await axios.get(url);
      setDeeps(res.data.data);
    } catch (error) {
      console.log(error);
    }
  };

  const dummy = [
    {
      id: "1",
      title: "Mountains | Beautiful Chill Mix WAAAAA~",
      createdAt: "2021-06-04T14:05:46.384Z",
      src: thumb,
    },
    {
      id: "2",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumb,
    },
    {
      id: "3",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumb,
    },
    {
      id: "4",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumb,
    },
  ];

  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);

  return (
    <S.Container>
      <Header
        isMenuClicked={isMenuClicked}
        setIsMenuCliecked={setIsMenuClicked}
        isUploadClicked={isUploadClicked}
        setIsUploadClicked={setIsUploadClicked}
      />
      <S.DeepWrapped>
        {deeps.map((deep) => (
          <Link to={`/detail/${deep.id}/`}>
            <MainVideo
              key={deep.id}
              id={deep.id}
              title={deep.title}
              createdAt={deep.createdAt}
              src={thumb}
            />
          </Link>
        ))}
      </S.DeepWrapped>

      <ModalContainer
        isUploadClicked={isUploadClicked}
        setIsUploadClicked={setIsUploadClicked}
        isMenuClicked={isMenuClicked}
        setIsMenuClicked={setIsMenuClicked}
        renderHandler={renderHandler}
      />
    </S.Container>
  );
};

export default MainPage;
