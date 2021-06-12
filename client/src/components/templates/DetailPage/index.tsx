import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
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
        // console.log(res.data.data);
        setDeep(res.data.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, []);

  return (
    <S.Container>
      <DetailVideo
        id={deep.id}
        title={deep.title}
        description={deep.description}
        createdAt={deep.createdAt}
        src={deep.videoFile}
      />
    </S.Container>
  );
};

export default DetailPage;
