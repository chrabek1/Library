import React from 'react';
import Book from './Book';

export default class BookList extends React.Component {

  /*BooksRender() {

    // const books = this.state.bookList.map(book => <Book/>)
    const booksComponents = booksData.map(book => <Book key={book.book_id} data={book}/>)
    let books = this.state.bookList.map((book) => {
      return (
        <tr key={book.book_id}>
          <td>{book.book_id}</td>
          <td>{book.name}</td>
          <td>{book.author}</td>
          <td>{book.description}</td>
          <td>{book.user_id}</td>
          <td>
            <button onClick={this.onEditHandle.bind(this,book.book_id)}>Edit</button>
            <button onClick={this.onDeleteHandle.bind(this, book.book_id)}>Delete</button>
            <button onClick={this.onDetailsHandle.bind(this, book.book_id)}>Details</button>
          </td>
          {this.detailsRender(book.book_id)}
        </tr>
      )
    });
    return (
      <div className="table">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Title</th>
              <th>Author</th>
              <th>Description</th>
              <th>Owner ID</th>
            </tr>
          </thead>
          <tbody>
            {booksComponents}
          </tbody>
        </table>
      </div>
    )

  }*/
  render() {
    const booksComponents = this.props.data.map(book => <Book key={book.book_id} data={book}/>)
    return (
      <div className="table">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Title</th>
              <th>Author</th>
              <th>Description</th>
              <th>Owner ID</th>
            </tr>
          </thead>
          <tbody>
            {booksComponents}
          </tbody>
        </table>
      </div>
    )
  }
}