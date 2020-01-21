import React from 'react';
import axios from 'axios';

export default class SearchBook extends React.Component {
  state = {
    search: "",
    searchResult: [],
    showResults: false
  }
  change(e) {
    this.setState({
      [e.target.name]: e.target.value
    });
  }
  onSearchHandle() {
    axios.post(this.props.url()+"seek_book/"+this.state.search, {headers: this.props.myHeaders}).then(res => {
      if(res.status==200) {
        this.setState({
          searchResult: res.data
        })
      }
    });
  }
  onAddHandle() {
    let book=arguments[0]
    axios.post(this.props.url()+"book", book, {headers: this.myHeaders}).then(res => {
      if(res.status==200) {
        console.log("dodano książke")
        this.props.getData();
      }
      else {
        console.log("NIE UDAŁO SIĘ DODAĆ KSIĄŻKI")
      }
    })
  }
  onSubmit(e) {
    e.preventDefault();
    this.onSearchHandle();
    this.setState({
      search: "",
      showResults: true
    })
  }
  resultRender(booksData) {
    let books = booksData.map((book) => {
      return (
        <tr key={book.name}>
          <td>{book.name}</td>
          <td>{book.author}</td>
          <td>
            <button onClick={this.onAddHandle.bind(this,book)}>Add</button>
          </td>
        </tr>
      )
    });
    if (this.state.showResults) {
      return (
        <div className="table">
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Author</th>
              </tr>
            </thead>
            <tbody>
              {books}
            </tbody>
          </table>
        </div>
      )
    }
  }
  formRender() {
    return(
      <form>
        <br />
        <input 
            name='search'
            placeholder='search'
            value={this.state.search}
            onChange={e => this.change(e)}
          />
          <button onClick={e => this.onSubmit(e)}>Szukaj</button>
      </form>
    )
  }
  render() {
    return(
      <div className="search">
        {this.formRender()}
        {this.resultRender(this.state.searchResult)}
      </div>
    )
  }
 }