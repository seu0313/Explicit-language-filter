import React from 'react';

// added
import axios from 'axios';
import { Player } from 'video-react';
import 'video-react/dist/video-react.css'

// design
import './VideoPreview.scss';
import { Button } from 'semantic-ui-react';


const VideoPreview = (props) => {
  const { Deep, _renderData } = props;

  // func
  const handleDelete = (e) => {
    axios
        .delete(`http://localhost:8000/api/v1/deeps/${Deep.id}`)
        .then(res => _renderData())
  }

  const convertMS = (duration) => {
    var seconds = parseInt((duration / 1000) % 60),
    minutes = parseInt((duration / (1000 * 60)) % 60),
    hours = parseInt((duration / (1000 * 60 * 60)) % 24);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    return hours + ":" + minutes + ":" + seconds ;
  }

  const convertCreatedAt = (date) => {
    var CreatedAt = date.substring(0, 10);
    return CreatedAt;
  }

  // render
  return (
    <div className='video-preview'>
      <div className='image-container'>
        <Player key={Deep.id} width='310px' height='200px' src={Deep.video_file} /> 
        <div className='time-label'>
          <span>{convertMS(Deep.video_duration)}</span>
        </div>
      </div>
      <div className='video-info'>
        <div className='semi-bold show-max-two-lines'>{Deep.title}</div>
        <div className='video-preview-metadata-container'>
          <div className='channel-title'>{Deep.description}</div>
          <div><span>생성일자 {convertCreatedAt(Deep.created_at)}</span></div>
          <div><Button id={Deep.id} size='small' color='linkedin' onClick={handleDelete}>삭제</Button></div>
        </div>
      </div>
    </div>
  );
}

export default VideoPreview;
