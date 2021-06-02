import React from "react";
import VideoItem from "./VideoItem";
import Container from "@material-ui/core/Container";
import {} from "react-bootstrap";

const VideoList = (props) => {
  const { deeps, _renderData } = props;

  return (
    <Container>
      {deeps.map((deep) => (
        <VideoItem key={deep.id} deep={deep} _renderData={_renderData} />
      ))}
    </Container>
  );
};

export default VideoList;
