import React from 'react'
import { TodoItems } from "./TodoItems";


export const Todos = (props) => {
  return (
    <div className='container'>
      <h3 className='text-center'>Todos list</h3>
      {props.todos.length===0?"no todos to display":
      props.todos.map (( todo )=>{
      return <TodoItems todo = {todo} key={todo.sr} onDelete={props.onDelete}/>
      
      }
      )}
    
      
    </div>
  )
}


