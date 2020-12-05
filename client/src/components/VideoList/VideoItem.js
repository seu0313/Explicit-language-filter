import React from 'react';
import axios from 'axios';
import { Player } from 'video-react';
import 'video-react/dist/video-react.css'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';


const useStyles = makeStyles({
    root: {
      maxWidth: 400,
    },
    media: {
      height: 140,
    },
  });

const VideoItem = (props) => {
    const { deep, _renderData } = props
    const classes = useStyles();

    const handleDelete = () => {
        axios
            .delete(`http://localhost:8000/api/v1/deeps/${deep.id}`)
            .then(res => _renderData())
    }

    return(
        <Card className={classes.root}>
            <CardActionArea>
                <Player className={classes.media} key={deep.id} fluid={false} width={400} height={300} src={deep.video_file}/>
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {deep.title}
                    </Typography>
                    <Typography variant="body2" color="textSecondary" component="p">
                        {deep.created_at}
                    </Typography>
                </CardContent>
            </CardActionArea>
            <CardActions>
                <Button size="small" color="primary">
                Share
                </Button>
                <Button size="small" color="primary" onClick={handleDelete}>
                Delete
                </Button>
            </CardActions>
        </Card> 
    );
}

export default VideoItem;