import React,{useRef} from 'react';
import CanvasDraw from "react-canvas-draw";
import { useScreenshot } from "use-screenshot-hook";
import styles from './canvas.module.css';
import Button from '../UI/Button';
const Canvas = () =>{
    const ref = useRef(null);
    const { image, takeScreenshot, isLoading, clear } = useScreenshot();
    function takeHandler(){
        takeScreenshot();
    }
    const saveHandler=()=>{
        const screenCaptureSource =image;
        const downloadLink = document.createElement('a');
        const fileName = 'Hello.jpeg';
        downloadLink.download = fileName;
        // console.log(image && (<img width={800} src={image} />));
   
      downloadLink.href = screenCaptureSource;
      downloadLink.click()
    }
    return(
       <div>
        <CanvasDraw  
        backgroundColor="white"
        brushColor = "black"
        className={styles.canvas}/>
        <Button type="submit" onClick={takeHandler}>
            SS
        </Button>
        <Button type="submit" onClick={saveHandler}>
            Save
        </Button>
       </div>
    );
}
export default Canvas;