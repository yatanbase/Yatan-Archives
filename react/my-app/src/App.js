import logo from './logo.svg';
import './App.css';
import Header from "./myComponents/Header";
import { Footer } from "./myComponents/Footer";
import  {Todos } from "./myComponents/Todos";
import PropTypes from 'prop-types'
import { useState } from "react";



function App() {

  const onDelete = (todo) => {
    console.log("deleted the task",todo);
    setTodos(todos.filter((e)=>
   { return e!==todo;  } 
  
  ));
  }

  const [todos, setTodos] = useState([
    {
      sr: 1,
      title: "Task 1",
      desc: "Eat"
    },
    {
      sr: 2,
      title: "Task 2",
      desc: "Sleep"
    },
    {
      sr: 3,
      title: "Task 3",
      desc: "Repeat"
    }
  ]);
  
  return (
    <>
      <Header />
      <Todos todos={todos} onDelete={onDelete} />
     
      <Footer/>
    </>
  );
}

export default App;

