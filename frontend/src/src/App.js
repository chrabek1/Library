import React, { Component } from 'react';
import axios from 'axios';
//import Todo from './Todo'; 
import Form from './Frorm';
import SearchBooks from './SearchBook'
import Book from './Book';
import BookList from './BookList';

class App extends Component {
  
  myHeaders={"API_KEY": "H10JZ74AT8CBUY57TP87", 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*'}
  state = {
    /*url: 'http://3.9.104.221:5001/',*/
    url: 'http://localhost:5001/',
    edit: false,
    editId: null,
    details: false,
    detailsId: null,
    books: [],
    searchResult: [],
    editedBook: {},
    loginData: {}
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
  onSignIn(googleUser) {
    this.setState({
      loginData: googleUser.getBasicProfile()
    })
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  }
  /*onLoadCallback() {
    gapi.auth2.init({
        client_id: 'filler_text_for_client_id.apps.googleusercontent.com'
      });
  }
  signOut() {
    if(gabi) {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      });
    }
  }*/

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
  GoogleLoginRender() {
    return(
      <div>
      <div className="g-signin2" data-onsuccess="onSignIn"></div>
      
      </div>
    )
  }
  render() {
    return (
      <div className="App-container">
        {/* {this.GoogleLoginRender()} */}
        <BookList key={1} data={this.state.books}/>
        <SearchBooks url={() => this.state.url} getData={() => this.getData()} myHeaders={() =>this.myHeaders } />
        {/* {this.FormRender()} */}
      </div>
      );
  }
}
export default App;