/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable no-console */
/* eslint-disable-next-line consistent-return */

import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import thumb from "assets/image/thumbnail2.png";
import MainVideo from "components/modules/MainVideo";
import ModalContainer from "components/modules/ModalContainer";
import * as S from "./style";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export interface Props {
  isMenuClicked: boolean
  setIsMenuClicked: (value: boolean) => void
  isUploadClicked: boolean
  setIsUploadClicked: (value: boolean) => void
}

const MainPage: React.FC<Props> = ({ isMenuClicked, setIsMenuClicked, isUploadClicked, setIsUploadClicked}): JSX.Element => {
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

  return (
    <S.Container>
      <S.DeepWrapped>
        {deeps.map((deep) => (
          <Link to={`/detail/${deep.id}/`}>
            <MainVideo
              key={deep.id}
              id={deep.id}
              title={deep.title}
              createdAt={deep.createdAt}
              src={deep.src}
            />
            <br/>
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
