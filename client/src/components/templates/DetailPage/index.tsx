import React, { useState, useEffect } from "react";
import { useParams, Redirect } from "react-router-dom";
import axios from "axios";
import DetailVideo from "components/modules/DetailVideo";
import * as S from "./style";

const DetailPage = (): JSX.Element => {
  const { id }: any = useParams();
  const [deep, setDeep] = useState<any>([]);

  useEffect(() => {
    async function fetchData() {
      const url = `http://127.0.0.1:8000/api/v1/deeps/${id}`;

      try {
        const res = await axios.get(url);
        setDeep(res.data.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, []);

  const onClickDelete = async () => {
    const url = `http://127.0.0.1:8000/api/v1/deeps/${id}`;

      try {
        await axios.delete(url);
        setDeep([]);
        window.location.href = "/"
      } catch (error) {
        console.log(error);
      }
  }

  return (
    <S.Container>
      <DetailVideo
        id={deep.id}
        title={deep.title}
        description={deep.description}
        createdAt={deep.createdAt}
        src={deep.videoFile}
        onClick={onClickDelete}
      />
    </S.Container>
  );
};

export default DetailPage;
