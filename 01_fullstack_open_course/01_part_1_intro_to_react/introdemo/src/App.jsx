const Footer = () => {
  return (
    <div>
      greeting app created by <a href='https://github.com/mluukkai'>mluukkai</a>
    </div>
  )
}

const Hello = (props) => {
  return (
    <div>
      <p>Hello {props.name}, are you  {props.age} years old</p>
    </div>
  )
}

const App = () => {
  const name = 'Peter'
  const age = 18
  const friends = ['william', 'john']
  
  return (
    <>
      <h1>Greetings</h1>
      <Hello name = 'Maya' age={26 + 10}/>
      <Hello name = {name} age={age}/>
      <Footer />
    </>
  )
}

export default App