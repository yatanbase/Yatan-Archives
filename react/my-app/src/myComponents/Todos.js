import React from 'react'
import { TodoItems } from "./TodoItems";

export const Todos = (props) => {
  return (
    <div>
      <h4>To-do List</h4>
      <TodoItems todo= {props.todo[1]}/>

    </div>
  )
}


