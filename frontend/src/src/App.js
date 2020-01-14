import React, { Component } from 'react';
import axios from 'axios';
//import Todo from './Todo'; 
import Form from './Frorm';

class App extends Component {
  
  myHeaders={"API_KEY": "H10JZ74AT8CBUY57TP87"}
  state = {
    url: 'http://localhost:5001/',
    edit: false,
    editId: null,
    details: false,
    detailsId: null,
    books: [],
    editedBook: {}
  }

  onChange(updatedValue) {
    this.setState({
      editedBook: {
        ...this.state.editedBook,
        ...updatedValue
      }
    });
  }
  getData(){
    axios.get(this.state.url+"view_books", {headers: this.myHeaders}).then(res => {
      this.setState({
        books: res.data
      })
    });
  }
  componentDidMount() {
    this.getData();
  }
  onDeleteHandle() {
    axios.delete(this.state.url+"book/"+arguments[0], {headers: this.myHeaders}).then(res => {
      if(res.status==200) {
        this.getData();
      }
    })
  }
  onEditHandle() {
    this.setState({
      edit: true,
      editId: arguments[0],
    });
  }
  onUpdateHandle() {
    axios.patch(this.state.url+"book/"+this.state.editId, this.state.editedBook, {headers: this.myHeaders}).then(res => {
      if(res.status==200) {
        this.getData();
        this.setState({
          edit: false,
          editId: null,
          editedBook: {}
        })
      }
      else {
        console.log("NIE UDAŁO SIĘ EDYTOWAĆ KSIĄŻKI")
      }
    })
  }
  onAddHandle() {
    axios.post(this.state.url+"book", this.state.editedBook, {headers: this.myHeaders}).then(res => {
      if(res.status==200) {
        this.getData();
        this.setState({
          edit: false,
          id: null,
          editedBook: {}
        })
      }
      else {
        console.log("NIE UDAŁO SIĘ DODAĆ KSIĄŻKI")
      }
    })
  }
  getRentalsData(book_id) {
    axios.get(this.state.url+"book/"+book_id, {headers: this.myHeaders}).then(res => {
      this.setState({
        details: res.data,
        detailsId: arguments[0],
      })
    });
  }
  onDetailsHandle() {
    this.getRentalsData(arguments[0])
    /*this.setState({
      
      details: true
    })*/
  }
  onRentHandle() {
    axios.post(this.state.url+"book/"+arguments[0]+"/rent",{}, {headers: this.myHeaders}).then(res => {
      if (res.status == 200) {
        this.getRentalsData(arguments[0])
        console.log("GICIOR KSIĄŻKA WYPOŻYCZONA")
      }
    });
  }
  onReturnHandle() {
    axios.post(this.state.url+"book/"+arguments[0]+"/return",{}, {headers: this.myHeaders}).then(res => {
      if (res.status == 200) {
        this.getRentalsData(arguments[0])
        console.log("GICIOR KSIĄŻKA ODDANA")
      }
    });
  }
  detailsRender(book_id) {
    if(this.state.details && book_id == this.state.detailsId) {
      let rentals = this.state.details.rentals.map((rental) => {
        return (
          <tr key={rental.rental_id}>
            <td>{rental.rental_id}</td>
            <br />
            <td>{rental.start_date}</td>
            <br />
            <td>{rental.end_date}</td>
            <br />
            <td>{rental.user_id}</td> 
          </tr>
        )
      });
      return (
        <tr>
          <button onClick={this.onRentHandle.bind(this, book_id)}>Rent</button>
          <button onClick={this.onReturnHandle.bind(this, book_id)}>Return</button>
          {rentals}
        </tr>

        )
    }
  }
  FormRender() {
    if(this.state.edit) {
      return (
        <div className="form">
          Edytowanie
          <Form onUpdateHandle={() => this.onUpdateHandle()} onChange={editedBook => this.onChange(editedBook)} />
          <p>
            {JSON.stringify(this.state.editedBook,null,2)}
          </p>
        </div>
      )
    }
    else {
      return (
        <div className="form">
          Dodawanie
          <Form onUpdateHandle={() => this.onAddHandle()} onChange={editedBook => this.onChange(editedBook)} />
          <p>
            {JSON.stringify(this.state.editedBook,null,2)}
          </p>
        </div>
      )

    }
  }
  render() {
    let books = this.state.books.map((book) => {
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
      
      <div className="App-container">
        {this.FormRender()}
        {this.renderDeleteInfo}
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
            {books}
          </tbody>
        </table>
      </div>
      );
  }
}
export default App;