import React from 'react';
import CanvasDraw from "react-canvas-draw";
import Button from '../UI/Button';
import styles from './canvas.module.css';
const final=()=>{
    const numCanvas=React.createRef();
    const saveHandler=()=>{
       const num=numCanvas.current.canvas.drawing.toDataURL('image/jpeg');
       const downloadLink = document.createElement('a');
       const fileName = 'digit.jpeg';
       downloadLink.download = fileName;
       // console.log(image && (<img width={800} src={image} />));

     downloadLink.href = num;
     downloadLink.click()
       console.log(num);
    }
    const clearHandler= () =>{

        numCanvas.current.clear()
     }
   return(
       <div>
        <CanvasDraw
        ref={numCanvas}
        brushColor="white"
        backgroundColor="black"
        canvasWidth="450px"
        brushRadius = "16"
        className={styles.canvas} />
        <Button type="submit" onClick={saveHandler}>Save</Button>
        <Button 
         type="submit" 
         onClick={clearHandler}>
             Clear
        </Button>
       </div>
   )
}
export default final;