import React from 'react';

// design
import './VideoGrid.scss';
import { Divider } from "semantic-ui-react";

// components
import VideoPreview from './VideoPreview';

const VideoGrid = (props) => {
    const {Deeps, _renderData, hideDivider} = props;
    const divider = hideDivider ? null : <Divider/>;
    
    return (
        <div className='video-section'>
            <h3>최근 영상</h3>
            <div className='video-grid'>
                {Deeps.map((deep) => (
                    <VideoPreview key={deep.id} Deep={deep} _renderData={_renderData} />
                ))}
            </div>
            {divider}
        </div>
    )
};

export default VideoGrid;
