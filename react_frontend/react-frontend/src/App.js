import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Button } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [loader, setLoader] = useState(false);


  const handleSubmit = async () => {
    setLoader(true)
    try {
      const response = await fetch('/get_response', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      setLoader(false);

      const result = await response.json();
      setOutputText(result.result);
    } catch (error) {
      console.error('Error submitting text:', error);
    }
  };

  return (
    <div className="App" >

    {/* <Box
      component="img"
      sx={{
        height: 333,
        width: 450,
        maxHeight: { xs: 233, md: 167 },
        maxWidth: { xs: 350, md: 250 },
      }}
      pl={150}
      alt="The house from the offer."
      src="https://png.pngtree.com/png-clipart/20230928/original/pngtree-colorful-bulb-vector-illustration-on-white-background-efficiency-electricity-invention-vector-png-image_12896701.png"
    /> */}

      <script src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs" type="module"></script> 

      <dotlottie-player src="https://lottie.host/4868aabb-1686-4e74-930e-3cee25f2aad1/lb12YdzQBS.json"  speed="1" width={300} height={300} loop autoplay></dotlottie-player>
            
      <div className='p-20'>

        <Box pl={10} fontSize={30}>
          <p >UniCopy</p>
        </Box>
        
      
        <Box className='p-20 w-full' p={10} >
          <TextField 
            id="outlined-multiline-flexible"
            label="Your Patent Here"
            multiline
            maxRows={4}
            className='w-full'
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            sx={{ width: 800 }}
          />
          
        </Box>
        <Box pl={10}>
          <Button className='text-white p-10'  style={{
        backgroundColor: "#2551da",
        fontSize: "18px",
        color:"#FFFFFF"
        
    }} onClick={handleSubmit}>Submit</Button>
        </Box>
    
        <Box className='p-20 w-full' p={10}>
        {loader ? <CircularProgress /> : <TextField 
            id="outlined-multiline-flexible"
            label="Other Similar Patents"
            multiline
            maxRows={8}
            className='w-full'
            value={outputText}
            readOnly
            sx={{ width: 800 }}
          />}
        {/* <CircularProgress></CircularProgress> */}
          {/* <TextField 
            id="outlined-multiline-flexible"
            label="Other Similar Patents"
            multiline
            maxRows={8}
            className='w-full'
            value={outputText}
            readOnly
            sx={{ width: 800 }}
          /> */}
        </Box>
      </div>
    </div>
  );
}

export default App;


