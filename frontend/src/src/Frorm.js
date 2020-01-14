import React from 'react';

export default class Form extends React.Component {
  state = {
    title: "",
    author: "",
    description: ""
  }
  change(e) {
    this.props.onChange({
      [e.target.name]: e.target.value
    });
    this.setState({
      [e.target.name]: e.target.value
    });
  }
  onSubmit(e) {
    e.preventDefault();
    this.setState({
      name: "",
      author: "",
      description: ""
    });
    this.props.onUpdateHandle();
    this.props.onChange({
      name: "",
      author: "",
      description: ""
    });
  }
  render() {
    return (
      <form>
        <br />
        <input 
          name='name'
          placeholder='Title'
          value={this.state.name}
          onChange={e => this.change(e)}
        />
        <br />
        <input 
          name='author'
          placeholder='Author'
          value={this.state.author}
          onChange={e => this.change(e)}
        />
        <br />
        <input 
          name='description'
          placeholder='Description'
          value={this.state.description}
          onChange={e => this.change(e)}
        />
        <br />
        <button onClick={e => this.onSubmit(e)}>Submit</button>
      </form>
    )
  }
}