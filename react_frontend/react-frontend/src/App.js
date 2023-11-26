import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Button } from '@mui/material';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await fetch('/get_response', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      const result = await response.json();
      setOutputText(result.result);
    } catch (error) {
      console.error('Error submitting text:', error);
    }
  };

  return (
    <div className="App">
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
          <TextField 
            id="outlined-multiline-flexible"
            label="Other Similar Patents"
            multiline
            maxRows={8}
            className='w-full'
            value={outputText}
            readOnly
            sx={{ width: 800 }}
          />
        </Box>
      </div>
    </div>
  );
}

export default App;
