import React from 'react';

export const TodoItems = ({ todo, onDelete }) => {
  return (
    <div>
      <h4>{todo.title}</h4>
      <p>{todo.desc}</p>
      <button className='btn btn-sml btn-danger' onClick={ () => {onDelete(todo)}}>delete</button>
    </div>
  );
};

