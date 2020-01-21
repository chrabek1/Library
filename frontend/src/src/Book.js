import React from 'react';
import axios from 'axios'
import BookDetails from './BookDetails'

export default class Book extends React.Component {
  onDetailsHandle() {
    return (
      <BookDetails key={this.props.data.book_id} data={this.props.data.book_id}/>
    )
  }
  render() {
    //console.log(this.props)
    return (
      <tr key={this.props.data.book_id}>
        <td>{this.props.data.book_id}</td>
        <td>{this.props.data.name}</td>
        <td>{this.props.data.author}</td>
        <td>{this.props.data.description}</td>
        <td>{this.props.data.user_id}</td>
        <td><button onClick={this.onDetailsHandle()}>Details</button></td>
      </tr>
    )
    
  }
}