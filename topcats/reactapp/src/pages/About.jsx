import React from 'react';
import '../styles/TopBar.css';
import TopBar from "../components/TopBar"

const About = () => {
  return (
    <div>
      <div>
        <TopBar />
      </div>
      <div>
        <p className='textbox'>The Active Recall tool facilitates reading comprehension through chatbot-driven question generation and dynamic answer checking. It is meant to help those who, like me, have a pesky habit of mind-wandering when attempting to absorb large chunks of text, leading to an ever-present "wait, what did I just read"?</p>
        <p className='textbox'>Developed with Django. Chatbot via Groq and Langchain. </p>
      </div>
    </div>

  );
};

export default About;
