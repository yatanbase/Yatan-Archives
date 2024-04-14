import logo from './logo.svg';
import './App.css';
import Header from "./myComponents/Header";
import { Footer } from "./myComponents/Footer";
import  {Todos } from "./myComponents/Todos";
import {TodoItems } from "./myComponents/TodoItems";
import PropTypes from 'prop-types'


function App() {
  let todos = [
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
  ];
  return (
    <>
      <Header />
      <Todos todos={todos} />
      <TodoItems/>
      <Footer/>
    </>
  );
}

export default App;
